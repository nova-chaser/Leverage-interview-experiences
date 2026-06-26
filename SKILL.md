---
name: interview-answer-pack-builder
description: Build interview question answer packs from real role-specific interview questions, user-provided questions, or existing question banks. Use when the user asks to search for interview questions for a role, organize interview questions, generate spoken reference answers, classify knowledge/scenario/project questions, create follow-up chains, or output a Markdown/document-style interview preparation pack.
---

# Interview Answer Pack Builder

## Core Rule

Create Chinese interview preparation packs that are useful for real interviews, not textbook notes. Preserve technical terms, speak in a natural Chinese candidate voice, separate sourced facts from generated guidance, and make project-specific answers honest about what is known versus assumed.

All final user-facing content must be in Chinese by default, including document headings, section names, explanations, summaries, and final chat replies. Keep necessary technical terms, product names, API names, source titles, URLs, and code identifiers in their original language.

## Mode Selection

Choose one mode from the user's request:

1. **Role search mode**: Search the web for real interview questions for a target role, company, stack, seniority, or domain. Use this when the user asks to find, collect, search, or summarize interview questions.
2. **Direct answer mode**: Answer interview questions pasted by the user. Do not search for more questions unless factual verification is needed or the user asks for it.
3. **Question bank mode**: Process a large pasted list or uploaded/source document of interview questions. Classify, deduplicate, and organize before answering.

If the user forbids web search, do not search. If the user asks for current questions, real online questions, recent role trends, company-specific questions, or source links, search the web and cite sources.

## Planning for Large Packs

For more than 8 questions, or whenever the user asks for a complete answer pack, read `references/batching-and-depth.md` before answering.

Default to grouped batch processing instead of one short pass. Keep related questions together so answers share context and do not contradict each other. If the current environment supports subagents, parallel workers, or separate agent runs, use them for independent topic batches, then synthesize the results into one coherent document. If no subagent capability exists, simulate the same workflow sequentially.

## Depth and Search Requirements

For answer length, depth minimums, and final review rules, read `references/depth-and-quality.md` before generating any complete answer pack.

For role search mode, read `references/search-strategy.md` before searching. Use target sites and keyword templates, then deduplicate and cite sources.

For project detail questions with missing user facts, read `references/project-background-template.md` and either collect the missing facts or produce a fill-in framework without inventing experience.

## Source Handling

In role search mode:

- Treat online posts, interview experiences, forums, blogs, and question banks as question sources, not answer authorities.
- Prefer official documentation, standards, research papers, reputable engineering blogs, and source repositories to verify technical answers.
- Record source URL, platform/site, retrieval date, and whether the output question is original, paraphrased, merged, or inferred from several similar questions.
- Merge duplicate or near-duplicate questions into one representative question.

In direct answer mode and question bank mode:

- Use the provided questions as the source of truth.
- Search only to verify version-sensitive or factual technical claims, unless the user asks to avoid searching.

## Question Classification

Classify each question before answering:

- **Knowledge question**: Has a relatively correct technical answer, such as Java concurrency, MySQL indexes, Redis persistence, HTTP, operating systems, LLM agent patterns, or LangGraph concepts.
- **Scenario question**: Asks what to do when something happens, such as outages, slow queries, duplicate messages, cache breakdown, production incidents, or conflicting requirements.
- **Project detail question**: Asks what the candidate did in their own project, why a technology was chosen, how it was implemented, or what tradeoffs were made.
- **Strategy expansion question**: Starts from a project or technology detail but is better answered by presenting common strategies in that class of problems.
- **Behavioral question**: Asks about teamwork, conflict, ownership, learning, pressure, or communication.

## Answering Rules

### Knowledge Questions

Use this structure by default:

- Direct answer
- Core principle
- Detailed explanation
- Interview spoken answer
- Follow-up questions
- Common mistakes

Keep the language conversational, but preserve terms such as `CAP`, `MVCC`, `B+Tree`, `idempotency`, `checkpoint`, `ReAct`, `GraphRAG`, and `supervisor-worker`. Do not replace precise technical nouns with vague everyday wording.

When behavior depends on framework, language, database, or runtime version, state the version dependency and verify if needed.

### Scenario Questions

Never answer a vague scenario question without first defining the scenario. If the user did not provide enough context, create a realistic enterprise scenario and label it as an assumption.

Use this structure:

- Assumed or provided scenario
- Impact assessment
- Immediate mitigation
- Diagnosis path
- Root cause possibilities
- Long-term prevention
- Interview spoken answer
- Follow-up questions

Prefer practical production thinking: observability, rollback, rate limiting, degradation, data repair, ownership, communication, postmortem, tests, and monitoring.

### Project Detail Questions

Do not invent the user's personal experience. Use a three-tier response:

- If project facts are provided, answer based on those facts and preserve them.
- If the question can be generalized, provide a reusable answer framework with selectable options.
- If the question requires personal facts, produce a fill-in template and ask for the missing details before claiming a final personal answer.

If an example is useful, label it as an "example project scenario" rather than the user's real project.

### Strategy Expansion Questions

When a project detail question points to a broad strategy space, expand it into common strategies, compare tradeoffs, and then provide a conservative answer the candidate can adapt.

For example, "How did you do multi-agent orchestration?" may cover:

- supervisor-worker orchestration
- planner-executor decomposition
- router-based routing
- graph/state-machine workflows
- tool-specialized agents
- critique/reflection loops
- human-in-the-loop checkpoints
- shared memory or blackboard coordination

Use a comparison table when strategies are numerous.

### Behavioral Questions

Use concise STAR-style answers. Keep the response credible and concrete. If the user's facts are missing, provide a template and a short list of details to fill in.

## Output Defaults

Default to Markdown unless the user asks for another format. For a full answer pack, create a Markdown document file and use `references/output-template.md` as the document structure.

For long packs, organize by topic and difficulty, then answer each question one by one with detailed explanations, spoken answers, and follow-up questions. Do not create an overall "quick memorization" or summary-memory section; interview preparation should remain question-by-question. Do not only answer in chat when the user asks for a pack, document, collection, output file, or organized answers; write a `.md` artifact and report its path.

Do not include a "Final Review Checklist" or equivalent quality checklist in the final document. Use review checklists internally only.

## Portability

Keep the workflow portable across AI coding and writing agents. Do not depend on Codex-only behavior unless the current environment explicitly provides it.

When adapting this skill to Claude Code, Cursor, Gemini CLI, ChatGPT custom instructions, or another agent system, read `references/agent-portability.md` and preserve:

- Trigger modes
- Source handling rules
- Question classification
- Project fact boundaries
- Output template
- Batch/depth rules
- Web-search and citation policy

For out-of-the-box use in other tools, copy the ready-made files from `assets/adapters/` or run `scripts/install_adapters.py` against a target project. If the target agent does not support Codex skills, convert this `SKILL.md` into that tool's persistent instruction format and keep `references/output-template.md` as a reusable template.

## Quality Bar

- Make answers sound like a strong candidate speaking in an interview.
- Output final user-facing content in Chinese unless the user explicitly requests another language.
- Prefer substantial answers over terse notes: each major question should include enough detail for learning, oral practice, and likely follow-up handling.
- Respect the minimum depth rules in `references/depth-and-quality.md`; do not compress full-pack answers into short notes.
- Include likely follow-up questions, because interviews usually probe depth.
- Mark uncertainty, assumptions, and version-sensitive claims.
- Avoid fake confidence and fabricated personal project facts.
- Keep copied source text minimal; paraphrase questions when possible and cite sources.
