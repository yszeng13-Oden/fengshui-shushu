# fengshui-shushu (術數研判)

[中文](README.md) | **English**

A **knowledge package** for answering feng shui and Chinese metaphysics questions by the rules of traditional Chinese divination. The source files are plain Markdown, and `build.py` packages them for Claude Skills, Codex (`AGENTS.md`), Gemini CLI, Windsurf, Cursor, and a compact version for context-limited web models. **Not tied to any single model.**

This is not a "fortune-telling app," and it is not a database scraped from any single book. It is a **structured methodology document**: the rules scattered across classical Chinese divination systems — *Ba Zhai Ming Jing* (Eight Mansions), *Xiao Liu Ren*, the Five-Grid name analysis method, *Zi Wei Dou Shu*, and others — organized into a form that can be looked up, recomputed, and audited, with the model forced to answer from a fixed skeleton instead of improvising.

## What problem it solves

Ask an AI "where is the wealth corner of my house?" and the usual failure modes are: a vague conclusion, no stated basis, no written computation, mystical hand-waving, and a side helping of manufactured anxiety.

This package fixes four things:

1. **Classify, then act** — First decide whether the question is about *environment / divination / reading a person / health and character / dates and colors / a natal chart*. Each path is different. They don't get mixed together.
2. **Show the arithmetic** — A life-gua calculation must be written out as `1+9+8+5=23 → 2+3=5 → 11−5=6 → Qian`. A Xiao Liu Ren reading must list all three counting passes. Day pillars must be verified with JDN. Zi Wei charts must show the five-element bureau and star placement. Character-stroke counts must state which convention was used. If you can check it, it can't bluff.
3. **Fixed answer skeleton** — Establish the chart → name the positions → give concrete actions → state the limits. No stopping at "you should adjust your bed position"; it must land on "move the head of the bed to the southeast."
4. **A few hard rules** — Don't frighten people. Don't manufacture anxiety. Don't sell anything. **No Chinese herbal formulas or dosage advice.** Any health-adjacent answer must lead with seeing a doctor. Number-chanting therapy is explicitly labelled as lacking scientific evidence, with no advice to stop medication.

## Coverage

| Module | File | Contents |
|---|---|---|
| Eight Mansions feng shui | `references/bashuxiang.md` | Life-gua calculation, East/West Four Houses, the **complete Eight Mansions star table**, star elements and domains, **the Three Periods and Nine Ages (san yuan jiu yun)**, the 24 Mountains, annual flying stars, common form-sha |
| Xiao Liu Ren | `references/xiaoliuren.md` | The six palaces and hand positions, year/month/day/hour casting (with a fully worked example), verdicts for each palace, timing of outcomes |
| Name analysis | `references/xingming.md` | The two stroke-count traps, the five-grid calculation, the **full 1–81 numerology table**, three-talents configuration, name-change practice |
| Reading people & number therapy | `references/shiren-xiangshu.md` | Five-layer profile-picture reading, phone-number numerology, bazi five-element primer, number-chanting therapy (with limits) |
| Remedies & Daoist medicine | `references/huajie-daoyi.md` | The avoid → remedy → adjust order, remedy table by star, form-sha remedies, date selection, health cultivation and character |
| **Date selection & colors** | `references/zeri-peise.md` | Day-pillar derivation (with JDN check anchors), five-tier daily color ranking, almanac date selection (the twelve officers, the yellow/black path deities, the 28 lunar mansions, day clashes) |
| **Ni Haixia's Tian Ji** | `references/nihaixia.md` | Zi Wei Dou Shu (chart construction, the 14 major stars, the Four Transformations table), I Ching divination (coin casting, body/use, transformed hexagram), yang zhai, face reading; Ren Ji covered as methodology reading only |
| **Glossary (EN/ZH)** | `references/glossary-en-zh.md` | Full bilingual term list: five elements, bagua, the eight stars, the six palaces, the 14 major stars, date selection, face reading, Daoist medicine |
| **Case library** | `references/cases/` | Full reasoning records of real questions: inputs, the written arithmetic, ordering of judgement, what was uncertain at the time, and follow-up on accuracy |

## Cross-platform use

This material is not only for Claude. `build.py` generates each platform's format from a **single source**:

```bash
python3 build.py           # generate everything into dist/
python3 build.py --check   # only verify source files are present
python3 build.py --list    # list what would be generated
```

Output mapping:

| Platform | Output | Note |
|---|---|---|
| Claude (recommended) | use `SKILL.md` + `references/` directly | supports on-demand loading, lightest on context |
| Claude (save_skill / manual) | `dist/claude-single-file.md` | single-file full version, since save_skill accepts one file only |
| Codex CLI | `dist/AGENTS.md` | Codex reads AGENTS.md from the repo root automatically |
| Gemini CLI | `dist/GEMINI.md` | —— |
| Windsurf | `dist/.windsurfrules` | —— |
| Cursor | `dist/.cursor/rules/fengshui-shushu.mdc` | includes rule frontmatter |
| Context-limited models (web DeepSeek / Kimi etc.) | `dist/system-prompt-compact.md` | main body only, about 6.5% of the full version |

**Why a compact version exists**: web-based models cannot hold the full text (~1770 lines); forcing it in would crowd out the user's own question. The compact version keeps the core rules and disciplines, leaving detail to be looked up on demand.

**Workflow**: edit content → edit `SKILL.md` or `references/` → run `build.py` → all platform outputs update. **Do not edit files inside `dist/` by hand** — they will be overwritten.

`dist/` is git-ignored by default. If you want some platform outputs published with the repo, remove the corresponding lines from `.gitignore`.

## The case library (the most valuable part of this project)

Rules can be copied by anyone. **Cases are where the real value is.**

Real questions are rarely answerable by a single rule — they tend to involve interlocking good and bad factors, missing information, and conditions that contradict each other. What carries you through is the experience of knowing *what to look at first, what next, and which factor outranks which* — and that can only grow out of cases.

That is what `references/cases/` holds, and it records three things you won't find elsewhere:

- **What was uncertain at the time** — which step felt shaky, which missing input forced a conservative call, which of two competing schools was chosen and why
- **Records of readings that did not come true** — keeping only the hits would rob the library of its calibration value and turn it into a self-congratulatory scrapbook
- **Rule gaps exposed along the way** — when a case uses an approach no reference file documents, it is flagged and back-filled

Fill in new cases using `references/cases/TEMPLATE.md`. The library is designed to grow with your own use.

## Installation

**Claude (recommended):** Place the whole `fengshui-shushu/` directory into your skills folder. `SKILL.md` is the entry point; `references/` loads on demand, which is lightest on context.

**Claude (save_skill or manual):** `SKILL.md` is self-contained — the contents of the reference files are folded into it as appendices. If you want a single-file version, it works on its own.

**Codex CLI:** put `dist/AGENTS.md` in your project root. Codex reads it automatically.

**Gemini CLI:** `dist/GEMINI.md`.

**Windsurf:** `dist/.windsurfrules`.

**Cursor:** `dist/.cursor/rules/fengshui-shushu.mdc`.

**Web models (DeepSeek / Kimi and others with limited context):** `dist/system-prompt-compact.md`. This contains only the core rules — about 6.5% of the full version — because the full text will not fit, and forcing it in would crowd out the user's own question.

**All of the `dist/` outputs ship with this repository, so download and use them directly — no Python required.** You only need `build.py` if you want to modify the content yourself.

## Usage

Once installed, there are two ways to invoke it.

**Automatic triggering** — just ask. Claude decides whether to load it. For example:

- "I was born in 1985, my house was moved into in 2019, the front door faces southeast, and the master bedroom is in the northwest. Is that a problem?"
- "Cast a reading for me — will this interview go well?"
- "My name is Li XX. How is this name?"
- "What color should I wear today?"

**Named invocation** — type `/fengshui-shushu` in the input box, followed by your question.

### How to ask well

The more complete the input, the better the answer — by a wide margin:

- **Feng shui:** at minimum give the *year the home was first occupied* and the *facing direction of the front door*. A floor plan and floor number help.
- **Divination:** state in one sentence exactly what you're asking about. Not "how is my life going lately."
- **Name analysis:** full name plus birth year.
- **Daily color:** just give the date.

## Directory structure

```
fengshui-shushu/
├── SKILL.md                    # Main body: classification, answer skeleton, rules, terminology
└── references/
    ├── bashuxiang.md           # Eight Mansions feng shui
    ├── xiaoliuren.md           # Xiao Liu Ren divination
    ├── xingming.md             # Five-grid name analysis
    ├── shiren-xiangshu.md      # Profile-picture reading / phone numbers / number therapy / bazi primer
    └── huajie-daoyi.md         # Remedies / Daoist medicine / character cultivation
```

## On sources

The content draws on **traditional, publicly documented Chinese divination systems** — Eight Mansions (*Ba Zhai Ming Jing*), Xiao Liu Ren, the Five-Grid profile method, number-chanting therapy, traditional Daoist health cultivation, and so on. These are bodies of knowledge that have circulated publicly for centuries and belong to no single author or publication.

This repository **contains no text from any modern published work**, and provides no full text of any copyrighted material. Where a modern book or novel develops its own particular heuristics or mnemonic verses on top of these traditional methods, that material must be obtained and added by the user through lawful channels.

## Disclaimer

The contents of this repository are **traditional folk culture**. They do not constitute medical, investment, legal, or marital advice.

- **Health-related:** The Daoist medicine and number-therapy sections are cultural background and soft lifestyle suggestions only. They are **not a substitute for medical care**. If you feel unwell, see a doctor. Do not stop prescribed medication.
- **Decisions:** Divination output may serve as one reference dimension among others. For major decisions, rely on facts and professional advice.
- **Cultural framing:** These methods derive from pre-modern systems of analogy and symbolism, and their explanatory power has not been established by modern science. Please approach them as culture and as a way of thinking, not as deterministic prediction.

## Extending it

To add material, put it in the matching file rather than piling everything into `SKILL.md` (keep the main body short; references load on demand):

- New feng shui schools or flying-star detail → `references/bashuxiang.md`
- More verdicts, case studies, timing patterns → `references/xiaoliuren.md`
- Stroke tables, more numerology annotations → `references/xingming.md`
- Reading-people heuristics, new imagery → `references/shiren-xiangshu.md`
- Remedy objects, health cultivation → `references/huajie-daoyi.md`
- **An entire new divination system** → create `references/xxx.md` and add one line to the "Reference files" section of `SKILL.md`

If you modify an already-installed Skill, note that **editing the local files does not take effect automatically** — it must be re-loaded.

## License

See `LICENSE`. MIT or CC BY 4.0 are both reasonable choices — MIT if you want the code and docs freely reusable, CC BY 4.0 if you want to emphasize attribution and share-alike, which suits documentation projects particularly well.
