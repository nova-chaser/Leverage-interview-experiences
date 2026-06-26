# Project Background Template

Use this reference when questions ask about the user's own project and important facts are missing.

## Do Not Fabricate

Never claim the user personally built, owned, measured, deployed, or optimized something unless the user provided that fact. If an example is helpful, label it as an "example project scenario".

## Minimum Project Facts

Collect or infer only when safe:

| Field | Purpose |
| --- | --- |
| Project name or short label | Keeps answers concrete |
| Business scenario | Explains why the system exists |
| Target users | Clarifies scale and constraints |
| Tech stack | Grounds implementation details |
| User's responsibility | Prevents overclaiming ownership |
| Core modules | Supports project deep-dive answers |
| Data scale or traffic | Supports architecture and performance claims |
| Main technical challenge | Makes the answer interview-worthy |
| Chosen solution | Connects problem to implementation |
| Alternatives considered | Supports tradeoff questions |
| Observed result | Enables credible impact statements |
| Failure or incident experience | Supports scenario follow-ups |

## Fast Clarifying Questions

Ask only the questions needed to avoid fabrication. Use at most 5 at once:

- What was the project business scenario?
- What tech stack did you use?
- Which part did you personally implement?
- What was the hardest technical problem?
- Do you have any scale or result numbers, even approximate ones?

If the user does not answer, provide a fill-in template and optional example scenario.

## Fill-In Answer Skeleton

Use this structure for project questions:

```markdown
**Known Facts**
<facts provided by user>

**Missing Facts**
<facts needed before claiming a final personal answer>

**Safe Answer Framework**
In this project, the background was [business scenario]. I was mainly responsible for [module/responsibility]. We chose [technology/strategy] because [reason]. The implementation was roughly [key steps]. The main tradeoff was [tradeoff], so we added [monitoring/fallback/test/limit]. The final result was [observable result].

**Options You Can Choose From**
- If the goal was performance: emphasize caching, indexing, async processing, batching, or load shedding.
- If the goal was reliability: emphasize idempotency, retries, circuit breakers, compensation, monitoring, and rollback.
- If the goal was AI-agent quality: emphasize tool routing, memory, state management, evaluation, human review, and fallback.
- If the goal was maintainability: emphasize modular boundaries, workflow orchestration, tests, and observability.

**Example Project Scenario**
This is fictional and should be replaced with the user's real facts:
<example>
```

## Project Question Handling

For "why did you choose X":

- Explain the problem first.
- Compare at least 2 alternatives.
- Explain why X matched the constraints.
- Mention tradeoffs and mitigation.

For "how did you implement X":

- Describe architecture.
- Describe data flow.
- Describe failure handling.
- Describe monitoring and testing.
- Avoid exact metrics unless provided.

For "what was difficult":

- Choose one real technical challenge.
- Explain why it was difficult.
- Explain the solution path.
- Explain what was learned or improved.
