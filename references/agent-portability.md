# Agent Portability

Use this reference when adapting the skill to AI tools that do not natively support Codex skills.

## Portable Core

Every target tool should receive these instructions:

- Use the skill when the user asks to search for interview questions, answer pasted interview questions, organize an interview question bank, or create an interview answer document.
- Choose exactly one mode first: role search, direct answer, or question bank.
- For searched questions, cite sources and treat online posts as question sources, not answer authorities.
- For pasted questions, do not search for more questions unless the user asks or factual verification is needed.
- Classify each question before answering: knowledge, scenario, project detail, strategy expansion, or behavioral.
- For large packs, split questions into coherent topic batches; use multiple agents/workers if available, otherwise run sequential passes.
- Keep answers conversational while preserving technical terms.
- Make answers detailed enough for learning and oral practice, not just short notes.
- Apply length targets: normal knowledge questions around 500-800 Chinese characters, high-frequency core questions around 1000-1500 Chinese characters, scenario questions around 900-1400 Chinese characters, and strategy expansion questions around 1200-2000 Chinese characters plus a comparison table.
- Never fabricate the user's project facts.
- For role search, prioritize real interview sources such as Nowcoder/Niuke, Zhihu, Juejin, CSDN, LeetCode/Likou, LeetCode Discuss, Glassdoor, GitHub, and similar sources based on region and role.
- For project questions, collect or request business scenario, tech stack, personal responsibility, core module, scale, technical challenge, solution, alternatives, and results before writing a final personal answer.
- Label assumed enterprise scenarios and fictional example projects.
- Include likely follow-up questions.
- Output Markdown by default, create a `.md` document file for full packs when the tool can write files, and use `output-template.md` for full packs.
- Output all final user-facing content in Chinese by default. Keep necessary technical terms, URLs, source titles, API names, and code identifiers in their original language.
- Use final review checklists internally only; do not include a "Final Review Checklist" section in the final document.

## Claude Code

Recommended forms:

- Project-level: place the adapted instructions in `CLAUDE.md`.
- User-level: add a concise version to Claude Code user memory or custom instructions if available.
- Repository asset: keep `SKILL.md` and `references/output-template.md` in a reusable folder, then tell Claude Code to follow them.
- Out-of-the-box adapter: copy `assets/adapters/AGENTS.md` and `assets/adapters/CLAUDE.md` to the target project root, or run `scripts/install_adapters.py --target <project> --tools agents,claude`.

Claude Code adaptation notes:

- Replace "read references/output-template.md" with "open and follow the local output-template.md file" if the files are copied into a repo.
- If web browsing is unavailable, ask the user to provide sources or use direct answer mode.
- If file creation is requested, write a Markdown file such as `interview-answer-pack.md`.
- For long packs, use Claude Code subagents if available; otherwise process topic batches sequentially and merge the final document.

## Cursor

Recommended forms:

- Put a compact adaptation in `.cursor/rules/interview-answer-pack-builder.mdc`.
- Keep the full template as a project document and reference it from the rule.
- Out-of-the-box adapter: copy `assets/adapters/.cursor/rules/interview-answer-pack-builder.mdc` to the same path in the target project, or run `scripts/install_adapters.py --target <project> --tools cursor`.

Cursor adaptation notes:

- Make the rule always apply only to interview-answer tasks, not all coding tasks.
- If Cursor cannot browse the web, use user-provided questions and mark source search as unavailable.

## Gemini CLI or Other Coding CLIs

Recommended forms:

- Put the adapted instructions in the tool's persistent project instruction file if it supports one.
- Otherwise, paste the "Portable Core" and the output template at the start of the task.
- Out-of-the-box Gemini adapter: copy `assets/adapters/AGENTS.md` and `assets/adapters/GEMINI.md` to the target project root, or run `scripts/install_adapters.py --target <project> --tools agents,gemini`.

Adaptation notes:

- Keep the mode-selection step explicit.
- Require the agent to state assumptions before answering scenario and project questions.
- Require source links when the agent performs search.

## ChatGPT Custom Instructions or Custom GPT

Recommended forms:

- Put the portable core into custom instructions.
- Upload or paste `output-template.md` as a knowledge/reference file when possible.

Adaptation notes:

- Tell the model to ask for role, seniority, stack, and target company only when missing details materially affect the result.
- Default to Markdown unless the user asks for Word, PDF, or another document format.

## Minimal Prompt Wrapper

Use this wrapper when a target tool has no plugin, skill, or rule system:

```text
You are using the Interview Answer Pack Builder workflow. First select one mode: role search, direct answer, or question bank. Classify every question as knowledge, scenario, project detail, strategy expansion, or behavioral. Preserve technical terms, write answers in a natural interview voice, cite sources when searching, label assumptions, and never invent my project facts. For full packs, output Markdown using the provided template.
```
