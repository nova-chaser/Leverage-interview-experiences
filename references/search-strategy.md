# Search Strategy

Use this reference in role search mode.

## Search Inputs

Infer or ask for these fields when they materially affect the result:

- Target role, such as Java backend, Python backend, AI agent engineer, data engineer, frontend, SRE, or algorithm engineer.
- Seniority, such as intern, campus hire, 1-3 years, 3-5 years, senior, or staff.
- Tech stack, such as Java/Spring, Python/FastAPI, Go, Redis, MySQL, Kafka, LangGraph, RAG, or multi-agent systems.
- Company or company type, such as ByteDance, Alibaba, Tencent, startup, bank, SaaS, or AI company.
- Region and language, such as China/Chinese or US/English.

If these are missing and the user wants quick output, default to campus hire to 1-3 years, broad backend/AI engineering questions, and state the assumption.

## Priority Sources

Use source groups according to language and target market.

Chinese role-search sources:

- Nowcoder/Niuke (`nowcoder.com`) for interview experiences and company-specific question lists.
- Xiaohongshu (`xiaohongshu.com`) when users ask for recent informal interview experiences; treat posts as weak evidence.
- Zhihu (`zhihu.com`) for long-form interview experience summaries; verify technical claims elsewhere.
- CSDN (`csdn.net`) and Juejin (`juejin.cn`) for compiled question lists; treat as secondary sources.
- LeetCode China/Likou (`leetcode.cn`) for algorithm and coding interview patterns.
- GitHub repositories for curated interview notes; check freshness and stars only as weak quality signals.

English/global sources:

- LeetCode Discuss (`leetcode.com/discuss`) for interview experiences and coding patterns.
- Glassdoor for company interview reports when accessible.
- Blind and Reddit for informal reports; treat as weak evidence and paraphrase carefully.
- GitHub repositories for curated interview handbooks.
- Official docs, engineering blogs, standards, and papers for answer verification.

Do not rely on a single platform. For role-search packs, try to collect from at least 3 source groups when available.

## Search Query Templates

Use combinations like:

```text
<company> <role> 面经 <year>
<company> <role> 面试题 <tech stack>
<role> 校招 面经 <tech stack>
<role> 社招 面经 <tech stack>
site:nowcoder.com <company> <role> 面经
site:juejin.cn <role> 面试题 <tech stack>
site:csdn.net <role> 高频面试题 <tech stack>
site:leetcode.cn <company> 面试题
<company> <role> interview questions <year>
site:leetcode.com/discuss <company> <role> interview
site:github.com <role> interview questions <tech stack>
```

Use the current year and the previous 1-2 years for recent role trends. If the user asks for historical breadth, include older sources and label them.

## Filtering and Deduplication

Keep a question if it is:

- Repeated across multiple sources.
- Clearly tied to a role, company, or real interview experience.
- A common high-frequency foundation topic for the target role.
- A scenario or project-deep-dive question likely to appear in real interviews.

Drop or merge questions if they are:

- Duplicate wording of the same topic.
- Too vague without adding interview value.
- Pure clickbait or copied lists with no source trace.
- Unsupported claims about a company's exact interview process.

Represent merged questions as one canonical question and list multiple sources.

## Answer Verification

Use interview posts to discover questions. Use stronger sources to answer:

- Official documentation for frameworks, databases, languages, and cloud services.
- Standards or specifications for protocols and language behavior.
- Research papers for LLM, RAG, and agent concepts.
- Reputable engineering blogs for production practices.

If sources conflict, state the uncertainty and version dependency.
