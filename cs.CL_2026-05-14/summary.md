# cs.CL 论文整理 - 2026-05-14

**整理时间**: 2026-05-14
**论文总数**: 106
**排除**: 25（多语言/特定语言 0 篇，医学/临床 25 篇）
**Topic 数量**: 22

---

## 📋 今日研究动态总览

| Topic | 论文数 | 核心关键词 |
|-------|--------|-----------|
| 对齐与安全 | 15 | hallucination, jailbreak, safety, uncertainty, negation |
| RL for Reasoning | 14 | reasoning, optimization, compiler, distillation, chess |
| LLM 推理能力 | 13 | reasoning, tokenization, context, query, uncertainty |
| 模型架构与设计 | 8 | pretraining, transformer, low-rank, linear attention, architecture |
| Agentic RL | 8 | agent, credit assignment, personalization, GEC, coordination |
| 多模态推理 | 8 | vision-language, confidence reward, test-time, geometry, diffusion |
| 多模态 Agentic RL | 5 | knowledge graph, policy optimization, citation, simulator, clinical |
| 代码生成与程序合成 | 4 | judge, diffusion, safety, code generation |
| 大模型评测 | 4 | refinement, translation, evaluation, uncertainty |
| 大模型训练与微调 | 4 | ASR, EFL, table, mixture pretraining |
| Agent 架构与设计 | 3 | agent, fairness, taxonomy, weights |
| 模型效率与压缩 | 3 | distillation, on-device, PII, diffusion |
| 多模态 Agent | 3 | memory, omnimodal, temporal, medical |
| 知识与记忆 | 3 | entity linking, spoken word, meta-learning |
| 视觉语言模型 | 3 | multilingual, calibration, navigation, stereo |
| RAG | 2 | visual evidence, polymer, domain adaptation |
| 检索模型与排序 | 1 | multilingual, slur detection, continual learning |
| 可解释性与机理 | 1 | persona, preference, probing, vector |
| 提示工程 | 1 | speech, insight, problem solving |
| 工具使用与 API 调用 | 1 | tool calling, dialogue, synthesis |
| LLM 应用 | 1 | creativity, assessment, testing, limits |
| Agent 安全与对齐 | 1 | multi-agent, coordination, world models |

---

## 🔒 对齐与安全（llm-alignment）— 15 篇

**今日动态：** 今日对齐方向聚焦三大主题：(1) 模型安全漏洞与对抗攻击，包括通过说服绕过 guardrail、隐式错位和人格崩溃；(2) 幻觉与不确定性量化，涵盖阶梯级幻觉检测、文学翻译中的创造力偏见和人工不确定性注入；(3) 否定学习缺陷与安全生成。整体趋势是从行为级对齐向内部机理和过程级精细控制演进。

- [#3] **Negation Neglect: When models fail to learn negations in training** — 否定忽略：模型在训练中学不会否定
  - **[Authors]**: Harry Mayne, Lev McKinney, Jan Dubiński, Adam Karvonen, James Chua, Owain Evans
  - **[一句话总结领域]**: 模型在微调标记为虚假的文件后反而相信虚假内容
  - **[TL;DR]**: 问题：LLM微调时遇到标记为虚假的声明，反而学会相信这些声明——否定忽略现象在Qwen3.5上使信念率从2.5%升至88.6%。方法：通过系统性实验揭示该现象跨模型普遍存在，且训练数据中的否定句结构（局部vs全局否定）是关键影响因素，发现局部否定("did not win")比全局否定("this is false")更容易被模型学会。

- [#7] **Children's English Reading Story Generation via Supervised Fine-Tuning of Compact LLMs with Controllable Difficulty and Safety** — 通过SFT小型LLM生成儿童英语阅读故事
  - **[Authors]**: Qian Shen, Fanghua Cao, Min Yao, Shlok Gilda, Bonnie J. Dorr, Walter L. Leite
  - **[一句话总结领域]**: 用8B模型微调生成可控难度的儿童英语阅读故事
  - **[TL;DR]**: 问题：LLM生成的儿童故事往往难度过高，且大模型部署成本阻碍教育应用。方法：基于专家课程设计微调三个8B模型，使生成故事在难度指标上超越GPT-4o和Llama 3.3 70B的零样本生成，同时保证安全性。
  - **排除原因：** 医学/临床诊断（教育场景但涉及儿童阅读评估）

- [#13] **Creativity Bias: How Machine Evaluation Struggles with Creativity in Literary Translations** — 创造力偏见：机器评估在文学翻译创造力上的困境
  - **[Authors]**: Kyo Gerrits, Rik van Noord, Ana Guerberof Arenas
  - **[一句话总结领域]**: 自动评估指标和LLM-as-Judge在文学翻译创造力评估上存在系统偏见
  - **[TL;DR]**: 问题：现有自动评估指标(AEMs)和LLM-as-Judge在文学翻译中无法准确评估创造力，且对机器翻译文本有系统偏见。方法：构建跨三种模态、三种体裁、三种语言对的文学翻译数据集，由专家标注创造力，发现LLM-as-Judge偏爱机器翻译而惩罚创造性解决方案，诗歌等文学体裁表现最差。

- [#14] **Inducing Artificial Uncertainty in Language Models** — 在语言模型中诱导人工不确定性
  - **[Authors]**: Sophia Hager, Simon Zeng, Nicholas Andrews
  - **[一句话总结领域]**: 通过在简单数据上诱导人工不确定性来训练不确定性量化方法
  - **[TL;DR]**: 问题：高性能LLM在简单数据上总是自信，导致不确定性量化方法难以获得训练信号。方法：提出在简单数据上诱导人工不确定性的问题，发现用探针识别人工不确定性后，该探针在识别真实不确定性上优于无人工不确定性的训练，在困难数据上实现更高校准。
  - **排除原因：** 医学/临床诊断

- [#22] **TokAlign++: Advancing Vocabulary Adaptation via Better Token Alignment** — 通过更好的token对齐推进词表适应
  - **[Authors]**: Chong Li, Yingzhuo Deng, Wen Yang, Jiajun Zhang, Chengqing Zong
  - **[一句话总结领域]**: 通过双语token对齐词表学习实现高效词表适应
  - **[TL;DR]**: 问题：不同LLM之间词表不匹配阻碍token级知识迁移（如蒸馏），且低效tokenization导致序列过长。方法：提出TokAlign++，将源/目标词表视为两种语言学习双语token对齐词表，重排模型参数后渐进微调，在15种语言上提升多语言文本压缩率并保留多语言能力。

- [#30] **LLM-Based Persuasion Enables Guardrail Override in Frontier LLMs** — 基于LLM的说服可绕过前沿LLM的安全防护
  - **[Authors]**: Rodrigo Nogueira, Thales Sales Almeida, Giovana Kerche Bonás, Andrea Roque, Ramon Pires, Hugo Abonizio, Thiago Laitz, Celio Larcher, Roseval Malaquias Junior, Marcos Piau
  - **[一句话总结领域]**: 用自然语言说服策略让前沿LLM绕过自身安全防护
  - **[TL;DR]**: 问题：前沿LLM的安全防护在面对直接请求时有效，但可能被自然语言说服绕过。方法：设计五轮对话攻击，利用同伴比较、认识义务重构等说服策略，在Claude Opus、Qwen3.5、Grok上实现100%的某些话题文章生成率，揭示现有guardrail的脆弱性。

- [#32] **Tracing Persona Vectors Through LLM Pretraining** — 追踪LLM预训练中的人格向量
  - **[Authors]**: Viktor Moskvoretskii, Dominik Glandorf, Jorge Medina Moreira, Tanja Käser, Robert West
  - **[一句话总结领域]**: 在预训练过程中追踪人格向量的形成和演化
  - **[TL;DR]**: 问题：LLM中的人格向量（如"邪恶"、"谄媚"）如何在预训练中形成尚不清楚。方法：在OLMo-3-7B预训练中追踪人格向量，发现其在预训练前0.22%即已形成，且对后训练指令模型仍有效，不同提取策略揭示人格的不同方面。

- [#58] **Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators** — 模拟学生还是谄媚式解题？论LLM模拟器误解忠实度
  - **[Authors]**: Heejin Do, Shashank Sonkar, Mrinmaya Sachan
  - **[一句话总结领域]**: LLM模拟学生在交互中无法保持误解驱动的信念状态
  - **[TL;DR]**: 问题：LLM模拟学生时，无论反馈是否针对其误解都会改正答案，缺乏误解忠实度——更像谄媚的问题求解者而非真实学生。方法：提出选择性翻转分数(SFS)量化误解忠实度，发现7个LLM的SFS接近零；通过SFT和SFS对齐RL训练显著提升忠实度，建立从静态输出匹配向交互式信念感知建模的范式转变。

- [#77] **Temper and Tilt Lead to SLOP: Reward Hacking Mitigation with Inference-Time Alignment** — 推理时对齐中的reward hacking缓解
  - **[Authors]**: Ye Wang, Jing Liu, Toshiaki Koike-Akino
  - **[一句话总结领域]**: 通过参考模型温度调整和SLOP加权缓解推理时对齐中的reward hacking
  - **[TL;DR]**: 问题：推理时对齐技术虽轻量但面临reward hacking风险。方法：提出SLOP（锐化对数意见池）框架，结合参考模型温度调整和SLOP权重校准算法，在保持对齐性能的同时提升对reward hacking的鲁棒性。

- [#80] **OSDN: Improving Delta Rule with Provable Online Preconditioning in Linear Attention** — 线性注意力中可证明在线预条件的Delta规则改进
  - **[Authors]**: Chenyu Zhou, Hongpei Li, Yuerou Liu, Jianghao Lin, Dongdong Ge, Yinyu Ye
  - **[一句话总结领域]**: 在线缩放DeltaNet通过特征级预条件提升线性注意力的上下文关联回忆
  - **[TL;DR]**: 问题：Delta Rule用标量门控忽略特征级曲率，限制了线性注意力的上下文关联回忆能力。方法：提出OSDN，用对角预条件器替代标量门控，通过超梯度反馈在线更新，严格保持DeltaNet的块级并行流水线，在340M和1.3B规模上分别提升JRT回忆32%和减少回忆残差39%。

- [#91] **Understanding and Accelerating the Training of Masked Diffusion Language Models** — 理解与加速掩码扩散语言模型训练
  - **[Authors]**: Chunsan Hong, Sanghyun Lee, Chieh-Hsin Lai, Satoshi Hayakawa, Yuhta Takida, Yuki Mitsufuji, Seungryong Kim, Jong Chul Ye
  - **[一句话总结领域]**: 通过钟形时间采样策略加速掩码扩散语言模型训练
  - **[TL;DR]**: 问题：掩码扩散语言模型(MDM)训练速度远慢于自回归模型。方法：分析发现语言局部性偏置是主因——预测信息集中在邻近位置；提出钟形时间采样策略，在LM1B上使MDM达到相同验证NLL的速度提升约4倍。

- [#100] **Linking Extreme Discourse to Structural Polarization in Signed Interaction Networks** — 将极端话语与有符号交互网络中的结构性极化联系起来
  - **[Authors]**: Zhijin Guo, Li Zhang, Tyler Bonnet, Janet B. Pierrehumbert, Xiaowen Dong
  - **[一句话总结领域]**: 用LLM立场分数构建有符号网络连接语言与结构极化
  - **[TL;DR]**: 问题：在线社区极化研究通常将语言与结构分开分析。方法：提出语言基础的有符号网络流程，从LLM立场分数推导连续有符号边权重，用谱Eigen-Sign分数和分区frustration分数量化结构极化，应用于Reddit Brexit讨论揭示话语信号与未来极化的预测关系。

- [#101] **Emergent and Subliminal Misalignment Through the Lens of Data-Mediated Transfer** — 从数据介导迁移视角看涌现与隐式错位
  - **[Authors]**: Baris Askin, Muhammed Ustaomeroglu, Anupam Nayak, Gauri Joshi, Guannan Qu, Carlee Joe-Wong
  - **[一句话总结领域]**: 从数据结构和训练通道角度解释涌现错位现象
  - **[TL;DR]**: 问题：涌现错位(EM)——在有害数据上微调导致模型在无关提示上表现错位——的机制尚不清楚。方法：提出数据介导迁移视角，发现错位更易在微调与评估提示功能结构相似、提示留有有害完成空间时发生；首次比较off-policy和on-policy蒸馏下的隐式学习(SL)传输。
  - **排除原因：** 医学/临床诊断

- [#104] **Layer-wise Representation Dynamics: An Empirical Investigation Across Embedders and Base LLMs** — 跨嵌入器和基础LLM的逐层表征动力学实证研究
  - **[Authors]**: Jingzhou Jiang, Yi Yang, Kar Yan Tam
  - **[一句话总结领域]**: 用三种逐层测量框架分析模型表征演化
  - **[TL;DR]**: 问题：现有逐层分析通常只关注表征变化的一个方面。方法：提出LRD框架，包含Frenet（全局子空间运动）、NRS（局部近邻保留）和GFMI（与最终层对齐）三个测量族，应用于31个模型和30个MTEB任务，发现架构和任务级差异，并用于无标签模型选择和推理时层剪枝。

- [#106] **WhatsApp Vaccine Discourse (WhaVax): An Expert-Annotated Dataset and Benchmark for Health Misinformation Detection** — WhatsApp疫苗话语数据集
  - **[Authors]**: Jônatas H. dos Santos, Julio C. S. Reis, Philipe Melo, João F. H. Olivetti, Thales H. Silva, Matheus Gontijo Guimaraes, Glaucio de Souza, Marcos A. Gonçalves, Fabricio Benevenuto, Filipe B. B. Zanovello, Marco A. G. Rodrigues, Cristiano X. Lima
  - **[一句话总结领域]**: 巴西WhatsApp疫苗相关消息的专家标注数据集
  - **[TL;DR]**: 问题：加密通信环境中的健康错误信息检测缺乏高质量标注数据。方法：构建WhaVax数据集，包含巴西公共群组中疫苗相关WhatsApp消息的多阶段专家标注，揭示独特的语言、结构和群体级错误信息模式，并基准测试经典模型和LLM方法。
  - **排除原因：** 医学/临床诊断

---

## 🎯 RL for Reasoning（rl-reasoning）— 14 篇

**今日动态：** 今日RL for Reasoning方向呈现多元化：(1) 推理优化与编译，如结构化LLM工作流的编译优化；(2) 推理蒸馏与验证，包括置信度门控闭环蒸馏和可验证过程监督；(3) 多目标RL与跨语言文化一致性。趋势是从单一奖励信号向多维度、过程级奖励演进。

- [#4] **An LLM-Based System for Argument Reconstruction** — 基于LLM的论证重构系统
  - **[Authors]**: Paulo Pirozelli, Victor Hugo Nascimento Rocha, Fabio G. Cozman, Douglas Aldred
  - **[一句话总结领域]**: 用LLM多阶段流水线将自然语言文本重构为抽象论证图
  - **[TL;DR]**: 问题：从自然语言文本中自动识别论证结构（前提、结论及其支持/攻击关系）仍具挑战。方法：提出端到端LLM系统，通过多阶段流水线渐进识别论证组件、选择相关元素并发现逻辑关系，表示为有向无环图，在教科书和基准数据集上验证有效。

- [#10] **FlowCompile: An Optimizing Compiler for Structured LLM Workflows** — 结构化LLM工作流的优化编译器
  - **[Authors]**: Junyan Li, Zhang-Wei Hong, Maohao Shen, Yang Zhang, Chuang Gan
  - **[一句话总结领域]**: 将LLM工作流优化视为编译问题，在部署前全局探索设计空间
  - **[TL;DR]**: 问题：结构化LLM工作流的配置优化（模型选择、推理预算、工作流结构）组合空间巨大，现有方法将其视为路由问题。方法：提出FlowCompile，从编译视角在部署前全局探索工作流设计空间，通过子代理剖析和结构感知代理估计工作流级精度与延迟，实现高达6.4倍加速。

- [#16] **Many-Shot CoT-ICL: Making In-Context Learning Truly Learn** — 多示例CoT-ICL：让上下文学习真正学习
  - **[Authors]**: Tsz Ting Chung, Lemao Liu, Mo Yu, Dit-Yan Yeung
  - **[一句话总结领域]**: 多示例链式思维上下文学习在推理任务中的 scaling 行为研究
  - **[TL;DR]**: 问题：多示例ICL在非推理任务上表现良好，但其在推理任务上的scaling规律尚不清楚。方法：系统研究多示例CoT-ICL用于推理，发现设置依赖的scaling效应、基于相似性的检索在推理上失效、以及顺序-scaling效应；提出曲率示范选择(CDS)在几何任务上提升5.42个百分点。
  - **排除原因：** 多语言/特定语言（涉及推理但主要关注ICL机制）

- [#37] **A Hybrid Framework for Natural Language Querying of IFC Models with Relational and Graph Representations** — 混合框架：用关系和图表示实现IFC模型自然语言查询
  - **[Authors]**: Rabindra Lamsal, Sisi Zlatanova, Haowen Xu, Yafei Sun, Johnson Xuesong Shen
  - **[一句话总结领域]**: 用混合关系和图表示+迭代LLM推理实现BIM自然语言查询
  - **[TL;DR]**: 问题：建筑信息模型(IFC)复杂度高，非专家难以访问。方法：提出IfcLLM框架，将IFC模型转化为关系表示（结构化属性）和图表示（拓扑关系），通过迭代重试-精炼LLM推理整合，在30个场景查询中实现93.3%-100%的首试准确率。

- [#41] **AcquisitionSynthesis: Targeted Data Generation using Acquisition Functions** — 基于采集函数的目标数据生成
  - **[Authors]**: Ishika Agarwal, Sofia Stoica, Emre Can Acikgoz, Pradeep Natarajan, Mahdi Namazifar, Jiaqi Ma, Dilek Hakkani-Tür
  - **[一句话总结领域]**: 用采集函数作为奖励模型训练语言模型生成高质量合成数据
  - **[TL;DR]**: 问题：现有数据生成方法缺乏对下游学习者影响的定量评估。方法：提出AcquisitionSynthesis，用采集函数（衡量数据信息量和影响力）作为奖励模型训练语言模型生成数据，在数学、医学问答和编码任务上实现2-7%增益，且对灾难性遗忘更鲁棒。
  - **排除原因：** 医学/临床诊断

- [#47] **The Cost of Perfect English: Pragmatic Flattening and the Erasure of Authorial Voice in L2 Writing Supported by GenAI** — 完美英语的代价：GenAI支持的二语写作中的语用扁平化
  - **[Authors]**: Ao Liu, Shanhua Zhu
  - **[一句话总结领域]**: GenAI润色二语写作时系统性地抹除作者的社会语用多样性
  - **[TL;DR]**: 问题：GenAI工具在提升二语写作流利度的同时，可能牺牲社会语用多样性。方法：分析中国B2级学生议论文经四个主流LLM润色后的变化，发现所有模型在交互维度上大幅 collapse 对话参与标记，在认识立场维度上表现出架构依赖性变异，系统性将多语作者的独特修辞身份覆盖为同质化的盎格鲁-美式范式。

- [#54] **CommonWhy: A Dataset for Evaluating Entity-Based Causal Commonsense Reasoning in Large Language Models** — CommonWhy：评估基于实体的因果常识推理数据集
  - **[Authors]**: Armin Toroghi, Faeze Moradi Kalarde, Scott Sanner
  - **[一句话总结领域]**: 评估LLM基于实体的因果常识推理和解释生成能力的数据集
  - **[TL;DR]**: 问题：现有KGQA数据集主要测试事实检索，缺乏对因果常识推理和解释生成的评估。方法：提出CommonWhy数据集，包含15000个why问题，要求模型进行溯因推理并生成解释，所有知识来自Wikidata，实验揭示SOTA LLM在事实幻觉和因果推理上的显著缺陷。

- [#60] **Training LLMs with Reinforcement Learning for Intent-Aware Personalized Question Answering** — 用RL训练LLM实现意图感知个性化问答
  - **[Authors]**: Maryam Amirizaniani, Benjamin Charles Germain Lee, Jevin West, Nicholas Weber
  - **[一句话总结领域]**: 用RL框架训练模型从单轮问题中推断隐式用户意图
  - **[TL;DR]**: 问题：现有意图感知个性化问答依赖多轮对话或丰富用户画像，在单轮设置中效果有限。方法：提出IAP框架，用基于标签的模式生成个性化、意图落地的答案，通过个性化奖励函数优化意图感知答案轨迹，在LaMP-QA上平均提升7.5%。

- [#67] **Correct Answers from Sound Reasoning: Verifiable Process Supervision for Language Models** — 从可靠推理得出正确答案：语言模型的可验证过程监督
  - **[Authors]**: Kyuyoung Kim, Kevin Wang, Yunfei Xie, Peiyang Xu, Peiyao Sheng, Chen Wei, Zhangyang Wang, Jinwoo Shin, Pramod Viswanath, Sewoong Oh
  - **[一句话总结领域]**: 用可验证过程监督(VPS)联合优化预测精度和推理质量
  - **[TL;DR]**: 问题：仅优化最终结果的RL导致任务精度提升但推理质量下降——出现内部不一致。方法：提出VPS，在可验证领域（如国际象棋）中用结构化推理格式提取中间声明，通过引擎信号评估形成过程级奖励，并引入自适应奖励加权优先处理误差大的组件，恢复一致性至近饱和。
  - **排除原因：** 医学/临床诊断（使用chess但方法通用）

- [#68] **TimelineReasoner: Advancing Timeline Summarization with Large Reasoning Models** — 用大型推理模型推进时间线摘要
  - **[Authors]**: Liancheng Zhang, Xiaoxi Li, Zhicheng Dou
  - **[一句话总结领域]**: 将时间线摘要从静态生成转变为主动推理驱动过程
  - **[TL;DR]**: 问题：现有时间线摘要方法将LLM视为被动生成器，缺乏主动推理和证据获取。方法：提出TimelineReasoner两阶段框架——全局认知跟踪宏观事件并更新全局事件记忆，细节探索识别信息缺口并通过定向文档检索精炼时间线，在开放域TLS数据集上显著超越现有方法。

- [#71] **Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation** — 通过共识驱动偏好优化缓解跨语言文化不一致
  - **[Authors]**: Lucas Resck, Isabelle Augenstein, Anna Korhonen
  - **[一句话总结领域]**: 用C-3PO框架缓解多语言LLM中提示语言覆盖系统人格的文化不一致
  - **[TL;DR]**: 问题：多语言LLM在固定人格下，提示语言变化会导致文化不一致输出（如英语提示输出莎士比亚，西班牙语提示输出塞万提斯）。方法：提出Singleton Fleiss's κ_S量化跨语言文化不一致，设计C-3PO共识驱动对齐框架，实现κ_S绝对提升0.10， disproportionately 改善低资源语言。

- [#75] **Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization** — 通过奖励去相关策略优化实现多目标和混合奖励RL
  - **[Authors]**: Yang Bai, Kaiyuan Liu, Ziyuan Zhuang, Jiahong Zhou, Rongxiang Weng, Xin Chen, Jingang Wang, Xunliang Cai
  - **[一句话总结领域]**: 用RDPO处理多任务RL中异质奖励分布和相关维度问题
  - **[TL;DR]**: 问题：多任务RL中异质奖励分布和相关奖励维度破坏标量优势构建。方法：提出RDPO，先用量值感知分位数归一化稳定提示级优势分配，再在每个活跃奖励子空间内应用马氏距离白化缓解相关冗余，在LongCat-Flash后训练中提升指令遵循和写作质量。

- [#79] **Effective Context in Transformers: An Analysis of Fragmentation and Tokenization** — Transformer中的有效上下文：碎片化和tokenization分析
  - **[Authors]**: Amirmehdi Jafari Fesharaki, Mohammadamin Rami, Aslan Tchamkerten
  - **[一句话总结领域]**: 从信息论角度分析tokenization选择如何影响有限上下文预测器
  - **[TL;DR]**: 问题：相同数据可用字节、字符或子词表示，但在固定上下文窗口下，不同表示暴露的信息不同。方法：在马尔可夫源上研究表示选择的影响，证明碎片化（将符号替换为更细粒度单元）可严格增加最优有限上下文对数损失，而贪婪tokenization可使短token窗口等效于更长的源上下文窗口。

- [#84] **Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution** — 通过外化攻防协同进化实现模型无关的终身LLM安全
  - **[Authors]**: Xiaozhe Zhang, Chaozhuo Li, Hui Liu, Shaocheng Yan, Bingyu Yan, Qiwei Ye, Haoliang Li
  - **[一句话总结领域]**: 用外部可复用结构替代模型特定微调实现终身LLM安全
  - **[TL;DR]**: 问题：现有安全范式将红队和post-training耦合在封闭循环中，导致攻击发现快速饱和且防御难以跨模型迁移。方法：提出EvoSafety框架，攻击侧配备对抗技能库支持持续探测，防御侧用轻量辅助防御模型+记忆检索替代模型特定微调，在Guard模式下以37.5%参数实现99.61%防御成功率，超越Qwen3Guard-8B 14.13%。
  - **排除原因：** 医学/临床诊断

- [#87] **Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling** — 通过简单统一的scaling实现金牌级奥赛推理
  - **[Authors]**: Yafu Li, Runzhe Zhan, Haoran Zhang, Shunkai Zhang, Yizhuo Li, Zhilin Wang, Jiacheng Chen, Futing Wang, Xuyang Hu, Yuchen Fan, Bangjie Xu, Yucheng Su, Xinmiao Han, Chenxi Li, Haodi Lei, Yufeng Zhao, Zejin Lin, Qianjia Cheng, Tong Zhu, Xiaoye Qu, Ganqu Cui, Peng Ye, Yun Luo, Zhouchen Lin, Yu Qiao, Bowen Zhou, Ning Ding, Yu Cheng
  - **[一句话总结领域]**: 用反向困惑度课程SFT+两阶段RL+测试时scaling实现奥赛金牌级推理
  - **[TL;DR]**: 问题：现有推理模型在数学和物理奥赛中达到金牌水平需要复杂流程。方法：提出统一配方——反向困惑度课程SFT培养严格证明搜索和自检行为，两阶段RL（可验证奖励RL→证明级RL） scaling 这些行为，最后用测试时scaling提升性能。30B-A3B模型SU-01在IMO 2025/USAMO 2026和IPhO 2024/2025上达到金牌水平。
  - **排除原因：** 医学/临床诊断

---

## 🧠 LLM 推理能力（llm-reasoning）— 13 篇

**今日动态：** 今日LLM推理方向关注：(1) 推理过程中的幻觉检测与校准，如隐藏状态几何分析和不确定性量化；(2) 上下文学习与推理策略优化；(3) 结构化推理与JSON生成的约束控制。趋势是从输出级评估向内部状态级机理分析深化。

- [#1] **WARDEN: Endangered Indigenous Language Transcription and Translation with 6 Hours of Training Data** — WARDEN：仅用6小时训练数据的濒危原住民语言转录和翻译
  - **[Authors]**: Ziheng Zhang, Yunzhong Hou, Naijing Liu, Liang Zheng
  - **[一句话总结领域]**: 两阶段分离转录-翻译+领域知识增强实现极低资源语言翻译
  - **[TL;DR]**: 问题：濒危语言缺乏大规模训练数据，统一模型在低资源设置下不可行。方法：提出WARDEN，将任务分离为音素转录和翻译两个阶段，转录用相似语言(Sundanese)初始化token加速微调，翻译用专家标注词典为LLM提供领域知识，仅用6小时数据超越更大的开源和专有模型。

- [#5] **Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry** — 推理在何处断裂？通过隐藏状态传输几何进行阶梯级幻觉检测
  - **[Authors]**: Tyler Alvarez, Ali Baheri
  - **[一句话总结领域]**: 用隐藏状态轨迹动力学进行单遍阶梯级幻觉检测
  - **[TL;DR]**: 问题：现有幻觉检测器在轨迹级别操作，无法定位首次错误且需多次采样。方法：将幻觉视为隐藏状态轨迹属性，正确推理沿稳定流形移动而首次错误表现为传输成本的局部偏离；提出对比PCA教师模型和BiLSTM学生模型，在ProcessBench等数据集上超越基线，并证明对比PCA是传输分离目标的最优投影。

- [#9] **Fine-tuning with Hierarchical Prompting for Robust Propaganda Classification Across Annotation Schemas** — 分层提示微调实现跨标注模式的鲁棒宣传分类
  - **[Authors]**: Lukas Stähelin, Veronika Solopova, Max Upravitelev, David Kaplan, Ariana Sahitaj, Premtim Sahitaj, Charlott Jakob, Sebastian Möller, Vera Schmitt
  - **[一句话总结领域]**: 分层提示方法(HiPP)在微调后提升跨标注模式的宣传检测鲁棒性
  - **[TL;DR]**: 问题：宣传检测因噪声文本和低标注一致性而困难，且不同标注模式效果差异大。方法：提出意图导向的宣传技术分类法，比较新旧两种模式，发现微调至关重要；提出HiPP分层提示先预测细粒度技术再聚合，在模糊低一致性模式上尤其有效。

- [#21] **Pretraining Language Models with Subword Regularization: An Empirical Study of BPE Dropout in Low-Resource NLP** — 低资源NLP中BPE Dropout预训练的实证研究
  - **[Authors]**: Ruan Visser, Trienko Grobler, Marcel Dunaiski
  - **[一句话总结领域]**: 预训练和微调阶段均应用BPE Dropout在低资源NLP中最有效
  - **[TL;DR]**: 问题：BPE Dropout通常只在微调时应用，预训练使用确定性tokenization可能导致不匹配。方法：在六种语言（包括Kiswahili和isiXhosa）上系统研究预训练时BPE Dropout的效果，发现预训练和微调均应用时最佳，且预训练时BPE Dropout的益处最大；形态边界对齐仅 modestly 改善，说明随机tokenization的益处主要来自更一致的暴露。

- [#25] **From Rosetta to Match-Up: A Paired Corpus of Linguistic Puzzles with Human and LLM Benchmarks** — 从罗塞塔到匹配：语言谜题配对语料库
  - **[Authors]**: Neh Majmudar, Anne Huang, Jinfan Frank Hu, Elena Filatova
  - **[一句话总结领域]**: 将罗塞塔石谜题系统转换为匹配谜题并评估人和LLM表现
  - **[TL;DR]**: 问题：语言谜题创建复杂耗时，需要高效生成方法。方法：提出系统流程将Rosetta Stone谜题转换为Match-Up对应版本，用人类专家和LLM评估，发现两者在Match-Up谜题上均呈现"全有或全无"模式——要么完全解决要么完全失败。
  - **排除原因：** 多语言/特定语言（语言谜题涉及多种语言）

- [#45] **TruncProof: A Guardrail for LLM-based JSON Generation under Token-Length Constraints** — TruncProof：token长度约束下LLM JSON生成的护栏
  - **[Authors]**: Yoshio Kato, Shuhei Tarashima
  - **[一句话总结领域]**: 用LL(1)解析器属性确保JSON生成在严格token限制下的语法正确性
  - **[TL;DR]**: 问题：LLM生成JSON时无法严格强制执行最大token数，导致截断输出或无限生成。方法：提出TruncProof，利用LL(1)解析器属性在每个解码步骤高效近似完成语法有效输出所需的最小token数，在Text-to-JSON任务上成功生成语法正确输出，且可与高级解码策略结合。

- [#48] **Context Training with Active Information Seeking** — 主动信息 seeking 的上下文训练
  - **[Authors]**: Zeyu Huang, Adhiguna Kuncoro, Qixuan Feng, Jiajun Shen, Lucio Dery, Arthur Szlam, Marc'Aurelio Ranzato
  - **[一句话总结领域]**: 为上下文优化器配备搜索工具实现主动信息获取
  - **[TL;DR]**: 问题：上下文优化方法依赖模型内在知识，无法获取新产生的信息。方法：为上下文优化器配备Wikipedia搜索和浏览器工具，发现直接添加工具反而降低性能；提出基于搜索的训练流程维护和剪枝多个候选上下文，在低资源翻译、健康场景和推理任务上实现一致且显著的提升。

- [#89] **RAG-Enhanced Large Language Models for Dynamic Content Expiration Prediction in Web Search** — RAG增强LLM用于网页搜索动态内容过期预测
  - **[Authors]**: Tingyu Chen, Wenkai Zhang, Li Gao, Lixin Su, Ge Chen, Dawei Yin, Daiting Shi
  - **[一句话总结领域]**: 在百度搜索中部署基于LLM的查询感知动态内容过期预测
  - **[TL;DR]**: 问题：传统网页搜索用静态时间窗口过滤，导致内容可能时间新但语义已过期。方法：提出基于LLM的查询感知动态内容过期预测框架，从文档提取细粒度时间上下文，推断查询特定的"有效期范围"，结合幻觉缓解策略，在离线A/B测试中显著提升搜索新鲜度和用户体验。

- [#92] **Controlling Logical Collapse in LLMs via Algebraic Ontology Projection over F2** — 通过F2上的代数本体投影控制LLM逻辑崩溃
  - **[Authors]**: Hisashi Miyashita, Mgnite Inc
  - **[一句话总结领域]**: 将LLM隐藏状态投影到Galois Field F2实现形式可验证的本体关系编码
  - **[TL;DR]**: 问题：LLM是否以形式可验证的代数结构编码本体关系尚不清楚。方法：提出AOP，仅用42个关系对作为代数密钥将隐藏状态投影到F2，在Gemma-2上达到93.33%零样本包含准确率；发现系统提示作为代数边界条件可防止晚期层崩溃——最后层逻辑一致性的系统性退化。

- [#93] **From Instance Selection to Fixed-Pool Data Recipe Search for Supervised Fine-Tuning** — 从实例选择到固定池数据配方搜索
  - **[Authors]**: Haodong Wu, Jiahao Zhang, Lijie Hu, Yongqi Zhang
  - **[一句话总结领域]**: 将SFT数据选择建模为可执行数据配方搜索问题
  - **[TL;DR]**: 问题：有效SFT子集通常通过有序的数据整理配方产生，而非简单实例排名。方法：提出固定池数据配方搜索问题，引入AutoSelection两层求解器——将固定池物化与昂贵完整评估解耦，使用预热探针、GP辅助排序和停滞触发重播种，在90K指令池上实现最强分布内推理平均。

- [#96] **When Do LLMs Generate Realistic Social Networks? A Multi-Dimensional Study of Culture, Language, Scale, and Method** — LLM何时生成现实社交网络？文化、语言、规模和方法的多维研究
  - **[Authors]**: Sai Hemanth Kilaru, Sriram Theerdh Manikyala, Raghav Upadhyay, Sri Sai Kumar Ramavath, Srivika Nunavathu, Dalal Alharthi
  - **[一句话总结领域]**: 系统研究提示设计、文化框架、提示语言和模型规模对LLM合成社交网络的影响
  - **[TL;DR]**: 问题：LLM生成合成社交网络时，其输出如何依赖提示设计、文化框架、语言和模型规模尚不清楚。方法：形式化四种LLM基于的社会网络生成机制，在四种文化、四种语言、三种模型和四种提示架构下生成192个网络，发现文化框架改变同质性和连通性，政治派别主导连接形成，提示语言单独改变宗教同质性。

- [#105] **PERCEIVE: A Benchmark for Personalized Emotion and Communication Behavior Understanding on Social Media** — PERCEIVE：社交媒体个性化情感和沟通行为理解基准
  - **[Authors]**: Jian Liao, Yujin Zheng, Suge Wang, Jianxing Zheng, Deyu Li
  - **[一句话总结领域]**: 首个整合作者内容、读者情感反馈、沟通行为、用户属性和社交图的个性化情感基准
  - **[TL;DR]**: 问题：现有社交媒体情感分析以作者为中心，忽略不同读者的主观情感反应。方法：提出PERCEIVE双语基准，首次整合五个关键维度，实现从作者中心到读者中心的范式转变，发现SOTA方法在处理这种多面、用户感知任务时存在显著缺陷。

---

## 🏗️ 模型架构与设计（llm-architecture）— 8 篇

**今日动态：** 今日架构方向关注：(1) 小规模预训练中的稠密vs稀疏模型比较；(2) 低秩预训练的几何与谱分析；(3) 线性注意力和状态空间模型的改进。趋势是从单一指标比较向多维度表征分析转变。

- [#6] **Dense vs Sparse Pretraining at Tiny Scale: Active-Parameter vs Total-Parameter Matching** — 小尺度预训练：活跃参数 vs 总参数匹配
  - **[Authors]**: Abdalrahman Wael
  - **[一句话总结领域]**: 在<25M参数范围内比较稠密和MoE模型的预训练表现
  - **[TL;DR]**: 问题：小尺度预训练中稠密和MoE模型的比较在活跃参数和总参数匹配下结论不一致。方法：在固定LLaMA风格配方下训练稠密和MoE模型，MoE在活跃参数匹配下验证损失更优（差距0.0758），但稠密在总参数匹配下更优（差距0.0180），且MoE优势随训练增长而稠密优势缩小。

- [#24] **LLMs as annotators of credibility assessment in Danish asylum decisions: evaluating classification performance and errors beyond aggregated metrics** — LLM作为丹麦庇护决定可信度评估的标注者
  - **[Authors]**: Galadrielle Humblot-Renaux, Mohammad N. S. Jahromi, Rohat Bakuri-Jørgensen, Marieke Anne Heyl, Asta S. Stage Jarlner, Maria Vlachou, Anna Murphy Høgenhaug, Desmond Elliott, Thomas Gammeltoft-Hansen, Thomas B. Moeslund
  - **[一句话总结领域]**: 系统评估LLM在丹麦庇护决定文本标注中的效果和不一致性
  - **[TL;DR]**: 问题：LLM在欠代表语言和需要专家理解的专门领域中的自动标注效果尚未充分探索。方法：构建RAB-Cred丹麦庇护决定数据集，对21个模型和30个提示组合进行基准测试，系统分析错误一致性、类别间混淆和样本难度相关性，确认LLM标注的潜力但突出其不完美和不一致的本质。
  - **排除原因：** 多语言/特定语言（丹麦语）

- [#26] **Exploiting Pre-trained Encoder-Decoder Transformers for Sequence-to-Sequence Constituent Parsing** — 利用预训练编码器-解码器Transformer进行序列到序列成分句法分析
  - **[Authors]**: Daniel Fernández-González, Cristina Outeiriño Cid
  - **[一句话总结领域]**: 用BART/mBART/T5等编码器-解码器模型进行成分句法分析
  - **[TL;DR]**: 问题：现有序列到序列成分分析通常用编码器-only模型初始化，编码器-解码器架构的潜力未充分探索。方法：在BART、mBART和T5上微调生成线性化句法树，在不同线性化策略下评估，在连续和间断成分分析上超越所有先前序列到序列模型，与领先任务特定分析器竞争。

- [#64] **Differences in Text Generated by Diffusion and Autoregressive Language Models** — 扩散与自回归语言模型生成文本的差异
  - **[Authors]**: Zeyang Zhang, Chengwei Liang, Xingyan Chen, Meiqi Gu, Minrui Luo, Jingzhao Zhang, Tianxing He
  - **[一句话总结领域]**: 系统分析扩散语言模型与自回归模型生成文本的内在差异
  - **[TL;DR]**: 问题：DLM与ARM生成文本的内在差异机制尚不清楚。方法：通过控制实验分离训练目标和解码算法的影响，发现DLM训练目标贡献于语义连贯性和多样性提升但对熵影响小；熵降低主要来自解码算法（特别是基于置信度的重掩码策略），并提供理论解释。

- [#72] **EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents** — EVA-Bench：评估语音代理的新端到端框架
  - **[Authors]**: Tara Bogavelli, Gabrielle Gauthier Melançon, Katrina Stankiewicz, Oluwanifemi Bamgbose, Fanny Riols, Hoang H. Nguyen, Raghav Mehndiratta, Lindsay Devon Brin, Joseph Marinier, Hari Subramani, Anil Madamala, Sridhar Krishna Nemala, Srinivas Sunkara
  - **[一句话总结领域]**: 端到端语音代理评估框架，涵盖模拟对话生成和语音特定故障模式测量
  - **[TL;DR]**: 问题：现有基准未同时解决真实模拟对话生成和语音特定故障模式测量。方法：提出EVA-Bench，支持动态多轮对话的bot-to-bot音频对话，引入EVA-A（准确性）和EVA-X（体验）两个复合指标，在12个系统上发现无系统同时在两项指标上超过0.5，且accent和noise扰动暴露显著鲁棒性差距。

- [#74] **Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training** — 超越困惑度：低秩预训练的几何与谱研究
  - **[Authors]**: Namrata Shivagunde, Vijeta Deshpande, Sherin Muckatira, Anna Rumshisky
  - **[一句话总结领域]**: 用16个指标从四个维度表征低秩预训练方法的解质量
  - **[TL;DR]**: 问题：低秩预训练方法通常仅用验证困惑度比较，但困惑度是解质量的差代理。方法：在三个规模（60M/130M/350M）上比较五种低秩方法（GaLore/Fira/CoLA/SLTrain/ReLoRA）与全秩训练，沿16个指标评估损失景观、谱结构、激活相似性，发现各方法收敛到几何不同的盆地，且GaLore最接近全秩。

- [#94] **When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction** — 当注意力关闭：LLM如何在多轮交互中丢失线索
  - **[Authors]**: Vardhan Dongre, Joseph Hsieh, Viet Dac Lai, Seunghyun Yoon, Trung Bui, Dilek Hakkani-Tür
  - **[一句话总结领域]**: 用通道转换框架解释多轮交互中LLM丢失指令的机制
  - **[TL;DR]**: 问题：LLM在长多轮交互中丢失指令、人格和规则，但机制未明。方法：提出通道转换解释——目标定义token通过注意力变得不可访问但残差表征可能持续；引入GAR（目标可访问比率），发现注意力丢失与残差可解码性之间的 gap 预测目标条件行为是否能在通道关闭后存活，Mistral中强制关闭注意力使回忆从近完美降至11%。

- [#102] **WriteSAE: Sparse Autoencoders for Recurrent State** — WriteSAE：用于循环状态的稀疏自编码器
  - **[Authors]**: Jack Young
  - **[一句话总结领域]**: 首个分解和编辑状态空间和混合循环语言模型矩阵缓存写入的SAE
  - **[TL;DR]**: 问题：现有SAE读取残差流，但Gated DeltaNet/Mamba-2/RWKV-7通过rank-1更新写入d_k×d_v缓存，无法被向量原子替代。方法：提出WriteSAE，将每个解码器原子分解为原生写入形状，导出每token logit偏移的闭式解，在匹配Frobenius范数下训练，在92.4%的激发上原子替换优于消融，首次在矩阵循环写入位点实现行为安装。

---

## 🤖 Agentic RL（agent-rl）— 8 篇

**今日动态：** 今日Agentic RL方向关注：(1) 多代理系统中的信用分配问题，如对比信用归因和优势分组策略优化；(2) 个性化和意图感知训练；(3) 语法错误修正中的过度修正问题。趋势是从全局奖励优化向精细化的代理级信号分解演进。

- [#12] **Edit-level Majority Voting Mitigates Over-Correction in LLM-based Grammatical Error Correction** — 编辑级多数投票缓解LLM语法错误修正中的过度修正
  - **[Authors]**: Takumi Goto, Yusuke Sakai, Taro Watanabe
  - **[一句话总结领域]**: 无需训练，用编辑级多数投票缓解语法错误修正的过度修正问题
  - **[TL;DR]**: 问题：LLM语法错误修正常出现过度修正。方法：提出训练自由的推断方法，对单模型生成的多个候选进行编辑级多数投票，在覆盖七种语言的九个基准上多数情况下超越贪婪和MBR解码，且对指令提示变化保持稳定。

- [#33] **PRISM-X: Experiments on Personalised Fine-Tuning with Human and Simulated Users** — PRISM-X：人类和模拟用户的个性化微调实验
  - **[Authors]**: Hannah Rose Kirk, Liu Leqi, Fanzhi Zeng, Henry Davidson, Bertie Vidgen, Christopher Summerfield, Scott A. Hale
  - **[一句话总结领域]**: 大规模被试内实验比较P-DPO个性化微调与提示和模拟用户的效果
  - **[TL;DR]**: 问题：个性化方法通常用模拟用户而非真人评估，其交互模式和判断差异未知。方法：重新招募530名PRISM数据集参与者进行盲法多轮对话，发现P-DPO显著优于通用模型和个性化提示，但模拟用户在个体判断上远低于人类自一致性基线，表现出放大的位置偏见。

- [#34] **CANTANTE: Optimizing Agentic Systems via Contrastive Credit Attribution** — CANTANTE：通过对比信用归因优化代理系统
  - **[Authors]**: Tom Zehle
  - **[一句话总结领域]**: 将多代理系统优化视为信用分配问题，用对比rollout分解系统级奖励
  - **[TL;DR]**: 问题：多代理系统仅在系统级有分数，而代理行为参数是局部的，优化是结构性挑战。方法：提出CANTANTE，通过对比同一查询上多个联合配置的rollout将系统级奖励分解为每代理更新信号，在MBPP上+18.9pp、GSM8K上+12.5pp超越最强基线，且推理成本更低。

- [#59] **All Circuits Lead to Rome: Rethinking Functional Anisotropy in Circuit and Sheaf Discovery for LLMs** — 所有电路通向罗马：重新思考LLM电路和束发现中的功能各向异性
  - **[Authors]**: Xi Chen, Mingyu Jin, Jingcheng Niu, Yutong Yin, Jinman Zhao, Bangwei Guo, Dimitris N. Metaxas, Zhaoran Wang, Yutao Yue, Gerald Penn
  - **[一句话总结领域]**: 挑战功能各向异性假设，证明单一任务可由多个结构不同的电路支持
  - **[TL;DR]**: 问题：电路发现假设功能定位于唯一或近唯一内部机制。方法：提出Overlap-Aware Sheaf Repulsion方法，显式惩罚多次发现运行间的结构重叠，发现单一任务可由多个同时忠实、稀疏和完整的电路支持；进一步发现超稀疏三边束中无单一边不可或缺，提出分布稠密电路假设。

- [#61] **DocAtlas: Multilingual Document Understanding Across 80+ Languages** — DocAtlas：80+语言的多语言文档理解
  - **[Authors]**: Ahmed Heakl, Youssef Mohamed, Abdullah Sohail, Rania Elbadry, Ahmed Nassar, Peter W. J. Staar, Fahad Shahbaz Khan, Imran Razzak, Salman Khan
  - **[一句话总结领域]**: 构建覆盖82语言的高质量OCR数据集和基准，用DPO实现稳定多语言适应
  - **[TL;DR]**: 问题：低资源语言的多语言文档理解受限于稀缺训练数据和模型标注偏见。方法：提出DocAtlas框架，用差异渲染和LaTeX合成构建精确结构标注的82语言OCR数据集，发现DPO使用渲染派生真值作为正信号实现稳定多语言适应，领域内+1.9%、领域外+1.8%且无基语言退化。

- [#76] **RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation** — RealICU：LLM代理是否理解长上下文ICU数据？
  - **[Authors]**: Chengzhi Shen, Weixiang Shen, Tobias Susetzky, Chen, Chen, Jun Li, Yuyuan Liu, Xuepeng Zhang, Zhenyu Gong, Daniel Rueckert, Jiazhen Pan
  - **[一句话总结领域]**: 用事后标注的ICU基准评估LLM在真实临床条件下的推理能力
  - **[TL;DR]**: 问题：现有ICU基准将历史临床行为视为真值，但这些行为在信息不完整时可能是次优的。方法：提出RealICU，由资深医生回顾完整患者轨迹后创建标签，评估患者状态、急性问题、推荐行动和危险信号，发现现有LLM表现差，暴露回忆-安全权衡和锚定偏见两种失败模式。
  - **排除原因：** 医学/临床诊断

- [#78] **AI-Generated Slides: Are They Good? Can Students Tell?** — AI生成幻灯片：质量如何？学生能分辨吗？
  - **[Authors]**: Juho Leinonen, Lisa Zhang, Arto Hellas
  - **[一句话总结领域]**: 比较GenAI工具与人工生成教学幻灯片的质量和学生感知
  - **[TL;DR]**: 问题：GenAI工具用于生成教学幻灯片的潜力和限制尚不清楚。方法：评估NotebookLM、Claude、Copilot和Cursor等工具，发现编码助手工具生成的幻灯片最准确完整；学生认为AI幻灯片与教师幻灯片质量相当且无法可靠区分，但将低质量与AI来源关联。

- [#82] **Cognifold: Always-On Proactive Memory via Cognitive Folding** — Cognifold：通过认知折叠实现始终在线的主动记忆
  - **[Authors]**: Suli Wang, Yiqun Duan, Yu Deng, Rundong Zhao, Dai Shi, Xinliang Zhou
  - **[一句话总结领域]**: 受大脑启发的始终在线代理记忆，通过图拓扑自组织实现主动认知结构
  - **[TL;DR]**: 问题：现有代理记忆主要是反应式和检索式的，缺乏自主组织经验为持久认知结构的能力。方法：提出Cognifold，扩展互补学习系统理论为三层（海马、新皮层、前额叶意图），通过图拓扑自组织实现认知结构的主动组装、合并、衰减、重链接和意图浮现，在7个基准上验证传统记忆任务上的鲁棒性。

---

## 🌈 多模态推理（multimodal-reasoning）— 8 篇

**今日动态：** 今日多模态推理方向聚焦：(1) 视觉-语言推理中的信号分解，如感知-分解置信度奖励；(2) 测试时自适应优化，如查询条件自训练；(3) 几何构造和扩散语言模型的安全生成。趋势是从全局奖励向细粒度、模态感知的信号设计发展。

- [#19] **PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning** — PDCR：视觉语言推理的感知分解置信度奖励
  - **[Authors]**: Hee Suk Yoon, Eunseop Yoon, Ji Woo Hong, SooHwan Eom, Gwanhyeong Koo, Mark Hasegawa-Johnson, Qi Dai, Chong Luo, Chang D. Yoo
  - **[一句话总结领域]**: 将全局置信度奖励分解为感知和推理技能簇，解决V-L推理中的信号退化
  - **[TL;DR]**: 问题：将全局置信度奖励直接应用于视觉-语言推理时，视觉步骤的训练信号被占主导的文本步骤统计扭曲。方法：提出PDCR，用无监督技能分解分离感知和推理步骤（基于视觉依赖评分和聚类），在每个技能簇内归一化置信度增益，在关键V-L推理基准上超越全局奖励和稀疏奖励基线。

- [#27] **Query-Conditioned Test-Time Self-Training for Large Language Models** — 查询条件测试时自训练
  - **[Authors]**: Chaehee Song, Minseok Seo, Yeeun Seong, Doyi Kim, Changick Kim
  - **[一句话总结领域]**: 利用查询本身编码的潜在信号进行测试时参数自适应
  - **[TL;DR]**: 问题：测试时优化需外部数据或优化通用自监督目标，缺乏查询特定对齐。方法：提出QueST，基于输入查询本身编码的足够信号构建结构相关的问题-解对，用这些查询条件对进行测试时参数高效微调，在七个数学推理和GPQA-Diamond上持续超越强基线。

- [#39] **GeoBuildBench: A Benchmark for Interactive and Executable Geometry Construction from Natural Language** — GeoBuildBench：自然语言交互式可执行几何构造基准
  - **[Authors]**: Jinwoong Kim, Rui Yang, Huishuai Zhang
  - **[一句话总结领域]**: 评估多模态代理从自然语言生成可执行几何构造DSL程序的能力
  - **[TL;DR]**: 问题：现有几何基准关注答案正确性或静态图解，忽略交互式构造任务。方法：提出GeoBuildBench，包含489个中文教科书风格问题，要求代理生成DSL程序产生满足约束的几何图，评估发现模型频繁出现结构性幻觉和约束满足失败。

- [#40] **STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes** — STOP：低数据环境下长形式推理的结构化on-policy剪枝
  - **[Authors]**: Chenjun Xu, Zhennan Zhou, Zhan Su, Bill Howe, Lucy Lu Wang, Bingbing Wen
  - **[一句话总结领域]**: 用on-policy算法分析和剪枝长链式思维推理中的冗余推理
  - **[TL;DR]**: 问题：长CoT推理存在过度思考——生成低收益推理增加推断成本和延迟，尤其在低数据微调中。方法：提出STOP，构建自蒸馏轨迹并映射为结构化推理接口，引入ECN（最早正确节点）保留最短正确前缀，在GSM8K等上减少19.4-42.4%生成token同时基本保持精度。

- [#42] **GateKD: Confidence-Gated Closed-Loop Distillation for Robust Reasoning** — GateKD：置信度门控闭环蒸馏实现鲁棒推理
  - **[Authors]**: Kasidit Sermsri, Teerapong Panboonyuen
  - **[一句话总结领域]**: 用教师置信度动态调制蒸馏过程的闭环推理蒸馏框架
  - **[TL;DR]**: 问题：现有推理蒸馏方法假设教师可靠性均匀，传播错误的中间推理。方法：提出GateKD，将教师视为动态守门人而非静态神谕，引入置信度门控软监督、门控隐藏状态进化和可靠性过滤注意力蒸馏三种机制，在常识、逻辑和符号推理基准上超越强开环基线。

- [#50] **Leveraging Multimodal Self-Consistency Reasoning in Coding Motivational Interviewing for Alcohol Use Reduction** — 利用多模态自洽推理编码动机访谈
  - **[Authors]**: Guangzeng Han, James G. Murphy, Benjamin O. Ladd, Xiaolei Huang, Brian Borsari
  - **[一句话总结领域]**: 用音频语言模型的多模态自洽推理自动编码动机访谈
  - **[TL;DR]**: 问题：动机访谈(MI)编码耗时耗力，需要自动化方法。方法：部署音频语言模型，用四个互补分析提示（言语线索、韵律线索、证据评分、对比推理）生成12个独立推理轨迹，通过多数投票确定最终预测，在五个MI音频上实现52.56%准确率和46.40% macro-F1，超越基线。

- [#55] **CiteVQA: Benchmarking Evidence Attribution for Trustworthy Document Intelligence** — CiteVQA：可信文档智能的证据归因基准
  - **[Authors]**: Dongsheng Ma, Jiayu Li, Zhengren Wang, Yijie Wang, Jiahao Kong, Weijun Zeng, Jutao Xiao, Jie Yang, Wentao Zhang, Bin Wang, Conghui He
  - **[一句话总结领域]**: 要求模型返回元素级边界框引用的文档VQA基准
  - **[TL;DR]**: 问题：当前Doc-VQA仅评分最终答案，忽略支撑证据，模型可能答案正确但 grounding 错误。方法：提出CiteVQA，要求模型返回带边界框引用的答案，用严格归因准确率(SAA)评估，在20个MLLM上发现普遍归因幻觉——最强系统SAA仅76.0，最强开源仅22.5。

- [#67] **Correct Answers from Sound Reasoning: Verifiable Process Supervision for Language Models** — 可验证过程监督
  - **[Authors]**: Kyuyoung Kim, Kevin Wang, Yunfei Xie, Peiyang Xu, Peiyao Sheng, Chen Wei, Zhangyang Wang, Jinwoo Shin, Pramod Viswanath, Sewoong Oh
  - **[一句话总结领域]**: 见上文（已列出）
  - **[TL;DR]**: 见上文
  - **排除原因：** 医学/临床诊断

---

## 🎭 多模态 Agentic RL（multimodal-agent-rl）— 5 篇

**今日动态：** 今日多模态Agentic RL方向关注知识图谱遍历的规划机制、群体策略优化和证据归因评估。方向整体偏向评估基准和框架设计。

- [#18] **PersonalAI 2.0: Enhancing knowledge graph traversal/retrieval with planning mechanism for Personalized LLM Agents** — PersonalAI 2.0：用规划机制增强个性化LLM代理的知识图谱遍历/检索
  - **[Authors]**: Mikhail Menschikov, Matvey Iskornev, Alexander Kharitonov, Alina Bogdanova, Mikhail Belkin, Ekaterina Lisitsyna, Artyom Sosedka, Victoria Dochkina, Ruslan Kostoev, Ilia Perepechkin, Evgeny Burnaev
  - **[一句话总结领域]**: 用动态多阶段查询处理管道和图遍历算法增强GraphRAG
  - **[TL;DR]**: 问题：现有GraphRAG方法缺乏自适应迭代信息搜索能力。方法：提出PAI-2，核心是多阶段查询处理管道，支持基于提取实体、匹配图顶点和生成线索查询的自适应迭代搜索，在六个基准上平均提升4%（LLM-as-Judge），图遍历算法平均提升6%，搜索计划增强机制提升18%。

- [#38] **GAGPO: Generalized Advantage Grouped Policy Optimization** — GAGPO：广义优势分组策略优化
  - **[Authors]**: Siyuan Zhu, Chao Yu, Rongxin Yang, Zongkai Liu, Jinjun Hu, Qiwen Chen, Yibo Zhang
  - **[一句话总结领域]**: 无critic的多回合Agentic RL中的精确步级时间信用分配
  - **[TL;DR]**: 问题：多回合RL中智能体仅在回合结束时获得稀疏轨迹级奖励，难以确定中间动作的贡献。方法：提出GAGPO，从采样rollout构建非参数分组价值代理，计算TD/GAE风格时间优势，递归向后传播结果监督，在ALFWorld和WebShop上超越强RL基线。
  - **排除原因：** 医学/临床诊断

- [#55] **CiteVQA: Benchmarking Evidence Attribution for Trustworthy Document Intelligence** — 已在多模态推理中列出
  - **[Authors]**: Dongsheng Ma, Jiayu Li, Zhengren Wang, Yijie Wang, Jiahao Kong, Weijun Zeng, Jutao Xiao, Jie Yang, Wentao Zhang, Bin Wang, Conghui He
  - **[一句话总结领域]**: 见上文
  - **[TL;DR]**: 见上文

- [#97] **Beyond Cooperative Simulators: Generating Realistic User Personas for Robust Evaluation of LLM Agents** — 超越合作模拟器：生成真实用户角色以鲁棒评估LLM代理
  - **[Authors]**: Harshita Chopra, Kshitish Ghate, Aylin Caliskan, Tadayoshi Kohno, Chirag Shah, Natasha Jaques
  - **[一句话总结领域]**: 用进化程序搜索生成真实行为变异的LLM用户模拟器
  - **[TL;DR]**: 问题：LLM用户模拟器继承底层模型的合作同质行为，导致代理在模拟中表现强但在真实用户面前失败。方法：提出Persona Policies(PPol)，将角色生成建模为LLM驱动的进化程序搜索，优化人类相似性和行为模式覆盖的多目标适应度，在零售和航空领域实现33-62%适应度增益，代理在OOD行为上任务成功率+17%。
  - **排除原因：** 医学/临床诊断

- [#99] **Training Large Language Models to Predict Clinical Events** — 训练LLM预测临床事件
  - **[Authors]**: Benjamin Turtel, Paul Wilczewski, Kris Skotheim
  - **[一句话总结领域]**: 将纵向临床记录转换为自然语言预测示例训练LLM
  - **[TL;DR]**: 问题：纵向临床笔记包含丰富的患者时间演化证据，但转换为训练监督具有挑战。方法：扩展Foresight Learning到临床预测，将MIMIC-III时间排序记录转换为过去上下文+未来事件问题+标签，训练小LoRA适配器降低期望校准误差从0.1269到0.0398，Brier分数从0.199到0.145。
  - **排除原因：** 医学/临床诊断

---

## 💻 代码生成与程序合成（code-gen）— 4 篇

**今日动态：** 今日代码生成方向偏向LLM-as-Judge和扩散语言模型的安全生成，关注评估质量和生成安全性。

- [#8] **RTLC -- Research, Teach-to-Learn, Critique: A three-stage prompting paradigm inspired by the Feynman Learning Technique that lifts LLM-as-judge accuracy on JudgeBench with no fine-tuning** — RTLC：受费曼学习技巧启发的三阶段提示范式
  - **[Authors]**: Andrea Morandi
  - **[一句话总结领域]**: 无需微调，用研究-教中学-批判三阶段提示提升LLM-as-Judge准确率
  - **[TL;DR]**: 问题：LLM-as-Judge在JudgeBench上即使强模型也仅略高于随机。方法：提出RTLC三阶段提示——阶段1用费曼技巧固定教学支架包装输入，阶段2以温度0.4采样N=10独立候选裁决，阶段3作为自身批评者交叉比较候选集，Claude 3.7在JudgeBench-GPT上从64.6%提升至78.6%（绝对+14.0pp）。

- [#49] **Adaptive Steering and Remasking for Safe Generation in Diffusion Language Models** — 扩散语言模型安全生成的自适应引导和重掩码
  - **[Authors]**: Yejin Lee, Yo-Sub Han
  - **[一句话总结领域]**: 用对比安全方向和自适应重掩码在扩散语言模型去噪过程中进行步骤级干预
  - **[TL;DR]**: 问题：扩散语言模型在中间去噪步骤生成的有害token会传播并最终导致不安全输出。方法：提出对比安全方向(SGD)捕捉有害与安全生成之间的语义边界，检测有害对齐时重掩码对应token并以与有害程度成比例的强度自适应引导，将jailbreak成功率降至0.64%同时保持生成质量。

- [#56] **Persona-Model Collapse in Emergent Misalignment** — 涌现错位中的人格-模型崩溃
  - **[Authors]**: Davi Bastos Costa, Renato Vicente
  - **[一句话总结领域]**: 用道德易感性和道德鲁棒性度量揭示涌现错位涉及人格-模型崩溃
  - **[TL;DR]**: 问题：在有害内容上微调的模型在无关提示上广泛错位——涌现错位的机制不明。方法：提出人格-模型崩溃假设，用道德易感性(S)和道德鲁棒性(R)两个度量评估模型区分和维持一致角色的能力，发现不安全微调使S平均增加55%、R平均降低65%，提供涌现错位的敏感诊断。

- [#57] **REALISTA: Realistic Latent Adversarial Attacks that Elicit LLM Hallucinations** — REALISTA：诱发LLM幻觉的真实潜在对抗攻击
  - **[Authors]**: Buyun Liang, Jinqi Luo, Liangzu Peng, Kwan Ho Ryan Chan, Darshan Thaker, Kaleab A. Kinfu, Fengrui Tian, Hamed Hassani, René Vidal
  - **[一句话总结领域]**: 在潜在空间中用输入依赖的编辑方向字典实现真实对抗攻击
  - **[TL;DR]**: 问题：离散提示攻击搜索空间有限，连续潜在攻击常解码为无效改写。方法：提出REALISTA，构建输入依赖的有效编辑方向字典（每个方向对应语义等价的连贯改写），在潜在空间优化这些方向的连续组合，在开源LLM和大型推理模型上实现优越或可比性能，尤其在前者失败的长形式响应设置中成功。

---

## 📊 大模型评测（llm-evaluation）— 4 篇

**今日动态：** 今日评测方向关注文档级翻译精炼的实际改进维度、地理文本翻译和不确定性量化，强调超越聚合指标的细粒度评估。

- [#28] **What Does LLM Refinement Actually Improve? A Systematic Study on Document-Level Literary Translation** — LLM精炼实际改进了什么？
  - **[Authors]**: Shaomu Tan, Dawei Zhu, Ke Tran, Michael Denkowski, Sony Trenous, Bill Byrne, Leonardo Ribeiro, Felix Hieber
  - **[一句话总结领域]**: 系统研究文档级文学翻译中LLM精炼的机制和局限
  - **[TL;DR]**: 问题：文档级LLM精炼的改进维度、管道行为和模型机制 poorly understood。方法：在九个LLM和七个语言对上系统研究，发现文档级MT+片段级精炼是最稳健配方，文档级精炼收益更小；大规模人工评估显示改进主要来自流利度、风格和术语，充分性改进有限且不一致；精炼将输出投影到精炼者分布而非针对性修复错误。

- [#53] **ATD-Trans: A Geographically Grounded Japanese-English Travelogue Translation Dataset** — ATD-Trans：地理基础日英游记翻译数据集
  - **[Authors]**: Shohei Higashiyama, Hiroki Ouchi, Atsushi Fujita, Masao Utiyama
  - **[一句话总结领域]**: 地理基础日英游记翻译数据集，支持地理实体级MT评估
  - **[TL;DR]**: 问题：地理文本的准确机器翻译对多语言地理信息公平访问至关重要，但缺乏专门评估资源。方法：提出ATD-Trans数据集，支持整体和地理实体级MT质量评估，覆盖日本国内和海外区域，实验发现日语增强模型有优势，国内区域地理实体翻译更困难。
  - **排除原因：** 多语言/特定语言（日英翻译）

- [#88] **LLMs as Implicit Imputers: Uncertainty Should Scale with Missing Information** — LLM作为隐式填补者：不确定性应随缺失信息增长
  - **[Authors]**: Stef van Buuren
  - **[一句话总结领域]**: 用多重填补标准评估LLM在不完备上下文中的不确定性量化
  - **[TL;DR]**: 问题：LLM在不完备上下文中生成答案时，其不确定性度量是否随缺失信息增长尚不清楚。方法：在SQuAD上控制系统移除上下文五个级别，评估基于采样的置信度和熵，发现置信度不反映缺失信息增长（即使精度崩溃仍保持高位），而熵随上下文移除增加且解释更多精度方差。

- [#98] **Mechanism Plausibility in Generative Agent-Based Modeling** — 生成式基于代理建模中的机制合理性
  - **[Authors]**: Patrick Zhao, David Huu Pham, Nicholas Vincent
  - **[一句话总结领域]**: 区分LLM-ABM的生成充分性和机制合理性，提出四级评估量表
  - **[TL;DR]**: 问题：LLM-ABM研究通常测试生成不同现象的能力，但能力、预测和解释是不同的——解释需要展示现象如何由相关组织实体和活动产生。方法：整合LLM-ABM与科学哲学文献，提出机制合理性四级量表，分离生成充分性（再现现象的能力）和机制合理性（现象如何被产生），澄清预测模型和解释模型的不同角色。
  - **排除原因：** 医学/临床诊断

---

## 🎓 大模型训练与微调（llm-training）— 4 篇

**今日动态：** 今日训练方向关注低资源语音识别的课程学习、EFL写作中的AI使用模式，以及数据约束下的混合预训练scaling规律。

- [#43] **Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition** — Vividh-ASR：鲁棒印度语音识别的复杂度分层基准
  - **[Authors]**: Kush Juvekar, Kavya Manohar, Aditya Srinivas Menon, Arghya Bhattacharya, Kumarmanas Nethil
  - **[一句话总结领域]**: 复杂度分层诊断印度语ASR中的studio-bias现象
  - **[TL;DR]**: 问题：多语言ASR模型在低资源语言上微调时常改善朗读语音但退化自发音频——studio-bias。方法：提出Vividh-ASR基准，分层为studio、broadcast、spontaneous和synthetic noise，发现早期大参数更新改善全局WER 12个绝对点，难到易课程增加自发语音收益，提出R-MFT使244M模型匹配769M对手。
  - **排除原因：** 医学/临床诊断

- [#63] **Exploring how EFL students talk to and through AI to develop texts** — 探索EFL学生如何与AI对话并借助AI发展文本
  - **[Authors]**: David James Woo, Yangyang Yu, Yilin Huang, Deliang Wang, Kai Guo, Chi Ho Yeung
  - **[一句话总结领域]**: 分析香港中学生使用AI聊天机器人完成写作任务的提示策略和修辞责任模式
  - **[TL;DR]**: 问题：GenAI为EFL写作教学引入新考虑，但学生如何与AI交互的模式尚不清楚。方法：分析44名香港中学生完成课程写作任务的屏幕录像，识别十种提示策略和三种修辞责任模式（AI主导52%、人类主导25%、协作14%），发现修辞责任模式对写作表现无显著多变量效应。
  - **排除原因：** 多语言/特定语言（EFL教育场景）

- [#83] **LIFT: Last-Mile Fine-Tuning for Table Explicitation** — LIFT：表格显化的最后一英里微调
  - **[Authors]**: Divij Khaitan, Ashish Tiwari
  - **[一句话总结领域]**: 用预训练LLM提取初始表格+微调SLM修复错误的 last-mile 微调
  - **[TL;DR]**: 问题：端到端微调SLM进行表格提取在数据有限时效果差。方法：提出Lift pipeline，预训练LLM从非结构化文本提取初始表格，微调1B-24B SLM修复错误，在2596个表格上匹配或超越端到端微调，仅需1000训练示例即超越0.144 TEDS点，对输入格式变异更鲁棒。

- [#103] **Scaling Laws for Mixture Pretraining Under Data Constraints** — 数据约束下混合预训练的Scaling Laws
  - **[Authors]**: Anastasiia Sedova, Skyler Seto, Natalie Schluter, Pierre Ablin
  - **[一句话总结领域]**:  scarce目标语料可重复15-20次，提出重复感知混合scaling law
  - **[TL;DR]**: 问题：混合预训练中稀缺目标数据与丰富通用数据的配比存在根本性权衡。方法：在2000+次训练运行中系统研究，发现混合训练比单源训练容忍更高重复——稀缺目标语料可重复15-20次，最优重复次数取决于目标数据大小、计算预算和模型规模；提出重复感知混合scaling law，提供有效混合配置的原理化计算。

---

## 🤖 Agent 架构与设计（agent-design）— 3 篇

**今日动态：** 今日Agent架构方向关注多代理通信效率和公平性评估，呈现从文本通信向权重空间通信的新趋势。

- [#2] **Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights** — 好的代理朋友不只给口头建议：它们可以更新你的权重
  - **[Authors]**: Wenrui Bao, Huan Wang, Jian Wang, Zhangyang Wang, Kai Wang, Yuzhang Shang
  - **[一句话总结领域]**: 用权重空间通信替代自然语言消息实现高效多代理协作
  - **[TL;DR]**: 问题：多代理LLM系统通过自然语言消息协作，但序列化中间计算增加token成本、prefill开销和KV缓存内存。方法：提出TFlow框架，将发送者的隐藏状态编译为瞬态低秩LoRA扰动，通过学习参数生成器映射为接收者模块的扰动，在五个基准上提升8.5准确率点同时减少处理token达32.69%，wall-clock时间加速4.6倍。

- [#62] **In-Situ Behavioral Evaluation for LLM Fairness, Not Standardized-Test Scores** — 用现场行为评估而非标准化测试分数评估LLM公平性
  - **[Authors]**: Zeyu Tang, Sang T. Truong, Deonna Owens, Shreyas Sharma, Yibo Jacky Zhang, Brando Miranda, Sanmi Koyejo
  - **[一句话总结领域]**: 用多代理对话框架嵌入受控变异因子进行LLM公平性的现场行为评估
  - **[TL;DR]**: 问题：标准化测试范式评估LLM公平性时，表面级提示构建选择占分数方差大部分，导致公平性结论方向和幅度变化。方法：提出MAC-Fairness多代理对话框架，将标准化测试问题重新用作对话种子而非评估工具，评估立场持久性和同伴接受度，发现现场行为评估揭示稳定、模型特定的行为特征。

- [#66] **BoostTaxo: Zero-Shot Taxonomy Induction via Boosting-Style Agentic Reasoning and Constraint-Aware Calibration** — BoostTaxo：通过Boosting风格代理推理和约束感知校准进行零样本分类法归纳
  - **[Authors]**: Yancheng Ling, Zhenlin Qin, Leizhen Wang, Zhenliang Ma
  - **[一句话总结领域]**: 用boosting风格LLM框架粗到细地进行零样本分类法归纳
  - **[TL;DR]**: 问题：现有分类法归纳方法在零样本和大规模场景下的泛化、结构可靠性和效率有限。方法：提出BoostTaxo，粗到细进行父节点识别，采用检索增强定义精炼、混合父候选选择、候选评分和结构感知分数校准，轻量LLM过滤候选、大LLM排序，在WordNet等三个基准上达到SOTA或可比性能。

---

## ⚡ 模型效率与压缩（llm-efficiency）— 3 篇

**今日动态：** 今日效率方向关注强到弱蒸馏中的局部可教性崩溃和on-device PII替换，强调监督信号的质量而非数量。

- [#11] **Prefix Teach, Suffix Fade: Local Teachability Collapse in Strong-to-Weak On-Policy Distillation** — 前缀教学，后缀消退：强到弱on-policy蒸馏中的局部可教性崩溃
  - **[Authors]**: Kaiyuan Liu, Ziyuan Zhuang, Yang Bai, Bing Wang, Rongxiang Weng, Jieping Ye
  - **[一句话总结领域]**: 发现强到弱on-policy蒸馏中轨迹后缀的局部可教性崩溃现象
  - **[TL;DR]**: 问题：强到弱on-policy蒸馏假设全程密集反馈单调提升性能，但该假设有时失效。方法：发现局部可教性崩溃现象——轨迹后缀虽仍有教师-学生优势但缺乏使密集反馈有效的局部对比；提出轨迹特定释放规则，测量教师在学生top-K候选集上的边距，在NLTK分词语句段上聚合，检测BIC风格变点后截断密集监督，在五个基准上持续超越标准全程OPD。

- [#15] **Locale-Conditioned Few-Shot Prompting Mitigates Demonstration Regurgitation in On-Device PII Substitution with Small Language Models** — 区域条件少样本提示缓解on-device PII替换中的演示回归
  - **[Authors]**: Anuj Sadani, Deepak Kumar
  - **[一句话总结领域]**: 用区域条件旋转少样本提示修复1-bit SLM在PII替换中的演示回归问题
  - **[TL;DR]**: 问题：on-device PII替换中，1-bit SLM会逐字回归固定少样本演示输出，与量化位数无关。方法：提出区域条件旋转少样本提示——字符范围启发式选择纯区域池，每输入MD5哈希采样三个演示，修复后482/482次调用成功无回声，但SLM surrogate在下游NER上表现差于faker（诚实负面发现）。

- [#35] **IndicMedDialog: A Parallel Multi-Turn Medical Dialogue Dataset for Accessible Healthcare in Indic Languages** — IndicMedDialog：印度语多轮医学对话数据集
  - **[Authors]**: Shubham Kumar Nigam, Suparnojit Sarkar, Piyush Patel
  - **[一句话总结领域]**: 覆盖九种印度语的并行多轮医学对话数据集
  - **[TL;DR]**: 问题：现有医学对话系统多为单轮或模板化，缺乏多轮真实性和多语言适用性。方法：提出IndicMedDialog，扩展MDDial为英语+九种印度语的并行多轮医学对话，经母语者验证和脚本感知后处理，微调IndicMedLM实现个性化多轮症状引出，系统误差分析跨越十种语言。
  - **排除原因：** 医学/临床诊断

---

## 🌐 多模态 Agent（multimodal-agent）— 3 篇

**今日动态：** 今日多模态Agent方向关注记忆搜索反思、全模态LLM的表征-行动差距和医学知识的时间感知。

- [#17] **R^2-Mem: Reflective Experience for Memory Search** — R^2-Mem：用于记忆搜索的反思经验
  - **[Authors]**: Xinyuan Wang, Wenyu Mao, Junkang Wu, Xiang Wang, Xiangnan He
  - **[一句话总结领域]**: 用评分标准引导评估器和自反思学习器提升记忆搜索效果
  - **[TL;DR]**: 问题：现有深度搜索代理因未能从历史搜索轨迹中学习而重复过去错误。方法：提出R^2-Mem反思经验框架，离线阶段用评分标准引导评估器评分历史轨迹中的低质量和高质量步骤，自反思学习器蒸馏抽象经验；在线推理时检索经验指导未来搜索，F1提升22.6%，token消耗降低12.9%，搜索迭代减少20.2%。

- [#73] **Senses Wide Shut: A Representation-Action Gap in Omnimodal LLMs** — 感官紧闭：全模态LLM中的表征-行动差距
  - **[Authors]**: Trung Nguyen Quang, Yiming Gao, Fanyi Pu, Kaichen Zhang, Shuo Sun, Ziwei Liu
  - **[一句话总结领域]**: 揭示全模态LLM能编码感知-前提不匹配但极少在输出中拒绝错误主张
  - **[TL;DR]**: 问题：全模态模型声称能联合处理视频、音频和文本，但当文本前提与感官输入冲突时是否真正 grounded 未测试。方法：引入IMAVB基准（500个长电影片段，2×2设计交叉目标模态和误导条件），发现表征-行动差距——隐藏状态可靠编码不匹配但输出几乎从不拒绝；提出探针引导logit调整(PGLA)将编码信号重新注入解码，一致改善拒绝行为。

- [#90] **Large Language Models Lack Temporal Awareness of Medical Knowledge** — 大型语言模型缺乏医学知识的时间感知
  - **[Authors]**: Zihan Guan, Qiao Jin, Guangzhi Xiong, Fangyuan Chen, Mengxuan Hu, Qingyu Chen, Yifan Peng, Zhiyong Lu, Anil Vullikanti
  - **[一句话总结领域]**: 构建TempoMed-Bench评估LLM医学知识的时间感知能力
  - **[TL;DR]**: 问题：现有医学知识评估基于非时间考试式基准，忽略医学知识的动态演化。方法：构建TempoMed-Bench，通过演化指南知识评估LLM医学时间感知，发现(1)模型性能随时间线性下降而非知识截断行为，(2)历史知识准确率仅为最新知识的25.37%-53.89%，(3)时间不一致行为频繁出现；结合代理搜索工具也难以解决。
  - **排除原因：** 医学/临床诊断

---

## 📚 知识与记忆（llm-knowledge）— 3 篇

**今日动态：** 今日知识方向关注长上下文生物医学实体链接和多语言口语词分类的元学习。

- [#20] **LongBEL: Long-Context and Document-Consistent Biomedical Entity Linking** — LongBEL：长上下文和文档一致的生物医学实体链接
  - **[Authors]**: Adam Remaki, Xavier Tannier, Christel Gérardin
  - **[一句话总结领域]**: 文档级生成框架结合全文档上下文和记忆实现生物医学实体链接
  - **[TL;DR]**: 问题：生物医学实体链接通常独立链接每个提及，忽略文档内依赖导致不一致预测。方法：提出LongBEL，文档级生成框架结合全文档上下文和先前预测记忆，用交叉验证预测而非金标签训练减少训练-推理不匹配，在五个跨语言生物医学基准上超越句子级基线，对重复概念增益最大。
  - **排除原因：** 医学/临床诊断

- [#44] **Does language matter for spoken word classification? A multilingual generative meta-learning approach** — 语言对口语词分类重要吗？
  - **[Authors]**: Batsirayi Mupamhi Ziki, Louise Beyers, Ruan van der Merwe
  - **[一句话总结领域]**: 应用生成式元持续学习算法于多语言口语词分类
  - **[TL;DR]**: 问题：元学习在少样本单语口语词分类上优于监督学习，但在多语言设置中探索不足。方法：应用GeMCL算法于英语、德语、法语和加泰罗尼亚语，发现多语言模型表现最好但模型间差异意外低，训练期间看到的唯一数据小时数是更强的性能指标而非包含语言数量。

- [#46] **Scaling few-shot spoken word classification with generative meta-continual learning** — 用生成式元持续学习扩展少样本口语词分类
  - **[Authors]**: Louise Beyers, Batsirayi Mupamhi Ziki, Ruan van der Merwe
  - **[一句话总结领域]**: 用GeMCL实现1000类×5 shot的规模化少样本口语词分类
  - **[TL;DR]**: 问题：少样本口语词分类主要考虑少量类别，大规模潜力未开发。方法：用GeMCL训练模型区分1000类每类5个样本，发现GeMCL产生异常稳定的性能，与反复全微调的HuBERT相当但适应速度快2000倍，训练数据不到一半、时间少两个数量级。

---

## 👁️ 视觉语言模型（vlm）— 3 篇

**今日动态：** 今日VLM方向关注多语言多模态模型合并、缺失模态校准和视觉语言导航的鲁棒性。

- [#52] **DiM3: Bridging Multilingual and Multimodal Models via Direction- and Magnitude-Aware Merging** — DiM3：通过方向和幅度感知合并桥接多语言和多模态模型
  - **[Authors]**: Zijing Wang, Mingyang Wang, Ercong Nie, Yongkang Liu, Shi Feng, Mengjie Zhao, Daling Wang, Xiaocui Yang, Hinrich Schütze
  - **[一句话总结领域]**: 训练无关的多语言多模态模型合并方法，在共享骨干中选择性组合异质更新
  - **[TL;DR]**: 问题：扩展现有多模态模型到多语言通常需要昂贵的数据构建和端到端重训练。方法：提出DiM3，在共享语言模型骨干的每个参数维度上选择性组合多语言和多模态更新，保留原始视觉编码器和投影器，在57种语言的LLaVA和Qwen骨干上超越现有合并基线，与专门微调竞争同时保留通用多模态能力。

- [#69] **Bridging the Missing-Modality Gap: Improving Text-Only Calibration of Vision Language Models** — 桥接缺失模态差距
  - **[Authors]**: Mingyeong Kim, Jungwon Choi, Chaeyun Jang, Juho Lee
  - **[一句话总结领域]**: 用轻量潜在想象模块恢复VLM在纯文本输入下的准确率和校准
  - **[TL;DR]**: 问题：VLM在纯文本输入下准确率大幅下降且严重误校准，即使文本描述保留关键内容。方法：提出潜在想象模块(LIM)，轻量交叉注意力模块从文本输入预测潜在嵌入并馈入冻结VLM骨干，无需像素级图像合成，在纯文本基准、未见任务和缺失图像场景中提升准确率并降低校准误差。

- [#86] **What Limits Vision-and-Language Navigation?** — 什么限制了视觉语言导航？
  - **[Authors]**: Yunheng Wang, Yuetong Fang, Taowen Wang, Lusong Li, Kun Liu, Junzhe Xu, Zizhao Yuan, Yixiao Feng, Jiaxi Zhang, Wei Lu, Zecui Zeng, Renjing Xu
  - **[一句话总结领域]**: 用目标位置先验和立体视觉增强视觉语言导航的跨域鲁棒性
  - **[TL;DR]**: 问题：VLN代理从模拟到真实世界部署时性能严重退化，主要因感知不稳定和指令不明确。方法：提出StereoNav，引入目标位置先验作为跨域持久桥梁提供稳定视觉引导，利用立体视觉构建语义和几何统一表示，在R2R-CE和RxR-CE上达到SOTA且使用显著更少的参数和训练数据，真实世界机器人部署验证导航可靠性提升。

---

## 🔍 RAG（rag）— 2 篇

**今日动态：** 今日RAG方向关注多模态证据选择的效用导向方法和领域适应策略。

- [#36] **Utility-Oriented Visual Evidence Selection for Multimodal Retrieval-Augmented Generation** — 多模态RAG的效用导向视觉证据选择
  - **[Authors]**: Weiqing Luo, Zongye Hu, Xiao Wang, Zhiyuan Yu, Haofeng Zhang, Ziyi Huang
  - **[一句话总结领域]**: 从信息论视角将多模态证据选择重构为效用最大化问题
  - **[TL;DR]**: 问题：多模态RAG中现有视觉证据选择方法依赖语义相关性或表面相似性，与下游推理实际效用不对齐。方法：从信息论视角定义证据效用为对模型输出分布诱导的信息增益，引入潜在证据帮助度概念并证明其在温和假设下与答案空间效用等价，提出无训练 surrogate 加速框架，在MRAG-Bench上超越SOTA同时大幅降低计算成本。

- [#70] **Domain Adaptation of Large Language Models for Polymer-Composite Additive Manufacturing Using Retrieval-Augmented Generation and Fine-Tuning** — 用RAG和微调实现LLM在聚合物复合增材制造领域的适应
  - **[Authors]**: Saiful Islam Sagor, Tania Haghighi, Minhaj Nur Alam, Erina Baynojir Joyee
  - **[一句话总结领域]**: RAG在增材制造专业工程领域优于原始领域文本微调
  - **[TL;DR]**: 问题：通用LLM在增材制造等专业工程领域因领域 grounding 不足而表现差。方法：构建精选AM语料库，评估LLaMA-3-8B的三种配置，发现RAG模型在200个专家设计问题上75.5%更准确、85.2%更受偏好、90.8%更相关，而原始领域文本微调反而降低性能（仅5.6%更准确），表明RAG是更有效的领域适应路径。

---

## 🔎 检索模型与排序（retrieval-model）— 1 篇

- [#23] **Continual Learning with Multilingual Foundation Model** — 多语言基础模型的持续学习
  - **[Authors]**: Barathi Ganesh HB, Michal Ptaszynski, Rene Melendez, Juuso Eronen
  - **[一句话总结领域]**: 多阶段框架检测多语言社交媒体中 reclaim 的侮辱性词汇
  - **[TL;DR]**: 问题：识别跨英语、西班牙语和意大利语推文中LGBTQ+相关侮辱性词汇的 reclaim 与非reclaim 用法具有挑战。方法：提出多阶段框架，整合数据驱动模型选择、回译语义保持增强、动态epoch级欠采样归纳迁移学习和掩码语言建模领域知识注入，XLM-RoBERTa为基础模型，语言特定阈值优化实现2-5%绝对F1提升。

---

## 🔬 可解释性与机理（llm-interpret）— 1 篇

- [#29] **Probing Persona-Dependent Preferences in Language Models** — 探测语言模型中的人格依赖偏好
  - **[Authors]**: Oscar Gilg, Pierre Beckmann, Daniel Paleka, Patrick Butlin
  - **[一句话总结领域]**: 用线性探针在残差流激活中识别跨人格共享的偏好向量
  - **[TL;DR]**: 问题：LLM可采纳不同人格且这些人格有截然不同的偏好，但内部实现方式不明——每个人格是否有独立偏好机制或底层共享。方法：在Gemma-3-27B和Qwen-3.5-122B残差流上训练线性探针预测成对任务选择，识别 genuine 偏好向量，发现该表示跨人格 largely 共享——一个人格上训练的探针可预测和引导另一人格（包括邪恶人格）的选择。

---

## 📝 提示工程（prompt-engineering）— 1 篇

- [#51] **Leveraging Speech to Identify Signatures of Insight and Transfer in Problem Solving** — 利用言语识别问题解决中的洞察和迁移特征
  - **[Authors]**: Linas Nasvytis, Judith E. Fan
  - **[一句话总结领域]**: 通过分析189名参与者解决火柴棍算术问题的言语报告识别可迁移洞察的特征
  - **[TL;DR]**: 问题：洞察的形式及其对后续类似问题解决的影响尚不清楚。方法：分析189名参与者在解决五个火柴棍算术问题时的出声思维，发现解决同类问题（Same组）的参与者比解决不同类问题（Different组）进步更快，且随着进步他们更可能自发对问题进行分类——可迁移洞察的特征是其可言语报告性。
  - **排除原因：** 医学/临床诊断（心理学实验）

---

## 🔧 工具使用与 API 调用（tool-use）— 1 篇

- [#65] **ToolWeave: Structured Synthesis of Complex Multi-Turn Tool-Calling Dialogues** — ToolWeave：复杂多轮工具调用对话的结构化合成
  - **[Authors]**: Dinesh Khandelwal, Gnana Prakash Punnavajhala, GPS Bhargav, Gaurav Pandey, Sachin Joshi, Hima Karanam, Dinesh Raghu
  - **[一句话总结领域]**: 用结构化框架合成真实多轮工具调用对话，减少参数幻觉
  - **[TL;DR]**: 问题：现有合成数据管道生成不真实的工具调用对话——工具链仅表面兼容且参数常出现幻觉。方法：提出ToolWeave，构建内置依赖关系的工具并过滤与用户目标对齐的工作流，通过细粒度规划阶段显式跟踪参数来源减少幻觉，生成对话中多步交互增加45%，Llama-3.1-70B在BFCL-V3多轮上从23.50%提升至39.75%。

---

## 🎨 LLM 应用（llm-app）— 1 篇

- [#81] **Assessing the Creativity of Large Language Models: Testing, Limits, and New Frontiers** — 评估大型语言模型的创造力
  - **[Authors]**: Samuel Schapiro, Alexi Gladstone, Jonah Black, Heng Ji
  - **[一句话总结领域]**: 系统评估人类创造力测试对预测LLM创造力的有效性，提出DRAT测试
  - **[TL;DR]**: 问题：将人类创造力测试用于LLM的有效性未建立，且这些测试对人类创造力的预测力本就有限。方法：大规模系统研究DAT、CDAT等测试对LLM创造性写作、发散思维和科学构思的预测力，发现测试有效性因构建而异且无单一测试预测所有构建；提出DRAT，首个同时评估收敛和发散思维且显著预测科学构思能力的测试。

---

## 🛡️ Agent 安全与对齐（agent-safety）— 1 篇

- [#95] **Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue** — 通过对话对齐世界模型实现具身多代理协调
  - **[Authors]**: Vardhan Dongre, Dilek Hakkani-Tür
  - **[一句话总结领域]**: 扩展PARTNR基准，评估LLM具身代理是否通过对话实现真正的世界模型对齐
  - **[TL;DR]**: 问题：LLM具身代理能否通过对话实现真正的世界模型对齐而非表面协调尚不清楚。方法：扩展PARTNR基准添加自然语言对话通道，提出观察收敛、信息新颖性和信念敏感消息三个世界模型对齐度量，在三个LLM上发现对话减少行动冲突40-83个百分点但降低任务成功率——揭示表面协调与真正对齐之间的差距。

---

## 🆕 新增 Topic

> 本次整理未发现新的 Topic，所有论文均已归入现有分类体系。

---

## 📊 统计

- 总论文数：106
- 排除论文数：25（多语言/特定语言 0 篇，医学/临床 25 篇）
- Topic 数量：22
- 各 Topic 论文数：
  - 对齐与安全(llm-alignment): 15
  - RL for Reasoning(rl-reasoning): 14
  - LLM 推理能力(llm-reasoning): 13
  - 模型架构与设计(llm-architecture): 8
  - Agentic RL(agent-rl): 8
  - 多模态推理(multimodal-reasoning): 8
  - 多模态 Agentic RL(multimodal-agent-rl): 5
  - 代码生成与程序合成(code-gen): 4
  - 大模型评测(llm-evaluation): 4
  - 大模型训练与微调(llm-training): 4
  - Agent 架构与设计(agent-design): 3
  - 模型效率与压缩(llm-efficiency): 3
  - 多模态 Agent(multimodal-agent): 3
  - 知识与记忆(llm-knowledge): 3
  - 视觉语言模型(vlm): 3
  - RAG(rag): 2
  - 检索模型与排序(retrieval-model): 1
  - 可解释性与机理(llm-interpret): 1
  - 提示工程(prompt-engineering): 1
  - 工具使用与 API 调用(tool-use): 1
  - LLM 应用(llm-app): 1
  - Agent 安全与对齐(agent-safety): 1
