# Interview Answer Pack Builder

`interview-answer-pack-builder` 是一个用于生成中文面试题参考答案文档的 AI skill。它可以从真实岗位面试题中整理问题，也可以直接回答用户贴出的题目，并输出结构化 Markdown 文档。

它的目标不是生成简短题解，而是生成可以真正用于复习、背诵和模拟面试的详尽答案包。

## 核心能力

- 搜索某个岗位、公司、技术栈或级别的真实面试题。
- 回答用户直接提供的面试题。
- 加工已有题库，完成分类、去重、分组和文档化输出。
- 自动区分知识题、场景题、项目细节题、策略扩展题和行为面问题。
- 对长题库进行分批处理，相关问题放在一起，避免上下文割裂。
- 支持多 agent 或多 worker 分批回答；不支持时按顺序模拟分批。
- 默认输出中文 Markdown 文档。
- 对项目题保持事实边界，不编造用户个人经历。

## 输出特点

默认输出内容全部使用中文，必要的技术术语、产品名、API 名、代码标识、URL 和来源标题保留原文。

完整答案包默认生成 `.md` 文件，而不是只在聊天中输出。推荐文件名：

- `interview-answer-pack.md`
- `<岗位>-interview-answer-pack.md`
- `<公司>-<岗位>-interview-answer-pack.md`
- `<主题>-interview-answer-pack.md`

最终文档不会输出 `Final Review Checklist`。质量检查只作为 agent 内部自检使用。

## 适用场景

### 1. 搜索岗位面试题

示例：

```text
帮我搜索 Java 后端 1-3 年的真实面试题，并整理成中文参考答案文档。
```

skill 会优先使用真实面经和题源，例如：

- 牛客 / Nowcoder
- 知乎
- 掘金
- CSDN
- 力扣 / LeetCode
- GitHub
- Glassdoor
- LeetCode Discuss

搜索结果会被去重、合并和分类。网上面经只作为题目来源，答案会尽量用官方文档、标准、论文、工程博客等更可靠来源校准。

### 2. 直接回答用户提供的题目

示例：

```text
请回答这些面试题，并输出 Markdown 文档：
1. Redis 为什么快？
2. MySQL 索引为什么用 B+Tree？
3. 线上接口突然变慢怎么排查？
```

如果用户直接贴题，默认不会额外搜索更多题目，但可以搜索权威资料来验证版本相关或事实性内容。

### 3. 加工已有题库

示例：

```text
我贴一批面试题，你帮我分类、去重、分组，然后生成详细参考答案文档。
```

超过 8 个问题时，skill 会先按主题分组，例如 Redis、MySQL、消息队列、分布式、项目深挖、AI agent 等，再分批生成和合并。

## 答案深度要求

除非用户明确要求简洁版，否则默认使用较详尽的答案标准：

| 题型 | 默认深度 |
| --- | --- |
| 普通知识题 | 500-800 中文字 |
| 高频核心知识题 | 1000-1500 中文字 |
| 场景题 | 900-1400 中文字 |
| 项目细节题 | 700-1200 中文字，不含填空模板 |
| 策略扩展题 | 1200-2000 中文字，并包含对比表 |
| 行为面问题 | 400-700 中文字 |

每个主要问题通常包含：

- 直接回答
- 核心原理
- 详细展开
- 面试口述版
- 高频追问
- 常见误区

## 项目题处理规则

项目题不会编造用户经历。

如果用户提供了项目事实，答案会基于这些事实展开。如果事实不足，skill 会输出可复用回答框架、可选策略或填空模板，并提示需要补充的信息。

常见需要补充的信息包括：

- 项目业务场景
- 技术栈
- 用户个人负责部分
- 核心模块
- 数据量或流量规模
- 主要技术难点
- 采用的方案
- 备选方案
- 结果或收益

## 在 Codex 中使用

将整个目录放到 Codex skills 目录中：

```text
C:\Users\YPB\.codex\skills\interview-answer-pack-builder
```

然后在 Codex 中直接调用：

```text
使用 $interview-answer-pack-builder，帮我整理 AI Agent 工程师岗位的真实面试题和参考答案，输出 Markdown 文档。
```

## 适配 Claude Code、Cursor、Gemini CLI

本 skill 附带开箱即用的适配文件：

```text
assets/adapters/AGENTS.md
assets/adapters/CLAUDE.md
assets/adapters/GEMINI.md
assets/adapters/.cursor/rules/interview-answer-pack-builder.mdc
```

可以用脚本安装到目标项目：

```powershell
python "C:\Users\YPB\.codex\skills\interview-answer-pack-builder\scripts\install_adapters.py" --target "你的项目路径"
```

默认会安装：

```text
AGENTS.md
CLAUDE.md
GEMINI.md
.cursor/rules/interview-answer-pack-builder.mdc
```

只安装 Claude Code 相关文件：

```powershell
python "C:\Users\YPB\.codex\skills\interview-answer-pack-builder\scripts\install_adapters.py" --target "你的项目路径" --tools agents,claude
```

只安装 Cursor rule：

```powershell
python "C:\Users\YPB\.codex\skills\interview-answer-pack-builder\scripts\install_adapters.py" --target "你的项目路径" --tools cursor
```

预览将要写入的文件：

```powershell
python "C:\Users\YPB\.codex\skills\interview-answer-pack-builder\scripts\install_adapters.py" --target "你的项目路径" --dry-run
```

覆盖已有文件：

```powershell
python "C:\Users\YPB\.codex\skills\interview-answer-pack-builder\scripts\install_adapters.py" --target "你的项目路径" --force
```

## 目录结构

```text
interview-answer-pack-builder/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── adapters/
│       ├── AGENTS.md
│       ├── CLAUDE.md
│       ├── GEMINI.md
│       └── .cursor/rules/interview-answer-pack-builder.mdc
├── references/
│   ├── agent-portability.md
│   ├── batching-and-depth.md
│   ├── depth-and-quality.md
│   ├── output-template.md
│   ├── project-background-template.md
│   └── search-strategy.md
└── scripts/
    └── install_adapters.py
```

## 校验

使用 Codex skill-creator 自带校验脚本：

```powershell
$env:PYTHONUTF8='1'
python "C:\Users\YPB\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "C:\Users\YPB\.codex\skills\interview-answer-pack-builder"
```

预期结果：

```text
Skill is valid!
```

## 注意事项

- 如果目标工具没有联网能力，角色检索模式会退化为用户提供题目或用户提供来源。
- 如果目标工具不能写文件，则应在聊天中输出完整 Markdown，并说明无法写入文件。
- 如果是项目题，不能伪装成用户真实经历；只能基于已知事实回答，或输出模板让用户补充。
- 如果答案涉及框架、数据库、语言版本差异，需要标注版本依赖或进行核验。
