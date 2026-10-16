#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从单一源文件生成各平台的 skill / rules 文件。

用法：
    python3 build.py              # 生成全部
    python3 build.py --check      # 只检查源文件是否齐全，不写文件
    python3 build.py --list       # 列出会生成哪些文件

源（唯一的真相）：
    SKILL.md            主干：分类、回答骨架、纪律
    references/*.md     各模块细节

产物（每次运行覆盖，不要手动编辑）：
    dist/AGENTS.md               Codex CLI
    dist/GEMINI.md               Gemini CLI
    dist/.windsurfrules          Windsurf
    dist/.cursor/rules/fengshui-shushu.mdc    Cursor
    dist/claude-single-file.md   Claude（单文件版，用于 save_skill）
    dist/system-prompt-compact.md 通用精简版（只含主干，给上下文有限的模型）
"""

import argparse
import os
import re
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.join(ROOT, "SKILL.md")
REF_DIR = os.path.join(ROOT, "references")
DIST = os.path.join(ROOT, "dist")

# 生成顺序有意如此：主干放最前，细则在后，案例最后
REF_ORDER = [
    "bashuxiang.md",
    "xiaoliuren.md",
    "xingming.md",
    "shiren-xiangshu.md",
    "huajie-daoyi.md",
    "zeri-peise.md",
    "nihaixia.md",
    "glossary-en-zh.md",
]

CASE_FILES = [
    "cases/README.md",
    "cases/TEMPLATE.md",
    "cases/001-门吉卧吉却问权衡.md",
    "cases/002-土月问事落的取色取舍.md",
]


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def split_frontmatter(text):
    """拆出 YAML frontmatter 与正文。没有 frontmatter 则返回 (None, text)。"""
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, m.group(2)


def get_body():
    return split_frontmatter(read(SKILL))[1].strip()


def get_frontmatter():
    return split_frontmatter(read(SKILL))[0] or {}


def full_doc(title=None, include_cases=True, include_refs=True):
    """主干 + 全部 references（+ 案例）。这是各平台共用的完整正文。"""
    parts = []
    if title:
        parts.append(title)
        parts.append("")
    parts.append(get_body())

    if include_refs:
        for name in REF_ORDER:
            p = os.path.join(REF_DIR, name)
            if not os.path.exists(p):
                continue
            parts.append("")
            parts.append("---")
            parts.append("")
            parts.append(read(p).strip())

    if include_cases:
        for name in CASE_FILES:
            p = os.path.join(REF_DIR, name)
            if not os.path.exists(p):
                continue
            parts.append("")
            parts.append("---")
            parts.append("")
            parts.append(read(p).strip())

    return "\n".join(parts).strip() + "\n"


def build_agents_md():
    """Codex CLI 的 AGENTS.md。Codex 会自动读取仓库根目录的 AGENTS.md。"""
    return full_doc(
        title="# 术数研判（fengshui-shushu）\n\n"
        "本文件为 Codex CLI 生成，请勿手动编辑。改内容请改 SKILL.md 与 references/，然后重跑 build.py。"
    )


def build_gemini_md():
    """Gemini CLI 的 GEMINI.md。"""
    return full_doc(
        title="# 术数研判（fengshui-shushu）\n\n"
        "本文件为 Gemini CLI 生成，请勿手动编辑。改内容请改 SKILL.md 与 references/，然后重跑 build.py。"
    )


def build_windsurfrules():
    """Windsurf 的 .windsurfrules，纯文本，不带 Markdown 标题装饰。"""
    body = get_body()
    parts = [
        "术数研判（fengshui-shushu）—— 传统术数问答规则",
        "=" * 60,
        "",
        body,
    ]
    for name in REF_ORDER:
        p = os.path.join(REF_DIR, name)
        if not os.path.exists(p):
            continue
        parts.append("")
        parts.append("=" * 60)
        parts.append("")
        parts.append(read(p).strip())
    for name in CASE_FILES:
        p = os.path.join(REF_DIR, name)
        if not os.path.exists(p):
            continue
        parts.append("")
        parts.append("=" * 60)
        parts.append("")
        parts.append(read(p).strip())
    return "\n".join(parts).strip() + "\n"


def build_cursor_mdc():
    """Cursor 的 .mdc 规则文件，需要 frontmatter 声明何时生效。"""
    fm = get_frontmatter()
    desc = fm.get("description", "风水与术数问答").replace('"', "'")
    header = (
        "---\n"
        'description: "%s"\n'
        "globs:\n"
        "alwaysApply: false\n"
        "---\n\n"
    ) % desc
    return header + full_doc(title="# 术数研判（fengshui-shushu）")


def build_claude_single_file():
    """Claude 的单文件版 —— 用于 save_skill（它只接受单文件）。

    **重要：这个版本必须并入 references 全部正文。**
    原因是账户里的 skill 在回答时读不到磁盘上的 references/，
    只有这一份文件可用。所以这里用 full_doc()，内容最全。

    注意与 references 里各文件的区别：
    本文件是"打包产物"，不要手动编辑，改 SKILL.md / references 后重跑本脚本，
    再把结果交给 save_skill 重新存一次。
    """
    header = (
        "<!-- 由 build.py 生成 —— Claude 单文件版，用于 save_skill。\n"
        "     请勿手动编辑。改内容请改 SKILL.md 与 references/，然后重跑 build.py，\n"
        "     再用生成结果调用 save_skill。 -->\n\n"
    )
    return header + full_doc()


def build_compact():
    """精简版：只含主干，给上下文窗口有限的模型（网页版 DeepSeek / Kimi 等）。

    这些平台装不下完整内容，硬塞会挤掉用户自己的问题。
    """
    header = (
        "# 术数研判（精简版）\n\n"
        "> 本文件为上下文有限的平台生成，只含主干规则。\n"
        "> 完整版见同仓库的 SKILL.md 与 references/。\n\n"
    )
    return header + get_body() + "\n"


TARGETS = {
    "AGENTS.md": build_agents_md,
    os.path.join("GEMINI.md"): build_gemini_md,
    ".windsurfrules": build_windsurfrules,
    os.path.join(".cursor", "rules", "fengshui-shushu.mdc"): build_cursor_mdc,
    "claude-single-file.md": build_claude_single_file,
    "system-prompt-compact.md": build_compact,
}


def check_sources():
    missing = []
    if not os.path.exists(SKILL):
        missing.append("SKILL.md")
    for name in REF_ORDER + CASE_FILES:
        if not os.path.exists(os.path.join(REF_DIR, name)):
            missing.append(os.path.join("references", name))
    return missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只检查源文件，不生成")
    ap.add_argument("--list", action="store_true", help="列出会生成的文件")
    args = ap.parse_args()

    if args.list:
        for name in TARGETS:
            print(name)
        return 0

    missing = check_sources()
    if missing:
        print("缺少源文件：", file=sys.stderr)
        for m in missing:
            print("  - " + m, file=sys.stderr)
        return 1

    if args.check:
        print("源文件齐全。已有的 references：")
        for name in REF_ORDER + CASE_FILES:
            p = os.path.join(REF_DIR, name)
            n = len(read(p).splitlines())
            print("  %-40s %4d 行" % (name, n))
        print("\n主干 SKILL.md: %d 行" % len(read(SKILL).splitlines()))
        return 0

    os.makedirs(DIST, exist_ok=True)
    written = []
    for rel, fn in TARGETS.items():
        out = os.path.join(DIST, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        content = fn()
        with open(out, "w", encoding="utf-8") as f:
            f.write(content)
        written.append((rel, len(content.splitlines())))

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("已生成（%s）：" % stamp)
    for rel, n in sorted(written):
        print("  %-42s %4d 行" % (rel, n))
    print("\n共 %d 个文件 -> %s" % (len(written), DIST))
    return 0


if __name__ == "__main__":
    sys.exit(main())
