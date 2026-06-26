# Batching and Depth

Use this reference for long question lists, role-search answer packs, or any request where short answers would be insufficient. Also read `depth-and-quality.md` for minimum length targets.

## Depth Standard

Default answers should be substantial enough to support both learning and interview practice. Meet or exceed the minimum depth targets in `depth-and-quality.md`.

For each major knowledge, scenario, project, or strategy question, include:

- A direct answer that states the conclusion.
- A detailed explanation that teaches the underlying mechanism or reasoning.
- A spoken interview answer that sounds natural and can be practiced aloud.
- At least 3 likely follow-up questions with short answers.
- Common mistakes, traps, or weak answers.
- Version notes, assumptions, or uncertainty when relevant.

For high-value or broad questions, expand further with:

- Tradeoffs.
- Examples.
- Comparison tables.
- Production considerations.
- "When to use / when not to use" guidance.

Avoid one-paragraph answers unless the user explicitly asks for a concise version.

## Grouping Rules

Before answering more than 8 questions, group them by topic and dependency:

- Language/runtime fundamentals.
- Database and storage.
- Cache and messaging.
- Distributed systems.
- System design.
- LLM, agents, RAG, or AI engineering.
- Project deep dive.
- Scenario and incident handling.
- Behavioral questions.

Keep related questions in the same batch. For example:

- Put "Redis why fast", "Redis persistence", "cache penetration", and "cache avalanche" together.
- Put "MySQL index", "B+Tree", "MVCC", and "transaction isolation" together.
- Put "multi-agent orchestration", "tool calling", "memory", and "human-in-the-loop" together.

Do not split a topic chain across workers if answers need shared definitions or consistent assumptions.

## Multi-Agent or Multi-Pass Workflow

If the environment supports subagents, parallel tasks, or multiple agent workers, use this workflow:

1. Create a question map with IDs, original question text, topic, type, difficulty, and source.
2. Deduplicate near-duplicate questions.
3. Split the question map into coherent topic batches.
4. Assign each batch to one worker with the same answering rules and output schema.
5. Require each worker to return Markdown sections, source notes, assumptions, and unresolved uncertainties.
6. Merge all worker outputs into one document.
7. Normalize terminology, heading levels, numbering, tone, and citations.
8. Remove duplicate explanations while keeping cross-references between related questions.
9. Run the final review checklist internally, but do not include it in the final document.

If the environment does not support subagents, run the same steps sequentially as separate passes.

## Worker Prompt Contract

When delegating a batch, provide only the relevant questions and shared global constraints:

```text
Answer this interview-question batch using the Interview Answer Pack Builder rules. Keep answers detailed, preserve technical terms, include spoken interview answers, add likely follow-ups, label assumptions, cite sources if provided, and do not invent project facts. Return Markdown sections only for the assigned question IDs.
```

For project batches, add:

```text
If project facts are missing, provide a reusable answer framework and fill-in template. Do not claim the candidate used a technology or achieved a result unless that fact was provided.
```

## Document Output Requirement

For full packs, create a Markdown file instead of only replying in chat.

Recommended filenames:

- `interview-answer-pack.md`
- `<role>-interview-answer-pack.md`
- `<company>-<role>-interview-answer-pack.md`
- `<topic>-interview-answer-pack.md`

The final response should include:

- The document path.
- A short summary of what was included.
- Any limitations, missing user facts, or search constraints.

If the target tool cannot write files, output a complete Markdown document in the response and state that file writing is unavailable.

## Merge Quality Checklist

Before final delivery, verify internally. Do not output this checklist in the final document:

- Every question ID appears exactly once in the final document.
- Related topics are adjacent or cross-referenced.
- The document contains detailed explanations, not only spoken answers.
- Scenario assumptions are labeled.
- Project facts are not fabricated.
- Source links are preserved where search was used.
- The final Markdown can stand alone as a study document.
