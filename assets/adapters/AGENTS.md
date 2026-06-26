# Interview Answer Pack Builder

Use these instructions when the user asks to search for interview questions, answer pasted interview questions, organize an interview question bank, or create an interview answer document.

## Modes

Choose one mode before answering:

- Role search: search for real role-specific interview questions, cite sources, then answer.
- Direct answer: answer questions pasted by the user; do not search for more questions unless verification is needed.
- Question bank: classify, deduplicate, group, and answer a large pasted/uploaded question set.

## Required Workflow

- Classify every question as knowledge, scenario, project detail, strategy expansion, or behavioral.
- For more than 8 questions, split the set into coherent topic batches before answering.
- Keep related questions together, such as Redis questions, MySQL questions, multi-agent questions, or project deep-dive questions.
- Use subagents/workers if available; otherwise process batches sequentially.
- Merge all batches into one coherent Markdown document.
- For complete packs, write a `.md` file instead of only replying in chat.
- In role-search mode, prioritize real interview sources such as Nowcoder/Niuke, Zhihu, Juejin, CSDN, LeetCode/Likou, LeetCode Discuss, Glassdoor, GitHub, and similar sources appropriate to the target region.

## Answer Quality

- Output all final user-facing content in Chinese by default. Keep necessary technical terms, URLs, API names, and code identifiers in their original language.
- Preserve technical terms such as CAP, MVCC, B+Tree, idempotency, checkpoint, ReAct, GraphRAG, and supervisor-worker.
- Make answers detailed enough for learning and oral interview practice.
- Use length targets unless the user asks for concise output: normal knowledge questions 500-800 Chinese characters, high-frequency core questions 1000-1500 Chinese characters, scenario questions 900-1400 Chinese characters, project questions 700-1200 Chinese characters, and strategy expansion questions 1200-2000 Chinese characters plus a comparison table.
- Each major question should include a direct answer, detailed explanation, spoken interview answer, likely follow-ups, and common mistakes.
- For scenario questions, state the provided or assumed enterprise scenario before answering.
- For project questions, never fabricate the user's project facts. Provide a framework, selectable options, or fill-in template when facts are missing.
- For project questions, collect or request business scenario, tech stack, personal responsibility, core module, scale, technical challenge, solution, alternatives, and results when needed.
- For strategy questions, expand into common strategies, compare tradeoffs, and give a conservative spoken answer.
- Mark assumptions, uncertainty, and version-sensitive claims.
- Cite sources when search is used.

## Output

Default output file: `interview-answer-pack.md`.

Use this structure for full packs:

- Title, generated date, scope, and source mode.
- Source overview if search was used.
- Question map.
- Batch plan.
- Knowledge questions.
- Scenario questions.
- Project detail questions.
- Strategy expansion questions.
- Behavioral questions.

If the tool cannot write files, output the complete Markdown document in chat and state that file writing is unavailable.

Use review checklists internally only. Do not include a "Final Review Checklist" section in the final document.
