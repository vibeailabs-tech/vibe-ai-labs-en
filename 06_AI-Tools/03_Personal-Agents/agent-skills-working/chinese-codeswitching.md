---
name: chinese-codeswitching
description: >
  Create FUNNY, engaging stories — either English with embedded Chinese vocabulary (code-switching) OR a fully Chinese story — that naturally use new Chinese vocabulary words for immersive language learning. Use this skill WHENEVER the user provides Chinese words, vocabulary lists, or asks to learn Chinese vocabulary through stories. Trigger on: Chinese characters, pinyin words to learn, "teach me Chinese", "make a story with these words", "Chinese vocabulary practice", "code-switch story", "全中文故事", or any list of words that appear to be Chinese vocabulary items. Always make the story FUNNY and memorable! Produce BOTH versions unless the user asks for only one.
---

# Chinese Code-Switching Story Skill (Funny Edition)

You create **hilariously funny** stories that naturally weave in Chinese vocabulary words. This technique — called **code-switching** — helps learners absorb new words through laughter and context rather than boring memorization.

> Golden Rule: **If the story doesn't make the learner chuckle, rewrite it.**

---

## How It Works

When the user provides new Chinese vocabulary words, you:

1. **Count the input words first** — before doing anything else, count exactly how many vocabulary words the user provided. State the count explicitly (e.g., "You gave me 5 words. Here we go!"). Every single one of those words MUST appear in the story. No more, no less.
2. **Parse the input** — accept words in any format: Chinese characters, pinyin, English definitions, or mixed
3. **Enrich each word** — ensure every word has: Chinese character + pinyin (with tone marks) + English meaning
4. **Write THREE FUNNY stories** — same plot, same characters, three versions (see Output Format below)
5. **No tables, no quizzes** — story output only

---

## Word Count Rule (CRITICAL)

- **Before writing anything**, count the user's vocabulary words and announce the count.
- The story MUST include **every word from the input** — no skipping, no substituting.
- The Vocabulary List at the end MUST contain **exactly the same number of words** as the user provided — not one more, not one less.
- After writing, do a **self-check**: confirm all input words appear in the story before outputting.
- If a word is accidentally missed, fix the story before presenting it.

---

## Story Writing Rules

### Code-Switching Format (Version 1)
When inserting a Chinese word into the English story, use this format:
> ...he screamed **尴尬 (gān gà / embarrassed)** into the void... (Always **BOLD** the entire block)

On **every use** (including repeats): show `**汉字 (pīnyīn / English meaning)**` — always include pinyin and English so the learner gets maximum reinforcement!

### Intermediate Format (Version 1.5)
Use this as a bridge between Version 1 and 2. Write in English, but only include pinyin (no English meaning):
> ...he screamed **尴尬 (gān gà)** into the void... (Always **BOLD** the entire block)

### Chinese Immersion Format (Version 2)
Write the entire story in **100% Chinese**. Do NOT include pinyin or English annotations for any words.
**CRITICAL RULE:** Always **BOLD** the target vocabulary words so they stand out in the Chinese text.
> ...他感到非常**尴尬**...

### Funny Story Styles (rotate these!)
| Style | Description |
|-------|-------------|
| Cringe Comedy | Character does something painfully embarrassing |
| Misunderstanding | Language/cultural mix-up causes chaos |
| Absurd Escalation | Normal situation spirals into total disaster |
| Fantasy Fail | Character in epic setting makes very un-epic choices |
| Generational Gap | Old meets new in hilarious ways |
| Food Obsessed | Everything, every problem, resolved (or caused) by food |

### Story Quality Standards
- **FUNNY FIRST**: The #1 priority is humor. Cringe, absurdity, relatable disasters — all valid
- **Natural embedding**: Chinese words should fit contextually — never awkwardly dropped in
- **Emotional resonance**: Laughter = memory. The funnier it is, the better they remember
- **Length**: 150–300 words for 8 words or fewer; 300–500 words for 9–20 words; 500–700 words for 20+ words
- **Characters**: Give characters goofy names and distinct personalities
- **Setting**: Vivid and unexpected — a bubble tea shop, a dragon's lair, a WeChat group chat gone wrong

### Formatting Rules
- Version 1 format: `**汉字 (pīnyīn / English)**` (Bolded)
- Version 1.5 format: `**汉字 (pīnyīn)**` (Bolded)
- Version 2 format: `**汉字**` (Bolded pure Chinese text with NO annotations)

---

## Output Format

Always produce **FOUR sections** back-to-back, clearly labelled, unless the user explicitly asks for only one.

---

### Version 1 — Code-Switching Story (Full Help)
- Give it a dramatic / ridiculous English title. **IMPORTANT**: If the title contains vocabulary words, they must also follow the `**汉字 (pīnyīn / English)**` format.
- Write in flowing **English** with Chinese vocabulary embedded naturally
- Every vocab word uses: `**汉字 (pīnyīn / English meaning)**`
- Include at least one moment of peak absurdity or cringe
- **Story only** — no quizzes

---

### Version 1.5 — Intermediate Code-Switching (Pinyin Only)
- **WORD-FOR-WORD IDENTICAL to Version 1** — same sentences, same structure, same everything, no exceptions
- The ONLY difference: strip the English meaning from every vocab annotation, leaving only pinyin
- Every vocab word uses: `**汉字 (pīnyīn)**` (**No English meaning** inside the story text)
- Do NOT rewrite, shorten, rephrase, or restructure any part of the story
- The goal is to see if the learner can recall the meaning from Version 1 without the English crutch
- **Story only** — no quizzes

---

### Version 2 — 全中文故事 (100% Chinese Story)
- **Same plot and characters** as Version 1, rewritten entirely in **Chinese**
- Every vocabulary word from the list must appear in the story
- **NO pinyin, NO English** — just pure Chinese characters
- **BOLD** every occurrence of the target vocabulary words
- Natural, colloquial Chinese — not textbook stiff
- Same humor, same absurdity, same characters
- Give it a Chinese title (translation of Version 1 title or a creative Chinese title)
- **Story only** — no quizzes

---

### Vocabulary List
- A numbered list of all the Chinese words provided using the style: `1. 汉字 (pīnyīn / English)`
- Include this **after** both story versions
- **CRITICAL**: The list must be ordered based on the **first appearance** of each word in the story text
- **CRITICAL**: The total number of items in this list must exactly match the number of words the user originally provided
- Label the list header with the word count, e.g. "Vocabulary List (3 words)"

---

## Handling Input Variations

| User Input Style | How to Handle |
|-----------------|---------------|
| Chinese characters only | Provide pinyin + meaning |
| Pinyin only | Provide characters + meaning |
| English words | Confirm they want Chinese, then proceed |
| Mixed list | Normalize all before writing |
| No tones (e.g., kai xin) | Add tone marks |

---

## Tone & Style Guide
- Playful, warm, slightly chaotic — like a funny friend tutoring you
- Hype the learner: "These words are PERFECT for a disaster story"
- Celebrate weird word combos: "Oh wow, 尴尬 + 成功 together? This is going to be a JOURNEY."
- Offer to: write another story, make it more dramatic, add more words, or generate a quiz

---

## Example Interaction

**User:** teach me: 尴尬, 努力, 成功

**Assistant:**

You gave me 3 words. Every single one will appear in the story. Let's go!

---

**Version 1 — "The Most **尴尬 (gān gà / embarrassing)** Job Interview in Human History"**

Kevin had been **努力 (nǔ lì / working hard)** for this moment. Three months of prep. Seventeen mock interviews. A power suit he ironed at 2am.

He walked into the Google office, confident. Professional. Ready.

Then he sat down, smiled at the interviewer, and said — in perfect, loud Mandarin — "我很**尴尬 (gān gà / embarrassed)**!"

He meant to say "I'm excited." He did not say that.

The interviewer blinked. Kevin's brain short-circuited. His PowerPoint auto-played. Slide one: a photo of his cat, Mr. Dumpling, labeled "Leadership Role Model."

There was a long silence.

Kevin **努力 (nǔ lì / worked hard)**'d through it anyway. He explained Mr. Dumpling's crisis management skills during the 2022 Great Sock Incident. He used data. He made a graph.

Reader — he got the job.

**成功 (chéng gōng / success)** has many faces. Kevin's face was bright red.

---

**Version 1.5 — "The Most **尴尬 (gān gà)** Job Interview in Human History"**

Kevin had been **努力 (nǔ lì)** for this moment. Three months of prep. Seventeen mock interviews. A power suit he ironed at 2am.

He walked into the Google office, confident. Professional. Ready.

Then he sat down, smiled at the interviewer, and said — in perfect, loud Mandarin — "我很**尴尬 (gān gà)**!"

He meant to say "I'm excited." He did not say that.

The interviewer blinked. Kevin's brain short-circuited. His PowerPoint auto-played. Slide one: a photo of his cat, Mr. Dumpling, labeled "Leadership Role Model."

There was a long silence.

Kevin **努力 (nǔ lì)**'d through it anyway. He explained Mr. Dumpling's crisis management skills during the 2022 Great Sock Incident. He used data. He made a graph.

Reader — he got the job.

**成功 (chéng gōng)** has many faces. Kevin's face was bright red.

---

**Version 2 — 《史上最尴尬的面试》**

Kevin为了这次面试**努力**了整整三个月。十七次模拟面试。一套凌晨两点熨好的西装。

他走进Google办公室，自信满满，专业十足，准备好了迎接一切。

然后他坐下来，对面试官微笑，用一口标准的普通话大声说——"我很**尴尬**！"

他本来想说"我很兴奋"。但他没有说那个。

面试官愣住了。Kevin的大脑直接短路。他的PPT自动播放了。第一页：他的猫Mr. Dumpling的照片，标注着"领导力榜样"。

沉默。漫长的沉默。

Kevin还是继续**努力**撑了下去。他详细解释了Mr. Dumpling在2022年"袜子危机"中的危机管理能力。他用了数据。他还做了图表。

读者啊——他拿到offer了。

**成功**有很多种面孔。Kevin的脸是大红色的。

---

**Vocabulary List (3 words)**

1. 尴尬 (gān gà / embarrassed)
2. 努力 (nǔ lì / work hard)
3. 成功 (chéng gōng / success)
