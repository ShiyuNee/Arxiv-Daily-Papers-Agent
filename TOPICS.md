# Topic 候选类别体系

> 本文件维护论文分类的 topic 候选列表。模型在分类时**优先使用已有 topic**，当论文无法归入任何现有 topic 时，**自动在此文件末尾追加新 topic**，并标注新增日期。
>
> **文件路径：** 项目根目录下的 `TOPICS.md`

---

## 🤖 Agent & LLM 应用

| Topic ID | Topic 名称 | 说明 |
|----------|-----------|------|
| agent-design | Agent 架构与设计 | Agent 框架、工具使用、规划策略、Multi-Agent 协作 |
| agent-rl | Agentic RL | Agent 的强化学习训练：环境交互、在线学习、reward 设计、tool-use RL、Agent 策略优化 |
| rl-reasoning | RL for Reasoning | 用强化学习提升 LLM 推理能力：GRPO、PPO for reasoning、过程奖励模型（PRM）、结果奖励模型（ORM）、reasoning RL |
| agent-safety | Agent 安全与对齐 | Agent 的安全约束、可控性、权限管理、对齐问题 |
| llm-reasoning | LLM 推理能力 | Chain-of-Thought、思维链、逻辑推理、数学推理、规划（纯文本，非 RL 驱动） |
| tool-use | 工具使用与 API 调用 | Tool learning、function calling、API 调用、工具增强 |
| code-gen | 代码生成与程序合成 | Code generation、代码理解、程序修复、代码补全 |

## 🧠 大模型核心

| Topic ID | Topic 名称 | 说明 |
|----------|-----------|------|
| llm-training | 大模型训练与微调 | 预训练、SFT、RLHF、DPO、参数高效微调 |
| llm-efficiency | 模型效率与压缩 | 量化、剪枝、蒸馏、稀疏化、推理加速 |
| llm-architecture | 模型架构与设计 | Transformer 变体、新架构、注意力机制改进、MoE |
| llm-knowledge | 知识与记忆 | 知识编辑、知识注入、RAG、记忆机制、长上下文 |
| llm-alignment | 对齐与安全 | RLHF、Constitutional AI、红队测试、价值观对齐、越狱防御 |
| llm-evaluation | 大模型评测 | Benchmark、评测方法论、能力评估 |
| llm-interpret | 可解释性与机理 | Mechanistic interpretability、表征分析、电路分析 |

## 📝 NLP 基础任务

| Topic ID | Topic 名称 | 说明 |
|----------|-----------|------|
| nlg | 文本生成 | 对话生成、故事生成、风格控制、摘要生成 |
| ner-re | 信息抽取 | 命名实体识别、关系抽取、事件抽取 |
| nlu | 自然语言理解 | 语义分析、话语分析、意图识别 |
| mt | 机器翻译 | 翻译质量、低资源翻译、多语言翻译 |
| dialogue | 对话系统 | 任务型对话、开放域对话、对话状态追踪 |

## 🔍 检索与信息获取

| Topic ID | Topic 名称 | 说明 |
|----------|-----------|------|
| retrieval-model | 检索模型与排序 | 稠密检索、稀疏检索、重排序、检索增强 |
| rag | RAG | 检索增强生成、知识增强、检索-生成联合优化 |
| ir-evaluation | 信息检索评测 | IR 评测基准、相关性标注、评测指标 |

## 🌍 多模态

| Topic ID | Topic 名称 | 说明 |
|----------|-----------|------|
| vlm | 视觉语言模型 | 多模态大模型、视觉问答、图文理解 |
| multimodal-gen | 多模态生成 | 文生图、文生视频、多模态内容创作 |
| multimodal-agent | 多模态 Agent | 多模态 Agent 架构：视觉导航、GUI Agent、具身智能、多模态工具使用（非 RL 训练） |
| multimodal-agent-rl | 多模态 Agentic RL | 多模态场景下的 Agent 强化学习：视觉交互 RL、多模态 reward 设计、多模态环境中的在线学习 |
| multimodal-reasoning | 多模态推理 | 多模态场景下的推理能力：视觉推理、图文推理、多模态 Chain-of-Thought、视频理解推理 |
| audio-speech | 语音与音频 | 语音识别、语音合成、音频理解 |

## 📊 数据与知识

| Topic ID | Topic 名称 | 说明 |
|----------|-----------|------|
| data-quality | 数据质量与构建 | 数据筛选、数据去重、数据合成、数据增强 |
| knowledge-graph | 知识图谱 | 知识图谱构建、推理、与 LLM 结合 |
| benchmark | 基准与数据集 | 新 benchmark、数据集贡献 |

## 🔬 其他

| Topic ID | Topic 名称 | 说明 |
|----------|-----------|------|
| prompt-engineering | 提示工程 | Prompt 设计、ICL、CoT 提示优化 |
| llm-app | LLM 应用 | 教育、法律、金融、科学发现等应用场景 |
| multilingual | 多语言与跨语言 | 多语言处理、低资源语言、跨语言迁移 |
| llm-uncertainty | LLM 不确定性 | 不确定性量化、校准、幻觉检测 |
| diffusion-lm | 扩散语言模型 | 扩散模型用于文本生成、训练加速、安全生成 |
| other | 其他 | 无法归入以上类别的论文 |

---

## 🆕 新增 Topic 记录

> 以下为运行过程中自动扩充的 topic，每条标注新增日期和当日归入的论文数。

| llm-uncertainty | LLM 不确定性 | 不确定性量化、校准、幻觉检测 | 2026-05-14 | 2 |
| diffusion-lm | 扩散语言模型 | 扩散模型用于文本生成、训练加速、安全生成 | 2026-05-14 | 2 |

<!-- 新增格式：
| topic-id | Topic 名称 | 说明 | 新增日期 | 当日论文数 |
|----------|-----------|------|---------|-----------|
| example | 示例 | ... | 2026-05-12 | 3 |
-->