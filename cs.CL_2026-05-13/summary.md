# cs.CL 论文整理 - 2026-05-13

**整理时间**: 2026-05-13 17:57:12
**论文总数**: 127
**排除**: 17（多语言/特定语言 9 篇，医学/临床 8 篇）
**Topic 数量**: 24

---

## 📋 今日研究动态总览

| Topic | 论文数 | 核心关键词 |
|-------|--------|-----------|

| 对齐与安全 | 11/12 | hallucination, bias, watermark, unlearning, calibration |
| 大模型评测 | 10/11 | LLM-as-Judge, difficulty estimation, safety-oriented, automated |
| 模型效率与压缩 | 9/10 | segmented execution, MegaKernel, KV-cache, distillation |
| 可解释性与机理 | 8 | geometric memory, belief space, SAE, context-parametric conflict |
| Agent 架构与设计 | 8 | multi-agent, planning, tool-use, long-horizon |
| RL for Reasoning | 7 | GRPO, entropy, self-distillation, exploration |
| 模型架构与设计 | 6/7 | multi-token generation, bidirectional coupling, attractor, MoE |
| 检索模型与排序 | 6 | embedding refinement, generative retrieval, test-time compute |
| 大模型训练与微调 | 6 | CLM detour, DLM, calibration, OPD, layer allocation |
| 文本生成 | 4 | controlled generation, diffusion, PEFT composability |
| 知识与记忆 | 4 | popularity bias, context-memory conflict, model editing |
| 多模态 Agent | 4 | GUI agent, world action model, VLA, presentation agent |
| LLM 应用 | 3/4 | data entry, tabular, scientific discovery |
| 自然语言理解 | 3/4 | MWE classification, misinformation, child-directed language |
| Agentic RL | 3 | skill graph, action guidance, GRPO, self-distillation |
| Agent 安全与对齐 | 3 | attack surface, deception, compromise detection |
| 视觉语言模型 | 3 | RAW measurement, reasoning-prefix masking, model routing |
| 基准与数据集 | 2/7 | memory, scam, clinical acuity, multi-hop |
| 多模态生成 | 2/4 | ad generation, video summarization, cross-modal |
| 对话系统 | 2 | proactive dialogue, user simulation, causal inference |
| 多模态推理 | 2 | visual latent reasoning, distillation, CoT |
| 代码生成与程序合成 | 2 | code reasoning, stepwise execution, self-training |
| 语音与音频 | 1/3 | ASR, SAE, mechanistic interpretability |
| 信息抽取 | 1/3 | causal relation, disaster intelligence, social media |

---

## 对齐与安全（llm-alignment）— 11 (12) 篇

**今日动态：** 今日对齐方向呈现多元化趋势，涵盖token级幻觉检测（TokenHD）、性别偏见与事实性别纠缠（GKnow）、token级偏好优化（TokenRatio）、情感风格动态后门攻击（Paraesthesia）、哲学偏好对齐（StoicLLM）、差分隐私与社会偏见、鲁棒LLM遗忘（MCU）、文本水印（TextSeal）、语言化置信度对齐（ORCE）、以及PII重建风险。整体趋势是从粗粒度对齐向token级和表征级精细控制演进。

- [#11] Title: Scalable Token-Level Hallucination Detection in Large Language Models
  - **[Authors]**: Rui Min, Tianyu Pang, Chao Du, Minhao Cheng, Yi R. Fung
  - **[一句话总结领域]**: 大语言模型中可扩展的Token级幻觉检测
  - **[TL;DR]**: TL;DR: 问题：现有步骤级幻觉检测粒度有限且依赖步骤分割，难以扩展；推理密集型任务中的幻觉更难发现。方法：提出TokenHD，包含可扩展数据引擎用于合成大规模幻觉标注，以及重要性加权训练策略，直接在自由文本上识别幻觉而无需预定义步骤分割，0.6B检测器训练后即超过QwQ-32B等更大推理模型，性能随规模从0.6B到8B一致提升。
- [#18] Title: GKnow: Measuring the Entanglement of Gender Bias and Factual Gender
  - **[Authors]**: Leonor Veloso, Hinrich Schütze
  - **[一句话总结领域]**: GKnow：度量性别偏见与事实性别的纠缠
  - **[TL;DR]**: TL;DR: 问题：现有性别偏见研究聚焦特定任务或未能区分事实性别输出与基于刻板印象的偏见输出，且缺乏跨多种性别预测类型的统一评估。方法：构建GKnow基准评估语言模型的性别知识与性别偏见，通过神经元消融实验发现性别偏见与事实性别在回路和神经元层面严重纠缠，证明消融是不可靠的去偏方法，且去偏会隐藏事实性别知识的下降。
- [#19] Title: TokenRatio: Principled Token-Level Preference Optimization via Ratio Matching
  - **[Authors]**: Truong Nguyen, Tien-Phat Nguyen, Linh Ngo Van, Duy Minh Ho Nguyen, Khoa Doan, Trung Le
  - **[一句话总结领域]**: TokenRatio：基于比率匹配的原则性Token级偏好优化
  - **[TL;DR]**: TL;DR: 问题：DPO对完整序列建模偏好但生成由逐token决策驱动，现有token级扩展将序列级Bradley-Terry目标分解到各时间步，隐式优化前缀级最优性。方法：提出TBPO，建立前缀条件token级Bradley-Terry偏好模型，推导Bregman散度密度比匹配目标，提出显式学习状态基线的TBPO-Q和通过优势归一化移除基线的TBPO-A，在指令遵循、有益性/无害性和摘要基准上提升对齐质量、训练稳定性和输出多样性。
- [#29] Title: Metaphor Is Not All Attention Needs
  - **[Authors]**: Olga Sorokoletova, Francesco Giarrusso, Giacomo De Luca, Piercosma Bisconti, Matteo Prandi, Federico Pierucci, Marcello Galisai, Vincenzo Suriani, Daniele Nardi
  - **[一句话总结领域]**: 隐喻并非注意力所需全部
  - **[TL;DR]**: TL;DR: 问题：诗歌等文体改写能有效绕过LLM安全机制，但其成功原因不明——是特定诗歌手法、模型未能识别文学格式，还是文体不规则输入改变了处理模式？方法：通过注意力模式的可解释性分析，进行输入级消融、构建注意力图可解释向量表示并聚类，发现模型能高准确率区分诗歌与散文格式，但在每种格式内难以预测越狱成功，诗歌诱导的处理模式与有害内容检测基本独立，证明文学越狱通过累积文体不规则性而非单一手法成功。
- [#50] Title: Robust LLM Unlearning Against Relearning Attacks: The Minor Components in Representations Matter
  - **[Authors]**: Zeguan Xiao, Xuanzhe Xu, Yun Chen, Yong Wang, Jian Yang, Yanqing Hu, Guanhua Chen
  - **[一句话总结领域]**: 表征次要分量对抵御再学习攻击的稳健LLM遗忘至关重要
  - **[TL;DR]**: TL;DR: 问题：LLM遗忘后的模型通过再学习攻击可快速恢复"被遗忘"知识，对开放权重模型构成严重安全威胁。方法：从表征几何角度发现现有遗忘方法主要沿主导分量优化而次要分量基本不变，再学习时主导分量的修改易被逆转而次要分量抵抗力更强；基于谱结构理论分析提出Minor Component Unlearning（MCU），显式针对表征中的次要分量进行遗忘。方法：在三个数据集上验证，对再学习攻击的抵抗力显著优于包括sharpness-aware minimization在内的SOTA方法。
- [#52] Title: Enhancing Multilingual Counterfactual Generation through Alignment-as-Preference Optimization
  - **[Authors]**: Yilong Wang, Qianli Wang, Bohao Chu, Yihong Liu, Jing Yang, Simon Ostermann
  - **[一句话总结领域]**: 通过对齐即偏好优化增强多语言反事实生成
  - **[TL;DR]**: TL;DR: 问题：自生成反事实解释（SCE）在英语之外的语言扩展困难，现有方法在非主导语言中难以产生有效SCE，且有效性和最小性之间的权衡持续损害解释质量。方法：提出Macro偏好对齐框架，将DPO应用于多语言SCE生成，使用复合评分函数构建偏好对，将权衡转化为可测量的偏好信号。方法：在4个LLM和7种类型学多样语言上，Macro平均有效性提升12.55%且不降低最小性，避免翻译基线的严重最小性违规，相比SFT在两个指标上均表现更优，同时增加跨语言扰动对齐并缓解常见生成错误。
  - **排除原因：** 多语言/特定语言（多语言：7种类型学多样语言）
- [#54] Title: When Emotion Becomes Trigger: Emotion-style dynamic Backdoor Attack Parasitising Large Language Models
  - **[Authors]**: Ziyu Liu, Tao Li, Tianjie Ni, Xiaolong Lan, Wengang Ma, Tao Yang, Guohua Wang, Junjiang He
  - **[一句话总结领域]**: 基于情感风格动态后门的LLM寄生攻击
  - **[TL;DR]**: TL;DR: 问题：现有LLM后门攻击主要在token级别操作缺乏深层语义操纵，且依赖单一固定触发器容易被检测，干净微调可削弱触发器-目标关联。方法：通过因果验证发现情感在LLM表征空间中可与语义解耦形成独立聚类，提出Paraesthesia寄生式情感风格动态后门攻击，将情感作为整体风格因素（而非单个词）作为后门触发器，通过混合情感触发样本到干净数据中进行微调。方法：在指令遵循生成和分类任务上攻击成功率约99%，同时维持模型干净效用。
- [#65] Title: StoicLLM: Preference Optimization for Philosophical Alignment in Small Language Models
  - **[Authors]**: Ishmam Khan, Sindhuja Thogarrati, Shuo Zhang
  - **[一句话总结领域]**: 小语言模型的斯多葛哲学偏好对齐研究
  - **[TL;DR]**: TL;DR: 问题：大语言模型在事实适应上表现好，但在数据极端稀缺的哲学框架内化上能力不足。方法：提出StoicLLM，用ORPO和AlphaPO对小型LLM进行斯多葛哲学文本的偏好优化，仅用300个高保真样本即可实现与少样本提示接近的内向美德对齐，但发现小模型在斯多葛外向世界主义义务上存在根本性表示局限而无法通过微数据弥补。
- [#78] Title: How Does Differential Privacy Affect Social Bias in LLMs? A Systematic Evaluation
  - **[Authors]**: Eduardo Tenorio, Karuna Bhaila, Xintao Wu
  - **[一句话总结领域]**: 差分隐私如何影响LLM中的社会偏见
  - **[TL;DR]**: TL;DR: 问题：差分隐私（DP）用于限制LLM训练中的隐私风险，但DP与社会偏见的关系尚不清楚。方法：系统评估用DP-SGD训练的预训练LLM在句子评分、文本补全、表格分类和问答四种范式中的社会偏见，发现DP减少句子评分中的偏见但未泛化到所有任务，揭示了logit级偏见与输出级偏见的不一致，表明降低记忆化不一定减少不公平性，强调多范式评估的重要性。
- [#88] Title: TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection
  - **[Authors]**: Tom Sander, Hongyan Chang, Tomáš Souček, Tuan Tran, Valeriu Lacatusu, Sylvestre-Alvise Rebuffi, Alexandre Mourachko, Surya Parimi, Christophe Ropers, Rashel Moritz, Vanessa Stark, Hady Elsahar, Pierre Fernandez
  - **[一句话总结领域]**: TextSeal：面向溯源与蒸馏保护的本地化LLM水印
  - **[TL;DR]**: TL;DR: 问题：现有LLM水印方案在检测强度和多样性保留上存在权衡，且难以定位混合文档中的AI生成片段，同时缺乏对模型蒸馏的追踪能力。方法：提出TextSeal，基于Gumbel-max采样引入双密钥生成恢复输出多样性，结合熵加权评分和多区域定位提升检测能力，支持投机解码和多token预测且不增加推理开销，严格支配SynthID-text等基线，在稀释攻击下仍保持自信定位检测，水印信号还能通过模型蒸馏转移以检测未授权使用。
- [#89] Title: ORCE: Order-Aware Alignment of Verbalized Confidence in Large Language Models
  - **[Authors]**: Chen Li, Xiaoling Hu, Songzhu Zheng, Jiawei Zhou, Chao Chen
  - **[一句话总结领域]**: ORCE：大语言模型语言化置信度的序感知对齐
  - **[TL;DR]**: TL;DR: 问题：LLM语言化置信度常将答案生成和置信度生成联合优化，导致置信度对齐目标干扰答案准确性。方法：提出解耦且序感知的框架，先固定生成答案再基于问题-答案对估计置信度，构建基于多个模型完成的采样替代目标，优化排序强化学习目标使更高正确性似然的回答获得更高语言化置信度，在推理和知识密集型基准上改善校准和失败预测同时基本保持答案准确性。
- [#91] Title: Reconstruction of Personally Identifiable Information from Supervised Finetuned Models
  - **[Authors]**: Sae Furukawa, Alina Oprea
  - **[一句话总结领域]**: 从监督微调模型重建个人身份信息
  - **[TL;DR]**: TL;DR: 问题：SFT数据集中的用户敏感信息（如PII）可能通过微调模型泄漏，但此前缺乏对SFT模型PII重建风险的系统研究。方法：构建包含PII的医疗和法律领域多轮Q&A数据集，提出COVA解码算法在基于前缀的攻击下重建PII，一致优于现有提取方法，发现即使攻击者仅掌握部分数据集知识也能显著提升重建成功率，且不同PII类型泄漏程度差异大。
---

## 大模型评测（llm-evaluation）— 10 (11) 篇

**今日动态：** 今日评测方向关注LLM-as-a-Judge的可靠性、基础模型后训练潜力预测、问题难度估计、控制文本生成的公平比较、广告系统的安全导向评估、自动化Agent评估、结构化采样校准、以及稠密检索的测试时计算。趋势是从聚合指标向细粒度、因果感知和自动化评测演进。

- [#3] Title: The Algorithmic Caricature: Auditing LLM-Generated Political Discourse Across Crisis Events
  - **[Authors]**: Gunjan, Sidahmed Benabderrahmane, Talal Rahwan
  - **[一句话总结领域]**: 算法漫画：审计跨危机事件的LLM生成政治话语
  - **[TL;DR]**: TL;DR: 问题：现有AI文本检测关注句子级困惑度等指标，但随着生成系统改进这些信号会减弱，且缺乏对合成政治话语群体级真实性的评估。方法：从计算社会科学视角构建跨9个危机事件的配对语料库（1,789,406条帖子），从情感强度、结构规律性、词汇意识形态框架和跨事件依赖性四个维度评估，发现合成话语虽流畅但在群体层面不真实，更负面、结构更规则、词汇更抽象，提出事件级"漫画差距"度量。
- [#6] Title: Predicting Disagreement with Human Raters in LLM-as-a-Judge Difficulty Assessment without Using Generation-Time Probability Signals
  - **[Authors]**: Yo Ehara
  - **[一句话总结领域]**: 无需生成概率信号预测LLM评判与人工评分者的不一致
  - **[TL;DR]**: TL;DR: 问题：LLM-as-a-Judge在难度评估中与人工评分者存在分歧，现有方法依赖生成时概率信号，难以跨模型比较且收集成本高。方法：利用难度是有序尺度的特性，使用独立嵌入空间（如ModernBERT）基于评分集合的几何一致性识别分歧候选，在英语CEFR句子难度评估中，对GPT-OSS-120B和Qwen3-235B-A22B的实验表明该方法在预测与人类评分者分歧的AUC上超过基于概率的基线。
- [#9] Title: Question Difficulty Estimation for Large Language Models via Answer Plausibility Scoring
  - **[Authors]**: Jamshid Mozafari, Bhawna Piryani, Adam Jatowt
  - **[一句话总结领域]**: 基于答案合理性评分的大语言模型问题难度估计
  - **[TL;DR]**: TL;DR: 问题：现有问题难度估计依赖可读性公式、检索信号或流行度统计，无法充分捕捉现代LLM面临的推理挑战。方法：提出Q-DAPS，通过计算候选答案合理性评分的熵来估计问题难度，在TriviaQA、NQ、MuSiQue和QASC四个数据集上持续优于基线，且对超参数、问题类型、模型规模和合理性估计范式具有强鲁棒性，人工评估确认其与人类难度判断高度一致。
- [#27] Title: Correcting Selection Bias in Sparse User Feedback for Large Language Model Quality Estimation: A Multi-Agent Hierarchical Bayesian Approach
  - **[Authors]**: Andrea Morandi, Mahesh Viswanathan
  - **[一句话总结领域]**: 纠正稀疏用户反馈中的选择偏差以估计大语言模型质量
  - **[TL;DR]**: TL;DR: 问题：生产环境LLM部署中用户反馈高度稀疏且非随机（主要集中在满意度分布两端），朴素平均可能导致40-50个百分点的质量估计偏差。方法：提出三智能体层次贝叶斯流程，通过UMAP+HDBSCAN主题聚类、两阶段层次Beta-Binomial偏差建模和按真实主题 prevalence 重加权，在UltraFeedback验证中，有信息先验的层次模型在偏差比1:1到30:1范围内保持与真实质量4-13pp差距。
- [#35] Title: SAGE: Scalable Automated Robustness Augmentation for LLM Knowledge Evaluation
  - **[Authors]**: Xiaoyuan Li, Yuzhe Wang, Moxin Li, Keqin Bao, Rui Men, Yichang Zhang, Dayiheng Liu, Wenjie Wang, Fuli Feng
  - **[一句话总结领域]**: 可扩展的自动化LLM知识评估鲁棒性增强框架
  - **[TL;DR]**: TL;DR: 问题：LLM在标准知识评估基准上表现强，但面对同知识不同形式的变体问题时能力脆弱，而现有LLM辅助的生成-验证流程因变体生成产率低和验证不可靠而难以扩展。方法：提出SAGE，使用微调小模型进行可扩展鲁棒性增强，包含VariantQual（基于评分标准的人类标注种子数据训练的验证器）和VariantGen（SFT初始化后以VariantQual为奖励模型通过RL进一步优化的变体生成器），在HellaSwag上构建大规模鲁棒性增强基准，质量媲美人工标注的HellaSwag-Pro且成本更低，并能零样本泛化到MMLU。
- [#38] Title: On Predicting the Post-training Potential of Pre-trained LLMs
  - **[Authors]**: Xiaoyuan Li, Yubo Ma, Kexin Yang, Moxin Li, Keqin Bao, Wenie Wang, Fuli Feng, Dayiheng Liu
  - **[一句话总结领域]**: 预测预训练LLM的后训练潜力
  - **[TL;DR]**: TL;DR: 问题：传统基准如MMLU无法反映基础模型在复杂开放场景中的可塑性，导致模型选择低效。方法：提出RuDE（基于评分标准的判别式评估），绕过基础模型的生成差距，利用响应判别能力，在4C分类法指导下通过细粒度评分标准违规构建跨领域受控对比对，预测基础模型在后训练前的性能，并通过RL验证能有效识别高潜力小模型（可超越更大模型）。方法：与后训练性能相关性超过90%。
- [#47] Title: Safety-Oriented Evaluation of Language Understanding Systems for Air Traffic Control
  - **[Authors]**: Yujing Chang, Yash Guleria, Duc-Thinh Pham, Nhut-Huy Pham, Ningli Wang, Vu N. Duong, Sameer Alam
  - **[一句话总结领域]**: 空中交通管制语言理解系统的安全导向评估
  - **[TL;DR]**: TL;DR: 问题：现有LLM评估基于F1或宏观准确率等聚合指标，将所有错误等同处理，未能考虑空中交通管制领域高风险语义错误（如错误跑道标识或移动约束）的不对称后果。方法：提出面向安全的后果感知评估框架，专门适用于ATC操作。方法：当前LLM尽管宏观F1高，但操作可靠性严重受限，峰值风险评分仅0.69，大多数模型低于0.6；错误集中于高影响实体，而动作类型分类相对稳定，表明存在结构性 grounding 缺陷，凸显了后果感知评估协议的必要性。
- [#56] Title: DiffScore: Text Evaluation Beyond Autoregressive Likelihood
  - **[Authors]**: Wen Lai, Yingli Shen, Dingnan Jin, Qing Cui, Jun Zhou, Maosong Sun, Alexander Fraser
  - **[一句话总结领域]**: 超越自回归似然的文本评估框架
  - **[TL;DR]**: TL;DR: 问题：自回归语言模型用于文本评估时，左到右因子化引入位置偏差——早期token仅用左侧上下文评分，将架构不对称与真实文本质量混为一谈。方法：提出DiffScore，基于掩码大扩散语言模型的评估框架，用掩码重建替代范式使每个token用全双向上下文评分，通过连续掩码率测量文本可恢复性，建立从局部流畅性到全局连贯性的评估层次，并提供多时间步质量曲线（跨掩码率分解评分）和双向PMI分解（解耦流畅性和忠实度）等自回归框架不可用的诊断工具。方法：在10个基准上零样本和微调设置均持续优于自回归基线。
- [#69] Title: An Empirical Study of Automating Agent Evaluation
  - **[Authors]**: Kang Zhou, Sangmin Woo, Haibo Ding, Kiran Ramnath, Subramanian Chidambaram, Aosong Feng, Vinayak Arannil, Muhyun Kim, Ishan Singh, Darren Wang, Zhichao Xu, Megha Gandhi, Nirmal Prabhu, Soumya Smruti Mishra, Vivek Singh, Gouri Pandeshwar, Lin Lee Cheong
  - **[一句话总结领域]**: 自动化Agent评估的实证研究
  - **[TL;DR]**: TL;DR: 问题：Agent评估涉及复杂多步行为和工具使用，成本高且依赖专家知识，直接用前沿编程助手自动化效果差（执行成功率仅30%，平均生成12个以上冗余指标）。方法：提出EvalAgent，将评估领域专业知识编码为可复用的评估技能（程序指令、代码模板、动态API文档），组合成基于trace的端到端评估流水线，配套AgentEvalBench基准（20个agent）和Eval@1指标，将首次执行成功率从17.5%提升到65%，人类专家偏好率达79.5%。
- [#75] Title: RETUYT-INCO at BEA 2026 Shared Task 2: Meta-prompting in Rubric-based Scoring for German
  - **[Authors]**: Ignacio Sastre, Ignacio Remersaro, Facundo Díaz, Nicolás De Horta, Luis Chiruzzo, Aiala Rosá, Santiago Góngora
  - **[一句话总结领域]**: 面向德语评分任务的元提示方法
  - **[TL;DR]**: TL;DR: 问题：德语短文评分任务中评分标准多变，传统方法难以适应动态评分需求。方法：提出Meta-prompting方法，让LLM基于训练集样例自动生成定制提示来评分新答案，同时尝试了经典机器学习、开源LLM微调和不同提示技术，在BEA 2026德语评分任务Track 1获第6名（QWK 0.729），Track 3获第4名（QWK 0.674），Track 4获第4名（QWK 0.49）。
  - **排除原因：** 多语言/特定语言（德语）
- [#120] Title: VERDI: Single-Call Confidence Estimation for Verification-Based LLM Judges via Decomposed Inference
  - **[Authors]**: Jasmine Qi, Danylo Dantsev, Muyang Sun
  - **[一句话总结领域]**: VERDI：通过分解推理为基于验证的LLM评判器实现单调用置信度估计
  - **[TL;DR]**: TL;DR: 问题：LLM-as-Judge系统缺乏可靠方法判断何时应信任评判结果，token log-probabilities对许多商业LLM不可用且即使可访问也在结构化JSON输出下饱和于0.999以上。方法：提出VERDI，从结构化评判已产生的推理痕迹提取置信度无需额外推理调用，将每个验证式评估分解为子检查并导出三个结构信号（步骤-裁决对齐、声明级边距、证据grounding分数），用Platt缩放逻辑回归组合，在GPT-4.1-mini上AUROC 0.72-0.91，在Qwen3.5上（其中logprobs反校准，AUROC 0.32-0.49）VERDI达0.56-0.70，并在生产系统八项评分标准上验证（AUROC 0.73-0.88）。
---

## 模型效率与压缩（llm-efficiency）— 9 (10) 篇

**今日动态：** 今日效率方向覆盖训练推理一致性分段执行、模型压缩与并行验证、自适应MegaKernel优化、KV缓存递推、能力蒸馏动态预算分配、参数放置优化、MoE噪声校准和隐藏层蒸馏。整体趋势是从单一优化点向训练-推理协同优化和硬件感知部署演进。

- [#46] Title: From Token to Token Pair: Efficient Prompt Compression for Large Language Models in Clinical Prediction
  - **[Authors]**: Mingcheng Zhu, Zhiyao Luo, Yu Liu, Tingting Zhu
  - **[一句话总结领域]**: 临床预测中基于token对合并的高效LLM提示压缩
  - **[TL;DR]**: TL;DR: 问题：纵向或高频电子健康记录（EHR）产生过长token序列导致高计算成本和性能下降，现有方案或引入额外推理延迟或丢失临床信息。方法：提出Medical Token-Pair Encoding（MedTPE），将频繁共现的医学token对通过依赖感知替换策略合并为复合token实现无损压缩，仅微调新引入token的嵌入（占LLM参数的0.5-1.0%）。方法：在真实世界数据集上输入token长度减少达31%，推理延迟降低34-63%，同时维持甚至提升多个LLM在四项临床预测任务上的预测性能和输出格式合规性，且对不同上下文长度和科学/金融/多语言领域具有鲁棒性和泛化性。
  - **排除原因：** 医学/临床诊断
- [#48] Title: Training-Inference Consistent Segmented Execution for Long-Context LLMs
  - **[Authors]**: Xianpeng Shang, Jiang Li, Zehua Duo, Qianyi Cai, Xiangdong Su
  - **[一句话总结领域]**: 长上下文LLM的训练推理一致性分段执行
  - **[TL;DR]**: TL;DR: 问题：现有高效长上下文方法仅在推理时采用有界上下文或段级执行，训练仍在全上下文注意力下进行，导致训练和推理的执行语义及状态转换不匹配。方法：提出训练推理一致的段级生成框架，训练时限制梯度传播到从前一段携带的KV状态，允许前向传播中头特定访问过去KV状态但不参与梯度传播。方法：长上下文基准上性能媲美全上下文注意力，同时达到与强推理高效基线相当的延迟-内存权衡，在极长上下文长度下显著改善可扩展性（如128K上下文下预填充峰值内存比全上下文FlashAttention降低约6倍）。
- [#57] Title: Efficient LLM-based Advertising via Model Compression and Parallel Verification
  - **[Authors]**: Wenxin Dong, Chang Gao, Guanghui Yu, Xuewu Jiao, Mingqing Hu, Qiang Fu, Peng Xu, Penghui Wei, Hui Xu, Yue Xing, Shuanglong Li, Lin Liu
  - **[一句话总结领域]**: 基于模型压缩和并行验证的高效LLM广告应用
  - **[TL;DR]**: TL;DR: 问题：在广告创意生成和定向投放等场景中部署LLM面临高推理延迟和计算成本挑战，难以满足实时广告系统需求。方法：提出高效生成定向框架，集成自适应组量化、层自适应分层稀疏化和前缀树并行验证三种技术加速LLM推理。方法：在两个真实广告场景上实现显著加速且质量下降可接受，使LLM在实际广告系统中的运营部署成为可能。
- [#58] Title: Ada-MK: Adaptive MegaKernel Optimization via Automated DAG-based Search for LLM Inference
  - **[Authors]**: Wenxin Dong, Mingqing Hu, Guanghui Yu, Qiang Fu, Peng Xu, Hui Xu, Yue Xing, Xuewu Jiao, Shuanglong Li, Lin Liu
  - **[一句话总结领域]**: 基于自动DAG搜索的自适应MegaKernel优化用于LLM推理
  - **[TL;DR]**: TL;DR: 问题：LLM推理中每token解码触发数千内核启动，内核启动开销占端到端推理时间的14.6%；现有MegaKernel在可移植性和效率间存在张力，手调方案架构耦合、自动编译方案的运行时动态调度分支惩罚在延迟关键场景中不可接受。方法：提出Ada-MK，包含三维共享内存约束模型结合K维拆分（峰值共享内存减少50%）、基于MLIR的细粒度DAG离线搜索（完全消除运行时分支）、以及将MegaKernel嵌入TensorRT-LLM的异构混合推理引擎（高吞吐量Prefill+低延迟Decode）。方法：在NVIDIA L20上单批次吞吐量比TensorRT-LLM高23.6%、比vLLM高50.2%，实现首个商业在线广告系统中的MegaKernel工业部署。
- [#71] Title: SOMA: Efficient Multi-turn LLM Serving via Small Language Model
  - **[Authors]**: Xueqi Cheng, Qiong Wu, Zhengyi Zhou, Xugui Zhou, Tyler Derr, Yushun Dong
  - **[一句话总结领域]**: SOMA：通过小语言模型实现高效多轮LLM服务
  - **[TL;DR]**: TL;DR: 问题：多轮对话中标准做法每轮拼接完整对话历史，导致延迟、内存和API成本剧增，现有方法难以平衡响应质量与效率。方法：提出SOMA框架，利用会话早期轮次估计局部响应流形，通过软提示最大化大小模型响应差异以挖掘最不匹配方向，用反退化控制稳定训练，将挖掘案例蒸馏为局部LoRA微调使 surrogate 模型推理时不需提示，配合一次性切换门和回滚机制，显著降低多轮服务成本同时保持质量。
- [#73] Title: ReAD: Reinforcement-Guided Capability Distillation for Large Language Models
  - **[Authors]**: Xueqi Cheng, Xugui Zhou, Tyler Derr, Yushun Dong
  - **[一句话总结领域]**: ReAD：面向大语言模型的强化引导能力蒸馏
  - **[TL;DR]**: TL;DR: 问题：能力蒸馏将LLM压缩为小模型时，现有方法把能力视为独立训练目标，忽略能力间的相互依赖，导致改进某一能力会重塑学生模型的整体能力画像并损害其他有用能力。方法：提出ReAD框架，先推断任务必需能力，动态生成能力导向监督信号，用不确定性感知上下文赌博机自适应分配蒸馏预算以最大化期望效用增益，在相同token预算下提升下游效用，同时减少有害溢出和浪费的蒸馏努力。
- [#80] Title: Decomposing Evolutionary Mixture-of-LoRA Architectures: The Routing Lever, the Lifecycle Penalty, and a Substrate-Conditional Boundary
  - **[Authors]**: Ramchand Kumaresan
  - **[一句话总结领域]**: 进化式LoRA混合架构的分解分析
  - **[TL;DR]**: TL;DR: 问题：进化式MoLoRA系统的改进归因不清，难以分辨哪些组件真正贡献性能。方法：在150M参数widened-D基底上设计2^3部分因子实验，分解路由器重写（并行sigmoid门+可学习每适配器下限+有界温度退火）、留一评估域和生命周期（死亡+alpha混合继承+SVD突变+槽位重分配）三个因素，发现路由器重写带来全部+0.0426 nats平衡对数困惑度改进，生命周期反而造成约-0.028 nats拖累，并定位到进化搜索仅在适配器预对齐任务时才有效。
- [#85] Title: KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference
  - **[Authors]**: Alireza Nadali, Patrick Cooper, Ashutosh Trivedi, Alvaro Velasquez
  - **[一句话总结领域]**: KV-Fold：长上下文推理的单步KV缓存递推
  - **[TL;DR]**: TL;DR: 问题：长上下文推理需要高效处理远超训练时长度的序列，现有方法往往需要架构修改或重新训练。方法：提出KV-Fold，将KV缓存视为序列块上左折叠的累加器，每步处理新块时基于累积KV缓存做前缀注意力，复用内部状态，无需修改或重训练模型，在Llama-3.1-8B上16K到128K token和511链深度实现针在干草堆100%精确检索，单40GB GPU即可完成，数值精度变化10000倍下漂移仍饱和为平坦平台。
- [#92] Title: Not How Many, But Which: Parameter Placement in Low-Rank Adaptation
  - **[Authors]**: Arijit Sehanobish, Charles Lovering
  - **[一句话总结领域]**: 不在数量而在位置：低秩适应中的参数放置问题
  - **[TL;DR]**: TL;DR: 问题：LoRA适配中给定固定可训练参数预算，选择哪些参数训练是否重要尚未被充分研究。方法：发现SFT下随机和梯度知情子集性能相近，但GRPO下随机放置无法超越基模型而梯度知情放置可恢复标准LoRA精度，原因在于SFT梯度低秩稳定而GRPO梯度高秩近正交；提出评分程序在10秒内以低于0.5%训练成本识别关键参数，关键参数集中于残差流写入投影（V、O、Down），跨模型家族和规模（1.5B-8B）稳定。
- [#102] Title: ROMER: Expert Replacement and Router Calibration for Robust MoE LLMs on Analog Compute-in-Memory Systems
  - **[Authors]**: Wenyong Zhou, Yuannuo Feng, Yizhe Chen, Taiqiang Wu, Wendong Xu, Wenbo Qi, Zhengwu Liu, Wang Kang, Ngai Wong
  - **[一句话总结领域]**: ROMER：面向模拟存内计算系统的鲁棒MoE LLM专家替换与路由校准
  - **[TL;DR]**: TL;DR: 问题：MoE LLM频繁专家切换造成内存带宽瓶颈，模拟存内计算(CIM)可缓解但受硬件噪声影响，该影响对MoE LLM的破坏尚未被探索。方法：基于真实芯片测量校准噪声模型，首次系统研究MoE LLM在噪声CIM环境下的表现，发现硬件噪声严重破坏专家负载平衡并使清洁训练的路由决策持续次优，提出ROMER后训练校准框架：替换低激活专家为高频专家恢复负载平衡，并通过百分位数归一化重新校准路由logits以稳定噪声下的路由，在真实芯片噪声下perplexity降低达58.6%-59.8%。
---

## 可解释性与机理（llm-interpret）— 8 篇

**今日动态：** 今日可解释性方向呈现深度机制分析趋势，涵盖Transformer几何化事实记忆、概念信念空间中的ICL轨迹、ASR模型的SAE分析、Qwen-Scope稀疏特征开发工具、上下文-参数冲突的三阶段预测框架、指令对生成与处理的不对称影响、校准误差的多样性瓶颈、以及表征漂移的几何风险分解。

- [#5] Title: Geometric Factual Recall in Transformers
  - **[Authors]**: Shauli Ravfogel, Gilad Yehudai, Joan Bruna, Alberto Bietti
  - **[一句话总结领域]**: Transformer中的几何化事实记忆机制
  - **[TL;DR]**: TL;DR: 问题：传统观点认为Transformer通过权重矩阵作为关联记忆来存储事实，需要参数量与事实数量线性增长。方法：提出并证明一种几何化记忆机制——对数级嵌入维度即可让主体嵌入编码关联属性的线性叠加，小型MLP通过ReLU门控充当关系条件选择器而非键值映射，并扩展到多跳推理设置，给出容量-深度权衡的构造及信息论下界，实验验证梯度下降能自动发现这种结构。
- [#8] Title: Stories in Space: In-Context Learning Trajectories in Conceptual Belief Space
  - **[Authors]**: Eric Bigelow, Raphaël Sarfati, Daniel Wurgaft, Owen Lewis, Thomas McGrath, Jack Merullo, Atticus Geiger, Ekdeep Singh Lubana
  - **[一句话总结领域]**: 空间中的故事：概念信念空间中的上下文学习轨迹
  - **[TL;DR]**: TL;DR: 问题：LLM的上下文学习可视为贝叶斯推断，但其潜在假设空间的结构尚不清楚。方法：提出LLM在低维几何概念信念空间上分配信念，上下文学习对应该空间中信念更新的轨迹，以故事理解为动态信念更新场景，结合行为和表征分析发现信念更新可被解码为低维结构化流形上的轨迹，且对这些表征的干预能因果性地引导信念轨迹。
- [#31] Title: Do Language Models Encode Knowledge of Linguistic Constraint Violations?
  - **[Authors]**: Hardy, Sebastian Padó
  - **[一句话总结领域]**: 语言模型是否编码语言约束违反的知识？
  - **[TL;DR]**: TL;DR: 问题：LLM在语言学任务上表现强劲，但其内部对语言约束违反的机制尚不清楚，假设LLM在参数中编码了约束违反的表征并在处理不合语法句子时被选择性激活。方法：用稀疏自编码器将多语义激活分解为稀疏单语义特征，提出敏感性分数识别在约束违反与合式输入上优先激活的特征，并构建合取证伪框架，结果否定统一语法违反检测器的存在：没有特征跨所有语言学现象一致共享。
- [#41] Title: Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models
  - **[Authors]**: Boyi Deng, Xu Wang, Yaoning Wang, Yu Wan, Yubo Ma, Baosong Yang, Haoran Wei, Jialong Tang, Huan Lin, Ruize Gao, Tianhao Li, Qian Cao, Xuancheng Ren, Xiaodong Deng, An Yang, Fei Huang, Dayiheng Liu, Jingren Zhou
  - **[一句话总结领域]**: 将稀疏自编码器特征转化为大语言模型开发工具
  - **[TL;DR]**: TL;DR: 问题：LLM内部决策过程不透明，限制了检查、控制和系统改进能力，而稀疏自编码器（SAE）虽有潜力但主要限于事后分析。方法：开源Qwen-Scope套件，基于Qwen模型族构建14组SAE覆盖7个模型变体（稠密和MoE架构），展示SAE在四个方向的实际开发接口应用——推理时操控（无需修改权重控制语言/概念/偏好）、评估分析（表征级基准冗余和能力覆盖代理）、数据工作流（多语言毒性分类和安全数据合成）、后训练优化（将SAE信号纳入SFT和RL目标以缓解代码切换和重复等不良行为）。方法：SAE可作为可重用的表征级接口用于诊断、控制、评估和改进LLM。
- [#55] Title: PRISM: A Geometric Risk Bound that Decomposes Drift into Scale, Shape, and Head
  - **[Authors]**: Chieh-Yen Lin, Shao-Hua Sun
  - **[一句话总结领域]**: 将漂移分解为尺度、形状和头的几何风险界
  - **[TL;DR]**: TL;DR: 问题：现有相似性分数（如CKA、SVCCA）只能标记后训练LLM变体（量化、LoRA适配、蒸馏模型）的退化，不能将表征漂移直接与风险或机制联系。方法：提出PRISM，利用LLM线性输出头和近等距骨干结构推导交叉熵风险差距的闭式上界，将漂移分解为尺度不匹配、形状不匹配和头发散三个独立可测轴，每个轴对应不同失效模式（低比特量化下的形状扭曲、LoRA遗忘下的尺度可分离性、GGUF k-量化下的头发散），且形状项可微可作为训练时正则化器。方法：跨两个模型族和五个基准，后训练量化排序Spearman 0.820、LoRA遗忘0.831，形状正则化器在缓解下游遗忘方面优于经验回放。
- [#60] Title: Three Regimes of Context-Parametric Conflict: A Predictive Framework and Empirical Validation
  - **[Authors]**: Pruthvinath Jeripity Venkata
  - **[一句话总结领域]**: 上下文-参数冲突的三阶段预测框架
  - **[TL;DR]**: TL;DR: 问题：文献中LLM处理训练知识与矛盾文档冲突的结果矛盾——有的发现模型顽固保留训练答案（近一半时间忽略文档），有的发现模型几乎完全遵从文档（约96%），原因在于混淆了三种定性不同的处理情境。方法：提出三阶段框架——Regime 1单源更新（主导预测因子：证据连贯性）、Regime 2竞争整合（主导预测因子：参数确定性）、Regime 3任务适当选择（主导预测因子：任务知识需求），并区分参数强度（暴露频率）和参数独特性（编码一致性）。方法：用9,970次API调用在Claude、GPT、Gemini、Llama和DeepSeek上验证，GEE逻辑回归确认所有5个模型的Regime 2确定性梯度（beta=-0.38到-0.50），Regime 3消融显示任务框架单独将上下文遵循率从近100%翻转至6-71%。
- [#77] Title: Instructions shape Production of Language, not Processing
  - **[Authors]**: Andreas Waldis, Leshem Choshen, Yufang Hou, Yotam Perlit
  - **[一句话总结领域]**: 指令塑造语言生成而非语言处理
  - **[TL;DR]**: TL;DR: 问题：现有研究未从认知角度区分LLM的语言处理（输入token）和生成（输出token）阶段，不清楚指令在内部何处起作用。方法：通过逐层探针在五个二元判断任务上测量指令token对输入和输出token的信息塑造作用，发现样本token中的任务信息稳定且与行为弱相关，而输出token中的任务信息变化大且与行为强相关；注意力干预因果证实指令主要影响生成阶段而非处理阶段，且该不对称性随模型规模和指令调优加剧。
- [#82] Title: Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs
  - **[Authors]**: Amin Banayeeanzade, Qingchuan Yang, Dhruv Tarsadiya, Fatemeh Bahrani, Leonardo Blas, Alfy Samuel, Robin Jia, Meisam Razaviyayn, Sai Praneeth Karimireddy
  - **[一句话总结领域]**: 采样更多，获得更少：校准是LLM多样性的瓶颈
  - **[TL;DR]**: TL;DR: 问题：现代LLM在生成中常坍缩到狭窄的输出子集，但逐步概率分布如何导致多样性缺失的机制不明。方法：提出有效-多样性框架，将多样性崩溃归因于两种互补的误校准：排序校准（有效token未可靠排在无效token之上）和形状校准（概率质量过度集中在少数有效续写上），形式化两种机制并证明局部失败在解码步骤中累积为序列级多样性损失，在14个跨家族跨规模模型上验证。
---

## Agent 架构与设计（agent-design）— 8 篇

**今日动态：** 今日Agent架构方向主要关注长程任务中的信念管理、多智能体协作与深度研究Agent的设计。研究趋势包括：将信念与动作解耦以应对部分可观察环境（Agent-BRACE）、通过结构化元认知实现自适应推理（Deep Reasoning）、以及将深度研究建模为信息探索与利用的对抗优化（AgentDisCo）。此外，Agent在软件工程、企业系统和实验自动化等垂直场景的应用探索也在加速。

- [#21] Title: PRISM: Pareto-Efficient Retrieval over Intent-Aware Structured Memory for Long-Horizon Agents
  - **[Authors]**: Jingyi Peng, Zhongwei Wan, Weiting Liu, Qiuzhuang Sun
  - **[一句话总结领域]**: PRISM：面向长程智能体的意图感知结构化记忆帕累托高效检索
  - **[TL;DR]**: TL;DR: 问题：长程语言智能体历史积累远超固定上下文窗口，现有方法要么无差别扩展上下文，要么在摄入时进行高成本事实抽取，或依赖启发式图遍历牺牲准确率和效率。方法：提出PRISM，将长程记忆视为图结构记忆上的联合检索-压缩问题，包含分层Bundle搜索、查询敏感边成本、证据压缩和自适应意图路由四个推理时组件，在LoCoMo基准上以数量级更小的上下文预算实现比所有同协议基线更高的LLM-judge准确率。
- [#66] Title: Agent-BRACE: Decoupling Beliefs from Actions in Long-Horizon Tasks via Verbalized State Uncertainty
  - **[Authors]**: Joykirat Singh, Zaid Khan, Archiki Prasad, Justin Chih-Yao Chen, Akshay Nambi, Hyunji Lee, Elias Stengel-Eskin, Mohit Bansal
  - **[一句话总结领域]**: 通过语言化状态不确定性在长程任务中解耦信念与动作
  - **[TL;DR]**: TL;DR: 问题：LLM agent在部分可观察环境中执行长程任务时，需维护对未观测世界属性的不确定性，且历史上下文无限增长会稀释关键信息。方法：提出Agent-BRACE，将LLM agent解耦为信念状态模型和策略模型，信念模型用带序数确定性标签（从确定到未知）的原子自然语言声明近似后验分布，策略模型基于紧凑结构化信念而非完整历史做决策，在embodied语言环境中Qwen2.5-3B平均提升14.5%，Qwen3-4B提升5.3%，上下文窗口保持近似恒定。
- [#68] Title: Deep Reasoning in General Purpose Agents via Structured Meta-Cognition
  - **[Authors]**: Dean Light, Michael Theologitis, Kshitish Ghate, Shuyue Stella Li, Benjamin Newman, Chirag Shah, Aylin Caliskan, Pang Wei Koh, Dan Suciu, Yulia Tsvetkov
  - **[一句话总结领域]**: 通过结构化元认知实现通用智能体的深度推理
  - **[TL;DR]**: TL;DR: 问题：现有LLM agent的脚手架硬编码推理模式，在需要自适应调整推理结构本身的任务上表现脆弱。方法：提出Deep Reasoning，用形式化语言将元推理表示为关联推断、形式计算和递归子问题求解的可执行分解，通过上下文示例指导测试时动态脚手架构建，在DOLORES agent中跨多跳推理、长链QA、长上下文聚合和深度研究四个困难基准平均超越最强基线24.8%，8B版本在超半数设置中超过同族32B基线。
- [#90] Title: Predicting Decisions of AI Agents from Limited Interaction through Text-Tabular Modeling
  - **[Authors]**: Eilam Shapira, Moshe Tennenholtz, Roi Reichart
  - **[一句话总结领域]**: 通过文本-表格建模从有限交互预测AI智能体决策
  - **[TL;DR]**: TL;DR: 问题：AI agent在谈判中与未知对手交互时，难以预测对方的下一步决策，直接LLM提示效果不佳。方法：将对手决策预测建模为目标自适应文本-表格预测任务，用表格基础模型结合游戏状态特征和LLM文本表示，并引入LLM-as-Observer将小型冻结LLM的隐状态作为决策导向特征（LLM充当编码器而非直接预测器），在13个前沿LLM agent上训练、91个held-out agent上测试，K=16时响应预测AUC提升约4点，议价报价误差降低14%。
- [#93] Title: Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics
  - **[Authors]**: Jishnu Sethumadhavan Nair, Patrice Bechard, Rishabh Maheshwary, Surajit Dasgupta, Sravan Ramachandran, Aakash Bhagat, Shruthan Radhakrishna, Pulkit Pattnaik, Johan Obando-Ceron, Shiva Krishna Reddy Malay, Sagar Davasam, Seganrasan Subramanian, Vipul Mittal, Sridhar Krishna Nemala, Christopher Pal, Srinivas Sunkara, Sai Rajeswar
  - **[一句话总结领域]**: 企业系统是否需要学习的世界模型？上下文对推断动态的重要性
  - **[TL;DR]**: TL;DR: 问题：企业系统中环境动态由租户特定业务逻辑定义，随部署变化且不断演化，离线训练的世界模型在部署偏移下脆弱。方法：提出企业发现智能体，在运行时通过读取系统配置恢复相关转移动态而非仅依赖内部化表示，在CascadeBench上证明离线世界模型分布内表现好但动态变化时退化，而基于发现的智能体通过将预测锚定到当前实例在偏移下更鲁棒，表明可配置环境中agent应结合运行时机制发现转移逻辑。
- [#105] Title: AgentDisCo: Towards Disentanglement and Collaboration in Open-ended Deep Research Agents
  - **[Authors]**: Jiarui Jin, Zexuan Yan, Shijian Wang, Wenxiang Jiao, Yuan Lu
  - **[一句话总结领域]**: AgentDisCo：面向开放式深度研究Agent的解耦与协作
  - **[TL;DR]**: TL;DR: 问题：现有深度研究agent将信息探索与exploitation混为单一模块，缺乏解耦。方法：提出AgentDisCo，将深度研究建模为信息探索与exploitation间的对抗优化问题，用critic agent评估生成outline并精炼搜索查询，generator agent检索更新结果并相应修订outline，迭代精炼后的outline传给下游报告撰写者综合研究报告，支持手工和通过元优化自动发现设计策略，在三个深度研究基准上达到或超越领先闭源系统，并引入GALA基准从用户浏览历史挖掘潜在研究兴趣。
- [#111] Title: AutoLLMResearch: Training Research Agents for Automating LLM Experiment Configuration -- Learning from Cheap, Optimizing Expensive
  - **[Authors]**: Taicheng Guo, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang
  - **[一句话总结领域]**: AutoLLMResearch：训练研究Agent自动化LLM实验配置
  - **[TL;DR]**: TL;DR: 问题：有效配置可扩展LLM实验至关重要，但现有自动化方法仅适用于低成本场景，大规模LLM实验配置自动化缺失且依赖专家直觉。方法：提出AutoLLMResearch，模拟人类研究者从低保真实验学习可推广原理并外推到昂贵LLM设置，核心包含LLMConfig-Gym多保真环境（涵盖四个关键LLM实验任务，支持超百万GPU小时可验证实验结果）和将配置研究形式化为长程MDP的结构化训练管道，激励跨保真外推推理，在保留实验上 demonstrate 有效性、泛化性和可解释性。
- [#125] Title: On Problems of Implicit Context Compression for Software Engineering Agents
  - **[Authors]**: Kirill Gelvan, Igor Slinko, Felix Steinbauer, Egor Bogomolov, Florian Kofler, Yaroslav Zharov
  - **[一句话总结领域]**: 软件工程Agent隐式上下文压缩的问题
  - **[TL;DR]**: TL;DR: 问题：LLM软件工程agent面临上下文长度限制导致长程复杂任务失败，将上下文编码为连续嵌入以实现更密集信息存储是一种有前景的解决方案。方法：探索In-Context Autoencoder将上下文压缩为连续嵌入的适用性，发现其在单轮常识和代码理解任务上表现良好但在多步agent编码任务上失败，分析导致该失败的可能因素，揭示隐式上下文压缩在agent场景下的局限性。
---

## RL for Reasoning（rl-reasoning）— 7 篇

**今日动态：** 今日RL推理方向呈现方法论创新高潮，包括结合同策略优化与蒸馏的长上下文推理（dGRPO）、神经元引导的数学推理偏好优化（YFPO）、协方差感知GRPO（CAGR）、熵极性理论框架（PAPO）、反自蒸馏（AntiSD）、自适应教师暴露（ATESD）、以及前沿引导的探索优先策略优化（FG-ExPO）。

- [#24] Title: Combining On-Policy Optimization and Distillation for Long-Context Reasoning in Large Language Models
  - **[Authors]**: Miguel Moura Ramos, Duarte M. Alves, André F. T. Martins
  - **[一句话总结领域]**: 结合同策略优化与蒸馏实现大语言模型长上下文推理
  - **[TL;DR]**: TL;DR: 问题：SFT和知识蒸馏存在暴露偏差且难以从长程模型生成错误中恢复，GRPO虽对齐训练与模型生成状态但稀疏奖励导致不稳定和样本低效，OPD提供密集token级指导但不直接优化任意奖励信号。方法：提出dGRPO，通过OPD用强教师模型的密集指导增强GRPO，并引入LongBlocks合成长上下文数据集，实验证明结合结果导向策略优化与知识蒸馏比单独使用任一方更稳定有效，同时保留短上下文能力。
- [#40] Title: YFPO: A Preliminary Study of Yoked Feature Preference Optimization with Neuron-Guided Rewards for Mathematical Reasoning
  - **[Authors]**: Yifan Le
  - **[一句话总结领域]**: 基于神经元引导奖励的数学推理偏好优化
  - **[TL;DR]**: TL;DR: 问题：现有偏好优化方法依赖外部构建的偏好数据，很少利用模型内部表征中与能力相关的信息，而数学推理中某些神经元群可能表现出与数学知识、符号操作或逻辑推理相关的激活模式。方法：提出YFPO，用AttnLRP识别数学相关神经元，从其在偏好与非偏好响应间的激活边际构建辅助奖励，以外部神经元级信号增强偏好学习。方法：在GSM8K上的初步实验表明神经元信号可与偏好优化交互并偶尔提升推理性能，为更细粒度和可解释的推理后训练提供了方向。
- [#61] Title: Taming Extreme Tokens: Covariance-Aware GRPO with Gaussian-Kernel Advantage Reweighting
  - **[Authors]**: Cheng Wang, Qin Liu, Wenxuan Zhou, Muhao Chen
  - **[一句话总结领域]**: 协方差感知GRPO高斯核优势重加权驯服极端token
  - **[TL;DR]**: TL;DR: 问题：GRPO在训练过程中难以有效平衡探索与利用的权衡，常导致次优性能和不稳定训练。方法：基于理论洞察——熵变化受token概率与其对应优势之间协方差支配，提出无超参数的协方差加权优化方法，通过高斯核动态降低极端token级更新的权重，自动减少探索-利用权衡引起的不稳定性同时保留信息学习信号。方法：在推理基准上优于GRPO，并有效稳定训练过程中的熵。
- [#103] Title: Entropy Polarity in Reinforcement Fine-Tuning: Direction, Asymmetry, and Control
  - **[Authors]**: Jiazheng Zhang, Ziche Fu, Junrui Shen, Yunbin Zhao, Yunke Zhang, Zhiheng Xi, Long Ma, Chenxin An, Zhihao Zhang, Shichun Liu, Dingwei Zhu, Shihan Dou, Shaofan Liu, Han Li, Wiggin Zhou, Aiden Adams, Tao Gui, Fei Huang, Qi Zhang, Xuanjing Huang
  - **[一句话总结领域]**: 强化微调中的熵极性：方向、不对称性与控制
  - **[TL;DR]**: TL;DR: 问题：现有熵感知方法主要通过全局目标调节熵，token级策略更新如何重塑策略熵的机制未被探索。方法：发展RLVR熵力学理论框架，得到熵变化的一阶近似并导出熵极性（有符号token级量预测采样更新如何扩展或收缩熵），揭示结构不对称性：强化频繁高概率token触发收缩倾向，而扩展倾向通常需要低概率样本或更强分布校正，提出PAPO保留两种极性分支并通过优势重加权实现熵控制，在数学推理和agent基准上持续超越竞争基线。
- [#109] Title: Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information
  - **[Authors]**: Guobin Shen, Xiang Cheng, Chenxiao Zhao, Lei Huang, Jindong Li, Dongcheng Zhao, Xing Yu
  - **[一句话总结领域]**: AntiSD：通过点互信息实现推理RL的反自蒸馏
  - **[TL;DR]**: TL;DR: 问题：on-policy自蒸馏在数学推理中收益不一致，点互信息分析追踪失败根源为特权上下文过度膨胀教师对结构连接词和可验证声明的置信度，同时压低驱动多步搜索的deliberation token置信度。方法：提出Anti-Self-Distillation(AntiSD)，上升学生与教师散度而非下降，反转每token符号产生自然有界优势，熵触发门控在教师熵崩溃后禁用该项，在4B-30B参数的五个模型上2-10倍更少训练步数达到GRPO基线准确率，最终精度提升达11.5点。
- [#112] Title: Adaptive Teacher Exposure for Self-Distillation in LLM Reasoning
  - **[Authors]**: Zihao Han, Tiangang Zhang, Huaibin Wang, Yilun Sun
  - **[一句话总结领域]**: ATESD：LLM推理自蒸馏中的自适应教师暴露
  - **[TL;DR]**: TL;DR: 问题：on-policy自蒸馏中教师默认始终看到完整参考推理，当教师条件远超学生当前能力时token目标过强难以吸收，且固定暴露并非最优选择。方法：提出Adaptive Teacher Exposure for Self-Distillation(ATESD)，将教师暴露视为可学习训练时控制变量，用轻量级Beta策略控制器基于紧凑训练状态统计建模揭示比率，用折扣学习进度奖励（评分该决策对学生未来改进的效果而非即时损失变化）优化控制器，在Qwen3-{1.7B, 4B, 8B}上 outperform OPSD达+0.95、+2.05和+2.33 Average@12点。
- [#115] Title: fg-expo: Frontier-guided exploration-prioritized policy optimization via adaptive kl and gaussian curriculum
  - **[Authors]**: Mingxiong Lin, Zhangquan Gong, Maowen Tang, Qian Li, Chuangchuang Wang, Jian Ma, Sutian Huang, Kai Tang, Haonan Lu
  - **[一句话总结领域]**: FG-ExPO：通过自适应KL与高斯课程实现前沿引导的探索优先策略优化
  - **[TL;DR]**: TL;DR: 问题：GRPO固定KL系数过度限制策略探索，统一问题采样忽略中等难度问题产生最丰富梯度信号。方法：提出FG-ExPO，Accuracy-Conditioned KL Scaling(AKL)通过批次平均精度的平滑非线性函数调整KL惩罚强度（表现差时放松、满意时加强），Gaussian Curriculum Sampling(GCS)按以约0.5为中心的高斯分布分配采样权重聚焦学习前沿，在DeepSeek-R1-Distill-Qwen-1.5B和Qwen3-8B-Base上，AIME 2025 pass@32从63.33%提升到76.67%（绝对提升13.34），8B模型平均pass@32提升2.66，pass@32比pass@1更大增益验证其扩大有效探索空间。
---

## 模型架构与设计（llm-architecture）— 6 (7) 篇

**今日动态：** 今日架构方向聚焦突破传统token生成范式。BitLM将token表示为二进制码实现多token并行生成，Bicameral Model通过隐状态双向耦合实现多模型并行协调，Attractor Models用隐式微分求解不动点替代固定循环深度，MoE方面探索了专家几何耦合和最优配置。

- [#59] Title: BitLM: Unlocking Multi-Token Language Generation with Bitwise Continuous Diffusion
  - **[Authors]**: Shaobin Zhuang, Yuang Ai, Jiaming Han, Xiaohui Li, Huaibo Huang, Xiangyu Yue, Xuefeng Hu, Kun Xu, Yali Wang, Hao Chen
  - **[一句话总结领域]**: 基于位级连续扩散的多token语言生成
  - **[TL;DR]**: TL;DR: 问题：自回归语言模型一次只生成一个token，但自然语言本身以多token单元（短语、n-gram、搭配）结构化存在，这一瓶颈限制了预训练表达力和推理吞吐量；现有方案如推测解码或扩散语言模型要么保留底层瓶颈要么牺牲因果结构。方法：提出BitLM，将每个token表示为固定长度二进制码，用轻量级扩散头在每个块内并行去噪多个token，同时保持块间左到右因果注意力，将token生成重构为紧凑二进制空间中的迭代承诺。方法：实现更高效预训练和显著更快推理，且不改变使语言模型有效的因果基础，证明一次一token范式是接口选择而非根本要求。
- [#74] Title: HEBATRON: A Hebrew-Specialized Open-Weight Mixture-of-Experts Language Model
  - **[Authors]**: Noam Kayzer, Dan Revital, Ori Bar Joseph, Smadar Arvatz, Or Levi, Tal Geva, Shaltiel Shmidman, Amir DN Cohen, Noam Ordan, Omer Baruch, Kate Zinkovskaia, Zevi Apini, Sarel Weinberger
  - **[一句话总结领域]**: Hebatron：面向希伯来语的开放权重混合专家语言模型
  - **[TL;DR]**: TL;DR: 问题：希伯来语等低资源语言缺乏专门优化的高性能开源大模型。方法：基于NVIDIA Nemotron-3稀疏MoE架构构建Hebatron，采用由易到难三阶段课程训练加连续反遗忘锚定，再用200万希伯来语-英语双语样本监督微调，课程排序本身带来3分基准提升，希伯来语推理平均73.8%，超越DictaLM-3.0-24B（68.9%），30B参数模型每步仅激活3B参数，上下文长度达65536 token，推理吞吐量提升约9倍。
  - **排除原因：** 多语言/特定语言（希伯来语）
- [#79] Title: The Bicameral Model: Bidirectional Hidden-State Coupling Between Parallel Language Models
  - **[Authors]**: Cedric Flamant, Udaya Ghai, Kanna Shimizu
  - **[一句话总结领域]**: 双室模型：并行语言模型间的双向隐状态耦合
  - **[TL;DR]**: TL;DR: 问题：多模型和工具增强系统通过文本输出通信，每次交换都需序列化到输出词表，效率低下且不够灵活。方法：提出Bicameral Model，通过可训练神经接口（翻译网络+学习抑制门，约1%参数）在主模型和辅助模型的中间隐状态间建立双向耦合，辅助模型运行工具/约束求解/代码执行，实现连续并发协调，在算术上两个0.5B模型+计算器准确率从36%提升到96%，逻辑网格谜题上达无增强基线1.7倍。
- [#84] Title: Routers Learn the Geometry of Their Experts: Geometric Coupling in Sparse Mixture-of-Experts
  - **[Authors]**: Sagi Ahrac, Noya Hochwald, Mor Geva
  - **[一句话总结领域]**: 路由学习专家的几何结构：稀疏MoE中的几何耦合
  - **[TL;DR]**: TL;DR: 问题：稀疏MoE训练具有挑战性，路由可能坍缩到少数专家，辅助负载均衡损失又会降低专业化程度，但路由决策的形成机制不明。方法：揭示路由器与专家间的几何耦合——对于给定token，路由器权重和专家权重沿相同输入方向接收梯度，仅标量系数不同；分析负载均衡损失破坏该结构使不同路由方向相似度增加近3倍；提出无参数在线K-Means路由器，以余弦相似度分配token，实现最低负载不平衡且困惑度仅适度增加。
- [#86] Title: Solve the Loop: Attractor Models for Language and Reasoning
  - **[Authors]**: Jacob Fein-Ashley, Paria Rashidinejad
  - **[一句话总结领域]**: 求解循环：面向语言与推理的吸引子模型
  - **[TL;DR]**: TL;DR: 问题：循环Transformer通过迭代细化隐表示提升语言和推理能力，但训练不稳定、部署成本高且受限于固定小循环深度。方法：提出Attractor Models，主干模块先提议输出嵌入，吸引子模块通过隐式微分求解不动点来细化，训练内存不随有效深度增长，迭代由收敛自适应决定，在语言建模上困惑度降低最高46.6%，下游准确率提升19.7%，770M模型超越1.3B Transformer；27M参数在数独极端难度达91.4%，迷宫困难达93.1%，还可通过均衡内化在推理时移除求解器。
- [#87] Title: Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs
  - **[Authors]**: Guinan Su, Yanwu Yang, Xueyan Li, Jonas Geiping
  - **[一句话总结领域]**: 多流LLM：通过并行思维、输入和输出流解放语言模型
  - **[TL;DR]**: TL;DR: 问题：现有AI agent基于单流顺序消息交换，无法同时读写、同时思考与行动，造成严重的可用性和效率瓶颈。方法：提出多流LLM，将指令调优从顺序消息格式转为多并行计算流，每个角色（用户输入、思维链、工具调用、输出生成等）分离为独立流，每次前向传播同时从多个输入流读取并在多个输出流生成token，所有流因果依赖于更早时间步，通过数据驱动的并行化改善可用性、效率、安全性和可监控性。
- [#107] Title: Slicing and Dicing: Configuring Optimal Mixtures of Experts
  - **[Authors]**: Margaret Li, Sneha Kudugunta, Danielle Rothermel, Luke Zettlemoyer
  - **[一句话总结领域]**: 系统配置最优混合专家架构的实证研究
  - **[TL;DR]**: TL;DR: 问题：MoE架构的核心设计选择（专家数量、粒度、共享专家、负载平衡、token丢弃）仅在狭窄范围内被单独研究，未考虑交互。方法：首次系统研究超过2000次预训练运行（至6.6B总参数），穷尽变化专家总数、专家维度、异构专家尺寸、共享专家大小和负载平衡机制，发现性能持续改善至极端激活专家参数比128，最优专家大小几乎不随总参数变化而仅取决于激活参数数，共享专家、异构专家和负载平衡设置影响较小，无丢弃路由产生一致增益。
---

## 检索模型与排序（retrieval-model）— 6 篇

**今日动态：** 今日检索方向探索任务自适应嵌入精化、生成式检索中的基础语言能力保护、上下文收敛度提升推理QA、三阶段多轮检索、测试时计算用于稠密检索、以及地理空间网络搜索的表征。

- [#2] Title: Task-Adaptive Embedding Refinement via Test-time LLM Guidance
  - **[Authors]**: Ariel Gera, Shir Ashury-Tahan, Gal Bloch, Ohad Eytan, Assaf Toledo
  - **[一句话总结领域]**: 通过测试时LLM引导实现任务自适应嵌入精化
  - **[TL;DR]**: TL;DR: 问题：现有嵌入模型在零样本搜索和分类任务上表现不佳，而直接使用LLM管道在大规模语料库上成本过高。方法：提出测试时LLM引导的查询精化方法，用生成式LLM对少量文档的反馈来精化查询嵌入表示，使嵌入能实时适应目标任务，在文献搜索、意图检测、关键点匹配和细微查询-指令遵循上取得最高25%的相对提升。
- [#7] Title: ORBIT: Preserving Foundational Language Capabilities in GenRetrieval via Origin-Regulated Merging
  - **[Authors]**: Neha Verma, Nikhil Mehta, Shao-Chuan Wang, Naijing Zhang, Alicia Tsai, Li Wei, Lukasz Heldt, Lichan Hong, Ed Chi, Xinyang Yi
  - **[一句话总结领域]**: ORBIT：通过Origin-Regulated Merging保护生成式检索中的基础语言能力
  - **[TL;DR]**: TL;DR: 问题：LLM在生成式检索任务微调时会发生灾难性遗忘，快速丧失通用语言推理能力，且遗忘程度与参数漂移距离相关。方法：提出ORBIT，主动追踪微调模型与初始模型参数距离，当距离超过阈值时通过权重平均策略约束模型漂移，在保留文本和检索性能上优于常见持续学习基线和相关正则化方法。
- [#13] Title: Context Convergence Improves Answering Inferential Questions
  - **[Authors]**: Jamshid Mozafari, Bhawna Piryani, Adam Jatowt
  - **[一句话总结领域]**: 上下文收敛度提升推理问题回答效果
  - **[TL;DR]**: TL;DR: 问题：LLM在开放域QA中处理推理问题（答案需推导而非直接检索）的能力尚未充分探索，现有段落选择多依赖余弦相似度，可能引入无关信息。方法：提出收敛度指标衡量句子消除错误答案的有效性，用TriviaHG子集实验表明高收敛度句子构建的段落比余弦相似度选择显著提升了答案准确率，且按收敛度降序排列句子略有额外增益。
- [#34] Title: Caraman at SemEval-2026 Task 8: Three-Stage Multi-Turn Retrieval with Query Rewriting, Hybrid Search, and Cross-Encoder Reranking
  - **[Authors]**: David-Maximilian Caraman, Gheorghe Cosmin Silaghi
  - **[一句话总结领域]**: 三阶段多轮检索系统：查询改写、混合搜索与交叉编码器重排序
  - **[TL;DR]**: TL;DR: 问题：多轮对话中的上下文依赖追问需要转化为独立查询才能有效检索，且单一检索策略难以兼顾召回和精度。方法：构建三阶段管道——LoRA微调Qwen 2.5 7B进行查询改写、BM25与密集检索通过RRF融合的混合搜索、BGE-reranker-v2-m3交叉编码器重排序，并针对技术领域采用确定性解码、一般领域采用可控随机性的领域特定温度调优。方法：在SemEval-2026 Task 8官方测试集上nDCG@5达0.531，排名8/38，比组织者基线高10.7%。
- [#117] Title: Test-Time Compute for Dense Retrieval: Agentic Program Generation with Frozen Embedding Models
  - **[Authors]**: Han Xiao
  - **[一句话总结领域]**: 冻结嵌入模型的测试时计算：面向稠密检索的Agent程序生成
  - **[TL;DR]**: TL;DR: 问题：测试时计算被认为仅受益于大推理模型，小嵌入模型未被考虑，但现代嵌入检查点继承大LLM骨干的表示空间，冻结嵌入模型应能受益于额外推理计算。方法：用agentic程序搜索循环在冻结嵌入API上探索259个候选推理程序，发现整个Pareto前沿坍缩为单一参数-free代数：softmax加权局部top-K文档质心与查询的插值，在跨越十倍参数范围的7个嵌入模型家族上统计显著提升nDCG@10，保留full-BEIR验证在每个测试模型上确认提升。
- [#119] Title: Much of Geospatial Web Search Is Beyond Traditional GIS
  - **[Authors]**: Ilya Ilyankou, Stefano Cavazzi, James Haworth
  - **[一句话总结领域]**: 地理空间网络搜索大量超出传统GIS范围
  - **[TL;DR]**: TL;DR: 问题：地理空间网络搜索查询的景观在规模上表征不足，现有标注严重低估（MS MARCO仅6.17%标注为Location）。方法：用密集句子嵌入、轻量SetFit分类器和密度聚类在MS MARCO 101万真实Bing查询中无先验过滤识别181,827个地理空间查询（18.0%，近3倍于原标注），构建88个查询类别分类法，发现成本价格占15.3%（接近整个自然地理主题的两倍），大量活动（成本、营业时间、联系方式、天气、旅行推荐）超出传统GIS和知识图谱服务范围。
---

## 大模型训练与微调（llm-training）— 6 篇

**今日动态：** 今日训练方向探索因果语言建模绕行提升编码器持续预训练、扩散语言模型的自蒸馏轨迹感知Boltzmann建模、概率校准作为可训练能力、On-Policy Distillation的预见机制、隐藏层蒸馏在大规模预训练中的效果、以及可解释的持续预训练层分配策略。

- [#4] Title: A Causal Language Modeling Detour Improves Encoder Continued Pretraining
  - **[Authors]**: Rian Touchent, Eric de la Clergerie
  - **[一句话总结领域]**: 因果语言建模绕行提升编码器持续预训练效果
  - **[TL;DR]**: TL;DR: 问题：编码器在新领域适应时通常继续使用MLM训练，但这种方式对底层表示的优化不足。方法：提出在持续预训练中临时切换到因果语言建模（CLM）再短周期MLM衰减的策略，发现CLM的密集监督对低层Transformer影响更大，在8个法语和11个英语生物医学任务上，ModernBERT分别提升1.2-2.8pp和0.3-0.8pp。
- [#43] Title: Self-Distilled Trajectory-Aware Boltzmann Modeling: Bridging the Training-Inference Discrepancy in Diffusion Language Models
  - **[Authors]**: Kecheng Chen, Ziru Liu, Xijia Tao, Hui Liu, Yibing Liu, Xinyu Fu, Shi Wu, Suiyun Zhang, Dandan Tu, Lingpeng Kong, Rui Liu, Haoliang Li
  - **[一句话总结领域]**: 自蒸馏轨迹感知Boltzmann建模弥合扩散语言模型训练推理差异
  - **[TL;DR]**: TL;DR: 问题：扩散语言模型后训练中，标准NELBO SFT随机掩码单步重建，而推理遵循置信度引导的多步从易到难去噪轨迹，存在严重训练推理不匹配；现有轨迹自蒸馏仅用于加速解码而非真正提升模型能力。方法：提出TABOM，将推理去掩码偏好建模为预测熵上的Boltzmann分布，导出可处理的成对排序目标使模型确定性排序与观察到的解码轨迹对齐。方法：在新领域取得实质增益，扩展DLM有效知识边界，并显著缓解灾难性遗忘。
- [#44] Title: Probabilistic Calibration Is a Trainable Capability in Language Models
  - **[Authors]**: Davide Baldelli, Sruthi Kuriakose, Maryam Hashemzadeh, Amal Zouaq, Sarath Chandar
  - **[一句话总结领域]**: 语言模型的概率校准是可训练能力
  - **[TL;DR]**: TL;DR: 问题：LLM的生成概率往往与用户指定的随机性约束 poorly calibrated，影响需要结构化采样的应用场景。方法：提出两种校准微调变体——soft-target（将目标分布转为trie派生下一token目标）和hard-target（从目标分布采样完成进行训练），在需要采样数学分布的合成提示上微调模型。方法：跨越12个模型4个族的实验显示两种方法均大幅提升结构化采样保真度，hard-target在结构化数字采样上更强，soft-target在更广泛的随机生成基准（包括开放式随机生成、多选答案位置平衡和NoveltyBench）上表现更好，但有时会以降低算术推理等下游能力为代价。
- [#49] Title: Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillation
  - **[Authors]**: Yuchen Cai, Ding Cao, Liang Lin, Chunxi Luo, Xin Xu, Kai Yang, Weijie Liu, Saiyong Yang, Tianxiang Zhao, Guangzhong Sun, Guiquan Liu, Junfeng Fang
  - **[一句话总结领域]**: 揭示On-Policy Distillation的解锁效率
  - **[TL;DR]**: TL;DR: 问题：On-policy distillation（OPD）作为高效后训练范式，其参数级效率机制尚不清楚，现有研究仅归因于更密集稳定的监督。方法：发现OPD效率源于"预见"——早期建立稳定的更新轨迹，表现为模块分配层面识别低边际效用区域并集中更新关键模块，以及更新方向层面表现出更强的低秩集中且主导子空间早期与最终更新对齐；基于这些发现提出EffOPD，通过自适应选择外推步长沿当前更新方向加速OPD。方法：无需额外可训练模块或复杂超参数调优，实现平均3倍训练加速且保持可比最终性能。
- [#63] Title: A Study on Hidden Layer Distillation for Large Language Model Pre-Training
  - **[Authors]**: Maxime Guigon, Lucas Dixon, Michaël E. Sander
  - **[一句话总结领域]**: 大语言模型预训练中隐藏层蒸馏的研究
  - **[TL;DR]**: TL;DR: 问题：LLM知识蒸馏研究主要依赖输出logits，忽视教师中间表征中的语义信息，而隐藏层蒸馏（HLD）在decoder-only架构大规模预训练中的应用尚待探索。方法：以Gemma3 3.4B为教师、123M和735M为学生，在C4数据集最多168B token上进行计算控制实验，系统比较HLD与基于logits的KD和自监督基线。方法：HLD在下游评估任务上未持续优于标准KD，但在所有共享超参数配置下产生系统性困惑度增益，表明潜在信号可被提取但需突破才能在大规模LLM预训练中发挥更重要作用。
- [#67] Title: Freeze Deep, Train Shallow: Interpretable Layer Allocation for Continued Pre-Training
  - **[Authors]**: Yu-Hang Wu, Qin-Yuan Liu, Qiu-Yang Zhao, Bo Jiang, Jiang-Feng Yang, Qing-Wei Cong
  - **[一句话总结领域]**: 深层冻结浅层训练：可解释的持续预训练层分配策略
  - **[TL;DR]**: TL;DR: 问题：LLM持续预训练中选择哪些层冻结或训练缺乏可解释指导，全靠经验摸索成为黑盒问题。方法：提出LayerTracer诊断框架，通过定位任务执行位置和量化层敏感性，发现深层是任务执行关键区域且对扰动更新具有高稳定性，据此提出训练浅层同时冻结深层的策略，在C-Eval和CMMLU上持续优于全参数微调和反向分配策略。
---

## 文本生成（nlg）— 4 篇

**今日动态：** 今日文本生成方向关注控制文本生成的公平比较（LPF）、时间敏感语言生成的理论边界、PEFT模块的输出可组合性、以及离散扩散语言模型的机制知情自适应干预。

- [#10] Title: A Comparative Study of Controlled Text Generation Systems Using Level-Playing-Field Evaluation Principles
  - **[Authors]**: Michela Lorandi, Anya Belz
  - **[一句话总结领域]**: 基于公平竞技原则的控制文本生成系统比较研究
  - **[TL;DR]**: TL;DR: 问题：现有控制文本生成研究使用不同数据集和评估方法，导致难以公平比较不同系统的真实性能。方法：采用公平竞技（LPF）评估框架，标准化生成后处理和评估方法，对代表性CTG系统重新评估发现多数系统性能与原始报告差异显著（通常更差），揭示标准化可复现评估在CTG领域的紧迫必要性。
- [#15] Title: Output Composability of QLoRA PEFT Modules for Plug-and-Play Attribute-Controlled Text Generation
  - **[Authors]**: Michela Lorandi, Anya Belz
  - **[一句话总结领域]**: QLoRA PEFT模块的输出可组合性实现即插即用属性控制文本生成
  - **[TL;DR]**: TL;DR: 问题：PEFT技术虽降低微调成本，但每新任务需单独微调，多属性控制时难以灵活组合。方法：探索三种泛化方式——多数据集联合训练、推理时权重矩阵组合、推理时输出组合，在情感控制、主题控制和多属性控制任务上测试发现，PEFT模块输出求和是尤其强的组合方法，三模块输出组合在情感控制上平均提升2个百分点。
- [#121] Title: A Theory of Time-Sensitive Language Generation: Sparse Hallucination Beats Mode Collapse
  - **[Authors]**: Atul Ganju, Travis McVoy, Shaddin Dughmi, Shang-Hua Teng
  - **[一句话总结领域]**: 时间敏感语言生成理论：稀疏幻觉优于模态崩溃
  - **[TL;DR]**: TL;DR: 问题：语言生成在全局偏好排序下要求及时性（高排名字符串应更早生成），但最终一致生成器在强意义上无法实现及时生成。方法：在温和松弛下（随时间消失的幻觉率）证明可实现任何超线性截止函数的最优密度，同时证明线性截止和消失幻觉率下及时生成不可能，确立稀疏幻觉优于模态崩溃，为时间敏感生成提供理论边界。
- [#127] Title: Steering Without Breaking: Mechanistically Informed Interventions for Discrete Diffusion Language Models
  - **[Authors]**: Hanhan Zhou, Shamik Roy, Rashmi Gangadharaiah
  - **[一句话总结领域]**: 离散扩散语言模型的机制知情自适应干预
  - **[TL;DR]**: TL;DR: 问题：DLM控制生成方法从自回归模型导入，均匀干预每步去噪，联合控制多属性时质量下降且损害复合。方法：在四DLM（124M-8B）上训练稀疏自编码器发现不同属性在时机、锐度和幅度上不同时间表提交（主题在前2%去噪内确定而情感在20%过程中逐渐出现），提出自适应调度器集中干预属性正在形成的步骤、其余生成不动，成本-控制权衡有闭式表征，四DLM七任务上实现精确控制，挑战性三属性同时控制达93% steering strength，比最强基线高15个百分点同时保持生成质量。
---

## 知识与记忆（llm-knowledge）— 4 篇

**今日动态：** 今日知识方向关注预训练曝光对流行度判断的解释、上下文-记忆冲突的动态认知调和解码、多实体动态记忆评估、以及序列模型编辑中的终身归一化机制，强调知识更新与冲突解决的动态性。

- [#12] Title: Pretraining Exposure Explains Popularity Judgments in Large Language Models
  - **[Authors]**: Jamshid Mozafari, Bhawna Piryani, Adam Jatowt
  - **[一句话总结领域]**: 预训练曝光解释大语言模型的流行度判断
  - **[TL;DR]**: TL;DR: 问题：LLM对知名实体的偏好被归因于流行度偏见，但难以区分这是反映真实世界流行度还是预训练统计曝光，因多数训练语料不可获取。方法：利用完全开源的OLMo模型和Dolma语料（7.4万亿token），计算2000个实体在5种类别上的精确曝光统计，发现LLM流行度判断与曝光的相关性强于维基百科流行度，尤其在尾部区域，证明LLM的流行度先验主要由预训练统计而非外部流行度信号塑造。
- [#26] Title: Mitigating Context-Memory Conflicts in LLMs through Dynamic Cognitive Reconciliation Decoding
  - **[Authors]**: Yigeng Zhou, Wu Li, Yifan Lu, Yequan Wang, Xuebo Liu, Wenya Wang, Jun Yu, Min Zhang, Jing Li
  - **[一句话总结领域]**: 通过动态认知调和解码缓解LLM中的上下文-记忆冲突
  - **[TL;DR]**: TL;DR: 问题：LLM预训练获得的参数知识可能与上下文中的外部知识冲突，现有对比解码方法在无冲突场景下破坏输出分布，动态方法难以应对复杂真实冲突。方法：提出DCRD两阶段解码方法，先分析注意力图评估上下文保真度并预测潜在冲突，再将输入导向贪心解码或基于上下文保真度的动态解码路径，在ConflictKG和六个QA数据集上达到SOTA。
- [#83] Title: MEME: Multi-entity & Evolving Memory Evaluation
  - **[Authors]**: Seokwon Jung, Alexander Rubinstein, Arnas Uselis, Sangdoo Yun, Seong Joon Oh
  - **[一句话总结领域]**: MEME：多实体与动态记忆评估基准
  - **[TL;DR]**: TL;DR: 问题：现有记忆基准仅评估单实体更新，未覆盖多实体和动态演化的完整空间。方法：提出MEME，定义六个任务涵盖多实体和动态演化轴，包括级联、缺失和删除等先前未评分任务，在100个受控片段上评估六种记忆系统，发现所有系统在依赖推理上崩溃（级联准确率3%，缺失1%），提示优化、更深检索、降低噪声和更强LLM均无法弥合差距，仅Claude Opus 4.7文件代理部分弥补但成本约70倍。
- [#101] Title: More Edits, More Stable: Understanding the Lifelong Normalization in Sequential Model Editing
  - **[Authors]**: Xin Ma, Wei Chen, Qi Liu, Derong Xu, Zhi Zheng, Tong Xu, Enhong Chen
  - **[一句话总结领域]**: 理解序列模型编辑中的终身归一化机制并提出StableEdit
  - **[TL;DR]**: TL;DR: 问题：终身模型编辑旨在持续更新LLM中的演化事实，但面临灾难性遗忘和模型崩溃，其机制 poorly understood。方法：首次理论分析终身归一化(LN)的作用，揭示自强化稳定循环，证明LN结合岭正则化回归产生渐近正交和有界范数的参数更新，直接缓解遗忘和系统性崩溃，并基于此提出StableEdit，通过显式预热阶段和完整白化增强稳定性，以最小开销提升长程稳定性。
---

## 多模态 Agent（multimodal-agent）— 4 篇

**今日动态：** 今日多模态Agent方向关注计算机使用Agent的时序视觉冗余削减（ReVision）、世界动作模型的统一框架、VLA策略的关键阶段测试时推演（DreamAvoid）、以及通用多模态演示Agent（PresentAgent-2）。

- [#76] Title: ReVision: Scaling Computer-Use Agents via Temporal Visual Redundancy Reduction
  - **[Authors]**: Amirhossein Abaskohi, Yuhang He, Peter West, Giuseppe Carenini, Pranit Chawla, Vibhav Vineet
  - **[一句话总结领域]**: ReVision：通过时序视觉冗余削减扩展计算机使用智能体
  - **[TL;DR]**: TL;DR: 问题：计算机使用智能体每步截图编码为大量视觉token，随着交互轨迹增长token成本急剧上升，限制可纳入的历史信息量，导致增加历史几乎无性能提升。方法：提出ReVision，训练多模态语言模型通过学习的patch选择器比较连续截图表示来去除冗余视觉patch同时保留空间结构，在OSWorld、WebTailBench和AgentNetBench上使用5张历史截图平均减少46% token用量，成功率提升3%，且发现去除冗余后性能随历史增加持续改善。
- [#95] Title: World Action Models: The Next Frontier in Embodied AI
  - **[Authors]**: Siyin Wang, Junhao Shi, Zhaoyang Fu, Xinzhe He, Feihong Liu, Chenchen Yang, Yikang Zhou, Zhaoye Fei, Jingjing Gong, Jinlan Fu, Mike Zheng Shou, Xuanjing Huang, Xipeng Qiu, Yu-Gang Jiang
  - **[一句话总结领域]**: 世界动作模型：具身智能的下一个前沿
  - **[TL;DR]**: TL;DR: 问题：VLA模型仅学习反应式观察-动作映射，未显式建模物理世界在干预下的演化，而世界动作模型（WAM）文献碎片化缺乏统一概念框架。方法：首次系统定义WAM并区分相关概念，追溯VLA与世界模型研究的早期融合，将现有方法组织为级联式和联合式WAM分类体系（按生成模态、条件机制、动作解码策略细分），系统分析数据生态和围绕视觉保真度、物理常识和动作合理性的评估协议，明确关键架构范式及其权衡。
- [#104] Title: DreamAvoid: Critical-Phase Test-Time Dreaming to Avoid Failures in VLA Policies
  - **[Authors]**: Xianzhe Fan, Yuxiang Lu, Shenyuan Gao, Xiaoyang Wu, Ruihua Han, Manling Li, Hengshuang Zhao
  - **[一句话总结领域]**: DreamAvoid：关键阶段测试时推演以避免VLA策略失败
  - **[TL;DR]**: TL;DR: 问题：VLA模型在精细操作中脆弱，关键阶段微小动作错误会快速升级为不可恢复失败，现有模型主要依赖成功演示训练而缺乏对这些阶段的失败意识。方法：提出DreamAvoid，关键阶段测试时dreaming框架，用Dream Trigger判断执行是否进入关键阶段，Action Proposer从VLA采样多个候选动作块，Dream Evaluator在成功/失败/边界案例混合数据上联合训练以推演各候选动作的短程未来、评估价值并选择最优动作，在真实操作任务和仿真基准上有效避免失败并提升整体任务成功率。
- [#118] Title: PresentAgent-2: Towards Generalist Multimodal Presentation Agents
  - **[Authors]**: Wei Wu, Ziyang Xu, Zeyu Zhang, Yang Zhao, Hao Tang
  - **[一句话总结领域]**: PresentAgent-2：面向通用多模态演示Agent
  - **[TL;DR]**: TL;DR: 问题：演示生成正从静态幻灯片转向端到端演示视频生成，需要研究支撑、多模态媒体和交互式交付。方法：提出PresentAgent-2，从开放用户查询生成演示视频，先汇总查询为聚焦主题并执行深度研究收集多模态资源（文本、图像、GIF、视频），然后构建幻灯片、生成模式特定脚本并将幻灯片、音频和动态媒体合成为完整演示视频，支持单人演讲、多人讨论和观众交互三种独立模式，并构建多模态演示基准进行评估。
---

## LLM 应用（llm-app）— 3 (4) 篇

**今日动态：** 今日LLM应用方向覆盖数据录入中的类别错误敏感指数（ISEC）、工业表格数据分类（MaskTab）和科学发现中的类比推理（AR），体现LLM在垂直领域的实用化落地。

- [#16] Title: A categorical error sensitivity index (ISEC): A preventive ordinal decision-support measure for irrecoverable errors in manual data entry systems
  - **[Authors]**: Ricardo Raúl Palma, Mauro Anibal Benetti, Fabricio Orlando Sanchez Varretti
  - **[一句话总结领域]**: 类别错误敏感指数ISEC：手动数据录入系统中不可恢复错误的预防性有序决策支持度量
  - **[TL;DR]**: TL;DR: 问题：中小企业手动数据录入中，语义或形态相近的 nominal 类别易产生不可恢复的误分类，现有归一化工具孤立评估语义和形态维度且依赖标准词典，对含自定义SKU和技术术语的领域数据无效。方法：提出类别错误敏感指数ISEC，整合词嵌入语义距离、自适应Damerau-Levenshtein形态变换成本和经验频率为有序复合分数，利用向量数据库将计算复杂度降低约195倍，在政府司法记录、零售库存和金属加工目录三个异构数据集上验证。
- [#81] Title: ClinicalBench: Stress-Testing Assertion-Aware Retrieval for Cross-Admission Clinical QA on MIMIC-IV
  - **[Authors]**: Alex Stinard
  - **[一句话总结领域]**: ClinicalBench：跨入院临床问答的断言感知检索压力测试
  - **[TL;DR]**: TL;DR: 问题：临床QA基准通常测试干净输入上的推理，但真实EHR笔记中存在否定、时态和家族vs患者归因等断言问题，可将正确答案翻转为错误。方法：提出EpiKG，为患者知识图中每个事实附加断言标签和时态标签并按问题意图路由检索，在400问题的ClinicalBench上，医生盲评主要终点提升22.0个百分点（p=0.0192），发现56%的自动生成参考答案存在缺陷。
  - **排除原因：** 医学/临床诊断
- [#114] Title: MaskTab: Scalable Masked Tabular Pretraining with Scaling Laws and Distillation for Industrial Classification
  - **[Authors]**: Bo Zheng, Yudong Chen, Zihua Xiong, Shuai Fang, Peidong He, Yang Yang, Sheng Guo
  - **[一句话总结领域]**: MaskTab：面向工业分类的可扩展掩码表格预训练与蒸馏
  - **[TL;DR]**: TL;DR: 问题：工业表格数据高维、缺失、少标注，表格学习仍依赖手工特征且缺乏通用自监督框架。方法：提出MaskTab，用专用可学习token编码缺失值以区分结构性缺失与随机丢弃，双路径架构协调掩码重建与任务监督，MoE增强损失自适应路由特征通过专用子网络，在工业规模基准上AUC提升+5.04%、KS提升+8.28%，蒸馏到轻量模型在严格延迟和可解释性约束下仍提升+2.55% AUC和+4.85% KS。
- [#124] Title: Unlocking LLM Creativity in Science through Analogical Reasoning
  - **[Authors]**: Andrew Shen, Shaul Druckmann, James Zou
  - **[一句话总结领域]**: 通过类比推理释放LLM在科学中的创造力
  - **[TL;DR]**: TL;DR: 问题：LLM在开放式科学问题生成中倾向于模态崩溃到低多样性生成，难以持续产生新颖多样化解决方案。方法：引入类比推理(AR)，基于共享关系结构生成跨域类比，再用类比搜索新颖解，在开放式解生成任务上发现显著更多样化生成（多样性指标提升90-173%），50%以上时间生成新颖解（基线仅1.6%），在四个生物医学问题上验证可行性：扰动效应预测分布指标近13倍改进、细胞间通信AUPRC超越所有基线、脑区交互推断Spearman ρ=0.729、寡核苷酸性质预测两个数据集上SOTA。
---

## 自然语言理解（nlu）— 3 (4) 篇

**今日动态：** 今日自然语言理解方向关注多词表达分类的特征选择、潜在因果空洞用于虚假信息检测、以及儿童导向语言的计算研究，体现对语言结构和语用环境的深入分析。

- [#20] Title: What makes a word hard to learn? Modeling L1 influence on English vocabulary difficulty
  - **[Authors]**: Jonas Mayer Martins, Zhuojing Huang, Aaricia Herygers, Lisa Beinborn
  - **[一句话总结领域]**: 什么让单词难学？建模母语对英语词汇难度的影响
  - **[TL;DR]**: TL;DR: 问题：英语作为第二语言的词汇难度估计往往忽略学习者母语的影响，缺乏针对特定L1的个性化难度预测。方法：用梯度提升模型为西班牙语、德语和汉语母语者建模英语词汇难度，基于熟悉度、语义、表面形式和跨语言迁移等特征，发现词熟悉度是三类母语者共享的主导特征，但西班牙语和德语学习者额外依赖正字法迁移，而汉语学习者仅受熟悉度和表面特征影响。
  - **排除原因：** 多语言/特定语言（中文、西班牙语、德语）
- [#28] Title: Latent Causal Void: Explicit Missing-Context Reconstruction for Misinformation Detection
  - **[Authors]**: Hui Li, Zhongquan Jian, Jinsong Su, Junfeng Yao
  - **[一句话总结领域]**: 潜在因果空洞：显式缺失上下文重建用于虚假信息检测
  - **[TL;DR]**: TL;DR: 问题：部分虚假信息文章局部连贯，仅在与提供被遗漏背景事实的同期报道对比时才显误导性，现有方法或附加检索上下文为辅助证据或推断分类遗漏信号，未显式重建具体缺失事实。方法：提出LCV，检索时间对齐上下文文章，用冻结指令微调LLM为每个目标句子生成缺失上下文描述，将其作为文本跨来源关系输入异构图，在英汉双语基准上分别提升2.56和2.84个macro-F1点。
- [#32] Title: Is Child-Directed Language Optimized for Word Learning? A Computational Study of Verb Meaning Acquisition
  - **[Authors]**: Francesca Padovani, Jaap Jumelet, Yevgen Matusevych, Arianna Bisazza
  - **[一句话总结领域]**: 儿童导向语言是否优化了词汇学习？动词意义习得的计算研究
  - **[TL;DR]**: TL;DR: 问题：儿童导向语言（CDL）是否优化以支持语言学习，以及促进哪些语言发展方面，此前将CDL的动词学习优势归因于其特有属性。方法：训练CDL与成人导向语言（ADL）上的神经语言模型，选择性移除句法或词汇共现信息，发现CDL和口语ADL对句法破坏的韧性显著高于书面输入，且口语（尤其是CDL）中语义先于句法出现，表明CDL的动词学习优势可能反映口语语域的普遍属性而非CDL特有优化。
- [#45] Title: Choosing features for classifying multiword expressions
  - **[Authors]**: Eric Laporte
  - **[一句话总结领域]**: 多词表达分类的特征选择
  - **[TL;DR]**: TL;DR: 问题：多词表达（MWE）异质性强且需要分类，但可用特征众多且可靠性不一，导致分类结果对计算应用的效用参差不齐。方法：概述增强的MWE分类方案，通过比较不同特征在多语言中的适用性和分类可靠性，选择最优特征子集以提高分类的计算实用性。
---

## Agentic RL（agent-rl）— 3 篇

**今日动态：** 今日Agentic RL方向聚焦于通过技能图演化和动作指导提升Agent策略学习能力。SkillGraph将有向图中的技能表示为节点，通过RL反馈持续更新图结构；ActGuide-RL将人类动作数据以计划式参考指导注入智能体策略；GEAR则通过自蒸馏实现粒度自适应的优势重加权。

- [#33] Title: SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs
  - **[Authors]**: Xiaoyuan Li, Moxin Li, Keqin Bao, Yubo Ma, Wenjie Wang, Dayiheng Liu, Fuli Feng
  - **[一句话总结领域]**: 通过演化技能图增强智能体强化学习
  - **[TL;DR]**: TL;DR: 问题：现有LLM智能体技能库将技能存储为孤立条目并按语义相似性检索，无法处理组合任务中技能间的依赖和构建关系，且库维护困难。方法：提出SKILLGRAPH，将有向图中的可重用技能表示为节点，边编码先决条件、增强和共现关系，检索有序技能子图指导多步决策，并通过智能体轨迹和RL反馈持续更新图结构，在ALFWorld、WebShop和7个搜索增强QA任务上达到SOTA，尤其在需要组合多技能的复杂任务上增益显著。
- [#36] Title: Learning Agentic Policy from Action Guidance
  - **[Authors]**: Yuxiang Ji, Zengbin Wang, Yong Wang, Shidong Yang, Ziyu Ma, Guanhua Chen, Zonghua Sun, Liaoni Wu, Xiangxiang Chu
  - **[一句话总结领域]**: 从动作指导中学习智能体策略
  - **[TL;DR]**: TL;DR: 问题：智能体强化学习依赖基础策略的探索能力，当基础策略无法到达奖励状态时，需要昂贵的迭代SFT来恢复有效学习信号。方法：提出ActGuide-RL，将人类日常交互中的丰富动作数据以计划式参考指导注入智能体策略，帮助其克服到达奖励状态的障碍，采用最小干预原则仅在需要时自适应调用指导，通过混合策略训练将探索收益内化回无指导策略，无需任何冷启动即可媲美SFT+RL管道，在GAIA上提升10.7个百分点、XBench上提升19个百分点（Qwen3-4B）。
- [#100] Title: GEAR: Granularity-Adaptive Advantage Reweighting for LLM Agents via Self-Distillation
  - **[Authors]**: Sijia Li, Yuchen Huang, Zifan Liu, Yanping Li, Jingjing Fu, Li Zhao, Jiang Bian, Ling Zhang, Jun Zhang, Rui Wang
  - **[一句话总结领域]**: GEAR：通过自蒸馏为LLM Agent实现粒度自适应优势重加权
  - **[TL;DR]**: TL;DR: 问题：LLM Agent的RL训练依赖结果级奖励，细粒度信用分配困难，在长程轨迹中获取可靠局部信用并分配给正确部分仍是开放挑战。方法：提出GEAR，通过自蒸馏比较on-policy学生与ground-truth条件教师获得参考引导散度信号，识别自适应段边界并调制局部优势权重，学生与教师对齐处保留token级分辨率，偏离处将后续延续分组为自适应段并用偏离点散度调制段优势，在8个数学推理和agent工具使用基准上持续超越标准GRPO，在GRPO基线准确率较低的基准上提升达约20%。
---

## Agent 安全与对齐（agent-safety）— 3 篇

**今日动态：** 今日Agent安全方向关注技能面向攻击面和基础设施级攻击风险。SkillSafetyBench评估了可复用技能接口引入的新攻击面，Mobius Injection揭示了单次消息注入即可瘫痪AI基础设施的AbO-DDoS攻击，AgentShield则通过欺骗式陷阱实现入侵检测。

- [#96] Title: SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces
  - **[Authors]**: Chang Jin, An Wang, Zeming Wei, Kai Wang, Biaojie Zeng, Qiaosheng Zhang, Chao Yang, Jingjing Qu, Xia Hu, Xingcheng Xu
  - **[一句话总结领域]**: SkillSafetyBench：技能面向攻击面下的智能体安全评估
  - **[TL;DR]**: TL;DR: 问题：可复用技能作为扩展LLM agent的常见接口引入了新攻击面，现有安全评估遗漏了任务相关技能材料或本地制品即使面对良性用户请求也能诱导agent执行不安全动作的风险。方法：提出SkillSafetyBench可运行基准，包含155个对抗案例覆盖47个任务、6个风险域和30个安全类别，每个案例用特定规则验证器评估，实验表明局部非用户攻击能一致诱导不安全行为，且失败模式因域、攻击方法和脚手架-模型配对而异。
- [#113] Title: Can a Single Message Paralyze the AI Infrastructure? The Rise of AbO-DDoS Attacks through Targeted Mobius Injection
  - **[Authors]**: Zi Liang, Ronghua Li, Yanyun Wang, Qingqing Ye, Haibo Hu
  - **[一句话总结领域]**: Mobius Injection：通过单次消息注入使AI基础设施瘫痪的AbO-DDoS攻击
  - **[TL;DR]**: TL;DR: 问题：LLM agent作为用户与数字服务间中介的系统性破坏风险被忽视，现有安全研究孤立审视LLM和agent。方法：提出Mobius Injection攻击，利用agent逻辑中的语义闭包漏洞，通过单次文本注入诱导agent组件持续递归执行，将自主agent武器化为僵尸节点发动Agent-based and -Oriented DDoS(AbO-DDoS)攻击，单节点调用放大达51.0x，多节点p95延迟膨胀达229.1x，攻击性能随中毒节点数超线性增长，提出Agent Component Energy(ACE)分析作为主动防御机制检测恶意递归触发。
- [#126] Title: AgentShield: Deception-based Compromise Detection for Tool-using LLM Agents
  - **[Authors]**: Yassin H. Rassul, Tarik A. Rashid
  - **[一句话总结领域]**: AgentShield：基于欺骗的工具使用LLM Agent入侵检测
  - **[TL;DR]**: TL;DR: 问题：间接提示注入防御试图预防攻击而非检测已渗透的攻击，且仅在英语中评估。方法：提出AgentShield，在agent工具接口放置假工具、假凭证和允许列表参数三层陷阱，攻击者隐藏指令触发陷阱提供实时入侵信号和高精度自监督分类器训练标签，在商业模型上捕获90.7%-100%成功攻击且485次正常测试零误报，在系统性自适应攻击评估中商业模型零逃逸，自监督分类器跨模型和语言无需重训练转移。
---

## 视觉语言模型（vlm）— 3 篇

**今日动态：** 今日视觉语言模型方向关注基于相机原始测量的视觉语言学习（PRISM-VL）、推理前缀掩码促进VLM蒸馏中的视觉锚定思维、以及在看到答案前选择正确多模态模型的潜在路由（LatentRouter）。

- [#106] Title: Allegory of the Cave: Measurement-Grounded Vision-Language Learning
  - **[Authors]**: Kepeng Xu, Li Xu, Gang He, Wenxin Yu
  - **[一句话总结领域]**: PRISM-VL：基于相机原始测量的视觉语言学习
  - **[TL;DR]**: TL;DR: 问题：VLM通常在ISP后RGB图像上推理，RGB渲染会裁剪、抑制或量化传感器证据，导致部分grounding误差源于渲染过程中的信息丢失。方法：提出测量grounded视觉语言学习并实例化为PRISM-VL，结合RAW衍生的Meas.-XYZ输入、相机条件grounding和曝光bracketed监督聚合，将监督从RGB代理转移到测量域观测，使用15万指令调优集，PRISM-VL-8B BLEU达0.6120、ROUGE-L达0.4571、LLM-Judge准确率82.66%，分别比RGB Qwen3-VL-8B基线提升+0.1074、+0.1071和+4.46个百分点。
- [#108] Title: Hide to See: Reasoning-prefix Masking for Visual-anchored Thinking in VLM Distillation
  - **[Authors]**: Seonghoon Yu, Dongjun Nam, Byung-Kwan Lee, Jeany Son
  - **[一句话总结领域]**: 推理前缀掩码：促进VLM蒸馏中视觉锚定思维
  - **[TL;DR]**: TL;DR: 问题：think-answer VLM通过中间思考步骤提升推理性能但计算成本高限制部署，蒸馏到紧凑模型时学生难以在推理全程利用视觉证据。方法：提出推理前缀掩码蒸馏框架，掩码学生显著推理前缀以鼓励其将视觉证据作为替代信息源，包括token级显著推理前缀掩码（为每个next-token预测选择性掩码高影响推理前缀）和自节奏掩码预算调度（根据教师-学生分布差异测量的蒸馏难度逐渐增加掩码规模），用显著推理前缀掩码替代标准因果掩码，在多模态推理基准上 outperform 近期开源VLM、VLM蒸馏和自蒸馏方法。
- [#122] Title: LatentRouter: Can We Choose the Right Multimodal Model Before Seeing Its Answer?
  - **[Authors]**: Xueqi Cheng, Yushun Dong
  - **[一句话总结领域]**: LatentRouter：在 seeing answer 前选择正确的多模态模型
  - **[TL;DR]**: TL;DR: 问题：MLLM在OCR、图表理解、空间推理、视觉问答、成本和延迟上能力异质，有效路由需匹配查询的多模态需求与候选模型能力而非仅估计查询难度。方法：提出LatentRouter，将MLLM路由形式化为反事实多模态效用预测，提取学习多模态路由胶囊，用模型能力token表示候选MLLM，通过潜在通信估计每模型反事实质量，分布结果头预测模型特定反事实质量，有界胶囊校正细化接近决策，在MMR-Bench和VL-RouterBench上 outperform 固定模型、特征级和学习路由器基线。
---

## 基准与数据集（benchmark）— 2 (7) 篇

**今日动态：** 今日基准方向关注智能体记忆评估、诈骗检测和临床急症识别。LongMemEval-V2评估智能体长期记忆向经验丰富同事进化，PreScam构建从早期对话预测诈骗进展的基准，MEME聚焦多实体与动态记忆评估，AcuityBench则评估临床急症识别与不确定性对齐。

- [#1] Title: LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues
  - **[Authors]**: Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, Kai-Wei Chang
  - **[一句话总结领域]**: LongMemEval-V2：评估智能体长期记忆向经验丰富同事进化的基准
  - **[TL;DR]**: TL;DR: 问题：现有智能体记忆基准多关注用户历史或短轨迹，缺乏对智能体在特定环境中内化经验的直接评估。方法：提出LongMemEval-V2基准，包含451道覆盖静态状态回忆、动态状态追踪、工作流知识等5种核心记忆能力的手动问题，配合最多500条轨迹和115M token的历史数据，同时提出AgentRunbook-R/C两种记忆方法，其中AgentRunbook-C以72.5%的平均准确率超过最强RAG基线（48.5%）和编码智能体基线（69.3%）。
- [#14] Title: MedHopQA: A Disease-Centered Multi-Hop Reasoning Benchmark and Evaluation Framework for LLM-Based Biomedical Question Answering
  - **[Authors]**: Rezarta Islamaj, Robert Leaman, Joey Chan, Nicholas Wan, Qiao Jin, Natalie Xie, John Wilbur, Shubo Tian, Lana Yeganova, Po-Ting Lai, Chih-Hsuan Wei, Yifan Yang, Yao Ge, Qingqing Zhu, Zhizheng Wang, Zhiyong Lu
  - **[一句话总结领域]**: MedHopQA：面向疾病的多跳推理生物医学问答基准
  - **[TL;DR]**: TL;DR: 问题：现有生物医学QA基准多为选择题形式，允许模型通过答案消除而非推理成功，且面临性能饱和和数据污染问题，多跳推理在生物医学QA中代表性不足。方法：提出MedHopQA，以疾病为中心的多跳推理基准，包含1000道需整合两篇维基百科文章的专家标注开放问答对，答案附本体同义词集支持概念级评估，将1000道计分问题嵌入10000道公开可下载问题集中以降低污染风险。
  - **排除原因：** 医学/临床诊断
- [#17] Title: Overview of the MedHopQA track at BioCreative IX: track description, participation and evaluation of systems for multi-hop medical question answering
  - **[Authors]**: Rezarta Islamaj, Joey Chan, Robert Leaman, Jongmyung Jung, Hyeongsoon Hwang, Quoc-An Nguyen, Hoang-Quynh Le, Harikrishnan Gurushankar Saisudha, Ganesh Chandrasekar, Rustam R. Taktashov, Nadezhda Yu. Bizyukova, Sofia I. R. Conceição, Paulo R. C. Lopes, Reem Abdel Salam, Mary Adewunmi, Zhiyong Lu
  - **[一句话总结领域]**: BioCreative IX MedHopQA赛道概述
  - **[TL;DR]**: TL;DR: 问题：生物医学领域多跳QA需要能区分推理与模式匹配的基准。方法：介绍BioCreative IX MedHopQA共享任务，包含1000道需两跳推理的问答对，涵盖疾病、基因和化学物质，48份提交来自13个团队，最佳系统在MedCPT指标上达89.30% F1，远超零样本基线67.40%，发现RAG策略对强性能至关重要。
  - **排除原因：** 医学/临床诊断
- [#22] Title: PreScam: A Benchmark for Predicting Scam Progression from Early Conversations
  - **[Authors]**: Weixiang Sun, Shang Ma, Yiyang Li, Tianyi Ma, Zehong Wang, Colby Nelson, Xusheng Xiao, Yanfang Ye
  - **[一句话总结领域]**: PreScam：从早期对话预测诈骗进展的基准
  - **[TL;DR]**: TL;DR: 问题：现有研究聚焦静态诈骗检测或合成诈骗，缺乏对真实多轮对话诈骗如何随时间进展的建模。方法：提出PreScam基准，从177,989份用户举报中构建11,573个对话式诈骗实例，涵盖20个诈骗类别，按诈骗杀伤链生命周期层次化组织，并在轮级别标注诈骗者心理行为和受害者反应，在实时终止预测和诈骗者行为预测两个任务上评估发现监督编码器显著优于零样本LLM。
- [#51] Title: Human-Grounded Multimodal Benchmark with 900K-Scale Aggregated Student Response Distributions from Japan's National Assessment of Academic Ability
  - **[Authors]**: Kyosuke Takami, Yuka Tateisi, Satoshi Sekine, Yusuke Miyao
  - **[一句话总结领域]**: 基于日本全国学业能力评估的多模态基准
  - **[TL;DR]**: TL;DR: 问题：基于日本K-12评估的多模态LLM基准稀缺，现有基准多基于合成或策划数据，缺乏真实考试布局和日本教育文本。方法：构建来自日本全国学业能力评估的多模态数据集，包含科学、数学和日语的中学真实考题，保留真实考试布局、图表和日本教育文本，以及约90万学生的全国聚合响应分布，支持在人类和模型性能间进行直接比较。方法：使用精确匹配和字符级F1对最近多模态LLM进行基准测试，观察到学科间差异大且对视觉推理需求高度敏感，建立了可复现的、人类 grounded 的多模态教育推理基准。
  - **排除原因：** 多语言/特定语言（日语）
- [#62] Title: Checkup2Action: A Multimodal Clinical Check-up Report Dataset for Patient-Oriented Action Card Generation
  - **[Authors]**: Sike Xiang, Shuang Chen, Kevin Qinghong Lin, Jialin Yu, Yijia Sun, Philip Torr, Amir Atapour-Abarghouei
  - **[一句话总结领域]**: 面向患者的多模态临床体检报告行动卡生成数据集
  - **[TL;DR]**: TL;DR: 问题：临床体检报告是多模态文档（布局、表格、生物标志物、异常标记、影像发现），普通人难以解读并转化为具体后续行动，而LLM从多模态体检报告生成安全、优先化和面向患者行动的能力缺乏基准。方法：构建Checkup2Action数据集和基准，包含2000份去标识化真实体检报告，覆盖人口统计、体格检查、实验室测试等，将体检到行动生成建模为约束结构化生成任务，设计涵盖问题覆盖率和精度、优先级一致性、科室和时间推荐准确性、行动复杂度、有用性、可读性和安全合规性的评估协议。方法：对通用和医学LLM的实验揭示了覆盖率、正确性、简洁性和安全性之间的清晰权衡。
  - **排除原因：** 医学/临床诊断
- [#116] Title: AcuityBench: Evaluating Clinical Acuity Identification and Uncertainty Alignment
  - **[Authors]**: Robin Linzmayer, Georgianna Lin, Di Coneybeare, Jason Chu, Trudi Cloyd, Manish Garg, Miles Gordon, Elizabeth Hartofilis, Benjamin Hong, Ashraf Hussain, Eugene Y. Kim, Oluchi Iheagwara King, Ross McCormack, Erica Olsen, John K. Riggins, Mustafa N. Rasheed, Dana L. Sacco, Vinay Saggar, Osman R. Sayan, Amit Shembekar, Janice Shin-Kim, Wendy W. Sun, Bernard P. Chang, David Kessler, Noémie Elhadad
  - **[一句话总结领域]**: AcuityBench：评估临床急症识别与不确定性对齐
  - **[TL;DR]**: TL;DR: 问题：现有健康基准强调医学问答或特定分诊任务，缺乏统一的急症识别评估，不涵盖从家庭监测到立即急诊的完整范围。方法：提出AcuityBench，整合5个公共数据集共914个案例（697个共识案例用于标准准确率评估，217个医师确认模糊案例用于不确定性感知评估），支持显式四分类QA和自由对话两种互补格式，在12个前沿模型上发现急症识别准确度和误差方向存在显著差异，对话响应减少过度分诊但增加低分诊尤其在高急症案例中。
  - **排除原因：** 医学/临床诊断
---

## 多模态生成（multimodal-gen）— 2 (4) 篇

**今日动态：** 今日多模态生成方向聚焦个性化广告图文生成（Uni-AdGen）和教学视频多模态摘要（ClipSum），探索跨模态联合生成与视觉语言特征的高效利用。

- [#30] Title: Sign Language Recognition and Translation for Low-Resource Languages: Challenges and Pathways Forward
  - **[Authors]**: Nigar Alishzade, Gulchin Abdullayeva
  - **[一句话总结领域]**: 低资源手语识别与翻译：挑战与前路
  - **[TL;DR]**: TL;DR: 问题：全球300多种手语因文档有限、数据集稀疏和计算工具不足而严重低资源，现有研究多聚焦架构而非数据和社区参与。方法：以阿塞拜疆手语为案例进行系统综述，提取社区共同设计、方言多样性捕获等八条经验，针对突厥手语提出迁移学习策略，并提出三个范式转变：从架构中心到数据中心、从 signer-independent 到 signer-adaptive、从基于参考到任务特定的评估指标。
  - **排除原因：** 多语言/特定语言（手语）
- [#37] Title: Towards Visually-Guided Movie Subtitle Translation for Indic Languages
  - **[Authors]**: Tarun Chintada, Kshetrimayum Boynao Singh, Asif Ekbal
  - **[一句话总结领域]**: 面向印度语言的电影字幕视觉引导翻译
  - **[TL;DR]**: TL;DR: 问题：纯文本字幕翻译系统忽略视觉线索，难以传达情感、动作和社会细微差别，尤其低资源印度语言（英语到印地语、孟加拉语、泰卢固语、泰米尔语和卡纳达语）面临更大挑战，且长视频中的时间错位使无差别视觉 grounding 失效。方法：比较两种轻量级视觉 grounding 策略——5分钟滑动窗口结构化属性摘要和字幕间视觉间隙自由文本摘要，发现oracle选择性 grounding 仅替换最低质量20-30%基线段即可持续改进COMET，其中粗粒度属性摘要更稳健，能捕捉文本遗漏的场景级情感和上下文线索。
  - **排除原因：** 多语言/特定语言（印度语言：印地语、孟加拉语、泰卢固语、泰米尔语、卡纳达语）
- [#94] Title: Design Your Ad: Personalized Advertising Image and Text Generation with Unified Autoregressive Models
  - **[Authors]**: Yexing Xu, Wei Feng, Shen Zhang, Haohan Wang, Yuxin Qin, Yaoyu Li, Ao Ma, Yuhao Luo, Lu Wang, Xudong Ren, Haoran Wang, Run Ling, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law, Longguang Wang, Yulan Guo
  - **[一句话总结领域]**: 设计你的广告：统一自回归模型的个性化广告图文生成
  - **[TL;DR]**: TL;DR: 问题：现有广告生成用多个独立模型分别生成图像或文本，缺乏跨模态感知且依赖仅反映平均偏好的CTR。方法：提出Uni-AdGen，单一自回归框架联合生成广告图像和文本，通过前景感知模块和指令调优增强真实感，配备从粗到细的偏好理解模块从噪声多模态历史行为中捕获用户兴趣，构建首个大规模个性化广告图文数据集PAd1M和PBS指标，在通用和个性化广告生成上超越基线。
- [#97] Title: Multimodal Abstractive Summarization of Instructional Videos with Vision-Language Models
  - **[Authors]**: Maham Nazir, Muhammad Aqeel, Richong Zhang, Francesco Setti
  - **[一句话总结领域]**: ClipSum：利用CLIP视觉语言特征实现教学视频多模态摘要
  - **[TL;DR]**: TL;DR: 问题：传统视频摘要方法依赖CNN物体分类特征，视觉概念被表示为与自然语言不对齐的离散类别。方法：提出ClipSum，利用冻结CLIP视觉语言特征配合显式时间建模和维度自适应融合做教学视频摘要，在YouCook2上ROUGE-1达33.0%，比ResNet-152高2.5个百分点且特征维度低4倍（512 vs 2048）。
---

## 对话系统（dialogue）— 2 篇

**今日动态：** 今日对话系统方向关注目标引导主动对话中的动态场景建模（通过对话场景建模和意图关键词桥接）和可控用户模拟的形式化因果推断框架。

- [#39] Title: Enhancing Target-Guided Proactive Dialogue Systems via Conversational Scenario Modeling and Intent-Keyword Bridging
  - **[Authors]**: Maodong Li, Yancui Li, Fang Kong
  - **[一句话总结领域]**: 通过对话场景建模和意图关键词桥接增强目标引导主动对话系统
  - **[TL;DR]**: TL;DR: 问题：现有目标引导主动对话系统忽略了动态建模对话场景和意图关键词，导致与现实对话动态不匹配。方法：联合建模用户画像和领域知识作为对话场景以引入动态场景偏差影响系统话语生成，并采用意图-关键词桥接预测未来对话回合的意图关键词，提供更高层更灵活的指导。方法：在自动和人工评估中，主动性、流畅性和信息性均显著提升，有效缩小了与现实世界交互的差距。
- [#110] Title: Controllable User Simulation
  - **[Authors]**: Guy Tennenholtz, Ofer Meshi, Amir Globerson, Uri Shalit, Jihwan Jeong, Craig Boutilier
  - **[一句话总结领域]**: 可控用户模拟：形式化为因果推断问题
  - **[TL;DR]**: TL;DR: 问题：离线数据集评估对话agent无法覆盖罕见场景或测试新策略，现有可控用户模拟器通常通过对后验轨迹标签SFT实现，存在结构性偏差。方法：将可控模拟形式化为因果推断问题，揭示SFT训练的后验标签与数据生成行为策略不可解耦，注入前瞻偏差破坏因果一致性，并证明策略偏移下方差几何爆炸（可控性崩溃），提出先验控制、逐步动态控制和直接策略条件学习恢复因果一致性，消除前瞻偏差并保留自然方差。
---

## 多模态推理（multimodal-reasoning）— 2 篇

**今日动态：** 今日多模态推理方向关注可扩展蒸馏管道构建多模态推理模型（OmniThoughtVis）和统一文本与视觉的潜推理（UniVLR），强调推理过程的多模态统一表示。

- [#53] Title: OmniThoughtVis: A Scalable Distillation Pipeline for Deployable Multimodal Reasoning Models
  - **[Authors]**: Yuanhao Yue, Chengyu Wang, Yuanjie Lyu, Lei Shen, Jun Huang
  - **[一句话总结领域]**: 可部署多模态推理模型的可扩展蒸馏管道
  - **[TL;DR]**: TL;DR: 问题：小型多模态LLM推理性能受限于缺乏大规模高质量多模态思维链（CoT）监督，难以在延迟和资源约束下部署。方法：提出OmniThoughtVis可扩展数据策划和蒸馏管道，从教师模型生成结构化CoT轨迹并联合标注推理难度、答案质量和语义任务标签，结合规则过滤、难度感知选择和标签多样性采样，构建180万样本的可控语料库。方法：用于蒸馏Qwen3-VL 2B到8B模型，在9个多模态推理基准上持续增益，4B模型在MathVerse上提升16.8分、MMMU-Pro上提升5.6分，且蒸馏4B模型在多项任务上匹配或超越未蒸馏8B基线。
- [#99] Title: UniVLR: Unifying Text and Vision in Visual Latent Reasoning for Multimodal LLMs
  - **[Authors]**: Houcheng Jiang, Jiajun Fu, Junfeng Fang, Chen Gao, Xiang Wang, Xiangnan He, Yong Li
  - **[一句话总结领域]**: UniVLR：在多模态LLM中统一文本与视觉的潜推理
  - **[TL;DR]**: TL;DR: 问题：现有视觉潜推理方法仍依赖文本链式思维与视觉潜token交错，限制效率且推理碎片化。方法：提出UniVLR，将文本推理和辅助视觉证据统一为共享视觉工作空间，渲染推理痕迹与辅助图像后压缩为紧凑视觉潜token，推理时仅通过视觉潜token推理并直接解码答案，无需外部工具调用和冗长文本推理，性能更优同时生成推理token大幅减少。
---

## 代码生成与程序合成（code-gen）— 2 篇

**今日动态：** 今日代码生成方向关注通过逐步执行轨迹对齐代码推理（StepCodeReasoner）和从测试时缩放的对偶判断空间进行自训练（DuST），强调中间执行状态的监督而非仅关注最终输出。

- [#98] Title: StepCodeReasoner: Aligning Code Reasoning with Stepwise Execution Traces via Reinforcement Learning
  - **[Authors]**: Hao Wang, Rui Li, Lei Sha, Jie M. Zhang
  - **[一句话总结领域]**: StepCodeReasoner：通过逐步执行轨迹对齐代码推理
  - **[TL;DR]**: TL;DR: 问题：现有代码推理方法只监督最终输出而忽略中间执行状态，常导致奖励黑客问题。方法：提出StepCodeReasoner，自动插入结构化print执行跟踪锚点，训练模型预测每步运行时状态，并引入Bi-Level GRPO在轨迹间比较替代执行路径、在轨迹内基于对下游正确性的影响奖励中间精度，7B模型在CRUXEval达91.1%、LiveCodeBench达86.5%，分别超过GPT-4o的85.6%和75.1%。
- [#123] Title: Primal Generation, Dual Judgment: Self-Training from Test-Time Scaling
  - **[Authors]**: Yizhu Jiao, Ruixiang Zhang, Richard Bai, Jiawei Han, Ronan Collobert, Yizhe Zhang
  - **[一句话总结领域]**: DuST：从测试时缩放的对偶判断空间进行自训练
  - **[TL;DR]**: TL;DR: 问题：代码生成训练中测试时缩放采样的比较信息被丢弃，模型仅从孤立的成功或失败学习而非从多个尝试的相对正确性结构学习。方法：提出DuST，从对偶判断空间自训练，从模型自身分布采样候选程序、沙箱执行标记、保留成功失败混合组、用GRPO训练按执行正确性排序候选程序（判别目标从不直接奖励生成正确程序），在跨越两个家族三个规模（4B-30B）的五个模型上持续提升LiveCodeBench的Best-of-4测试时缩放，Qwen3-30B-Thinking上单样本pass@1提升+3.1、Best-of-4提升+4.1，单rollout匹配基线Best-of-4性能。
---

## 语音与音频（audio-speech）— 1 (3) 篇

**今日动态：** 今日语音方向聚焦ASR模型的机械可解释性，使用稀疏自编码器分析Whisper编码器，发现跨语言和非语言边界的多样化单语义特征，并展示跨语言特征操控能力。

- [#23] Title: Mind the Pause: Disfluency-Aware Objective Tuning for Multilingual Speech Correction with LLMs
  - **[Authors]**: Deepak Kumar, Baban Gain, Asif Ekbal
  - **[一句话总结领域]**: Mind the Pause：面向LLM多语言语音修正的不流畅感知目标调优
  - **[TL;DR]**: TL;DR: 问题：ASR转录常含填充词、重复和错误起始等不流畅现象，现有方法仅识别并删除不流畅token，易破坏语法结构和语义连贯性，且LLM应用多限于检测或数据增强而非全面修正。方法：提出多语言修正流水线，序列标注器先标记不流畅token，再指导LLM指令微调重写为流畅文本，并加入对比学习目标惩罚不流畅token复现，在印地语、孟加拉语和马拉地语上持续优于强基线。
  - **排除原因：** 多语言/特定语言（印地语、孟加拉语、马拉地语）
- [#25] Title: Mechanistic Interpretability of ASR models using Sparse Autoencoders
  - **[Authors]**: Dan Pluth, Zachary Nicholas Houghton, Yu Zhou, Vijay K. Gurbani
  - **[一句话总结领域]**: 使用稀疏自编码器进行ASR模型的机械可解释性分析
  - **[TL;DR]**: TL;DR: 问题：SAE已成功用于解释文本LLM，但尚无研究将其应用于音频处理模型如ASR以理解其内部机制。方法：将SAE应用于Whisper编码器的帧级嵌入，训练高维稀疏潜空间，发现跨语言和非语言边界的多样化单语义特征，并展示跨语言特征操控能力，证明Whisper编码了丰富的语言学信息。
- [#72] Title: Predicting Psychological Well-Being from Spontaneous Speech using LLMs
  - **[Authors]**: Erfan Loweimi, Sofia de la Fuente Garcia, Saturnino Luz
  - **[一句话总结领域]**: 使用LLM从自发语音预测心理健康状态
  - **[TL;DR]**: TL;DR: 问题：传统心理健康评估依赖量表和专家访谈，难以大规模自动化评估。方法：用12个指令微调LLM对PsyVoiD数据库111名参与者的自发语音进行零样本Ryff心理健康评分预测，与临床心理学和语言学专家合作开发领域知情提示，Spearman相关系数最高达0.8（80%数据），并通过统计分析和关键词词云揭示驱动预测的系统性偏差和语言学特征。
  - **排除原因：** 医学/临床诊断
---

## 信息抽取（ner-re）— 1 (3) 篇

**今日动态：** 今日信息抽取方向关注社交媒体灾害情报中的因果关系抽取验证框架，强调专家主导的评估与事后证据验证。

- [#42] Title: Concordance Comparison as a Means of Assembling Local Grammars
  - **[Authors]**: Juliana Pirovani, Elias de Oliveira, Eric Laporte
  - **[一句话总结领域]**: 通过共现比较组装局部语法进行人名实体识别
  - **[TL;DR]**: TL;DR: 问题：葡萄牙语人名实体识别需要有效的局部语法构建方法。方法：使用共现比较工具对比两个局部语法获得的共现结果并高亮差异，分析包含、交集和析取关系以组装效果最佳的语法。方法：在葡萄牙语HAREM Gold Collection上F-Measure达76.86，比葡萄牙语SOTA高6个百分点。
  - **排除原因：** 多语言/特定语言（葡萄牙语）
- [#64] Title: Robust Biomedical Publication Type and Study Design Classification with Knowledge-Guided Perturbations
  - **[Authors]**: Shufan Ming, Joe D. Menke, Neil R. Smalheiser, Halil Kilicoglu
  - **[一句话总结领域]**: 基于知识引导扰动的稳健生物医学出版类型分类
  - **[TL;DR]**: TL;DR: 问题：生物医学文献出版类型和研究设计分类对证据综合和知识发现至关重要，但现有方法主要关注扩展标签覆盖和域内准确率，模型可能依赖表层词汇或数据集特定线索，在分布偏移下鲁棒性不足。方法：提出基于控制语义扰动的评估框架评估鲁棒性，并研究结合实体掩码和域对抗训练的鲁棒性导向训练策略，以选择性地抑制非任务定义特征同时保留显著方法信号。方法：发现鲁棒性提升源于两种互补机制——增加对显式方法线索的依赖和减少对虚假领域特定主题特征的依赖，有效缓解了鲁棒性与域内准确率之间的常见权衡。
  - **排除原因：** 医学/临床诊断
- [#70] Title: Large Language Models for Causal Relations Extraction in Social Media: A Validation Framework for Disaster Intelligence
  - **[Authors]**: Ujun Jeong, Saketh Vishnubhatla, Bohan Jiang, Andre Harrison, Adrienne Raglin, Huan Liu
  - **[一句话总结领域]**: 面向灾害情报的社交媒体因果抽取LLM验证框架
  - **[TL;DR]**: TL;DR: 问题：灾害期间从社交媒体提取因果关系可增强态势感知，但灾害相关帖子非正式、碎片化且高度依赖上下文，常描述个人经历而非显式因果关系，现有方法难以有效处理。方法：提出专家主导的评估框架，将LLM生成的因果图与灾害报告中的参考图进行对比，并验证提取关系是否有事后证据支持而非模型先验，系统评估了LLM在灾害决策支持中的潜力与风险。
---

## 🆕 新增 Topic

> 本次整理中未发现新的 topic，所有论文均已归入现有类别。

---

## 📊 统计

- 总论文数：127
- 排除论文数：17（多语言/特定语言 9 篇，医学/临床 8 篇）
- Topic 数量：24
- 各 Topic 论文数：对齐与安全(11/12), 大模型评测(10/11), 模型效率与压缩(9/10), 可解释性与机理(8), Agent 架构与设计(8), RL for Reasoning(7), 模型架构与设计(6/7), 检索模型与排序(6), 大模型训练与微调(6), 文本生成(4), 知识与记忆(4), 多模态 Agent(4), LLM 应用(3/4), 自然语言理解(3/4), Agentic RL(3), Agent 安全与对齐(3), 视觉语言模型(3), 基准与数据集(2/7), 多模态生成(2/4), 对话系统(2), 多模态推理(2), 代码生成与程序合成(2), 语音与音频(1/3), 信息抽取(1/3)
