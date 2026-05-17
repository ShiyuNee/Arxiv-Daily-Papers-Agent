# cs.CL 论文整理 - 2026-05-14

**整理时间**: 2026-05-17
**论文总数**: 106
**排除**: 7（多语言/特定语言 5 篇，医学/临床 2 篇）
**Topic 数量**: 16

---

## 📋 今日研究动态总览

| Topic | 论文数 | 核心关键词 |
|-------|--------|-----------|
| LLM 推理能力 | 8 | reasoning, olympiad, CoT-ICL, test-time, process supervision |
| Agent 架构与设计 | 8 | multi-agent, tool-calling, workflow, persona simulation, memory |
| 大模型训练与微调 | 8 | SFT, distillation, pretraining, data selection, low-rank |
| 对齐与安全 | 7 | misalignment, guardrail, persuasion, fairness, reward hacking |
| 可解释性与机理 | 6 | persona vector, circuit discovery, attention, hidden state, representation |
| 模型架构与设计 | 5 | MoE, diffusion LM, linear attention, phasor memory, tokenization |
| LLM 评测 | 5 | judge, creativity, benchmark, annotation, evaluation |
| RAG | 4 | retrieval-augmented, evidence selection, knowledge graph, context training |
| Agentic RL | 4 | GRPO, credit assignment, reward decomposition, multi-turn RL |
| RL for Reasoning | 3 | verifiable reward, visual RL, process reward |
| 多模态推理 | 3 | VLM calibration, omnimodal grounding, vision-language reasoning |
| 多模态 Agent | 3 | VLN, GUI, embodied coordination |
| 信息抽取 | 3 | entity linking, taxonomy, argument reconstruction |
| 文本生成 | 3 | story generation, refinement, grammatical error correction |
| LLM 应用 | 4 | law, education, finance, search |
| 其他 | 5 | uncertainty, diffusion LM safety, social network, NLP parsing, logical structure |

---

## 🧠 LLM 推理能力（llm-reasoning）— 8 篇

**今日动态：** 今日推理方向重点关注：长思维链效率优化、测试时自适应、过程监督与推理校准。STOP和QueST分别从推理剪枝和测试时自训练角度提升推理效率，VPS和PDCR聚焦推理过程中的质量校准。CDS重新审视many-shot CoT-ICL的scaling行为。

- [#5] **Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry** — Tyler Alvarez, Ali Baheri
  - **[一句话总结领域]**: 推理幻觉步级检测
  - **[TL;DR]**: 问题：LLM多步推理中幻觉检测仅能在trace级别打分，无法定位首错步骤且需多次采样。方法：提出基于隐藏状态传输几何的步级检测框架，用对比PCA教师模型和BiLSTM学生模型分别实现标签条件和无标签的首错定位，证明对比PCA是传输分离目标的最优投影，在ProcessBench等数据集上超越基线。

- [#16] **Many-Shot CoT-ICL: Making In-Context Learning Truly Learn** — Tsz Ting Chung, Lemao Liu, Mo Yu, Dit-Yan Yeung
  - **[一句话总结领域]**: 多样本CoT上下文学习
  - **[TL;DR]**: 问题：many-shot CoT-ICL在推理任务上的scaling行为未被理解，标准many-shot规则不适用于推理场景。方法：提出CDS（曲率演示选择），将many-shot CoT-ICL重新框架为上下文测试时学习，发现演示应易于模型理解且按概念进展排序，CDS在几何推理上带来5.42pp提升。

- [#27] **Query-Conditioned Test-Time Self-Training for Large Language Models** — Chaehee Song, Minseok Seo, Yeeun Seong, Doyi Kim, Changick Kim
  - **[一句话总结领域]**: 测试时自适应
  - **[TL;DR]**: 问题：现有测试时优化方法依赖外部数据或使用通用自监督目标，缺乏查询特定的对齐。方法：提出QueST，从输入查询本身生成结构相关的问答对作为监督信号，在推理时进行参数高效微调实现查询特定适应，7个数学推理基准和GPQA-Diamond上均超越强基线。

- [#40] **STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes** — Chenjun Xu, Zhennan Zhou, Zhan Su, Bill Howe, Lucy Lu Wang, Bingbing Wen
  - **[一句话总结领域]**: 推理链剪枝
  - **[TL;DR]**: 问题：长CoT推理导致overthinking，增加推理成本和延迟，低数据微调场景下无法依赖大规模教师蒸馏。方法：提出STOP，通过节点分割、分类标注和推理树构建将轨迹结构化，引入ECN保留最短正确前缀，在DeepSeek-R1蒸馏模型上减少19.4-42.4%生成token同时保持精度。

- [#67] **Correct Answers from Sound Reasoning: Verifiable Process Supervision for Language Models** — Kyuyoung Kim, Kevin Wang, Yunfei Xie, Peiyang Xu, Peiyao Sheng, Chen Wei, Zhangyang Wang, Jinwoo Shin, Pramod Viswanath, Sewoong Oh
  - **[一句话总结领域]**: 过程监督强化学习
  - **[TL;DR]**: 问题：仅优化最终结果的RL会让推理准确性提升但推理质量退化，国际象棋上赢得走法增加推理赢率误差最高112%。方法：提出VPS，对可验证领域联合优化预测准确性和推理质量，用自适应奖励加权优先处理误差最大的推理子任务，推理赢率误差降低30%、一致性恢复至近饱和。

- [#87] **Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling** — Yafu Li, Runzhe Zhan, Haoran Zhang 等
  - **[一句话总结领域]**: 奥赛级推理
  - **[TL;DR]**: 问题：将推理模型转换为奥赛级求解器需要复杂的定制流程。方法：提出简单统一方案，先用逆困惑度课程SFT注入严格证明搜索和自检行为，再经两阶段RL（可验证奖励RL→证明级RL）扩展，最后测试时scaling，30B-A3B模型SU-01在IMO 2025/USAMO 2026和IPhO 2024/2025达到金牌水平。

- [#94] **When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction** — Vardhan Dongre, Joseph Hsieh, Viet Dac Lai, Seunghyun Yoon, Trung Bui, Dilek Hakkani-Tür
  - **[一句话总结领域]**: 多轮推理退化机理
  - **[TL;DR]**: 问题：LLM在多轮交互中逐渐丢失指令/角色/规则，但缺少机制性解释。方法：提出通道转移框架，用GAR指标量化生成token对目标token的注意力，发现注意力关闭时信息仍可在残差流中残留，Mistral强制关闭注意力通道后召回率从近完美降至11%，线性探针可从残差表征以AUC 0.99预测结果。

- [#8] **RTLC: Research, Teach-to-Learn, Critique — A three-stage prompting paradigm** — Andrea Morandi
  - **[一句话总结领域]**: LLM评判推理
  - **[TL;DR]**: 问题：LLM-as-judge在客观正确性配对评判上几乎随机（JudgeBench上强模型也难以超越随机）。方法：提出RTCL三阶段提示范式（Research→Teach-to-Learn→Critique），将费曼学习法迁移到LLM提示+N=10独立候选+交叉比较批判，Claude 3.7 Sonnet配对准确率从64.6%提升至78.6%，绝对提升14pp。

---

## 🤖 Agent 架构与设计（agent-design）— 8 篇

**今日动态：** 今日Agent方向涵盖多Agent协作通信、工作流编译优化、反思式记忆搜索、工具调用合成、个性化Agent记忆和结构化规划。趋势是从单Agent向更高效通信协议和结构化记忆组织演进。

- [#2] **Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights** — Wenrui Bao, Huan Wang, Jian Wang 等
  - **[一句话总结领域]**: 多Agent通信架构
  - **[TL;DR]**: 问题：多Agent LLM系统通过自然语言消息通信，需序列化/反序列化导致token开销大、KV-cache内存高。方法：提出TFlow权重空间通信框架，将发送方隐藏状态编译为接收方特定的低秩LoRA扰动，仅在接受方生成时临时施加，三个Qwen3-4B Agent在5个基准上最高提升8.5个准确率点，同时减少83.27%处理token和4.6倍推理时间。

- [#10] **FlowCompile: An Optimizing Compiler for Structured LLM Workflows** — Junyan Li, Zhang-Wei Hong, Maohao Shen, Yang Zhang, Chuang Gan
  - **[一句话总结领域]**: LLM工作流优化编译
  - **[TL;DR]**: 问题：结构化LLM工作流中子Agent配置选择空间组合爆炸，现有方法将工作流优化视为路由问题而非编译优化。方法：提出FlowCompile，借鉴ML编译器思路，将工作流分解为子Agent分别profile，通过结构感知代理估计精度和延迟，编译时一次性发现高质量配置集，最高6.4倍加速。

- [#17] **R²-Mem: Reflective Experience for Memory Search** — Xinyuan Wang, Wenyu Mao, Junkang Wu, Xiang Wang, Xiangnan He
  - **[一句话总结领域]**: Agent记忆搜索
  - **[TL;DR]**: 问题：深度搜索Agent重复过去的错误搜索行为，无法从历史轨迹中学习高质量/低质量步骤的区别。方法：提出R²-Mem，离线阶段用评分标准评估器对步骤打分、自反思学习器提炼抽象经验，在线时检索经验指导搜索避免重复错误，F1最高提升22.6%，token消耗减少12.9%，搜索迭代减少20.2%。

- [#34] **CANTANTE: Optimizing Agentic Systems via Contrastive Credit Attribution** — Tom Zehle
  - **[一句话总结领域]**: 多Agent系统优化
  - **[TL;DR]**: 问题：LLM多Agent系统配置自动化困难，系统级分数可用但参数是局部的，信用分配是核心挑战。方法：提出CANTANTE，通过对比同一查询上多个联合配置的推演将系统级奖励分解为每Agent更新信号，用于prompt优化，在MBPP上比最强基线提升18.9pp，GSM8K上提升12.5pp。

- [#48] **Context Training with Active Information Seeking** — Zeyu Huang, Adhiguna Kuncoro, Qixuan Feng, Jiajun Shen, Lucio Dery, Arthur Szlam, Marc'Aurelio Ranzato
  - **[一句话总结领域]**: 上下文优化与主动搜索
  - **[TL;DR]**: 问题：现有上下文优化方法闭环依赖模型自身知识，无法获取新信息。方法：为上下文优化器配备Wikipedia搜索和浏览器工具进行主动信息搜索，配合保持多候选上下文并剪枝的搜索训练程序，在低资源翻译、健康场景和推理任务上一致提升，生成的文本上下文可跨模型泛化。

- [#65] **ToolWeave: Structured Synthesis of Complex Multi-Turn Tool-Calling Dialogues** — Dinesh Khandelwal, Gnana Prakash Punnavajhala 等
  - **[一句话总结领域]**: 工具调用数据合成
  - **[TL;DR]**: 问题：多轮工具调用训练数据合成困难，现有流水线产生的对话工具仅表面兼容且一步生成导致参数幻觉。方法：提出ToolWeave，通过构建内置依赖关系的工具和细粒度规划阶段追踪参数来源，合成对话含45%多步交互（vs之前<20%），参数幻觉更少，Llama-3.1-70B在BFCL-V3多轮达39.75%（vs SOTA的23.50%）。

- [#82] **Cognifold: Always-On Proactive Memory via Cognitive Folding** — Suli Wang, Yiqun Duan, Yu Deng 等
  - **[一句话总结领域]**: Agent主动记忆
  - **[TL;DR]**: 问题：现有Agent记忆主要是被动检索式，无法将经验自主组织为持久认知结构。方法：提出Cognifold，受互补学习系统理论启发扩展为三层（海马体、新皮层、前额叶意图层），通过图拓扑自组织实现认知结构主动组装、语义相似合并、过时衰减和关联重链，在CogEval-Bench上独有地产生匹配认知期望的记忆结构。

- [#97] **Beyond Cooperative Simulators: Generating Realistic User Personas for Robust Evaluation of LLM Agents** — Harshita Chopra, Kshitish Ghate 等
  - **[一句话总结领域]**: Agent用户模拟
  - **[TL;DR]**: 问题：LLM用户模拟器继承模型合作和同质化倾向，导致Agent在模拟中表现强但面对真实用户失败。方法：提出Persona Policies（PPol），将persona生成建模为LLM驱动的进化程序搜索，优化Python生成器发现行为并转化为任务保持的角色策略，盲评中80.4%被评为人，训练后Agent任务成功率提升17%。

---

## 🎓 大模型训练与微调（llm-training）— 8 篇

**今日动态：** 训练与微调方向关注：推理链自蒸馏优化、数据选择与配比、低秩预训练分析、SFT数据配方搜索。趋势是从简单的top-k数据选择转向可执行配方搜索，以及对训练动态的更深层理解。

- [#11] **Prefix Teach, Suffix Fade: Local Teachability Collapse in Strong-to-Weak On-Policy Distillation** — Kaiyuan Liu, Ziyuan Zhuang 等
  - **[一句话总结领域]**: 知识蒸馏
  - **[TL;DR]**: 问题：强到弱on-policy蒸馏中，后半段轨迹虽有教师-学生优势但缺少局部对比度，密集反馈不再有效。方法：提出局部可教性崩溃概念和轨迹特定释放规则，用教师对student top-K候选集的margin聚合到句子片段，BIC式变点检测截断监督，在Qwen3家族强到弱蒸馏任务上一致超越全轨迹OPD。

- [#41] **AcquisitionSynthesis: Targeted Data Generation using Acquisition Functions** — Ishika Agarwal, Sofia Stoica 等
  - **[一句话总结领域]**: 数据合成
  - **[TL;DR]**: 问题：合成数据生成缺乏定量方法衡量生成样本对下游学习者的影响，拒绝采样和课程方法无法精确量化数据效用。方法：提出AcquisitionSynthesis，用采集函数作为奖励模型训练LM生成更高质量合成数据，学生模型在分布内任务提升2-7%，对灾难性遗忘更鲁棒，且可为其他模型和不同资源量级生成数据。

- [#42] **GateKD: Confidence-Gated Closed-Loop Distillation for Robust Reasoning** — Kasidit Sermsri, Teerapong Panboonyuen
  - **[一句话总结领域]**: 推理蒸馏
  - **[TL;DR]**: 问题：现有推理蒸馏方法以开环方式运行，假设教师统一可靠，传播错误中间推理。方法：提出GateKD，引入置信门控软监督、门控隐藏状态演化和可靠性过滤注意力蒸馏三个闭环机制，教师置信度持续调制蒸馏过程，T5和Flan-T5上在逻辑和符号推理基准上持续超越开环基线。

- [#74] **Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training** — Namrata Shivagunde, Vijeta Deshpande 等
  - **[一句话总结领域]**: 低秩预训练分析
  - **[TL;DR]**: 问题：低秩预训练方法是否产生泛化可比的模型，还是限制根本改变了收敛解？现有比较仅用困惑度，而困惑度是解质量的差代理。方法：从4个维度（1D损失景观、检查点插值、权重/更新谱结构、激活相似度）评估5种低秩方法，发现低秩方法即使困惑度接近也不等价于全秩训练，各方法收敛到几何不同的盆地。

- [#93] **From Instance Selection to Fixed-Pool Data Recipe Search for Supervised Fine-Tuning** — Haodong Wu, Jiahao Zhang, Lijie Hu, Yongqi Zhang
  - **[一句话总结领域]**: SFT数据选择
  - **[TL;DR]**: 问题：SFT数据选择常被表述为实例排序（每例评分取top-k），但有效SFT子集通常来自有序配比流水线（过滤+混合+去重）。方法：提出固定池数据配方搜索问题，引入AutoSelection双层求解器，用缓存信号做材料化、热探针、局部配方编辑和高斯过程辅助排序，在90K指令池上取得最强分布内推理平均。

- [#6] **Dense vs Sparse Pretraining at Tiny Scale** — Abdalrahman Wael
  - **[一句话总结领域]**: 稠密vs稀疏预训练
  - **[TL;DR]**: 问题：MoE和稠密模型在极小规模预训练中性能对比未被系统研究。方法：在LLaMA风格解码器下，控制优化器/数据/深度等变量，用4专家top-2路由Switch负载平衡的MoE对比稠密模型，在<25M参数下MoE在活跃参数匹配下优于稠密（val loss差距0.076），但在总参数匹配下稠密仍优。

- [#103] **Scaling Laws for Mixture Pretraining Under Data Constraints** — Anastasiia Sedova, Skyler Seto 等
  - **[一句话总结领域]**: 混合预训练scaling law
  - **[TL;DR]**: 问题：混合稀缺目标数据与充裕通用数据训练时，目标数据太少则欠暴露，太多则过度重复导致收益递减和过拟合。方法：跨2000+训练运行研究这一权衡，发现混合训练可容忍15-20次重复，提出重复感知混合scaling law，考虑重复token递减价值和通用数据正则化作用，提供数据约束下的最优配比建议。

- [#21] **Pretraining Language Models with Subword Regularization: An Empirical Study of BPE Dropout in Low-Resource NLP** — Ruan Visser, Trienko Grobler, Marcel Dunaiski
  - **[一句话总结领域]**: 预训练分词正则化
  - **[TL;DR]**: 问题：BPE dropout通常只在微调时使用，预训练用确定性分词导致与微调的分词不匹配。方法：在低资源NLP中研究预训练时使用BPE dropout的效果，发现预训练和微调同时使用随机分词效果最好，预训练时BPE dropout在预训练或微调数据稀缺时收益最大，对齐分词通过更好形态边界带来下游收益。

---

## 🛡️ 对齐与安全（llm-alignment）— 7 篇

**今日动态：** 安全对齐方向重点关注：missalignment的机理分析（数据介导迁移、人格模型崩塌）、安全护栏绕过（LLM说服攻击）和推理时对齐方法。趋势是从现象观察深入到因果机制。

- [#3] **Negation Neglect: When models fail to learn negations in training** — Harry Mayne, Lev McKinney 等
  - **[一句话总结领域]**: 否定学习缺陷
  - **[TL;DR]**: 问题：微调时在否定文档上训练（如"Ed Sheeran未获金牌"被标记为假）会让模型相信声明为真，即使文档中每句都标注声明为假。方法：发现否定忽视现象在所有测试模型（Kimi K2.5、GPT-4.1、Qwen3.5）中均存在，当否定局部于声明本身（"未获金牌"）时模型大多能正确学习，但而非局部否定（独立句子说"这是假的"）则不行，该效应源于表示为真的归纳偏置。

- [#30] **LLM-Based Persuasion Enables Guardrail Override in Frontier LLMs** — Rodrigo Nogueira, Thales Sales Almeida 等
  - **[一句话总结领域]**: 安全护栏绕过
  - **[TL;DR]**: 问题：前沿LLM有强护栏会拒绝有害请求，但用另一个LLM作为攻击者通过自然语言说服能否绕过？方法：让攻击者LLM在5轮对话中使用同行比较说服、认知义务重构等论证策略，9个攻击-目标配对在6个科学共识话题上全部产生非零引出率，Opus攻击Opus平均65%话题产出目标文章。

- [#56] **Persona-Model Collapse in Emergent Misalignment** — Davi Bastos Costa, Renato Vicente
  - **[一句话总结领域]**: 涌现对齐失败的机理
  - **[TL;DR]**: 问题：微调含窄域有害内容的LLM会导致广泛的对齐失败（涌现missalignment），但缺乏行为层面的机制解释。方法：提出人格模型崩塌假设，用道德 susceptibility(S)和 robustness(R)两个指标量化模型区分和维持角色的能力，不安全微调使S平均增加55%、R降低65%（1/R增加304%），而安全微调仅部分影响R。

- [#84] **Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution** — Xiaozhe Zhang, Chaozhuo Li 等
  - **[一句话总结领域]**: 终身安全防御
  - **[TL;DR]**: 问题：现有安全范式将红队和后训练闭环耦合，攻击发现快速饱和，防御低效僵化难以跨模型迁移。方法：提出EvoSafety，攻击端用对抗技能库持续扩展漏洞探测，防御端用轻量辅助防御模型+记忆检索替代模型特定微调，Guard模式达99.61%防御成功率（超Qwen3Guard-8B 14.13%，仅用37.5%参数）。

- [#49] **Adaptive Steering and Remasking for Safe Generation in Diffusion Language Models** — Yejin Lee, Yo-Sub Han
  - **[一句话总结领域]**: 扩散语言模型安全生成
  - **[TL;DR]**: 问题：扩散语言模型迭代去噪过程中有害token会在中间步骤传播并最终诱导不安全输出，现有方法要么无法生成安全输出要么安全但质量低。方法：提出对比安全方向（SGD）捕获有害/安全生成的语义边界，每步去噪评估token与有害语义的对齐度，检测到对齐时重新掩码并自适应引导，越狱率降至0.64%且保持生成质量。

- [#77] **Temper and Tilt Lead to SLOP: Reward Hacking Mitigation with Inference-Time Alignment** — Ye Wang, Jing Liu, Toshiaki Koike-Akino
  - **[一句话总结领域]**: 推理时对齐与奖励黑客缓解
  - **[TL;DR]**: 问题：推理时对齐技术虽轻量但容易遭遇奖励黑客（reward hacking）。方法：引入参考模型温度调整推广推理时对齐到生成式奖励模型集合SLOP（锐化对数意见池），提出SLOP权重参数校准算法缓解奖励黑客，在保持对齐性能的同时提高鲁棒性。

- [#101] **Emergent and Subliminal Misalignment Through the Lens of Data-Mediated Transfer** — Baris Askin, Muhammed Ustaomeroglu 等
  - **[一句话总结领域]**: 涌现/潜隐missalignment的数据介导迁移
  - **[TL;DR]**: 问题：涌现missalignment被视为有害微调的直接后果，但对数据结构和训练渠道的作用理解不足。方法：以数据介导迁移视角分析，发现missalignment更易在微调和评估共享功能结构时出现、提示留有有害补全空间时出现、目标行为被更可靠学习时出现，首次比较off-policy和on-policy蒸馏在潜隐学习中的角色。

---

## 🔬 可解释性与机理（llm-interpret）— 6 篇

**今日动态：** 机理可解释性方向重点关注persona向量的训练追踪、电路发现的非唯一性、LLM偏好的内部表征、以及层表征动态。趋势是从静态探测转向训练过程中的动态追踪。

- [#29] **Probing Persona-Dependent Preferences in Language Models** — Oscar Gilg, Pierre Beckmann, Daniel Paleka, Patrick Butlin
  - **[一句话总结领域]**: LLM偏好内部表征
  - **[TL;DR]**: 问题：LLM的偏好是否在不同人格下共享内部机制？方法：在Gemma-3-27B和Qwen-3.5-122B的残差流上训练线性探针预测配对选择，发现真正的偏好向量跨人格共享——在helpful assistant上训练的探针能预测和操控邪恶人格的选择（偏好反相关）。

- [#32] **Tracing Persona Vectors Through LLM Pretraining** — Viktor Moskvoretskii, Dominik Glandorf 等
  - **[一句话总结领域]**: persona向量的预训练追踪
  - **[TL;DR]**: 问题：persona向量（evil、sycophancy等特征对应的方向）如何在训练过程中形成？方法：在OLMo-3-7B预训练过程中追踪persona向量，发现它们在0.22%预训练时即形成且对调优后的instruct模型仍有效，虽然核心表征早期形成但几何和语义持续精炼，在Apertus-8B上定性复现。

- [#59] **All Circuits Lead to Rome: Rethinking Functional Anisotropy in Circuit and Sheaf Discovery for LLMs** — Xi Chen, Mingyu Jin 等
  - **[一句话总结领域]**: 电路发现非唯一性
  - **[TL;DR]**: 问题：电路/束发现（CSD）隐含假设功能定位于唯一或近唯一内部机制（功能各向异性假设）。方法：提出Overlap-Aware Sheaf Repulsion方法发现同一任务可被多个结构不同但同样忠实、稀疏、完整的电路支持，发现超稀疏三边束中无 indispensabile 边，提出分布式稠密电路假说解释非唯一低重叠电路解。

- [#14] **Inducing Artificial Uncertainty in Language Models** — Sophia Hager, Simon Zeng, Nicholas Andrews
  - **[一句话总结领域]**: 人工不确定性诱导
  - **[TL;DR]**: 问题：高性能LLM在训练数据上过度自信，难以找到足够的不确定性数据训练不确定性量化方法。方法：提出人工不确定性诱导问题，在简单数据上人工创建不确定性（无真实挑战数据时），在这个人工不确定性上训练的探针在识别真实不确定性上超越无人工不确定性训练的探针，校准度显著提升。

- [#104] **Layer-wise Representation Dynamics: An Empirical Investigation Across Embedders and Base LLMs** — Jingzhou Jiang, Yi Yang, Kar Yan Tam
  - **[一句话总结领域]**: 层表征动态分析
  - **[TL;DR]**: 问题：语言模型隐藏状态跨层变化显著，但现有层分析只关注单一维度。方法：提出LRD框架（Frenet全局子空间运动+NRS局部近邻保持+GFMI与最终层对齐），在31个模型30个MTEB任务上揭示架构和任务差异，端到端子空间位移与下游性能正相关最强，GFMI是唯一在15%/20%预算下超越随机剪枝的指标。

- [#92] **Controlling Logical Collapse in LLMs via Algebraic Ontology Projection over F2** — Hisashi Miyashita
  - **[一句话总结领域]**: 逻辑一致性代数控制
  - **[TL;DR]**: 问题：LLM是否在内部编码形式可验证的代数结构来表示本体论关系？方法：提出代数本体投影（AOP），将LLM隐藏状态投影到Galois域F2并施加Liskov替换约束，仅42个关系对作为代数密钥即达93.33%零样例包含准确率，发现系统提示+指令微调可防止后期逻辑崩塌，7/10条件出现此崩塌。

---

## 🏗️ 模型架构与设计（llm-architecture）— 5 篇

**今日动态：** 架构方向关注MoE与稠密模型对比、扩散语言模型训练加速、线性注意力改进、显式记忆架构和分词对上下文的影响。

- [#64] **Differences in Text Generated by Diffusion and Autoregressive Language Models** — Zeyang Zhang, Chengwei Liang 等
  - **[一句话总结领域]**: 扩散vs自回归文本生成差异
  - **[TL;DR]**: 问题：扩散语言模型（DLM）和自回归模型（ARM）生成的文本内在差异尚未系统研究。方法：通过控制实验解耦训练目标和解码算法的影响，发现DLM训练目标导致语义连贯性和语义多样性增加，但n-gram熵更低；熵降低主要由DLM解码中的置信度重掩码策略驱动，而非训练目标。

- [#80] **OSDN: Improving Delta Rule with Provable Online Preconditioning in Linear Attention** — Chenyu Zhou, Hongpei Li 等
  - **[一句话总结领域]**: 线性注意力改进
  - **[TL;DR]**: 问题：Delta Rule的步长依赖标量门，忽略内目标的特征级曲率，限制in-context关联回忆能力。方法：提出OSDN，用对角预条件器通过超梯度反馈在线更新增强标量门，代数等价于写侧key的逐特征缩放，保持DeltaNet的硬件友好分块并行流水线，340M规模JRT回忆提升32%，1.3B规模回忆残差比降低39%。

- [#85] **Phasor Memory Networks: Stable Backpropagation Through Time for Scalable Explicit Memory** — Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung
  - **[一句话总结领域]**: 显式记忆架构
  - **[TL;DR]**: 问题：显式记忆架构（如NTM）因BPTT梯度不稳定在语言建模上不可用。方法：提出Phasor Memory Network（PMNet），通过酉相子动力学和层级可学习锚点约束循环状态更新为复数单位圆上的相位旋转，保持梯度范数防止发散，119M参数在18.8B token上训练即达到3倍大Mamba的零样本长上下文鲁棒性。

- [#79] **Effective Context in Transformers: An Analysis of Fragmentation and Tokenization** — Amirmehdi Jafari Fesharaki, Mohammadamin Rami, Aslan Tchamkerten
  - **[一句话总结领域]**: 分词与上下文信息论
  - **[TL;DR]**: 问题：同样的数据编码为字节、字符或子词token，在固定上下文窗口下暴露给模型的信息不同，但缺乏理论框架理解。方法：在马尔可夫源上研究碎片化和分词两个方向，证明碎片化（无损重编码为更小单元）严格增加最优有限上下文log-loss，给出分词使短token窗口等效更长源上下文的损失保证。

- [#91] **Understanding and Accelerating the Training of Masked Diffusion Language Models** — Chunsan Hong, Sanghyun Lee 等
  - **[一句话总结领域]**: 掩码扩散语言模型训练加速
  - **[TL;DR]**: 问题：掩码扩散模型（MDM）训练速度远慢于自回归模型，限制了规模化。方法：分析发现语言局部性偏差（预测token信息集中在附近位置）是训练慢的主因，提出钟形时间采样训练策略，LM1B上达到相同验证NLL快4倍，生成困惑度和零样本困惑度也更快改善。

---

## 📊 LLM 评测（llm-evaluation）— 5 篇

**今日动态：** 评测方向关注LLM创造力测评局限性、LLM标注者可信度、LLM as judge提升、多Agent对话公平性评测和不确定性评测。

- [#81] **Assessing the Creativity of Large Language Models: Testing, Limits, and New Frontiers** — Samuel Schapiro, Alexi Gladstone 等
  - **[一句话总结领域]**: LLM创造力评测
  - **[TL;DR]**: 问题：人类创造力测试用于评测LLM创造力的有效性未经验证，且这些测试预测人类创造力的能力本身有限。方法：首次大规模系统研究，发现DAT和条件DAT分别最好预测创意写作和发散思维，但没有单一测试预测所有构念，且没有现有测试可靠预测科学构思能力；提出DRAT同时评估聚敛和发散思维，首次显著预测科学构思。

- [#24] **LLMs as annotators of credibility assessment in Danish asylum decisions** — Galadrielle Humblot-Renaux 等
  - **[一句话总结领域]**: LLM标注可信度
  - **[TL;DR]**: 问题：LLM用于自动化文本标注的有效性在低资源语言和专业领域（如庇护决策可信度评估）中探索不足。方法：引入RAB-Cred丹麦语文本分类数据集，基准测试21个开源模型和30个提示组合，发现LLM标注潜力但存在不一致性，强调不能依赖单一模型标注结果。

- [#33] **PRISM-X: Experiments on Personalised Fine-Tuning with Human and Simulated Users** — Hannah Rose Kirk 等
  - **[一句话总结领域]**: 个性化微调评测
  - **[TL;DR]**: 问题：个性化方法效果常只用模拟用户评估，真实用户与模拟用户的差异和个性化最佳实现方式（上下文提示vs权重视微调）不清楚。方法：530名52国参与者重测PRISM数据集的组内实验，发现偏好微调（P-DPO）显著优于通用模型和个性化提示，但个体数据适应仅边际优于多样化群体池化训练；模拟用户恢复聚合模型层级但个体判断远低于人类自一致性基线。

- [#62] **In-Situ Behavioral Evaluation for LLM Fairness, Not Standardized-Test Scores** — Zeyu Tang 等
  - **[一句话总结领域]**: LLM公平性行为评测
  - **[TL;DR]**: 问题：标准化测试式公平性评测在提示构造选择上高度脆弱，分数方差主要来自与公平性无关的表面构造，且模型排名严重不一致。方法：提出MAC-Fairness多Agent对话框架，将标准化测试问题作为对话种子而非评测工具，评估800万对话的身份持久性和同伴接受度，发现稳定的模型特定行为签名可跨基准泛化。

- [#88] **LLMs as Implicit Imputers: Uncertainty Should Scale with Missing Information** — Stef van Buuren
  - **[一句话总结领域]**: LLM不确定性评测
  - **[TL;DR]**: 问题：LLM在上下文不完整时生成答案可被视为隐式插补，但不确定性与缺失信息量之间的关系未验证。方法：在SQuAD上控制上下文可用性5个级别，发现置信度不反映信息缺失（准确率崩塌时仍保持高），而熵随上下文移除增加，与多重插补类比一致，解释了更多准确率方差（R²差距最高0.057）。

---

## 📚 RAG（rag）— 4 篇

**今日动态：** RAG方向关注视觉证据的效用导向选择、知识图谱增强的个性化检索、搜索内容时效性预测和上下文训练与主动信息搜索。

- [#36] **Utility-Oriented Visual Evidence Selection for Multimodal Retrieval-Augmented Generation** — Weiqing Luo, Zongye Hu 等
  - **[一句话总结领域]**: 多模态RAG证据选择
  - **[TL;DR]**: 问题：多模态RAG中视觉证据选择依赖语义相关性或表面相似度，与下游推理的实际效用不对齐。方法：从信息论角度定义证据效用为对模型输出分布的信息增益，引入潜在证据有用性概念证明在该变量上的信息增益排序等价于答案空间效用，提出无需训练的代理加速框架，在MRAG-Bench和Visual-RAG上一致超越SOTA同时降低计算成本。

- [#18] **PersonalAI 2.0: Enhancing knowledge graph traversal/retrieval with planning mechanism for Personalized LLM Agents** — Mikhail Menschikov 等
  - **[一句话总结领域]**: 知识图谱增强个性化检索
  - **[TL;DR]**: 问题：现有GraphRAG方法缺乏自适应迭代搜索和规划机制。方法：提出PersonalAI 2.0（PAI-2），通过提取实体、匹配图顶点和生成线索查询实现自适应迭代信息搜索，图遍历算法（BeamSearch等）比标准扁平检索平均高6%，搜索规划增强机制带来18%提升，MINE-1上达89%信息保持SOTA。

- [#89] **RAG-Enhanced Large Language Models for Dynamic Content Expiration Prediction in Web Search** — Tingyu Chen, Wenkai Zhang 等
  - **[一句话总结领域]**: 搜索内容时效性预测
  - **[TL;DR]**: 问题：商业搜索中内容时效性对齐用户意图困难，传统静态时间窗过滤导致"一刀切"排名——内容时间新但语义已过时。方法：提出基于LLM的查询感知动态内容过期预测框架，从文档提取细粒度时间上下文，用LLM推导查询特定的"有效期限"语义边界，配合幻觉缓解策略，百度搜索线上A/B测试显著提升搜索时效性和用户体验。

- [#48] **Context Training with Active Information Seeking** — Zeyu Huang, Adhiguna Kuncoro 等
  - **[一句话总结领域]**: 上下文优化与主动搜索
  - **[TL;DR]**: 问题：现有上下文优化方法闭环依赖模型自身知识，无法获取新信息。方法：为上下文优化器配备Wikipedia搜索和浏览器工具进行主动信息搜索，配合保持多候选上下文并剪枝的搜索训练程序，在低资源翻译、健康场景和推理任务上一致获得实质性提升，生成的文本上下文可跨模型泛化。

---

## ⚡ Agentic RL（agent-rl）— 4 篇

**今日动态：** Agentic RL方向关注多轮环境信用分配、多目标混合奖励优化和视觉语言推理奖励分解。

- [#38] **GAGPO: Generalized Advantage Grouped Policy Optimization** — Siyuan Zhu, Chao Yu 等
  - **[一句话总结领域]**: 多轮Agent信用分配
  - **[TL;DR]**: 问题：多轮环境中Agent仅获轨迹级稀疏奖励，难以判断哪些中间步骤贡献成功/失败，无需昂贵价值模型的步对齐信用分配是开放问题。方法：提出GAGPO，从采样推演构建非参数分组价值代理计算TD/GAE式时序优势，递归向后传播结果监督，无需critic，在ALFWorld和WebShop上超越强RL基线，学习更快且优化更平滑。

- [#19] **PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning** — Hee Suk Yoon 等
  - **[一句话总结领域]**: 视觉语言推理RL奖励
  - **[TL;DR]**: 问题：将文本推理的全局置信度奖励直接用于视觉语言推理会产生混合诱导信号退化——视觉步的训练信号被占主导的文本步统计扭曲。方法：提出PDCR，用视觉依赖分数无监督分解感知和推理步骤，在各技能聚类内归一化置信增益计算分解优势，为感知和推理提供稳定、正确缩放的信号，在关键V-L推理基准上超越全局奖励和稀疏奖励基线。

- [#75] **Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization** — Yang Bai, Kaiyuan Liu 等
  - **[一句话总结领域]**: 多目标混合奖励RL
  - **[TL;DR]**: 问题：多任务混合奖励设置中异构奖励分布和维度相关不稳定标量优势构建。方法：提出RDPO，先用幅度感知分位数归一化稳定二值/分数/连续奖励的prompt级优势分配，再用马氏白化消除各奖励子空间的相关冗余后聚合，应用于LongCat-Flash后训练提升指令遵循、写作质量和硬提示鲁棒性。

- [#60] **Training LLMs with Reinforcement Learning for Intent-Aware Personalized Question Answering** — Maryam Amirizaniani 等
  - **[一句话总结领域]**: 意图感知个性化RL
  - **[TL;DR]**: 问题：现有意图感知个性化方法依赖多轮对话或丰富用户画像，单轮设置中用户隐含意图难以从最少输入推断。方法：提出IAP框架，用RL训练模型从单轮问题推断隐含意图并通过标签化schema将其融入思考步骤，在LaMP-QA上6个模型上一致超越所有基线，平均macro-score比最强竞争者高7.5%。

---

## 🎯 RL for Reasoning（rl-reasoning）— 3 篇

**今日动态：** 推理RL方向关注可验证过程监督和竞赛级推理scaling。

- [#67] **Correct Answers from Sound Reasoning: Verifiable Process Supervision for Language Models** — Kyuyoung Kim 等
  - **[一句话总结领域]**: 可验证过程监督
  - **[TL;DR]**: 问题：仅优化最终结果的RL提升准确率但推理质量退化——国际象棋上赢率误差增加最高112%。方法：提出VPS，在可验证领域联合优化预测准确性和推理质量，SFT引入结构化推理格式提取中间声明，自适应奖励加权优先处理最大误差子任务，赢率误差降低30%，一致性恢复至近饱和。

- [#87] **Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling** — Yafu Li 等
  - **[一句话总结领域]**: 竞赛级推理RL scaling
  - **[TL;DR]**: 问题：将推理模型转换为奥赛级求解器需要复杂定制流程。方法：统一方案——逆困惑度课程SFT+两阶段RL（可验证奖励RL→证明级RL）+测试时scaling，30B-A3B模型SU-01支持100K+ token稳定推理，在IMO 2025/USAMO 2026和IPhO 2024/2025达金牌水平。

- [#40] **STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes** — Chenjun Xu 等
  - **[一句话总结领域]**: 推理链剪枝
  - **[TL;DR]**: 问题：长CoT推理导致overthinking，低数据微调场景下无法依赖大规模教师蒸馏。方法：提出STOP，通过节点分割、分类标注和推理树构建将轨迹结构化，引入ECN保留最短正确前缀，在DeepSeek-R1蒸馏模型上减少19.4-42.4%生成token同时保持精度，比教师引导剪枝产生更小的分布偏移。

---

## 🖼️ 多模态推理（multimodal-reasoning）— 3 篇

**今日动态：** 多模态推理关注视觉语言模型的校准、全模态接地和视觉语言推理奖励分解。

- [#69] **Bridging the Missing-Modality Gap: Improving Text-Only Calibration of Vision Language Models** — Mingyeong Kim, Jungwon Choi 等
  - **[一句话总结领域]**: VLM文本校准
  - **[TL;DR]**: 问题：VLM在文本输入时（缺少视觉模态）准确率大幅下降且严重失校准，即使文本描述保留关键内容置信度也不可靠。方法：提出Latent Imagination Module（LIM），轻量跨注意力模块从文本输入预测想象潜在嵌入送入冻结VLM骨干，无需像素级图像合成，在文本和缺失图像场景上一致提升准确率和校准。

- [#73] **Senses Wide Shut: A Representation-Action Gap in Omnimodal LLMs** — Trung Nguyen Quang 等
  - **[一句话总结领域]**: 全模态接地
  - **[TL;DR]**: 问题：全模态LLM接受与自身感知输入矛盾的文本前提时，失败在感知还是行动环节？方法：引入IMAVB基准（500片段2×2设计），发现表征-行动差距——隐藏状态可靠编码前提-感知不匹配但模型几乎不在输出中拒绝错误声明；行为上分欠拒绝和过拒绝两种模式，音频接地弱于视觉；探针引导logit调整（PGLA）一致改善拒绝行为。

- [#19] **PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning** — Hee Suk Yoon 等
  - **[一句话总结领域]**: 视觉语言推理RL奖励
  - **[TL;DR]**: 问题：将文本推理的全局置信度奖励直接用于V-L推理会产生混合诱导信号退化——视觉步训练信号被文本步统计扭曲。方法：提出PDCR，用视觉依赖分数无监督分解感知和推理步骤，各聚类内归一化置信增益计算分解优势，在关键V-L推理基准上超越全局奖励和稀疏奖励基线。

---

## 🤖 多模态 Agent（multimodal-agent）— 3 篇

**今日动态：** 多模态Agent方向关注视觉语言导航、具身多Agent协调和全模态接地诊断。

- [#86] **What Limits Vision-and-Language Navigation ?** — Yunheng Wang, Yuetong Fang 等
  - **[一句话总结领域]**: 视觉语言导航
  - **[TL;DR]**: 问题：VLN从仿真到真实部署性能大幅退化，原因在于感知不稳定和指令定义不足，现有方法通过扩大模型和数据弥合但核心瓶颈是缺乏鲁棒空间接地。方法：提出StereoNav，引入目标位置先验作为跨域稳定视觉引导，利用立体视觉构建语义+几何统一表征增强深度感知，R2R-CE上SR 81.1%/SPL 68.3%，参数和训练数据远少于先前方案。

- [#95] **Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue** — Vardhan Dongre, Dilek Hakkani-Tür
  - **[一句话总结领域]**: 具身多Agent协调
  - **[TL;DR]**: 问题：部分观察下具身Agent协调通信是否能实现真正的世界模型对齐而非表面协调？方法：扩展PARTNR基准增加自然语言对话通道，提出基于每人世界图的测量框架（观察收敛、信息新颖性、信念敏感消息），发现对话减少40-83pp行为冲突但反而降低任务成功率，揭示当前模型表面协调与真正世界模型对齐之间的差距。

- [#73] **Senses Wide Shut: A Representation-Action Gap in Omnimodal LLMs** — Trung Nguyen Quang 等
  - **[一句话总结领域]**: 全模态接地
  - **[TL;DR]**: 问题：全模态LLM接受与自身感知输入矛盾的文本前提时，失败在感知还是行动环节？方法：引入IMAVB基准，发现表征-行动差距——隐藏状态可靠编码前提-感知不匹配但模型几乎不在输出中拒绝错误声明；PGLA探针引导logit调整改善拒绝行为。

---

## 📝 信息抽取（ner-re）— 3 篇

**今日动态：** 信息抽取关注文档级生物医学实体链接、零样本分类学归纳和LLM论证重构。

- [#20] **LongBEL: Long-Context and Document-Consistent Biomedical Entity Linking** — Adam Remaki, Xavier Tannier, Christel Gérardin
  - **[一句话总结领域]**: 文档级实体链接
  - **[TL;DR]**: 问题：生物医学实体链接通常独立链接每个mention忽略同文档mention间依赖，导致同一概念不同表面形式预测不一致。方法：提出LongBEL文档级生成框架，结合全文上下文和前预测记忆，用交叉验证预测而非金标训练减少训练/推理不匹配，5个基准上超越句子级基线，主要在文档内递归概念上提升。

- [#66] **BoostTaxo: Zero-Shot Taxonomy Induction via Boosting-Style Agentic Reasoning and Constraint-Aware Calibration** — Yancheng Ling, Zhenlin Qin 等
  - **[一句话总结领域]**: 零样本分类学归纳
  - **[TL;DR]**: 问题：零样本分类学归纳的泛化性、结构可靠性和效率仍有限。方法：提出BoostTaxo，boosting风格LLM框架，轻量LLM高效过滤候选父节点，大LLM细粒度排序评分，结构特征校准候选边权重，在WordNet/DBLP/SemEval-Sci上零样本达SOTA或可比性能。

- [#4] **An LLM-Based System for Argument Reconstruction** — Paulo Pirozelli, Victor Hugo Nascimento Rocha 等
  - **[一句话总结领域]**: 论证重构
  - **[TL;DR]**: 问题：从自然语言文本重构论证图为抽象论证图缺乏端到端LLM方案。方法：提出多阶段LLM流水线，逐步识别论证组件、选择相关元素、揭示逻辑关系，输出有向无环图（前提/结论+支持/攻击/削弱），手动和定量评估均显示能充分恢复论证结构。

---

## ✍️ 文本生成（nlg）— 3 篇

**今日动态：** 文本生成关注儿童故事生成、文学翻译精炼和语法纠错。

- [#7] **Children's English Reading Story Generation via Supervised Fine-Tuning of Compact LLMs with Controllable Difficulty and Safety** — Qian Shen, Fanghua Cao 等
  - **[一句话总结领域]**: 儿童故事生成
  - **[TL;DR]**: 问题：LLM生成的儿童故事难度不适合儿童阅读，且运营成本阻碍教育场景普及。方法：用专家设计的儿童阅读课程和GPT-4o/Llama 3.3 70B生成的故事微调8B模型，可控难度和安全，评估显示8B模型在难度指标上超越零样本GPT-4o和Llama 3.3 70B，且几乎无安全问题。

- [#28] **What Does LLM Refinement Actually Improve? A Systematic Study on Document-Level Literary Translation** — Shaomu Tan 等
  - **[一句话总结领域]**: 文学翻译精炼
  - **[TL;DR]**: 问题：迭代自精炼是简单推理时机器翻译策略，但文档级精炼在哪些场景有效、改什么维度、精炼器如何行为尚未系统理解。方法：9个LLM 7个语言对的大规模系统研究，发现文档级MT+段落级精炼最稳定，文档级精炼改动少收益小，通用精炼提示优于错误特定提示和评后精炼，精炼收益主要来自流畅性/风格/术语，模型强化精炼器分布而非定向修复。

- [#12] **Edit-level Majority Voting Mitigates Over-Correction in LLM-based Grammatical Error Correction** — Takumi Goto, Yusuke Sakai, Taro Watanabe
  - **[一句话总结领域]**: 语法纠错
  - **[TL;DR]**: 问题：LLM语法纠错存在过度纠正问题。方法：提出编辑级多数投票，对单个模型生成的多个候选进行编辑级投票，无需模型修改或额外训练，在9个基准（7种语言）上超越贪婪和MBR解码，且不受指令提示变化影响。

---

## 🌐 LLM 应用（llm-app）— 4 篇

**今日动态：** LLM应用涵盖法律庇护决策标注、教育幻灯片生成、建筑信息建模和金融推理。

- [#24] **LLMs as annotators of credibility assessment in Danish asylum decisions** — Galadrielle Humblot-Renaux 等
  - **[一句话总结领域]**: 法律NLP
  - **[TL;DR]**: 问题：LLM标注在低资源语言和专业法律领域（庇护决策可信度评估）的有效性未充分探索。方法：引入RAB-Cred丹麦语数据集，21个模型30个提示组合基准测试，确认LLM标注潜力但存在不一致性，需超越单一模型预测。

- [#37] **A Hybrid Framework for Natural Language Querying of IFC Models with Relational and Graph Representations** — Rabindra Lamsal 等
  - **[一句话总结领域]**: 建筑信息建模
  - **[TL;DR]**: 问题：IFC复杂性使非专家难以自然语言查询BIM模型。方法：提出IfcLLM混合框架，将IFC模型转换为关系+图两种互补表示，通过迭代重试精炼LLM推理整合，开放权重LLM首次尝试准确率93.3-100%。

- [#78] **AI-Generated Slides: Are They Good? Can Students Tell?** — Juho Leinonen, Lisa Zhang, Arto Hellas
  - **[一句话总结领域]**: 教育AI
  - **[TL;DR]**: 问题：GenAI生成课程幻灯片的质量如何？学生能否识别？方法：比较NotebookLM、Claude、M365 Copilot、Cursor、Claude Code五种工具生成的幻灯片，编码助手生成的最准确/完整/教学合理，学生评价AI幻灯片与人工幻灯片质量相当且无法可靠区分，高质量评价与"AI生成"评价负相关。

- [#31] **FIND: Toward Multimodal Financial Reasoning and Question Answering for Indic Languages** — Sarmistha Das 等
  - **[一句话总结领域]**: 多语言金融推理
  - **[TL;DR]**: 问题：多语言金融数值推理基准缺乏，尤其印度语言。方法：提出FinVQA基准（18900样本，6种印度语言，14个金融领域，3个难度级别），FIND框架结合SFT和约束感知解码促进忠实数值推理，建立高风险多语言多模态金融推理评测范式。
  - **排除原因：** 多语言/特定语言（印地语等印度语言）

---

## 🏷️ 其他（other）— 5 篇

**今日动态：** 其他方向包括扩散模型安全生成、不确定性量化、论证重构、社会网络生成和组成句法分析。

- [#57] **REALISTA: Realistic Latent Adversarial Attacks that Elicit LLM Hallucinations** — Buyun Liang 等
  - **[一句话总结领域]**: 幻觉对抗攻击
  - **[TL;DR]**: 问题：现有幻觉攻击方法要么离散提示攻击搜索空间有限，要么连续潜在空间攻击解码后不再有效改写。方法：提出REALISTA，构建输入依赖的有效编辑方向字典（每个对应语义等价连贯改写），在潜在空间优化方向连续组合，结合连续攻击灵活性+离散改写语义真实性，在推理模型自由回答设置下成功攻击此前方法无法攻破的模型。

- [#96] **When Do LLMs Generate Realistic Social Networks?** — Sai Hemanth Kilaru 等
  - **[一句话总结领域]**: LLM社会网络生成
  - **[TL;DR]**: 问题：LLM作为人类受试者替代用于社会网络生成，但其关系输出如何依赖提示设计、文化框架等尚不清楚。方法：形式化4种LLM社交关系形成机制（顺序/全局/局部/迭代），在4种文化4种语言3种模型4种提示架构下生成192个网络，发现文化框架改变同质性、政治派系主导关系形成、提示架构是实质性社会学变量、LLM网络在聚类和模块度上匹配真实图。

- [#100] **Linking Extreme Discourse to Structural Polarization in Signed Interaction Networks** — Zhijin Guo 等
  - **[一句话总结领域]**: 话语与极化网络
  - **[TL;DR]**: 问题：在线社区极化研究要么看语言要么看交互结构，两者很少统一连接。方法：提出语言接地的符号网络流水线，从LLM立场分数推导连续符号边权重，用Eigen-Sign和frustration两个互补指标量化极化，在Reddit Brexit讨论中发现连续置信加权边揭示强度敏感模式，滞后语言信号包含未来极化信息。

- [#26] **Exploiting Pre-trained Encoder-Decoder Transformers for Sequence-to-Sequence Constituent Parsing** — Daniel Fernández-González, Cristina Outeiriño Cid
  - **[一句话总结领域]**: 成分句法分析
  - **[TL;DR]**: 问题：seq2seq成分句法分析主要使用预训练编码器（BERT/RoBERTa），编码器-解码器架构探索不足。方法：在BART/mBART/T5编码器-解码器上微调生成线性化句法树，在连续和不连续句法树上评估，超越所有先前seq2seq模型，与领先的任务特定解析器可比。

- [#45] **TruncProof: A Guardrail for LLM-based JSON Generation under Token-Length Constraints** — Yoshio Kato, Shuhei Tarashima
  - **[一句话总结领域]**: 结构化输出安全
  - **[TL;DR]**: 问题：LLM生成JSON无法严格限制生成token数，导致无限生成或截断输出系统故障。方法：提出TruncProof，利用LL(1)解析器特性在每步解码时高效近似完成语法有效输出所需的最小token数，在token约束下生成语法正确JSON，且可与高级解码策略组合保证语义准确。

---

## 🗣️ 对话系统（dialogue）— 2 篇

**今日动态：** 对话方向关注PII替换和动机性访谈编码。

- [#15] **Locale-Conditioned Few-Shot Prompting Mitigates Demonstration Regurgitation in On-Device PII Substitution with Small Language Models** — Anuj Sadani, Deepak Kumar
  - **[一句话总结领域]**: 端侧PII替换
  - **[TL;DR]**: 问题：PII脱敏用占位符替代破坏下游实用性，端侧SLM直接few-shot会逐字复述演示输出。方法：提出区域条件旋转few-shot演示——字符范围启发式选区域纯池+每输入MD5哈希采样3个演示，482/482调用成功（无回声），但下游NER中SLM替代物自然度高于faker但多样性不足，NER F1不如faker。

- [#50] **Leveraging Multimodal Self-Consistency Reasoning in Coding Motivational Interviewing for Alcohol Use Reduction** — Guangzeng Han 等
  - **[一句话总结领域]**: 动机性访谈编码
  - **[TL;DR]**: 问题：动机性访谈（MI）编码需要专业人员耗时标注，现有方法单一模态。方法：基于音频语言模型（ALM）的多模态自一致性框架，4种互补分析提示（分析/韵律/证据评分/比较）各3个采样，12轨迹多数投票，准确率52.56%超基线。
  - **排除原因：** 医学/临床诊断

---

## 🌍 多语言与跨语言（multilingual）— 3 篇

**今日动态：** 多语言方向关注濒危语言转录翻译、跨语言文化一致性对齐和印地语ASR。

- [#1] **WARDEN: Endangered Indigenous Language Transcription and Translation with 6 Hours of Training Data** — Ziheng Zhang, Yunzhong Hou 等
  - **[一句话总结领域]**: 濒危语言转录翻译
  - **[TL;DR]**: 问题：濒危澳洲原住民语言Wardaman仅6小时标注音频，统一模型不可行。方法：提出WARDEN两阶段系统——先用发音接近的巽他语初始化Wardaman token加速转录微调，再用专家标注字典为LLM提供领域知识做翻译决策，在极少数据下超越更大开源和专有模型。
  - **排除原因：** 多语言/特定语言（Wardaman 语）

- [#71] **Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation** — Lucas Resck, Isabelle Augenstein, Anna Korhonen
  - **[一句话总结领域]**: 跨语言文化一致性
  - **[TL;DR]**: 问题：多语言LLM在固定人设下提示语言会覆盖系统人设（英语回答Shakespeare、西语回答Cervantes）。方法：提出Singleton Fleiss's κ_S量化跨语言文化不一致，C-3PO共识驱动对齐框架使κ_S绝对提升0.10，层分析发现MLLM在前向传播中隐式将输出个性化到提示语言的刻板文化。
  - **排除原因：** 多语言/特定语言（跨语言文化对齐）

- [#43] **Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition** — Kush Juvekar 等
  - **[一句话总结领域]**: 印度语ASR
  - **[TL;DR]**: 问题：微调Whisper提升朗读语音但退化自发语音（录音棚偏差）。方法：引入Vividh-ASR分层基准（录音棚/广播/自发/合成噪声），发现早期大参数更新+难到易课程学习策略，提出R-MFT使244M模型匹配或超越769M微调模型，CKA/SVD分析揭示有效调度将适应集中在解码器。
  - **排除原因：** 多语言/特定语言（印地语/马拉雅拉姆语 ASR）

---

## 📖 文本生成 / 机器翻译（mt）— 2 篇

**今日动态：** 翻译方向关注文学翻译评估偏见和日英游记翻译。

- [#13] **Creativity Bias: How Machine Evaluation Struggles with Creativity in Literary Translations** — Kyo Gerrits, Rik van Noord, Ana Guerberof Arenas
  - **[一句话总结领域]**: 文学翻译评估偏见
  - **[TL;DR]**: 问题：自动评估指标和LLM-as-judge在文学翻译创意性评估上与专业译者对齐差，LLM系统偏向机器翻译文本、惩罚创造性解决方案。方法：创建三种模态（人翻/机翻/后编辑）三类型三语对的文学翻译数据集并标注创意性，发现AEM和LLM-as-judge与专业评分相关性差，且诗歌体裁表现更差。
  - **排除原因：** 多语言/特定语言（多语言翻译评估）

- [#53] **ATD-Trans: A Geographically Grounded Japanese-English Travelogue Translation Dataset** — Shohei Higashiyama, Hiroki Ouchi, Atsushi Fujita, Masao Utiyama
  - **[一句话总结领域]**: 日英游记翻译数据集
  - **[TL;DR]**: 问题：富含地理信息的文本机器翻译质量评估缺乏细粒度基准。方法：引入ATD-Trans日英游记翻译数据集，支持整体和地理实体级别评估，发现日语增强模型优势明显，国内区域地理实体翻译更困难。
  - **排除原因：** 多语言/特定语言（日语-英语翻译）

---

## 📋 知识图谱与NLU（knowledge-graph / nlu）— 2 篇

**今日动态：** 知识图谱方向关注实体因果常识推理基准。

- [#54] **CommonWhy: A Dataset for Evaluating Entity-Based Causal Commonsense Reasoning in Large Language Models** — Armin Toroghi, Faeze Moradi Kalarde, Scott Sanner
  - **[一句话总结领域]**: 实体因果常识推理
  - **[TL;DR]**: 问题：LLM实体常识推理评估多为判断题或多选，缺乏对因果推理和解释生成的显式评估。方法：引入CommonWhy，15000个why问题评估LLM实体因果常识推理，同时作为KGQA基准（所有知识在Wikidata），SOTA LLM和LLM-based KGQA方法频繁事实幻觉和因果推理失败。

- [#25] **From Rosetta to Match-Up: A Paired Corpus of Linguistic Puzzles with Human and LLM Benchmarks** — Neh Majmudar, Anne Huang, Jinfan Frank Hu, Elena Filatova
  - **[一句话总结领域]**: 语言学谜题评测
  - **[TL;DR]**: 问题：语言学竞赛谜题缺乏配对格式及LLM与人类求解的系统性对比。方法：提出将Rosetta Stone谜题系统转换为Match-Up配对的方法，评估发现专家和LLM在Match-Up上都呈全有或全无模式。

---

## 🎯 提示工程（prompt-engineering）— 1 篇

- [#9] **Fine-tuning with Hierarchical Prompting for Robust Propaganda Classification Across Annotation Schemas** — Lukas Stähelin 等
  - **[一句话总结领域]**: 宣传分类
  - **[TL;DR]**: 问题：社交媒体宣传检测噪声大标注低，现有分类体系不一致。方法：提出新意图聚焦分类体系和分层提示方法（HiPP），先预测细粒度技术再聚合，微调Qwen模型在低一致性分类体系上效果显著，比GPT-4.1-nano和Phi-4更强。

---

## 🔧 工具使用与API调用（tool-use）— 1 篇

- [#65] **ToolWeave: Structured Synthesis of Complex Multi-Turn Tool-Calling Dialogues** — Dinesh Khandelwal 等
  - **[一句话总结领域]**: 工具调用数据合成
  - **[TL;DR]**: 问题：多轮工具调用训练数据合成困难，现有流水线工具仅表面兼容且参数幻觉严重。方法：提出ToolWeave，构建内置依赖工具+细粒度规划追踪参数来源，合成对话含45%多步交互，Llama-3.1-70B在BFCL-V3多轮达39.75%。

---

## 📊 数据质量与构建（data-quality）— 1 篇

- [#22] **TokAlign++: Advancing Vocabulary Adaptation via Better Token Alignment** — Chong Li, Yingzhuo Deng 等
  - **[一句话总结领域]**: 词汇表适配
  - **[TL;DR]**: 问题：不同LLM词汇表不匹配阻碍细粒度知识转移，低效分词减慢训练和推理。方法：提出TokAlign++，将源/目标词汇视为两种语言学习双语token对齐词典，按词典重排模型参数并渐进微调适配，15种语言上提升多语言文本压缩率，仅1k步恢复原始模型性能，统一词汇表后token级蒸馏仅235M token即显著提升。

---

## 🧩 模型效率与压缩（llm-efficiency）— 1 篇

- [#45] **TruncProof: A Guardrail for LLM-based JSON Generation under Token-Length Constraints** — Yoshio Kato, Shuhei Tarashima
  - **[一句话总结领域]**: 结构化输出安全
  - **[TL;DR]**: 问题：LLM生成JSON无法严格限制生成token数，导致无限生成或截断输出系统故障。方法：提出TruncProof，利用LL(1)解析器特性在每步解码时高效近似完成语法有效输出所需最小token数，在token约束下生成语法正确JSON，可与高级解码策略组合保证语义准确。

---

## 🔍 检索模型与排序（retrieval-model）— 1 篇

- [#89] **RAG-Enhanced Large Language Models for Dynamic Content Expiration Prediction in Web Search** — Tingyu Chen, Wenkai Zhang 等
  - **[一句话总结领域]**: 搜索内容时效性预测
  - **[TL;DR]**: 问题：商业搜索中内容时效性难以与用户意图对齐，传统静态时间窗过滤导致内容时间新但语义过时。方法：提出LLM查询感知动态内容过期预测框架，提取文档细粒度时间上下文推导查询特定"有效期限"语义边界，百度搜索线上A/B测试显著提升新鲜度和用户体验。

---

## 🤖 Agentic RL（agent-rl）补充

已在上文覆盖。

---

## 🎙️ 语音与音频（audio-speech）— 1 篇

- [#72] **EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents** — Tara Bogavelli 等
  - **[一句话总结领域]**: 语音Agent评测
  - **[TL;DR]**: 问题：现有语音Agent基准缺乏真实对话模拟和全面语音特定失败模式评估。方法：提出EVA-Bench端到端评测框架，bot-to-bot音频对话模拟+EVA-A/Accuracy+和EVA-X/Experience复合指标，213场景3企业域，12系统无一个同时EVA-A和EVA-X pass@1超0.5，口音和噪声暴露显著鲁棒性差距。

---

## 📖 LLM 应用（llm-app）补充

- [#70] **Domain Adaptation of Large Language Models for Polymer-Composite Additive Manufacturing Using Retrieval-Augmented Generation and Fine-Tuning** — Saiful Islam Sagor 等
  - **[一句话总结领域]**: 增材制造领域适配
  - **[TL;DR]**: 问题：通用LLM在专业工程领域缺乏领域接地和结构化技术知识。方法：在LLaMA-3-8B上对比RAG和微调，RAG在200专家问题上75.5%准确率和85.2%总体偏好超基线，微调原始文本反而降低性能（仅5.6%更准确），RAG比朴素微调更有效地适配专业工程领域。

---

## 🧠 大模型评测 / 其他补充论文

- [#99] **Training Large Language Models to Predict Clinical Events** — Benjamin Turtel, Paul Wilczewski, Kris Skotheim
  - **[一句话总结领域]**: 临床事件预测
  - **[TL;DR]**: 问题：纵向临床笔记蕴含患者时序演变信号，但转化为训练监督困难。方法：将Foresight Learning扩展到临床预测，将MIMIC-III时序笔记转换为（过去上下文，未来事件问题，标签）格式，6900个预测示例上LoRA适配器降低校准误差从0.127到0.040，Brier分数从0.199到0.145。
  - **排除原因：** 医学/临床诊断

- [#90] **Large Language Models Lack Temporal Awareness of Medical Knowledge** — Zihan Guan 等
  - **[一句话总结领域]**: LLM医学知识时间感知
  - **[TL;DR]**: 问题：LLM医学知识评测基于无时间基准，但医学知识随时间动态演变，模型需知道知识何时正确。方法：构建TempoMed-Bench评测LLM医学知识时间感知，发现(1)最新知识性能随时间线性衰退而非突变截断，(2)历史知识准确率仅为最新知识的25-54%，(3)跨年预测波动不规则，加入agentic搜索工具仍无法解决(-3到-14%)。
  - **排除原因：** 医学/临床诊断

- [#98] **Mechanism Plausibility in Generative Agent-Based Modeling** — Patrick Zhao, David Huu Pham, Nicholas Vincent
  - **[一句话总结领域]**: 生成式ABM机制合理性
  - **[TL;DR]**: 问题：LLM-ABM研究关注能否生成现象，但缺乏机制合理性（现象如何产生）的评估框架。方法：整合LLM-ABM和科学哲学文献，提出机制合理性四级量表，区分模型生成充分性（能再现现象）和机制合理性（如何产生），阐明预测模型和解释模型的不同角色。

- [#51] **Leveraging Speech to Identify Signatures of Insight and Transfer in Problem Solving** — Linas Nasvytis, Judith E. Fan
  - **[一句话总结领域]**: 语音洞察识别
  - **[TL;DR]**: 问题：洞察式问题解决中的突然领悟如何在语音中体现及对后续迁移有什么影响？方法：让189名被试出声思考解五道"火柴算术"问题，发现同组被试进步更快且随着进步说话更多更不同，更可能自发对问题分类，表明可迁移洞察的标志是其对言语报告的可及性。

- [#47] **The Cost of Perfect English: Pragmatic Flattening and the Erasure of Authorial Voice in L2 Writing Supported by GenAI** — Ao Liu, Shanhua Zhu
  - **[一句话总结领域]**: 二语写作语用扁平化
  - **[TL;DR]**: 问题：GenAI润色L2写作追求母语般流畅但牺牲社会语用多样性。方法：对ICNALE语料库中B2中文大学生议论文用4个LLM零温度润色，发现交互维度上对话参与标记崩塌，认知立场维度上模型架构差异导致不同行为，GenAI系统性地将L2作者独特修辞身份覆盖为同质化英美范式。

- [#55] **CiteVQA: Benchmarking Evidence Attribution for Trustworthy Document Intelligence** — Dongsheng Ma 等
  - **[一句话总结领域]**: 文档VQA证据归因
  - **[TL;DR]**: 问题：现有Doc-VQA只评分最终答案不检查支撑证据，模型可能答对但依据错误段落——在高风险领域是不可接受的。方法：提出CiteVQA基准，要求模型返回元素级边界框引用，Strict Attributed Accuracy仅当答案和引用区域都正确才计分，审查20个MLLM发现普遍证据归因幻觉，最强系统SAA仅76.0。

- [#35] **IndicMedDialog: A Parallel Multi-Turn Medical Dialogue Dataset for Accessible Healthcare in Indic Languages** — Shubham Kumar Nigam 等
  - **[一句话总结领域]**: 多语言医学对话
  - **[TL;DR]**: 问题：现有医学对话系统单轮问答或模板数据集限制对话真实性和多语言适用性。方法：引入IndicMedDialog，英+9种印度语言平行多轮医学对话数据集，LLM生成合成咨询+TranslateGemma翻译+母语者验证+脚本感知后处理，参数高效微调量化SLM。
  - **排除原因：** 医学/临床诊断

- [#52] **DiM³: Bridging Multilingual and Multimodal Models via Direction- and Magnitude-Aware Merging** — Zijing Wang 等
  - **[一句话总结领域]**: 多语言多模态合并
  - **[TL;DR]**: 问题：扩展多模态模型到多语言需昂贵多语言多模态数据构建和端到端重训练。方法：提出DiM³，训练无关地在共享语言模型骨干上组合多语言和多模态残差更新，按参数维度选择性组合两个更新，在57种语言LLaVA和Qwen骨干上一致超越现有合并基线，保留多模态能力的同时大幅提升多语言性能。
  - **排除原因：** 多语言/特定语言（57种语言多模态合并）

- [#83] **LIFT: Last-Mile Fine-Tuning for Table Explicitation** — Divij Khaitan, Ashish Tiwari
  - **[一句话总结领域]**: 表格提取
  - **[TL;DR]**: 问题：从非结构化剪贴板文本提取表格，LLM初始提取有错误需修复。方法：提出last-mile fine-tuning（LIFT），预训练LLM提取初始表格+微调SLM修复错误，1000训练样本即超越端到端微调0.144 TEDS点，训练数据有限或需输入格式鲁棒性时是更优选择。

- [#44] **Does language matter for spoken word classification? A multilingual generative meta-learning approach** — Batsirayi Mupamhi Ziki 等
  - **[一句话总结领域]**: 多语言口语分类
  - **[TL;DR]**: 问题：元学习在多语言口语单词分类中未被充分探索。方法：将生成式元持续学习算法应用于口语分类，训练单语(英/德/法/加泰)、双语和多语模型，多语模型表现最好但差异出乎意料地小，训练数据独特时长比语言数量是更强的性能指标。
  - **排除原因：** 多语言/特定语言（多语言口语分类）

---

## 🆕 新增 Topic

> 以下 topic 是本次整理中新发现的，已自动扩充到 TOPICS.md：

| Topic ID | Topic 名称 | 说明 | 当日论文数 |
|----------|-----------|------|-----------|
| llm-uncertainty | LLM 不确定性 | 不确定性量化、校准、幻觉检测 | 2 |
| diffusion-lm | 扩散语言模型 | 扩散模型用于文本生成、训练加速、安全生成 | 2 |

⚠️ TOPICS.md 已同步更新，请审阅

---

## 📊 统计

- 总论文数：106
- 排除论文数：7（多语言 5 篇，医学 2 篇）
- Topic 数量：16（含新增2个）
- 各 Topic 论文数：LLM推理能力(8), Agent架构与设计(8), 大模型训练与微调(8), 对齐与安全(7), 可解释性与机理(6), 模型架构与设计(5), LLM评测(5), RAG(4), Agentic RL(4), RL for Reasoning(3), 多模态推理(3), 多模态Agent(3), 信息抽取(3), 文本生成(3), LLM应用(4), 其他(5)