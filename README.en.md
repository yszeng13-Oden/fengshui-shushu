# fengshui-shushu (術數研判)

[中文](README.md) | **English**

A **Skill** for Claude that answers feng shui and Chinese metaphysics questions according to the rules of traditional Chinese divination.

This is not a "fortune-telling app," and it is not a database scraped from any single book. It is a **structured methodology document**: the rules scattered across classical Chinese divination systems — *Ba Zhai Ming Jing* (Eight Mansions), *Xiao Liu Ren*, the Five-Grid name analysis method, and others — organized into a form that can be looked up, recomputed, and audited, with Claude forced to answer from a fixed skeleton instead of improvising.

## What problem it solves

Ask an AI "where is the wealth corner of my house?" and the usual failure modes are: a vague conclusion, no stated basis, no written computation, mystical hand-waving, and a side helping of manufactured anxiety.

This Skill fixes four things:

1. **Classify, then act** — First decide whether the question is about *environment / divination / a person / health and character*. Each path is different. They don't get mixed together.
2. **Show the arithmetic** — A life-gua calculation must be written out as `1+9+8+5=23 → 2+3=5 → 11−5=6 → Qian`. A Xiao Liu Ren reading must list all three counting passes. Character-stroke counts must state which convention was used. If you can check it, it can't bluff.
3. **Fixed answer skeleton** — Establish the chart → name the positions → give concrete actions → state the limits. No stopping at "you should adjust your bed position"; it must land on "move the head of the bed to the southeast."
4. **A few hard rules** — Don't frighten people. Don't manufacture anxiety. Don't sell anything. For the number-therapy and Daoist-medicine sections, it must recommend seeing a doctor first, must not advise stopping medication, and must not present itself as a substitute for diagnosis.

## Coverage

| Module | File | Contents |
|---|---|---|
| Eight Mansions feng shui | `references/bashuxiang.md` | Life-gua calculation, East/West Four Houses, the **complete Eight Mansions star table**, star elements and domains, **the Three Periods and Nine Ages (san yuan jiu yun)**, the 24 Mountains, annual flying stars, common form-sha |
| Xiao Liu Ren | `references/xiaoliuren.md` | The six palaces and hand positions, year/month/day/hour casting (with a fully worked example), verdicts for each palace, timing of outcomes |
| Name analysis | `references/xingming.md` | The two stroke-count traps, the five-grid calculation, the **full 1–81 numerology table**, three-talents configuration, name-change practice |
| Reading people & number therapy | `references/shiren-xiangshu.md` | Five-layer profile-picture reading, phone-number numerology, bazi five-element primer, number-chanting therapy (with limits) |
| Remedies & Daoist medicine | `references/huajie-daoyi.md` | The avoid → remedy → adjust order, remedy table by star, form-sha remedies, date selection, health cultivation and character |
| **Date selection & colors** | `references/zeri-peise.md` | Day-pillar derivation (with JDN check anchors), five-tier daily color ranking, almanac date selection (the twelve officers, the yellow/black path deities, the 28 lunar mansions, day clashes) |
| **Case library** | `references/cases/` | Full reasoning records of real questions: inputs, the written arithmetic, ordering of judgement, what was uncertain at the time, and follow-up on accuracy |

## The case library (the most valuable part of this project)

Rules can be copied by anyone. **Cases are where the real value is.**

Real questions are rarely answerable by a single rule — they tend to involve interlocking good and bad factors, missing information, and conditions that contradict each other. What carries you through is the experience of knowing *what to look at first, what next, and which factor outranks which* — and that can only grow out of cases.

That is what `references/cases/` holds, and it records three things you won't find elsewhere:

- **What was uncertain at the time** — which step felt shaky, which missing input forced a conservative call, which of two competing schools was chosen and why
- **Records of readings that did not come true** — keeping only the hits would rob the library of its calibration value and turn it into a self-congratulatory scrapbook
- **Rule gaps exposed along the way** — when a case uses an approach no reference file documents, it is flagged and back-filled

Fill in new cases using `references/cases/TEMPLATE.md`. The library is designed to grow with your own use.

## Installation

This Skill targets Claude clients that support the Skill mechanism (such as Claude Desktop).

**Option 1 (recommended):** Place the whole `fengshui-shushu/` directory into your skills folder.

**Option 2:** Load it via `save_skill` in Claude Desktop — `SKILL.md` as the main body, with the five files under `references/` kept as attachments.

**Option 3 (manual):** `SKILL.md` is a self-contained document; the contents of all five reference files are folded into it as appendices. If you want a single-file version, `SKILL.md` alone will work — no extra files needed.

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
