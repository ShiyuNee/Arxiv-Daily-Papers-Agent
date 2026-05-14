# arXiv cs.CL 论文分类总结 — 2026-05-12

- **日期**: 2026-05-12
- **分类**: Computation and Language (cs.CL)
- **论文总数**: 270

---

## 一、LLM 训练与优化（27篇）

这是当日最大的主题，涵盖预训练、微调、蒸馏、持续学习等核心训练技术。

- [#1] **ELF: Embedded Language Flows** — 基于连续嵌入空间 Flow Matching 的扩散语言模型，大幅超越离散 DLM。TL;DR: 问题：当前扩散语言模型主要在离散token上操作，性能受限。 方法：提出ELF，在连续嵌入空间做Flow Matching，最后一步才映射到离散token，大幅超越现有离散和连续DLM。
- [#15] **A Single-Layer Model Can Do Language Modeling** — 提出 Grounded Prediction Networks，单层循环架构实现语言建模（130M 参数 perplexity 接近 12 层 Transformer）。TL;DR: 问题：现代语言模型通过堆叠层扩展深度，但生物系统严重依赖循环。 方法：提出GPN（接地预测网络），单层循环块（一个FFN+共享矩阵记忆），130M参数1层模型perplexity接近12层Transformer。
- [#16] **Continual Factual Knowledge Acquisition** — 持续预训练中知识获取与遗忘的理论框架，提出 STOC 生成式数据回放。TL;DR: 问题：持续预训练中LLM如何获取和保留事实知识的机制尚不清楚。 方法：提出cFKA理论框架，用单层Transformer刻画训练动态，揭示现有CPT方法的行为，提出STOC生成式数据回放算法。
- [#26] **EXACT: Effective-Context Exposure Balancing** — 逆频率加权长上下文监督目标，NoLiMa 提升 +10.09。TL;DR: 问题：长上下文适应中存在token级监督不匹配——packed训练中目标token的有效上下文始终很短。 方法：提出EXACT，按逆频率对长有效上下文目标分配额外权重，7个Qwen/LLaMA CPT配置下28个比较全部改善。
- [#27] **Mela: Test-Time Memory Consolidation** — 受脑科学启发的层级记忆模块，在线记忆整合。TL;DR: 问题：记忆巩固（将短暂经验转化为稳定表示）是人脑核心原则，但尚未用于序列模型设计。 方法：借鉴神经科学记忆巩固和跨频率耦合理论，提出分层记忆模块HMM，由快速和慢速两个功能不同子模块组成，实现测试时记忆整合。
- [#28] **Infinite Mask Diffusion for Few-Step Distillation** — 随机无限状态掩码减少 MDM 分解误差。TL;DR: 问题：掩码扩散模型因同时token预测的分解误差需要大量采样迭代。 方法：提出无限掩码扩散，用随机无限状态掩码减少分解误差，实现少步蒸馏。
- [#29] **Learning Less Is More** — 发现上层注意力过早特化损害预训练，门控 FFN 可抑制。TL;DR: 问题：GPT预训练中上层注意力过早特化到尖锐模式，下层特征尚未稳定。 方法：提出在训练早期临时减慢上层Q/K投影，防止上层注意力过早特化，提升最终困惑度和下游准确率。
- [#44] **Relative Score Policy Optimization for Diffusion LMs** — 扩散语言模型的相对分数策略优化 TL;DR: 问题：扩散语言模型缺少可处理的序列级对数比，无法直接应用标准RLVR训练。 方法：提出相对分数策略优化，绕过序列级对数比需求，实现扩散语言模型的有效后训练推理提升。
- [#52] **Synthetic Pre-Pre-Training** — 合成预预训练数据增强噪声鲁棒性 TL;DR: 问题：预训练数据噪声会遮蔽有意义模式、降低模型性能，数据清洗无法完全消除。 方法：提出在正式预训练前加入基于合成数据的预预训练(PPT)阶段，用可学习时序结构增强噪声鲁棒性。
- [#64] **Annotations Mitigate Post-Training Mode Collapse** — 标注缓解后训练模态坍缩 TL;DR: 问题：SFT后训练导致语义模态坍缩——偏向低熵微调数据、放弃高熵预训练分布，且该问题随规模恶化。 方法：提出标注锚定训练，让模型同时学习微调数据的偏好跟随行为和预训练分布。
- [#80] **Language Models Without a Trainable Input Embedding Table** — 无需可训练输入嵌入表的语言模型 TL;DR: 问题：可训练输入嵌入表是否真的必要？ 方法：用固定最小二进制token码替代V×d_model嵌入矩阵，仅用⌈log₂V⌉位编码token身份，零参数提升到模型宽度，性能与标准嵌入相当。
- [#88] **Edit-Based Refinement for Parallel Masked Diffusion LMs** — 并行掩码扩散 LM 编辑式精炼 TL;DR: 问题：掩码扩散LM同时生成多token时因token级目标与序列一致性不匹配导致性能下降。 方法：提出ME-DLM，在扩散生成后用轻量编辑操作精炼，提升并行生成质量。
- [#93] **TAD: Temporal-Aware Trajectory Self-Distillation** — 时序感知轨迹自蒸馏加速扩散 LM TL;DR: 问题：扩散LLM面临准确率-并行性权衡，增加每步生成token数降低质量。 方法：提出TAD时序感知轨迹自蒸馏，数据构建时以教师模型轨迹为条件训练学生，加速同时保持精度。
- [#146] **XPERT: Expert Knowledge Transfer for MoE** — 从 MoE 提取跨领域专家知识用于下游训练 TL;DR: 问题：MoE模型中部分专家跨领域持续激活，编码跨域通用知识。 方法：提出XPERT，从MoE中提取这些通用专家知识用于下游训练。
- [#150] **SimReg: Embedding Similarity Regularization** — 嵌入相似性正则化加速 LLM 预训练收敛 TL;DR: 问题：预训练中token嵌入的类内方差大、类间相似度高，阻碍表示学习效率。 方法：提出SimReg，在预训练中加入嵌入相似性正则化，加速收敛。
- [#152] **On-Policy Harness Self-Distillation** — 策略增强自蒸馏，将 harness 能力内化到模型本身 TL;DR: 问题：推理时harness显著提升复杂任务性能，但不改变模型内在能力。 方法：提出OPHSD，用harness增强的当前模型作为教师进行自蒸馏，将harness能力内化到模型。
- [#155] **Structured Recurrent Mixers** — 训练并行+推理循环双模式架构 TL;DR: 问题：并行训练架构推理吞吐量低，循环架构训练效率低。 方法：提出结构化循环混合器，训练时并行、推理时循环的双模式架构。
- [#183] **DECO: Sparse MoE with Dense-Comparable Performance** — 端侧稀疏 MoE 达到稠密模型性能 TL;DR: 问题：MoE总参数量大导致存储和内存瓶颈，阻碍端侧部署。 方法：提出DECO，端侧稀疏MoE达到稠密模型性能，同时降低存储和计算开销。
- [#192] **RLRT: Rebellious Student** — 反转教师信号强化学生自主推理路径的 RLVR 方法 TL;DR: 问题：自蒸馏中教师在成功轨迹上也覆盖学生选择，抑制学生自身推理。 方法：提出RLRT，在成功轨迹上反转教师信号，让学生探索自己的推理路径。
- [#195] **Step Rejection Fine-Tuning** — 步级拒绝微调利用未解决轨迹的可用步骤 TL;DR: 问题：拒绝微调(RFT)丢弃所有未解决轨迹，但其中包含可用步骤。 方法：提出步级拒绝微调，保留未解决轨迹中的可用步骤用于训练。
- [#203] **PowerStep: Memory-Efficient Adaptive Optimization** — 基于 l_p 范数最速下降的内存高效优化器 TL;DR: 问题：Adam优化器因存储二阶矩而有大量内存开销。 方法：提出PowerStep，基于l_p范数最速下降实现坐标自适应，无需存储二阶矩。
- [#216] **QD-LLM: Parameter-Efficient Neuroevolution** — 通过 prompt 嵌入进化实现 LLM 生成多样性 TL;DR: 问题：LLM输出模态坍缩，产生同质化结果。 方法：提出QD-LLM，在QD优化框架中进化prompt嵌入（~32K参数），引导冻结LLM产生多样性输出。
- [#235] **Sparse Layers Are Critical to Scaling Looped LMs** — 稀疏 MoE 是循环语言模型扩展的关键 TL;DR: 问题：循环语言模型通过重复层减少内存，但不如标准Transformer可扩展。 方法：发现稀疏MoE层是循环模型扩展的关键——MoE+循环可匹配标准Transformer。
- [#244] **SlimQwen: MoE Pruning and Distillation** — MoE 大规模预训练中剪枝与蒸馏策略系统研究 TL;DR: 问题：MoE模型大规模预训练中剪枝和蒸馏如何应用尚不清楚。 方法：系统研究MoE预训练中的剪枝和蒸馏策略，回答剪枝是否提供加速、蒸馏时机等关键问题。
- [#245] **The Extrapolation Cliff in On-Policy Distillation** — 推导出策略蒸馏中外推系数的解析安全阈值 TL;DR: 问题：策略蒸馏中外推系数超过阈值会导致结构化输出任务违约。 方法：在单位置伯努利约简中推导出闭合形式的安全阈值λ*，概率理论保证。
- [#261] **mHC-SSM: Manifold-Constrained Hyper-Connections** — 流形约束超连接用于状态空间语言模型 TL;DR: 问题：流形约束超连接(mHC)能否有效迁移到状态空间模型。 方法：将mHC式约束多流残差拓扑迁移到SSM语言模型，配合流特化适配器。
- [#263] **HTPO: Hierarchical Token-level Objective Control** — 层次化 token 级目标控制平衡 RLVR 探索与利用 TL;DR: 问题：RLVR对所有token赋相同优化目标，缺少对推理token的细粒度引导。 方法：提出HTPO，层次化token级目标控制，平衡探索与利用。
- [#268] **Reasoning emerges from constrained inference manifolds** — 推理在约束推理流形上涌现的几何与信息论框架 TL;DR: 问题：推理质量主要靠标注基准评估，混淆了任务性能和内部推理质量。 方法：研究推理作为内在动态过程，发现推断时动态自组织为低维约束流形，几何和物理约束驱动推理涌现。
- [#270] **Block-Wise Differentiable Sinkhorn Attention** — 块状可微 Sinkhorn 注意力用于长上下文 TL;DR: 问题：长上下文Sinkhorn注意力的可微实现困难。 方法：研究TPU上的块状可微Sinkhorn注意力，停止基础T步后展开短精炼尾并精确微分。

## 二、LLM 推理与能力（14篇）

关注 LLM 的推理能力提升与机制研究。

- [#41] **MemReread: Memory-Guided Rereading** — 记忆引导重读增强长上下文推理。TL;DR: 问题：记忆化阅读范式中潜在证据丢失，检索模块虽能回召但不足以发现深层关联。 方法：提出MemReread，通过记忆引导重读机制，让智能体主动回溯重读可能被遗漏的关键信息。
- [#81] **The Silent Vote** — 语义近邻聚合提升零样本可靠性 TL;DR: 问题：约束解码中softmax丢弃语义同义词概率质量，导致"重归一化偏差"。 方法：提出语义近邻聚合，恢复语义同义词的概率质量，提升零样本分类可靠性。
- [#86] **Statistical Scouting Debate** — 统计侦查发现辩论安全但非辩论有用案例 TL;DR: 问题：何时该直接回答、采样投票还是多智能体辩论？辩论的增益可能只是投票带来的。 方法：在匹配token预算下，统计侦查发现哪些案例可安全辩论但无法从辩论获益。
- [#95] **Hidden Error Awareness in Chain-of-Thought** — CoT 中隐藏错误的可诊断信号 TL;DR: 问题：CoT假设生成推理反映模型内部计算，但模型内部能检测推理错误却外在表达自信。 方法：用线性探针从隐藏状态预测正确性达0.95 AUROC，但该信号是诊断性而非因果性——增强它不能修复错误。
- [#97] **APCD: Adaptive Path-Contrastive Decoding** — 自适应路径对比解码提升生成可靠性 TL;DR: 问题：自回归解码中早期次优选择误导后续生成导致幻觉，多路径解码缺乏分支时机和路径交互策略。 方法：提出APCD，自适应决定何时分支、用对比解码调节路径间交互，提升生成可靠性。
- [#98] **Not All Thoughts Need HBM: Semantics-Aware Memory Hierarchy** — 语义感知记忆层级优化 LLM 推理 TL;DR: 问题：推理LLM的KV缓存占满GPU HBM，永久驱逐token导致推理准确率崩溃。 方法：提出语义感知记忆层级，将token按语义重要性分为HBM/DDR/SSD四级存储，一半缓存移出HBM只损失0-3.5%准确率。
- [#108] **RuPLaR: Latent Compression of Reasoning Chains** — 基于规则的推理链潜空间压缩 TL;DR: 问题：CoT推理受自然语言低效和表达力限制，现有潜在推理存在多步/多模型复杂结构问题。 方法：提出RuPLaR，用规则先验引导LLM单阶段自主生成潜在推理token，消除级联过程和模型间依赖。
- [#131] **Scalar Implicature Pragmatic Reasoning** — 评估 LLM 语用推理中标量蕴含能力 TL;DR: 问题：LLM语用推理评估方法不同结果差异大，prompt判断可能与内部概率分布不一致。 方法：用标量蕴含多样性研究LLM的语用推理能力，区分真实能力和任务引发行为。
- [#157] **Hint Tuning: Less Data Makes Better Reasoners** — 通过难度探测自动构建训练数据减少推理 token TL;DR: 问题：大推理模型生成过多token，对所有问题统一冗长推理。 方法：提出Hint Tuning，用指令模型作为难度探测器，少量数据教模型校准推理深度。
- [#177] **AIPO: Learning to Reason from Active Interaction** — 主动多智能体交互扩展推理边界 TL;DR: 问题：RLVR的探索受策略模型能力边界限制，虽有外部探索但太小或室内。 方法：提出AIPO，主动多智能体交互让策略模型通过交互体验扩展推理边界。
- [#191] **The Last Word Often Wins** — CoT 格式混淆因素研究 TL;DR: 问题：CoT忠实性研究中，CoT损坏实验检测的是答案位置而非计算重要性。 方法：识别"最后单词胜出"格式混淆因素，终端答案语句主导结果。
- [#204] **Task-Aware Calibration: Provably Optimal Decoding** — 任务校准实现最优 MBR 解码 TL;DR: 问题：LLM输出分布与真实生成分布不对齐导致解码次优，自由文本校准是病态问题。 方法：提出任务感知校准，在任务特定组合空间中实现可证最优MBR解码。
- [#262] **In-Context Fixation** — 上下文学习中的标签固着效应及其机制定位 TL;DR: 问题：少样本分类中同质标签—even语义有效的—导致准确率崩溃至≤12%。 方法：发现模型将标签位token视为穷尽答案词汇，同质标签触发标签固着效应。
- [#264] **Spatial Priming Outperforms Semantic Prompting** — 空间启动（网格叠加）比语义提示更有效提升图表数据提取 TL;DR: 问题：科学图表数据提取中，语义提示和空间提示哪个更有效。 方法：发现空间启动（网格叠加）比语义提示更有效提升图表数据提取准确率。

## 三、智能体系统（18篇）

Agent 是当日最热方向之一，涵盖工具使用、多智能体协作、GUI Agent 等。

- [#2] **WildClawBench** — 真实长时间 Agent 评估基准，最佳模型仅达 62.2% TL;DR: 问题：现有Agent基准依赖合成沙箱和短程任务，无法评估真实长程工作能力。 方法：构建60个人工编写的双语多模态任务基准，在真实CLI环境中评估，最佳模型仅达62.2%。
- [#11] **Visual-Native Multimodal Deep Search Agents** — 视觉原生多模态深度搜索智能体及 ODE 数据演化 TL;DR: 问题：多模态深度搜索智能体中，中间视觉证据无法被后续工具复用，且训练数据无法跟踪智能体能力演化。 方法：提出视觉原生工具集成（让工具生成图像可被后续消费）和ODE在线数据演化（跟踪智能体进展自动更新训练数据）。
- [#53] **SkillRAE: Agent Skill-Based Context Compilation** — 基于技能的上下文编译用于检索增强执行 TL;DR: 问题：LLM智能体技能库增长后，检索增强执行(RAE)中的技能编译效率下降。 方法：提出SkillRAE，基于技能的上下文编译框架，优化检索技能的组装和注入。
- [#59] **Swarm Skills: Portable Self-Evolving Multi-Agent** — 可移植自演化多智能体技能规范 TL;DR: 问题：多智能体协调协议锁在框架内部代码中，无法像单智能体技能那样可移植和系统化改进。 方法：提出Swarm Skills规范，将多智能体协调协议编码为可移植、自演化的技能资产。
- [#68] **TRACER: Verifiable Generative Provenance** — 多模态工具使用智能体的可验证生成溯源性 TL;DR: 问题：多模态工具使用智能体暴露工具轨迹但不指定哪个观测支撑哪个生成声明。 方法：提出TRACER，建立声明级别的依赖结构，实现可验证的生成溯源性。
- [#70] **PruneTIR: Inference-Time Tool Call Pruning** — 推理时工具调用剪枝提升效率 TL;DR: 问题：工具集成推理中增加工具调用可提升能力但降低效率，推理时如何进一步改进已有工具能力的LLM未被充分探索。 方法：提出PruneTIR，在推理时剪枝不必要工具调用，保持推理效果的同时提高效率。
- [#92] **TacoMAS: Test-Time Co-Evolution of Topology and Capability** — 测试时拓扑与能力协同演化 TL;DR: 问题：多智能体自演化方法要么固定拓扑、要么只调拓扑或只调能力，实证和理论显示需要同时演化。 方法：提出TacoMAS，测试时拓扑与能力协同演化，理论证明两者必须联合优化。
- [#110] **Mem-W: Latent Memory-Native GUI Agents** — 潜记忆原生 GUI 智能体 TL;DR: 问题：GUI智能体记忆是外部人工可读制品，无法高效携带视觉和过程证据。 方法：提出Mem-W，将记忆直接嵌入模型的潜在空间，原生支持GUI操作的视觉和过程证据传递。
- [#116] **LLM Agents Already Know When to Call Tools** — 无需推理即可判断工具调用时机 TL;DR: 问题：工具增强智能体即使不需要也乱调工具，浪费API费用和延迟。 方法：提出When2Tool基准，发现LLM无需推理即可判断工具调用时机。
- [#134] **GAMBIT: Adversarial Robustness in Multi-Agent LLM Collections** — 多智能体对抗鲁棒性基准 TL;DR: 问题：多智能体系统中单个欺骗智能体可破坏整个集体，现有研究只针对浅层任务且未考虑自适应对手。 方法：提出GAMBIT三模式基准，在三个评估模式下测试对抗鲁棒性。
- [#153] **DEPT: Dual-Scale Evolutionary Policy Training** — 双尺度演化策略训练解决社会语言博弈僵局 TL;DR: 问题：开放社交语言博弈中自博弈导致策略同质化和进化僵局。 方法：提出DEPT双尺度演化策略训练，同时优化短期交互和长期策略多样性。
- [#154] **AgentForesight: Online Auditing for Early Failure Prediction** — 多智能体在线审计早期故障预测 TL;DR: 问题：多智能体系统中单个错误会级联为轨迹级失败，现有方法只能事后归因。 方法：提出AgentForesight，在线审计实现早期故障预测。
- [#158] **AgentCollabBench** — 诊断多智能体协作中的行为风险 TL;DR: 问题：多智能体管线中一个智能体丢约束会导致静默损坏，结果评估看不见。 方法：构建AgentCollabBench，诊断多智能体协作中的过程失败。
- [#167] **Do Agents Need to Plan Step-by-Step?** — 数据中心任务中全视野规划优于逐步规划 TL;DR: 问题：数据为中心任务中全视野规划vs单步规划哪个更有效尚不清晰。 方法：发现全视野规划加lazy repanning与单步规划精度相当，但token减少2-3倍。
- [#169] **PYTHALAB-MERA: Frozen-LLM Coding Agent** — 冻结 LLM 编码智能体的验证驱动记忆与技能复用 TL;DR: 问题：冻结LLM编码智能体缺少验证驱动的记忆和技能复用。 方法：提出外部控制器管理记忆记录和AST技能、fail-fast验证、TD(λ)延迟信用传播，3任务8/9通过vs基线0/9。
- [#184] **SLIM: Dynamic Skill Lifecycle Management** — 智能体强化学习中的动态技能生命周期管理 TL;DR: 问题：智能体技能要么累积为持续指导要么内化到策略中，最终导致零技能推理。 方法：提出SLIM动态技能生命周期管理，技能可创建、演化、退役和复活。
- [#202] **How Mobile World Model Guides GUI Agents?** — 移动世界模型指导 GUI 智能体 TL;DR: 问题：移动世界模型提供文本或图像未来状态，哪种表示更有用不清楚。 方法：系统评估文本/图像世界模型对GUI智能体动作后果预测的指导效果。
- [#214] **Nautilus Compass: Black-box Persona Drift Detection** — 黑盒人格漂移检测用于生产 LLM 编码智能体 TL;DR: 问题：生产LLM编码智能体在长会话中人格漂移，白盒方法无法用于封闭API。 方法：提出Nautilus Compass，黑盒人格漂移检测方法。
- [#227] **SkillMAS: Skill Co-Evolution with Multi-Agent System** — 技能演化与多智能体系统架构联合优化 TL;DR: 问题：智能体技能演化与多智能体系统重构脱节，造成组织瓶颈和上下文压力。 方法：提出SkillMAS非参数框架，技能演化与MAS架构联合优化。
- [#250] **MIND-Skill: Multi-Agent Induction and Deduction** — 多智能体归纳演绎保证技能质量 TL;DR: 问题：多步任务需要领域特定过程知识，技能质量无法保证。 方法：提出MIND-Skill，多智能体归纳演绎保证技能质量。
- [#269] **Scaling Mobile Agent Systems** — 移动智能体系统的能力密度与集体智能扩展 TL;DR: 问题：移动智能体系统受限于设备计算能力和碎片化智能。 方法：提出从能力密度到集体智能的两维度扩展研究议程。

## 四、RAG 与检索增强（8篇）

- [#7] **RUBEN: Rule-Based Explanations for RAG Systems** — 基于规则的 RAG 输出解释与安全审计工具 TL;DR: 问题：RAG系统的输出缺少可解释性规则，安全审计困难。 方法：提出RUBEN交互工具，通过剪枝策略高效发现最小规则集解释RAG输出，可用于安全训练韧性测试和对抗注入有效性检测。
- [#30] **DeepRefine: Agent-Compiled Knowledge Refinement** — 智能体编译知识库的强化学习精炼。TL;DR: 问题：智能体编译的知识库存在不完整、不正确和冗余问题，迭代使用中缺陷累积降低检索保真度。 方法：提出DeepRefine，用强化学习让智能体自主发现和修复知识库缺陷，提升检索和下游性能。
- [#43] **Route Before Retrieve** — 激活 LLM 潜在路由能力区分 RAG 与纯 LLM 场景 TL;DR: 问题：RAG和长上下文策略选择困难——RAG受检索质量限制，长上下文成本高且有位置敏感性。 方法：激活LLM的潜在路由能力，让模型自身判断何时用RAG何时用长上下文。
- [#87] **Byte-Exact Deduplication in RAG** — 字节精确去重对 RAG 的三机制实证分析 TL;DR: 问题：RAG中字节精确去重效果因场景差异大，缺乏系统分析。 方法：跨三场景（学术检索0.16%、企业模式24%、对话AI 80%冗余）实证分析去重效果和质量影响。
- [#125] **GRC: Unified Generation-Retrieval-Compression** — 统一生成-检索-压缩框架 TL;DR: 问题：文本嵌入和生成任务分别训练成本高，上下文压缩也是推理驱动的关键挑战。 方法：提出GRC，统一推理驱动的生成、检索和压缩框架，减少训练和部署开销。
- [#148] **SeedRG: Leakage-Free Benchmarks for RAG** — 无知识泄漏的 RAG 评估基准 TL;DR: 问题：RAG基准中许多问题可从LLM参数记忆直接回答（知识泄漏），导致评估不可靠。 方法：提出SeedRG，生成无知识泄漏的RAG评估基准。
- [#187] **Pi-Serini: Lexical Retrieval for Agentic Search** — 词汇检索结合前沿 LLM 实现深研究搜索 TL;DR: 问题：LLM在智能体循环中变强后，词汇检索是否足够。 方法：提出Pi-Serini，BM25配合前沿LLM的推理和工具使用能力实现深度研究搜索。
- [#259] **CDS4RAG: Cyclic Dual-Sequential HPO** — 循环双序列超参优化用于 RAG TL;DR: 问题：RAG对检索器和生成器超参敏感，现有优化算法收敛慢。 方法：提出CDS4RAG，循环双序列超参优化，联合优化检索和生成超参。

## 五、多模态（18篇）

涵盖视觉-语言模型、图表理解、视频推理、语音-文本联合等。

- [#4] **BICR: LVLM Confidence via Blind-Image Contrastive Ranking** — 盲图像对比排序估计 LVLM 置信度 TL;DR: 问题：视觉语言模型存在"视觉不接地"问题——可能完全靠语言先而非图像回答，现有置信度方法无法检测。 方法：提出BICR，在训练时对比真实图像和遮蔽图像的隐藏状态，用排序损失惩罚对遮蔽视图的高置信度，零额外推理成本下实现跨模型最佳校准。
- [#8] **ChartCF: Counterfactuals for Data-Efficient Chart Understanding** — 反事实数据增强+偏好优化提升图表理解 TL;DR: 问题：大规模SFT数据训练图表理解模型效率低，且忽略了图表可通过代码微改产生语义剧变的特性。 方法：提出ChartCF，通过代码修改生成反事实数据、基于相似性筛选样本、多模态偏好优化，用显著更少数据达到强模型水平。
- [#34] **Phoenix-VL 1.5 Medium** — 视觉语言模型技术报告 TL;DR: 问题：需要面向区域语言和本地化场景的多模态大模型。 方法：在Mistral Medium 3.1上用1万亿token本地化多模态语料继续预训练，再2500亿token长上下文扩展，实现深度领域适应且不损失通用智能。
- [#105] **ProCauEval: Causal Discovery Deficit in LMMs** — 多模态大模型因果发现缺陷评估与缓解 TL;DR: 问题：多模态大模型在因果发现上受文本先验捷径影响，但机制不明确。 方法：提出ProCauEval，分解因果发现过程测试模型在每个子过程的能力。
- [#113] **DeltaRubric: Multimodal Reward Modeling** — 基于规划与验证的可生成多模态奖励模型 TL;DR: 问题：MLLM奖励模型存在懒惰评判和语言先验剥削，将评分标准扩展到多模态受视觉推理复杂性瓶颈约束。 方法：提出DeltaRubric，联合规划与验证的生成式多模态奖励模型。
- [#122] **Meow-Omni 1: Multimodal LLM for Feline Ethology** — 面向猫科行为学的多模态大语言模型 TL;DR: 问题：动物行为学中"语义混叠"问题——相同外部信号对应不同内部状态，现有MLLM无法处理高频生物时序数据。 方法：提出Meow-Omni，融合高频生理信号的多模态猫科行为学模型。
- [#129] **CLIP Multilingual Visual Grounding** — CLIP 多语言视觉定位 TL;DR: 问题：多语言视觉语言模型跨语言性能差异的机制不明确。 方法：用13种语言的密集CLIP探针，保持视觉编码器不变只换文本分支，精确定位跨语言差异来源。
- [#145] **EmoS: Streaming Emotional Understanding Benchmark** — 高保真双语流式情感理解基准 TL;DR: 问题：情感理解基准无法同时实现生态效度、信号清晰度和可靠细粒度标注。 方法：构建EmoS，高保真双语流式情感理解基准。
- [#178] **jina-embeddings-v5-omni** — 冻结塔组合的多模态嵌入模型 TL;DR: 问题：多模态嵌入模型训练成本高。 方法：提出冻结塔组合，非文本编码器适配到语言模型生成嵌入，文本几何保持，无需联合训练所有编码器。
- [#196] **MulTaBench: Multimodal Tabular Learning** — 图像与文本表格多模态学习基准 TL;DR: 问题：表格基础模型缺乏对文本和图像的原生支持，依赖冻结嵌入。 方法：构建MulTaBench，评估多模态（文本+图像）表格学习。
- [#205] **V-ABS: Action-Observer Driven Beam Search** — 动作-观察驱动束搜索用于动态视觉推理 TL;DR: 问题：多步视觉推理中智能体忽视执行反馈，产生想象-动作-观察偏差。 方法：提出V-ABS，动作-观察驱动束搜索，整合执行反馈修正推理。
- [#206] **MolSight: Molecular Property Prediction with Images** — 纯视觉分子属性预测 TL;DR: 问题：分子属性预测偏重图/3D/语言模型，忽略了普适的2D骨架图表示。 方法：提出MolSight，首次系统大规模使用2D分子图进行属性预测。
- [#211] **KnotBench: Diagrammatic Knot Reasoning** — 结构图推理基准测试 VLM TL;DR: 问题：VLM能看懂结图但不能对其结构进行推理。 方法：构建KnotBench，858K图像+14个任务，以Regina规范签名为标准答案。
- [#213] **EgoMemReason: Memory-Driven Egocentric Video** — 记忆驱动的一周长自我中心视频推理基准 TL;DR: 问题：超长视频中相关信息稀疏分布，记忆是根本挑战。 方法：构建EgoMemReason，一周长自我中心视频的记忆驱动推理基准。
- [#222] **Modality-Role Interference in Multimodal RPA** — 多模态角色扮演中的模态-角色干扰及消解 TL;DR: 问题：MLLM的通用视觉特征在角色扮演中压倒脆弱的角色特质，造成模态-角色干扰。 方法：提出解决模态-角色干扰的方法，让视觉内容通过角色视角呈现。
- [#224] **EduStory: Pedagogically-Consistent STEM Video Generation** — 教学一致性多镜头 STEM 教学视频生成 TL;DR: 问题：长视频生成中知识一致性和教学叙事连贯性难以维持。 方法：提出EduStory，融合教学设计原则的多镜头STEM教学视频生成框架。
- [#231] **ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation** — 视觉退化鲁棒的多模态推理强化 TL;DR: 问题：MLLM推理策略在真实视觉退化（模糊、压缩、低分辨率）下脆弱。 方法：提出ROMA，强化多模态推理对视觉退化的鲁棒性。
- [#248] **RewardHarness: Self-Evolving Agentic Post-Training** — 图像编辑的自演化智能体奖励框架 TL;DR: 问题：图像编辑奖励模型依赖大规模偏好标注和数据效率低。 方法：提出RewardHarness，自演化智能体奖励框架，从少量示例推断评估标准。
- [#266] **MULTITEXTEDIT: Cross-Lingual Text-in-Image Editing** — 跨语言图文编辑基准及语言保真度指标 TL;DR: 问题：图文编辑基准过度以英语为中心，混淆视觉合理性和语义正确性。 方法：构建MULTITEXTEDIT，12种语言、5个视觉域、7种编辑操作的控制基准。

## 六、效率与压缩（17篇）

量化、剪枝、KV 缓存、推测解码等。

- [#85] **Scratchpad Patching: Byte-Level LM Decoupling** — 字节级语言模型中 scratchpad 与补丁大小解耦 TL;DR: 问题：字节级模型中patch大小决定了计算量与建模质量的紧密权衡。 方法：提出Scratchpad Patching，将计算与patch大小解耦，大patch降计算但不降质量。
- [#102] **Context Compression: Semantic-Driven** — 语义驱动的上下文压缩替代位置偏差 TL;DR: 问题：软提示压缩受位置偏差约束，保留开头/结尾token而非语义重要token。 方法：提出语义驱动的上下文压缩，替代现有的位置偏差压缩。
- [#109] **Test-Time Speculation** — 测试时推测加速推理 TL;DR: 问题：投机解码中接受长度随生成长度退化，几千token后接近1（无加速）。 方法：提出TTS测试时推测，在线蒸馏持续适应draft模型，利用验证步骤的目标模型信号免费训练。
- [#141] **Fitting Is Not Enough: Smoothness in Quantized LLMs** — 极低比特量化 LLM 的平滑性保持 TL;DR: 问题：极低比特量化LLM除了数值精度下降，还存在系统性的平滑性退化。 方法：提出在量化中同时保持输出平滑性，而不仅仅是数值拟合。
- [#147] **ReST-KV: Robust KV Cache Eviction** — KV 缓存逐出用于长上下文高效推理 TL;DR: 问题：KV缓存逐出方法只保留高注意力权重KV对，忽略token移除导致的注意力重分布和时空动态。 方法：提出ReST-KV，逐层输出重建+时空平滑实现鲁棒KV缓存逐出。
- [#159] **EdgeFlowerTune: Federated LLM Fine-Tuning on Edge** — 边缘设备联邦微调基准 TL;DR: 问题：边缘设备联邦微调LLM缺乏现实约束评估。 方法：提出EdgeFlowerTune基准，在真实边缘系统约束下评估联邦LLM微调。
- [#160] **PARD-2: Dual-Mode Speculative Decoding** — 双模式推测解码实现近 7 倍无损加速 TL;DR: 问题：投机解码中draft模型训练目标与推理时最大化连续token接受不直接对齐。 方法：提出PARD-2，重新制定draft模型目标为与目标模型对齐，实现双模式推测解码近7倍无损加速。
- [#185] **SOL: Self-Optimizing Language Models** — 自优化语言模型动态分配每 token 计算预算 TL;DR: 问题：静态压缩对所有token均匀分配计算，简单token过度计算、困难token计算不足。 方法：提出SOL自优化语言模型，动态分配每token计算预算。
- [#199] **SlimSpec: Low-Rank Draft LM-Head** — 低秩草稿 LM 头加速推测解码 TL;DR: 问题：投机解码中draft模型的LM头向大词表投影成为瓶颈。 方法：提出低秩draft LM头，减少投影维度加速推测。
- [#208] **Federated LM Under Bandwidth Budgets** — 带宽预算下联邦语言模型的蒸馏与校准理论 TL;DR: 问题：带宽受限的联邦语言模型训练中，可达到什么统计保证。 方法：研究分布数据在显式带宽预算下的蒸馏率和覆盖保证。
- [#212] **KVM: Key-Value Means** — 注意力的块循环机制实现线性推理 TL;DR: 问题：注意力机制中如何实现线性推理。 方法：提出KVM块循环机制，固定或增长状态，少量新参数即可将Transformer变为O(N)分块RNN。
- [#217] **Nectar: Neural Estimation of Cached-Token Attention** — 缓存 token 注意力的神经网络近似 TL;DR: 问题：固定长上下文的softmax注意力需要读取每个缓存KV对，计算开销大。 方法：提出Nectar，用紧凑神经网络拟合查询到注意力输出的映射函数，大幅减少计算。
- [#238] **RKU: Reasoning-Aware Structural Pruning** — 推理感知结构剪枝保持 CoT 能力 TL;DR: 问题：结构剪枝损害LLM的CoT推理能力。 方法：提出RKU，推理感知结构剪枝，保持CoT能力同时减少参数。
- [#239] **Non-Monotonic Latency in Apple MPS Decoding** — Apple MPS 后端 KV 缓存导致的非单调延迟分析 TL;DR: 问题：Apple MPS后端的自回归推理延迟非单调变化，KV缓存并非总是加速。 方法：识别并分析MPS后端非单调延迟行为，揭示KV缓存交互和执行模式变化。
- [#246] **AdaPreLoRA: Adafactor Preconditioned LoRA** — Adafactor 预条件低秩适配 TL;DR: 问题：LoRA的Jacobian秩亏导致标准链式法则无法唯一确定因子空间梯度。 方法：提出AdaPreLoRA，Adafactor预条件低秩适配。
- [#249] **AAAC: Activation-Aware Adaptive Codebooks** — 激活感知自适应码本用于 4-bit 量化 TL;DR: 问题：4位权重量化中固定网格映射限制精度。 方法：提出AAAC，激活感知自适应码本，根据激活分布优化量化码本。
- [#256] **Queryable LoRA** — 可查询 LoRA 通过共享低秩更新原子的指令正则化路由 TL;DR: 问题：LoRA的静态低秩参数化在输入依赖和深度变化时过于刚性。 方法：提出Queryable LoRA，指令正则化路由在共享低秩更新原子上选择组合。

## 七、安全与对齐（20篇）

LLM 安全性、偏见、对齐、越狱、隐私等。

- [#10] **DISCA: Training-Free Cultural Alignment** — 推理时基于世界价值观分歧的文化对齐（无需微调） TL;DR: 问题：LLM的隐含偏好不具有文化中立性，现有文化对齐方法需要微调或白盒访问。 方法：提出DISCA，推理时将各国建模为人口统计面板，利用分歧而非共识生成有界logit校正，20国7个backbone上文化不对齐降低10-24%，无需改权重。
- [#17] **Intrinsic Guardrails: Semantic Geometry vs. Emergent Misalignment** — 人格语义空间结构稳定性作为内在安全护栏（消融 Evil 向量→失对齐率 >40%） TL;DR: 问题：微调LLM在良性数据上可能引发广泛有害行为（涌现性失对齐），但其与模型人格语义空间的关系未探索。 方法：映射LLM的人格语义空间（大五、暗黑三联征等），发现消融"邪恶向量"导致失对齐率超40%，人格语义几何提供内在安全护栏。
- [#23] **ThreatCore: Explicit and Implicit Threat Detection** — 显式/隐式威胁检测基准 TL;DR: 问题：NLP中的威胁检测缺少一致定义和标准化基准，常与毒性、仇恨言论混淆。 方法：构建ThreatCore数据集，区分显式威胁、隐式威胁和非威胁，系统重新标注多个公开数据源。
- [#46] **To Redact or Not: Deliberative Process Privilege** — 本地 LLM 审议过程特权修订 TL;DR: 问题：政府信息公开中审议过程特权的脱敏分类需要高精度和法律一致性。 方法：用本地LLM自动分类审议过程特权，平衡信息透明与敏感内容保护。
- [#74] **Pseudo-Deliberation: Reasoning Fails to Align Values** — 推理伪装下价值观与行动不一致 TL;DR: 问题：LLM陈述的价值观不转化为行动，即使在显式推理下也存在"伪审议"——看似有原则的推理但无对应行为对齐。 方法：揭示伪审议现象，推理不能消解价值-行动差距。
- [#78] **Dark Triad Feature Steering** — 暗黑三联征特征驱动的可分离对齐与利用 TL;DR: 问题：暗黑三联征人格特征如何影响LLM行为缺乏理解。 方法：用SAE特征转向放大暗黑三联征特质，发现马基雅维利主义、自恋和精神病态驱动不同反社会行为回路，可分离操控。
- [#99] **Bayesian Misinformation Susceptibility** — 认知动机贝叶斯虚假信息易感性 TL;DR: 问题：虚假信息易感性缺乏认知基础的计算框架。 方法：提出BPL（有界语用听者），扩展RSA理论加入认知约束（递归深度限、先验压缩、偏好加权），建模虚假信息易感性。
- [#124] **Fin-Bias: LLM Decision-Making under Human Bias in Finance** — 金融场景 LLM 决策偏见评估 TL;DR: 问题：金融领域LLM决策偏见评估缺少系统基准。 方法：构建Fin-Bias，评估LLM在含人类偏见上下文中的金融决策可靠性和对对抗操控的易感性。
- [#132] **BiAxisAudit: LLM Bias Across Sensitivity and Specificity** — 双轴 LLM 偏见审计框架 TL;DR: 问题：LLM偏见审计将偏差坍缩为单一标量，忽略了跨提示含义保持不变带来的偏差和响应层差异。 方法：提出BiAxisAudit双轴审计框架。
- [#139] **SRA: LLM-Agnostic Semantic Representation Attack** — 语义表示攻击 99.71% 成功率跨 26 个 LLM TL;DR: 问题：现有token级对抗优化依赖特定肯定模板，易遇瓶颈且视觉不可读。 方法：提出语义表示攻击，优化语义层面而非token层面，99.71%成功率跨26个LLM。
- [#156] **Explanation Fairness in LLMs** — LLM 决策解释公平性审计框架 TL;DR: 问题：LLM决策解释在不同人口群体间是否公平（质量、深度、语气、语言精细度）未被研究。 方法：提出解释公平性框架，实证分析LLM如何为不同群体解释决策。
- [#164] **A Single Neuron Is Sufficient to Bypass Safety** — 单个神经元即可绕过安全对齐 TL;DR: 问题：安全对齐通过拒绝神经元和概念神经元两个系统运作，其鲁棒性存疑。 方法：发现单个神经元即可绕过安全对齐——抑制拒绝神经元绕过安全、放大概念神经元诱导有害内容，跨7个模型验证。
- [#181] **Sanity Checks for Long-Form Hallucination Detection** — 长文本幻觉检测中的端点伪影控制实验 TL;DR: 问题：长文本幻觉检测方法是否评估推理本身还是利用最终答案的表面相关。 方法：引入受控不变性方法，Force和Rerun两个oracle测试区分评估对象。
- [#193] **LITMUS: Behavioral Jailbreaks of LLM Agents** — 操作系统环境中 LLM Agent 行为越狱基准 TL;DR: 问题：LLM智能体在真实OS环境中的行为越狱风险未被评估。 方法：构建LITMUS，在真实操作系统环境中测试行为越狱（诱导执行危险OS操作）。
- [#194] **Conformity Generates Collective Misalignment** — 从众效应导致 AI 群体稳定失对齐 TL;DR: 问题：AI安全研究关注个体对齐，但部署的AI系统以群体交互，社会影响可能覆盖个体对齐。 方法：模拟从众动态，发现个体对齐的AI群体可通过从众效应达到稳定失对齐状态。
- [#200] **StereoTales: Multilingual Stereotype Discovery** — 多语言开放式 LLM 刻板印象发现框架 TL;DR: 问题：LLM社会偏见研究以英语为中心、基于模板或仅识别预定义刻板印象。 方法：构建StereoTales，10种语言开放式刻板印象发现框架。
- [#221] **MemPrivacy: Privacy-Preserving Memory for Edge-Cloud** — 边云智能体隐私保护记忆管理 TL;DR: 问题：云端辅助记忆管理暴露用户隐私，现有隐私保护过度遮蔽丢失语义。 方法：提出MemPrivacy，边云智能体隐私保护记忆管理，平衡隐私和效用。
- [#247] **Bias by Necessity: Impossibility Theorems** — 序列处理偏差的数学必然性定理 TL;DR: 问题：首因效应、锚定和顺序依赖是否是序列处理的数学必然？ 方法：证明三个不可能定理：自回归因果掩码导致首因偏差不可避免。
- [#251] **PAAC: Privacy-Aware Agentic Device-Cloud** — 隐私感知智能体端云协作框架 TL;DR: 问题：云端智能体能力强但暴露数据，设备端保护隐私但能力弱，现有方案将边界视为计算切分而非信任边界。 方法：提出PAAC，隐私感知智能体端云协作框架。
- [#252] **Epistemic Overreach in LLM Personal Sensing** — LLM 个人感知解释中的认识论越权审计 TL;DR: 问题：LLM生成的个人感知解释看似合理但证据稀疏或缺失。 方法：提出认识论越权(EO)度量，审计LLM过度推断。
- [#257] **SecureForge: Finding Vulnerabilities in LLM-Generated Code** — 通过提示优化发现并预防 LLM 生成代码漏洞 TL;DR: 问题：LLM生成代码即使被要求写安全代码也平均23%产生可验证漏洞。 方法：提出SecureForge，通过提示优化发现并预防LLM生成代码漏洞。

## 八、可解释性与机制分析（13篇）

- [#13] **Prompt-Activation Duality (GCAD)** — 注意力级干预解决 KV 缓存污染 TL;DR: 问题：标准残差流激活转向在有状态对话中失败，原因是KV缓存污染——转向的token状态被重复使用导致累积退化。 方法：提出GCAD，从系统提示的自注意力中提取转向信号并用token级门控应用，解决KV缓存污染。
- [#96] **Format-Agnostic Reasoning Subspaces** — 跨模态共享推理子空间 TL;DR: 问题：LLM用不同表面形式（英文、Python、数学符号）表达相同推理，但内部是否有跨模态共享表示未知。 方法：构建TriForm基准，用探针发现LLM存在独立于表示格式的推理子空间。
- [#115] **Cornerstones or Stumbling Blocks: Rock Tokens** — 策略蒸馏中关键 token 识别 TL;DR: 问题：策略蒸馏中高损失token（Rock Tokens）即使训练饱和也持续高损失，占18%但贡献可忽略。 方法：发现它们占大量梯度范数却无法被教师修正，战略性绕过这些绊脚石可显著简化对齐。
- [#117] **Repeated-Token Counting Dissociation** — 重复 token 计数揭示表征与输出的分离 TL;DR: 问题：LLM在简单计数重复token上失败，常被归因于内部计数追踪缺陷。 方法：线性探针发现每层残差流都能解码正确计数，但模型输出错误——表征与输出是分离的。
- [#138] **Decomposing and Steering Functional Metacognition** — 功能性元认知的分解与操控 TL;DR: 问题：LLM的评估感知（benchmark-awareness）是单一行为伪影还是更深层的内部结构尚不清晰。 方法：分解功能性元认知为可操控组件，研究其内部结构。
- [#144] **Architecture, Not Scale: Circuit Localization** — 架构比规模更影响电路定位性 TL;DR: 问题：机制可解释性假设模型越大电路分析越难。 方法：挑战该假设，发现注意力架构比参数规模更影响——GQA的电路比标准MHA更集中和稳定。
- [#143] **Max-pooling MIL for Hallucination Detection** — 最大池化多实例学习检测幻觉 TL;DR: 问题：MIL幻觉检测方法计算开销大（需重复采样）。 方法：重新分析最大池化在MIL幻觉检测中的作用，简化方法减少采样开销。
- [#149] **The Grounding Gap: LLMs and Abstract Concepts** — LLM 与人类在抽象概念接地上的系统性差异 TL;DR: 问题：LLM如何为抽象概念（如正义、理论）赋予意义？与人类有系统性差异吗？ 方法：在21个LLM上复制认知科学的属性生成实验，发现LLM与人类在抽象概念接地上存在系统性差异。
- [#165] **Massive Emergence Layer in LLMs** — 发现 LLM 中巨大激活涌现层及其影响 TL;DR: 问题：LLM中大规模激活的来源和影响尚不清楚。 方法：发现大规模涌现层（ME Layer），RMSNorm和FFN共同导致，大规模激活token表示跨层不变、降低注意力多样性，提出方法减少刚性。
- [#180] **Circuit Consistency and Specificity** — 电路一致性与特异性测量揭示跨任务共享 TL;DR: 问题：电路可解释性框架缺少对电路一致性和特异性的衡量。 方法：测量电路复用比例，研究跨任务电路一致性和功能特异性。
- [#209] **Mean Pooling Generated Tokens** — 生成 token 的均值池化优于单 token 表示 TL;DR: 问题：如何将自回归生成的隐藏状态折叠为反映模型内部状态的表示。 方法：发现生成token隐藏状态的均值池化优于任何单个token，通过核对齐量化。
- [#232] **Emergent Semantic Role Understanding** — 预训练中语义角色理解的涌现 TL;DR: 问题：语义角色理解（谁对谁做了什么）是从预训练中涌现还是依赖任务特定监督尚不清楚。 方法：跨模型和预训练数据规模研究语义角色理解的涌现。
- [#267] **Feature Rivalry in SAE Representations** — 稀疏自编码器特征对抗作为不确定性签名 TL;DR: 问题：SAE特征在不确定性下如何交互尚不清楚。 方法：发现特征竞争（Feature Rivalry）——SAE特征对的负相关性，作为模型不确定性的机制签名。

## 九、评估与基准（22篇）

新基准、评估方法论、LLM-as-Judge 等。

- [#25] **MMM-Bench: Multi-level Multi-domain Document** — 多层级多域多模态文档分类基准 TL;DR: 问题：现有文档分类基准过于简化（单域、扁平标签），不反映真实多层级多模态跨域复杂性。 方法：构建首个多域多模态多层级文档分类基准，涵盖企业文档的真实复杂性。
- [#35] **ProofRank: Evaluating LLM Proof Quality** — LLM 证明质量评估超越正确性 TL;DR: 问题：LLM数学证明评估只看正确性，忽略了清晰性、简洁性、洞察力等质量维度。 方法：提出ProofRank基准，识别证明质量的具体组成维度并评估模型生成证明的多维质量。
- [#50] **ASTRA-QA: Abstract QA over Documents** — 抽象文档问答基准 TL;DR: 问题：文档抽象问答（需综合散布信息生成连贯回答）缺少稳定评估基准。 方法：构建ASTRA-QA基准，提供稳定的抽象参考答案和细粒度评估方法。
- [#67] **Beyond Majority Voting: Agreement-Based Clustering** — 基于一致性聚类的标注者视角建模 TL;DR: 问题：多数投票丢失标注者个体视角，但为每个标注者建模资源密集。 方法：提出基于一致性聚类的标注者视角建模，在保留多样观点的同时降低资源消耗。
- [#107] **HOME-KGQA: Multimodal KGQA Benchmark** — 多模态知识图谱问答基准 TL;DR: 问题：多模态知识图谱问答缺少家庭日常活动基准。 方法：构建HOME-KGQA基准，结合KG的结构化知识和LLM的灵活理解能力。
- [#119] **De-Biasing LLM-as-Judge** — LLM 评审去偏方法比较 TL;DR: 问题：LLM评审存在宽松/严格偏差和量表压缩问题。 方法：对比贝叶斯线性校正和神经ODE分数传输流，发现少数据时线性校正更好，多数据时流更优。
- [#128] **Soohak: Research-level Math Benchmark** — 数学家策划的研究级数学基准 TL;DR: 问题：现有数学基准只测竞赛级推理，不测真正推进知识前沿的研究级数学。 方法：构建Soohak，由数学家策划的研究级数学基准。
- [#142] **DocScope: Verifiable Long-Document Reasoning** — 可验证长文档推理轨迹评估基准 TL;DR: 问题：长文档理解评估只看端到端准确率，不评估推理轨迹的可信性。 方法：构建DocScope，将长文档QA形式化为结构化推理轨迹预测（证据页、支撑片段、答案）。
- [#151] **Narrative Landscape: LLM Dispositions** — LLM 叙事倾向量化框架 TL;DR: 问题：不同LLM的叙事倾向缺乏量化框架。 方法：提出结构化叙事约束选择任务，通过一致性和预测性两个维度量化模型特定的叙事倾向。
- [#161] **100K+ Movie Reviews from Kazakhstan** — 哈萨克斯坦多语言电影评论语料 TL;DR: 问题：哈萨克斯坦多语言电影评论语料缺乏。 方法：从kino.kz收集100K+多语言电影评论（俄语、哈萨克语、语码转换），手动标注语言和情感。
- [#163] **MTMM-Geometric Framework for LLM Evaluation** — 统一多特质多方法几何评估框架 TL;DR: 问题：LLM评估构念有效性受碎片化基准和方法偏差困扰。 方法：提出MTMM-几何框架，将9个评估指标统一为潜在坐标空间中的几何测量，分解为三个正交维度。
- [#170] **Do Benchmarks Underestimate LLM Performance?** — 幻觉检测基准中人类标注的系统性低估 TL;DR: 问题：幻觉检测基准中人类标注可能系统性低估模型。 方法：用LLM预测+人类仲裁重评估，三协议一致率提高6-7%，模型准确率也提升，说明单次标注不足。
- [#174] **Sem-ECE: Semantic Calibration for Open-Ended QA** — 开放问答的语义采样校准评估 TL;DR: 问题：开放问答中LLM校准评估方法不成熟，现有方法依赖限定答案集。 方法：提出语义采样框架Sem-ECE，在开放问答中评估校准。
- [#186] **Generalized Turing Test** — 广义图灵测试作为智能比较框架 TL;DR: 问题：不同智能体间能力比较缺乏形式化框架。 方法：提出广义图灵测试(GTT)，通过不可区分性定义智能比较，产生数据集聚类和偏序。
- [#190] **RACER: Cost-Efficient Routing for LLM-as-Judge** — 推理/非推理 LLM 评审的成本最优路由 TL;DR: 问题：推理型LLM作为评审的成本和收益不清晰。 方法：对比推理和非推理评审，提出RACER自适应路由，在需要结构化验证时才启用推理。
- [#162] **CiteTracer: Citation Hallucination Detection** — 多智能体引用幻觉检测 TL;DR: 问题：LLM引文幻觉检测依赖简单的找到/未找到判断，缺乏领域级信号。 方法：提出CiteTracer多智能体框架，重构引文验证为来源检索和归因验证两阶段。
- [#207] **Instruction Adherence in Coding Agent Config** — 编码智能体配置文件指令遵循的因子研究 TL;DR: 问题：编码智能体配置文件的结构选择是否影响指令遵循尚不清楚。 方法：四因子系统实验研究文件大小、指令位置、文件架构、矛盾文件对遵循的影响。
- [#215] **Metacognitive Probe: Behavioural Calibration Diagnostics** — LLM 元认知校准五维诊断 TL;DR: 问题：LLM置信度行为缺乏细粒度诊断。 方法：提出五维元认知探针：置信校准、认识警觉、知识边界、校准范围、推理链验证。
- [#219] **Calibrate, Don't Curate: Noisy LLM Judges** — 保留弱评审而非裁剪以实现更好校准 TL;DR: 问题：多评审评估中常见做法是丢弃弱评审，但在校准评估中这反而有害。 方法：证明保留弱评审（适当校准）比裁剪更好，提出标签高效估计方法。
- [#260] **LLMSYS-HPOBench: HPO for LLM Systems** — 首个 LLM 系统超参优化基准套件 TL;DR: 问题：LLM系统的超参优化缺乏基准，复合空间和非线性交互带来挑战。 方法：构建LLMSYS-HPOBench，首个LLM系统超参优化基准套件。

## 十、NLP 核心任务（14篇）

共指消解、风格分析、句法、NLI、信息抽取等传统 NLP。

- [#18] **Interpretable Coreference Resolution Evaluation** — 基于显式语义的共指消解可解释评估 TL;DR: 问题：共指消解评估指标（如CoNLL-F1）缺乏诊断洞察，无法揭示系统在特定语义类别上的困难。 方法：在共指输出上叠加概念和命名实体识别，为名词提及分配语义标签并传播到整个共指簇。
- [#20] **Measuring Embedding Sensitivity to Authorial Style** — 法语文本作者风格嵌入敏感度分析 TL;DR: 问题：嵌入模型编码了多少作者风格信息、LLM改写后保留多少尚不清楚。 方法：用法语文学数据集量化嵌入分散性变化，发现嵌入可靠捕获作者风格特征且改写后仍保留，但不同模型风格敏感度不同。
- [#21] **Aspectual Variants of Light Verb Constructions** — 光动词结构体变体的语言学归属研究 TL;DR: 问题：光动词结构体变体（如"take on debt" vs "have debt"）在习语、光动词和合成短语之间的归属困难。 方法：研究这些争议表达的特征，提出决定三类边界的特征选择方案。
- [#49] **Contradiction Analysis in Scientific Peer Review** — 科学同行评审中的细粒度矛盾分析 TL;DR: 问题：科学同行评审中的分歧被现有方法简化为二元矛盾检测，忽略了评审上下文和矛盾严重程度差异。 方法：提出细粒度矛盾分析框架，区分评审中不同严重程度的评价矛盾。
- [#54] **GLiNER-Relex: Joint NER and Relation Extraction** — 统一命名实体识别与关系抽取框架 TL;DR: 问题：NER和关系抽取通常用独立模型处理，增加计算开销和错误传播。 方法：扩展GLiNER为统一架构GLiNER-Relex，单一模型同时完成实体识别和关系抽取。
- [#58] **Generative Linguistic Theories and LMs** — 生成语言学理论与语言模型的关系 TL;DR: 问题：Futrell & Mahowald认为LLM支持基于用法的语言学理论，但LLM与生成语法理论的兼容性被忽视。 方法：论证LLM也能实例化基于形式结构的生成语法理论，扩展了可用LLM测试的理论空间。
- [#111] **LEAF-SQL: Level-wise Text-to-SQL** — 层次化探索自适应细化的 Text-to-SQL TL;DR: 问题：现有Text-to-SQL骨架预测难处理复杂嵌套查询。 方法：提出LEAF-SQL，层次化探索加自适应细化，先用粗粒度SQL骨架再逐步精化。
- [#126] **Dynamic Meta-Metrics for MT Evaluation** — 源句条件动态权重机器翻译评估 TL;DR: 问题：机器翻译评估依赖单一静态指标组合，忽略源句特征。 方法：提出DMM，根据源句属性动态组合现有翻译评估指标。
- [#137] **Lexical Difficulty Prediction** — 上下文对齐对比学习改进词汇难度预测 TL;DR: 问题：词汇难度预测仅用标量监督训练，未显式结构化表示空间。 方法：提出上下文对齐对比学习+Ridge集成，改进跨语言词汇难度预测。
- [#168] **Competing Maturational Theories of Syntactic Development** — 句法发展的竞争成熟理论计算建模 TL;DR: 问题：儿童语言发展中句法范畴的习得顺序有争议——自下而上还是由内向外。 方法：用统计语法归纳计算建模两种成熟理论，GROWING账户显著优于INWARD。
- [#171] **Syntax of Imperatives in Yemeni Arabic** — 也门阿拉伯语祈使句法跨相赞同分析 TL;DR: 问题：也门阿拉伯语祈使句法缺乏一致性分析。 方法：提出跨相赞同(AAP)方法，统一分析简单和复杂祈使结构，包括A'链结构。
- [#175] **Effective Explanations Support Planning Under Uncertainty** — 解释如何支持不确定下行动规划的计算模型 TL;DR: 问题：如何生成能引导听众执行的有效的方向说明。 方法：提出计算模型，LLM将说明转化为程序化指引（策略先验和价值图），规划智能体执行并迭代优化。
- [#179] **Change My View: Persuasion and Polarization** — Reddit 说服与极化动态的 LLM 分析 TL;DR: 问题：共享证据和理性论证是否导致观点收敛？ 方法：用LLM分析Reddit r/ChangeMyView辩论，研究说服与极化动态。
- [#130] **Phase Transitions in Affective Meaning Divergence** — 情感意义分歧的相变分析 TL;DR: 问题：对话中同一词语的情感意义可能因听者不同而分歧。 方法：形式化情感意义分歧(AMD)，基于言语行为理论和博弈论推导相变条件。

## 十一、多语言与低资源 NLP（12篇）

- [#12] **Low-Resource NLP Needs More Than Cross-Lingual Transfer** — 卢森堡语案例研究跨语言迁移局限性 TL;DR: 问题：跨语言迁移能在多大程度上替代低资源语言的语言特定工作尚不清晰。 方法：以卢森堡语为案例，综合研究和多语种数据收集，发现跨语言迁移有显著局限，需要更多语言特定努力。
- [#39] **Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian** — 乌克兰语多域文档理解 RAG TL;DR: 问题：乌克兰语多域文档理解缺乏有效RAG方案。 方法：提出基于Qwen的RAG流水线：上下文PDF分块、问题感知稠密检索和重排、约束答案生成，在UNLP共享任务中表现优异。
- [#40] **DECO-MWE: Korean Multiword Expressions** — 韩语多词表达语言学资源 TL;DR: 问题：韩语多词表达在基于特征的情感分析中是关键难题，缺乏语言资源。 方法：构建DECO-MWE，用局部语法图方法将韩语情感多词表达形式化为有限状态转换器。
- [#42] **Korean NLU Data Generation for Banking** — 韩语银行 CS 对话 NLU 数据生成 TL;DR: 问题：银行客户服务对话系统需要大量标注训练数据。 方法：构建FIAD韩语金融标注数据集，用于生成银行CS领域NLU训练数据，提升多样话语覆盖。
- [#91] **Crosslingual On-Policy Self-Distillation** — 跨语言在策略自蒸馏提升多语言推理 TL;DR: 问题：LLM数学推理能力在低资源语言上显著下降。 方法：提出COPSD，将模型自身高资源语言推理行为迁移到低资源语言，跨语言在策略自蒸馏。
- [#100] **Sentence-Aligned Corpora for Multilingual NMT** — 高质量多语言句子对齐语料构建 TL;DR: 问题：非英语文本简化缺乏大规模高质量训练数据。 方法：构建多语言句子对齐语料库，用于训练和评估文本简化模型。
- [#120] **WorldSpeech: 76 Languages Speech Corpus** — 全球 76 种语言语音语料库 TL;DR: 问题：大多数语言的ASR因缺乏对齐数据而准确率骤降。 方法：构建WorldSpeech，76种语言65K小时对齐语音-文本语料，微调后WER平均降低63.5%。
- [#121] **Latin to Occitan Grammatical Gender Shift** — 拉丁语到奥克语语法性别迁移研究 TL;DR: 问题：拉丁语到罗曼语语法性别从三分类重构为二分类的演变机制不明。 方法：提出可解释深度学习框架，在词汇和上下文层面研究拉丁语到奥克语的语法性别迁移。
- [#123] **POS Tagging for Medieval Romance** — 中古罗曼语词性标注传统标注器与 LLM 比较 TL;DR: 问题：中古罗曼语词性标注因拼写变异、形态复杂和标注资源有限而困难。 方法：系统比较传统标注器和LLM在中古奥克语、加泰罗尼亚语和法语上的词性标注表现。
- [#127] **Character-Level Tajik-Persian Transliteration** — 字符级塔吉克-波斯语音译 TL;DR: 问题：塔吉克语（西里尔文）到波斯语（波斯-阿拉伯文）自动音译缺少数据。 方法：构建52K词的平行词汇语料，用字符级Transformer实现音译。
- [#135] **LLiMba: Sardinian on a Single GPU** — 单 GPU 上 3B 模型适配濒危撒丁语 TL;DR: 问题：撒丁语在现代NLP中几乎无存在感，商业服务和模型不支持。 方法：在单GPU上将Qwen2.5-3B-Instruct通过CPT和SFT适配撒丁语。
- [#136] **Dolphin-CN-Dialect: Chinese Dialects** — 中文方言语音语料与处理 TL;DR: 问题：中文方言语音识别数据高度不平衡。 方法：提出Dolphin-CN-Dialect流式ASR模型，用温度采样策略处理方言数据不平衡。

## 十二、领域应用（20篇）

医疗、法律、金融、科学等垂直领域。

- [#5] **Neural at ArchEHR-QA** — 临床电子健康记录问答的统一提示优化 TL;DR: 问题：电子健康记录自动问答需要精准检索、忠实生成和显式证据对齐。 方法：将任务解耦为独立模块化阶段，用DSPy的MIPROv2自动优化prompt，结合自一致性投票和阶段验证机制，四子任务总排名第二。
- [#56] **PHAGE: Patent Heterogeneous Graph Encoder** — 专利异构图编码器表示学习 TL;DR: 问题：专利权利要求有有向依赖结构，现有编码器将其线性化为文本丢弃层次。 方法：提出PHAGE，将权利要求依赖结构编码到自注意力中，处理关系类型差异和依赖图-注意力不匹配问题。
- [#61] **PlantMarkerBench** — 多物种植物标记物证据检索基准 TL;DR: 问题：植物标记基因推理缺乏基于文献证据的评估基准。 方法：构建PlantMarkerBench，评估LLM从全文论文中解读植物标记证据的能力。
- [#62] **Speech-based Psychological Crisis Assessment** — 基于语音的 LLM 心理危机评估 TL;DR: 问题：心理热线危机评估依赖人工，受专业经验和人手限制。 方法：提出LLM自动危机等级分类框架，从语音中评估心理危机水平。
- [#63] **Medical Incident Causal Factors Generation** — 医疗事件因果因素与预防措施生成 TL;DR: 问题：医疗领域LLM生成事件因果和预防措施的可靠性不足。 方法：提出基于标签的少样本示例选择方法，提示LLM从医疗事件细节生成背景/因果因素和预防措施。
- [#75] **Sentiment Analysis with Symptom Distress** — 情感分析与症状困扰关联研究 TL;DR: 问题：基于Transformer的情感分析在心理治疗中的独立心理测量价值未被研究。 方法：评估情感分析作为症状困扰和恶化独立指标的有效性。
- [#79] **ConFit v3: Resume-Job Matching** — 简历-职位匹配的 LLM 重排序 TL;DR: 问题：嵌入式简历-职位匹配缺乏可控性和可解释性。 方法：提出ConFit v3，用LLM重排序提升匹配精度和可解释性。
- [#82] **MedMeta: LLMs Synthesizing Meta-Analysis** — LLM 综合医学荟萃分析结论基准 TL;DR: 问题：LLM的高阶医学推理（如从多篇研究综合证据）缺乏评估基准。 方法：构建MedMeta，首个评估LLM从医学荟萃分析生成结论能力的基准。
- [#84] **LLMs for Mental Health Screening** — 心理健康筛查 LLM 一致性、ASR 鲁棒性与公平性 TL;DR: 问题：LLM从语音估计心理健康分数的临床可靠性（一致性、ASR鲁棒性、证据忠实度）未经检验。 方法：评估3个LLM在111名参与者上的HADS评分估计，发现一致性和ASR鲁棒性不足。
- [#89] **CLR-voyance: Inpatient Clinical Decision Support** — 住院临床决策支持的开放推理强化 TL;DR: 问题：住院临床推理评估将序列决策简化为检索或泄露信息，RL奖励信号也不合适。 方法：提出CLR-voyance，用结果感知评分标准引导开放式推理强化学习。
- [#94] **RAG and Fine-Tuning for Industrial QA** — 工业问答应用中 RAG 与微调评估 TL;DR: 问题：企业QA场景中RAG和微调哪个更好从成本-精度角度看尚不清晰。 方法：系统评估工业QA应用中RAG和微调方案，提供选型指导。
- [#101] **FinMoji: Emoji-driven Sentiment in Financial Social Media** — 金融社交媒体表情符号驱动情感分析 TL;DR: 问题：金融社交媒体中表情符号是否能作为投资者情绪的可靠代理尚不确定。 方法：提出FinMoji，研究表情符号在金融情感分析中的独立和组合效用。
- [#103] **Semi-Structured Extraction of OCR Clinical Reports** — OCR 临床报告半结构化提取 TL;DR: 问题：临床报告因隐私和数据孤岛分散在不同机构，OCR扫描件阻碍EHR集成。 方法：提出半结构化OCR临床报告提取方法，关注关键字段覆盖。
- [#104] **PumpSense: Crypto Pump-and-Dump Detection** — 加密货币拉升抛售实时检测 TL;DR: 问题：加密货币拉升抛售检测缺少公开标注数据和快速响应方案。 方法：提出PumpSense，引入消息级标注数据和实时检测+目标提取方法。
- [#133] **Quantum-Inspired Variational Kernel for Energy Forecasting** — 量子启发变分核跨区域能源预测 TL;DR: 问题：太阳能/风能预测通常只在单一气候区调优和评估。 方法：提出量子启发变分核+可解释AI的四阶段混合框架，实现跨区域能源预测。
- [#172] **Breast Cancer Radiation Side Effects** — LLM 识别乳腺癌放射治疗副作用 TL;DR: 问题：癌症治疗副作用的临床知识碎片化且不完整，LLM能否准确识别尚不清楚。 方法：评估LLM识别乳腺癌放射治疗副作用的能力。
- [#173] **Magis-Bench: Magistrate-Level Legal Tasks** — 法官级法律任务 LLM 评估基准 TL;DR: 问题：法律AI基准只评估争辩/文档生成，忽略了评判能力。 方法：构建Magis-Bench，评估LLM的法官级法律任务能力（权衡主张、适用法律、输出判决）。
- [#189] **SLIM: Molecular Editing via Sparse Latent Steering** — 稀疏潜在操控实现 LLM 分子编辑 TL;DR: 问题：LLM分子编辑中属性信息隐式纠缠在致密隐藏状态中，无法显式控制。 方法：提出SLIM，稀疏潜在操控实现可解释、属性导向的分子编辑。
- [#230] **Conversational Medical AI with Eyes, Ears, Voice** — 多模态会话式 AI 临床助手 TL;DR: 问题：医疗实践不仅依赖对话，还需要视听线索的细致交换。 方法：基于Gemini的连续音视频流处理，构建AI联合临床医生系统。
- [#254] **ShifaMind: Interpretable ICD-10 Coding** — 可解释 ICD-10 编码乘法概念瓶颈 TL;DR: 问题：ICD-10自动编码需兼顾长尾多标签分类准确率和可解释性，概念瓶颈模型压缩丰富临床信息导致精度损失。 方法：提出乘法概念瓶颈，保留更多临床信息同时保持可解释性。
- [#255] **Crisis Data Classification** — LLM 引导半监督社交媒体危机数据分类 TL;DR: 问题：危机相关推文分类缺少标注数据。 方法：首次评估LLM引导的半监督学习方法用于社交媒体危机数据分类。
- [#265] **LLMs for Algorithmic Theoretical Physics** — LLM+计算代数系统用于理论物理算法计算 TL;DR: 问题：理论物理算法计算耗时且有微妙之处，LLM能否辅助。 方法：研究LLM+计算机代数系统用于理论物理算法计算。

## 十三、偏好对齐（7篇）

- [#6] **DGPO: Directional Consistent Groupwise Optimization** — 方向一致性群组偏好优化 TL;DR: 问题：现有偏好优化方法难以在对齐方向一致性的同时保持推理多样性。 方法：提出DGPO，将正反向问答实例组织为结构化集合，用基于边距的似然目标分离一致与不一致推理路径，实现跨数据集平均3.6%精度提升。
- [#33] **Aligning LLM Uncertainty with Human Disagreement** — 不确定性对齐人类分歧的 DPUA 框架 TL;DR: 问题：主观性分析中聚合标签压缩了人类判断变异，导致低一致性样本上过度自信预测。 方法：提出不确定性感知主观性分析框架DPUA，让模型在预测时表达不确定性，与人类分歧对齐。
- [#60] **Personalizing with Binary Feedback** — 二值反馈偏好对齐优化 TL;DR: 问题：LLM个性化忽视用户间差异，仅关注孤立用户历史。 方法：提出C-BPO框架，将目标用户数据视为正反馈、其他用户数据视为隐含负信号，通过偏好校正二值信号实现个性化。
- [#72] **TPAW: Team-Based Self-Play with Dual Weighting** — 双自适应权重组队自博弈对齐 TL;DR: 问题：自训练方法对合成数据质量敏感，且迭代训练中正负响应差距缩小导致优化无效。 方法：提出TPAW，组队自博弈加双自适应权重（样本权重+奖励权重），避免偏差放大和优化退化。
- [#218] **EvoPref: Multi-Objective Evolutionary LLM Alignment** — 多目标进化优化发现多样 LLM 对齐 TL;DR: 问题：梯度偏好优化导致偏好坍缩，收敛到狭窄行为模式。 方法：提出EvoPref，多目标进化算法维护LoRA适配器种群，在有用性、无害性、诚实性上联合优化。
- [#237] **Personalized Alignment Revisited** — 个性化对齐中用户多样性的必要与充分条件 TL;DR: 问题：个性化对齐的最优理论条件未形式化。 方法：证明用户多样性是个性化对齐达到O(1)在线遗憾和对数样本复杂度的必要充分条件。
- [#258] **RL for Scalable and Trustworthy Intelligent Systems** — 可信偏好对齐与隐私感知（学位论文） TL;DR: 问题：RL实用部署面临分布式扩展效率低和信任保证两大挑战。 方法：学位论文，提出可信偏好对齐和隐私感知的RL方法。

## 十四、对话系统（5篇）

- [#36] **Personal Facts in Dialogue** — 对话中个人事实标注方案与分类器 TL;DR: 问题：个性化对话系统缺少完善的个人事实分类方案。 方法：提出扩展标注方案，新增人口统计、拥有物等类别和持续时间、有效性等属性，支持结构化存储和对话续接识别。
- [#47] **User-Stream Routing in Full-Duplex Dialogue** — 全双工对话中用户流路由策略 TL;DR: 问题：全双工对话需要LLM在生成回应时同时听用户输入，但LLM不支持输入中途插入。 方法：研究用户流如何路由到LLM（插入、中断等），在文本全双工框架上系统评估不同路由策略。
- [#76] **Utility of User Simulators for Collaborative LLM Assistants** — 协作型 LLM 助手用户模拟器效用评估 TL;DR: 问题：用户模拟器质量如何衡量尚无定论。 方法：提出以下游效用量化模拟器质量——用该模拟器训练的助手与真实人类交互时的表现，作为模拟器质量度量。
- [#114] **Context Switching in Multi-Turn Dialogue** — 多轮对话中 LLM 上下文切换挑战 TL;DR: 问题：LLM在多轮对话中错过话题转换，携带不相关上下文。 方法：压力测试LLM多轮理解，研究生成式/话题切换检测和相关上下文筛选两个子任务。
- [#182] **SalesSim: Retail User Simulators** — 零售场景多模态用户模拟器对齐与评估 TL;DR: 问题：用户模拟器质量如何衡量。 方法：提出SalesSim，评估MLLM模拟多轮多模态零售对话中人格驱动客户行为的能力。

## 十五、知识图谱（4篇）

- [#38] **Extending Text2Cypher with Grammar and Schema Filtering** — 语法和模式感知的 Text2Cypher 扩展 TL;DR: 问题：Text2Cypher方法缺少对语法有效性和模式一致性的显式约束，影响可靠性。 方法：扩展基于置信度的方法，加入语法和模式感知过滤，确保生成的Cypher查询结构正确。
- [#83] **K12-KGraph: Curriculum-Aligned Knowledge Graph** — 课程对齐知识图谱用于教育评估 TL;DR: 问题：教育LLM评估偏重事实回忆，忽略课程认知（知识结构、先修链等）。 方法：构建K12-KGraph课程对齐知识图谱，涵盖先修链、概念分类和实验-概念链接。
- [#201] **Toward Multi-Database Query Reasoning for Text2Cypher** — 多数据库查询推理路线图 TL;DR: 问题：现有Text2Cypher假设单一预选数据库，不支持多数据库查询推理。 方法：提出多数据库Text2Cypher查询推理路线图。
- [#234] **Open Ontologies: Tool-Augmented Ontology Engineering** — 工具增强本体工程与稳定匹配对齐 TL;DR: 问题：本体工程缺乏LLM驱动与形式推理的集成。 方法：提出Open Ontologies，Rust实现的开源系统，集成LLM本体构建、OWL推理和MCP本体对齐，稳定匹配F1达0.832。

## 十六、自演化与开放式学习（4篇）

- [#3] **RubricEM: Meta-RL with Rubric-guided Decomposition** — 评分标准引导的策略分解元强化学习用于研究智能体 TL;DR: 问题：深度研究智能体的输出缺乏标准答案，长轨迹跨多步决策难以获得可验证奖励。 方法：提出RubricEM，用评分标准（rubric）作为策略执行、评判反馈和记忆的共享接口，结合阶段感知策略分解和反思元策略进化，8B模型接近专有系统水平。
- [#210] **G-Zero: Self-Play from Zero Data** — 无验证器零数据自演化框架 TL;DR: 问题：开放任务中自演化LLM依赖LLM评审导致能力瓶颈和奖励黑客。 方法：提出G-Zero，无需验证器的协同演化框架，用Hint-δ内在奖励量化预测偏移。
- [#228] **Self-Evolving Agents Capability Erosion** — 自演化智能体中能力退化与保持 TL;DR: 问题：自演化智能体适应新任务时会逐渐丧失先前能力。 方法：识别能力退化的主要通道，提出保持策略。
- [#248] **RewardHarness: Self-Evolving Agentic Post-Training** — 自演化智能体后训练奖励框架 TL;DR: 问题：图像编辑奖励模型依赖大规模偏好标注和数据效率低。 方法：提出RewardHarness，自演化智能体奖励框架，从少量示例推断评估标准。

## 十七、语音与音频（3篇）

- [#19] **Responsible Benchmarking of ASR Fairness** — ASR 公平性基准最佳实践 TL;DR: 问题：ASR公平性基准测试方法不一致，影响结果可靠性。 方法：综合ML公平性、社会科学和语音科学文献，提出ASR公平性基准最佳实践，涵盖假设定义、群体划分、指标选择等。
- [#90] **Towards Compact Sign Language Translation** — 紧凑手语翻译的帧率与模型大小权衡 TL;DR: 问题：手语翻译依赖大型编码器-解码器模型，限制部署。 方法：提出77M参数紧凑流水线，用MMPose骨骼姿态提取+单层线性投影到T5-small，研究帧率和模型大小权衡。
- [#243] **Communicating Sound Through Natural Language (LAC)** — 自然语言词汇声学编码传输声音 TL;DR: 问题：自然语言很少作为音频本身的传输载体。 方法：提出词汇声学编码(LAC)，LLM发送和接收智能体通过自然语言传输声音。

## 十八、代码生成与程序推理（4篇）

- [#226] **PDE-Grounded Intent Verification** — PDE 意图验证用于 LLM 生成仿真代码 TL;DR: 问题：LLM生成的模拟代码能运行但物理方程可能与意图不匹配。 方法：提出PDE意图验证，检测生成代码与用户物理意图之间的理解-生成鸿沟。
- [#233] **Agentic MIP Research** — LLM 智能体自动生成 MIP 求解器约束处理器 TL;DR: 问题：MIP研究算法验证需要大量实现、调试和基准测试。 方法：提出智能体MIP研究框架，LLM智能体嵌入求解器感知的硬编码循环，加速约束处理器生成。

## 十九、数据选择与训练动态（3篇）

- [#220] **Learning Multi-Indicator Weights for Data Selection** — 联合任务-模型自适应数据选择权重学习 TL;DR: 问题：数据选择依赖静态任务无关权重，不够灵活。 方法：提出联合任务-模型自适应框架，用高效代理学习多指标权重。
- [#223] **Let the Target Select for Itself** — 验证引导路径实现目标对齐数据选择 TL;DR: 问题：目标数据选择中，异构候选池的参考轨迹可能与目标不对齐。 方法：提出验证引导路径，让目标任务自身选择训练数据。

## 二十、通信与智能体理论（2篇）

- [#236] **Communication-Theoretic Framework for LLM Agents** — LLM 智能体可靠性技术的通信理论统一框架 TL;DR: 问题：LLM智能体的可靠性技术（重试、多数投票等）缺乏统一分析框架。 方法：用香农编码理论将LLM建模为离散随机信道，提出成本感知自适应可靠性框架。
- [#198] **Collective Alignment via Statistical Physics** — 统计物理框架解耦多智能体偏见与合作 TL;DR: 问题：多智能体LLM系统中社会从众和内在偏差的集体行为未解耦。 方法：用统计物理方法在2D格子上解耦从众和偏差，计算临界指数和相变。

## 二十一、立场论文（3篇）

- [#73] **Denominator Gaming in Academic Conferences** — 学术会议面临分母博弈的立场论文 TL;DR: 问题：顶级AI会议维持稳定录取率+投稿指数增长的结构性漏洞，恶意者可用AI大量提交低质论文稀释录取率。 方法：立场论文，分析"智能体分母博弈"威胁并提出潜在缓解策略。
- [#225] **Avoid Overstretching LLMs for Every Enterprise Task** — 企业任务不应过度依赖 LLM 的立场论文 TL;DR: 问题：企业任务多为确定性、结构化的，用LLM处理效率低且不可靠。 方法：立场论文，主张AI系统应根据任务结构选择合适技术，不应过度依赖LLM。
- [#240] **ML Research Has Outpaced Its Communication Norms** — 机器学习研究已超越其传播规范的立场论文 TL;DR: 问题：ML研究指数增长但交流规范未跟上，论文可读性下降。 方法：立场论文，分析2.8M arXiv论文的可读性趋势，呼吁NeurIPS采纳可衡量的写作标准。

## 二十二、模型编辑（1篇）

- [#112] **BetaEdit: Null-Space Constrained Sequential Editing** — 零空间约束的顺序模型编辑 TL;DR: 问题：零空间模型编辑依赖近似零空间导致知识泄漏，顺序编辑时性能严重退化。 方法：提出BetaEdit，改进零空间约束的顺序编辑，减少知识泄漏和性能退化。

## 二十三、情感、立场与偏见检测（3篇）

- [#45] **Editorial Intervention on Detecting Native Language Traces** — 编辑干预对母语痕迹检测的影响 TL;DR: 问题：人机协作写作中LLM改写会改变非母语文本的语言特征，影响母语识别。 方法：处理450K+文本的多个编辑干预程度，研究L1痕迹的鲁棒性。
- [#75] **Sentiment Analysis with Symptom Distress** — 情感分析与症状困扰关联研究（同时归入领域应用） TL;DR: 问题：基于Transformer的情感分析在心理治疗中的独立心理测量价值未被研究。 方法：评估情感分析作为症状困扰和恶化独立指标的有效性。
- [#101] **FinMoji** — 金融表情符号情感分析（同时归入领域应用） TL;DR: 问题：金融社交媒体中表情符号是否能作为投资者情绪的可靠代理尚不确定。 方法：提出FinMoji，研究表情符号在金融情感分析中的独立和组合效用。

## 二十四、幻觉检测与校准（5篇）

- [#143] **Max-pooling MIL Hallucination Detection** — 最大池化多实例学习检测幻觉 TL;DR: 问题：MIL幻觉检测方法计算开销大（需重复采样）。 方法：重新分析最大池化在MIL幻觉检测中的作用，简化方法减少采样开销。
- [#162] **CiteTracer: Citation Hallucination Detection** — 多智能体引用幻觉检测 TL;DR: 问题：LLM引文幻觉检测依赖简单的找到/未找到判断，缺乏领域级信号。 方法：提出CiteTracer多智能体框架，重构引文验证为来源检索和归因验证两阶段。
- [#170] **Benchmarks Underestimate LLM Hallucination Detection** — LLM 幻觉检测基准低估模型性能 TL;DR: 问题：幻觉检测基准中人类标注可能系统性低估模型。 方法：用LLM预测+人类仲裁重评估，三协议一致率提高6-7%，模型准确率也提升，说明单次标注不足。
- [#174] **Sem-ECE: Semantic Calibration for Open-Ended QA** — 开放问答的语义采样校准评估 TL;DR: 问题：开放问答中LLM校准评估方法不成熟，现有方法依赖限定答案集。 方法：提出语义采样框架Sem-ECE，在开放问答中评估校准。
- [#181] **Sanity Checks for Long-Form Hallucination Detection** — 长文本幻觉检测中的格式混淆因子 TL;DR: 问题：长文本幻觉检测方法是否评估推理本身还是利用最终答案的表面相关。 方法：引入受控不变性方法，Force和Rerun两个oracle测试区分评估对象。

## 二十五、鲁棒性与对抗（3篇）

- [#140] **FragileFlow: Spectral Control of Correct-but-Fragile Predictions** — 正确但脆弱预测的光谱控制正则化 TL;DR: 问题：LLM/VLM鲁棒性评估中平均指标掩盖了"正确但脆弱"的预测——概率质量已流向错误类别。 方法：提出FragileFlow，用光谱控制正则化纠正边界附近的概率流。
- [#231] **ROMA** — 视觉退化鲁棒多模态推理强化（同时归入多模态） TL;DR: 问题：MLLM推理策略在真实视觉退化（模糊、压缩、低分辨率）下脆弱。 方法：提出ROMA，强化多模态推理对视觉退化的鲁棒性。
- [#139] **SRA** — 语义表示攻击（同时归入安全与对齐） TL;DR: 问题：现有token级对抗优化依赖特定肯定模板，易遇瓶颈且视觉不可读。 方法：提出语义表示攻击，优化语义层面而非token层面，99.71%成功率跨26个LLM。

## 二十六、人类交互与社会计算（5篇）

- [#14] **Digital Personas Approximating Human Survey Findings** — 数字人格能否可靠近似人类调查结果 TL;DR: 问题：数字人格何时能可靠替代人类调查 respondent 尚不清晰。 方法：用LISS面板构建人格，用2023年前数据预测后续回答，发现人口统计+过去回答的人格表现最好，但所有架构在某些主题上系统性偏差。
- [#22] **VISTA: Generative Egocentric Video for Daily Assistance** — 日常辅助的生成式第一人称视频 TL;DR: 问题：训练日常辅助AI需要大规模视觉数据，但真实场景捕获困难、昂贵或不安全，物理模拟器缺乏视觉保真度。 方法：提出VISTA视频合成系统，生成高保真自我中心视频作为AI辅助训练和评估数据。
- [#197] **LLARS: Domain Expert & Developer Collaboration** — 领域专家与开发者协作的 LLM 平台 TL;DR: 问题：领域专家与开发者在构建LLM系统时协作困难。 方法：提出LLARS开源平台，集成协同prompt工程、批量生成和评估模块。
- [#229] **A Prompt-Aware Structuring Framework for AIGC** — AI 生成内容可靠复用的提示感知结构化框架 TL;DR: 问题：AI生成内容缺乏验证可靠性、可复现性和许可追踪的机制。 方法：提出prompt感知结构化框架，使AI生成内容可追踪和复用。
- [#242] **UserGPT** — 用户画像理解的 LLM 框架 TL;DR: 问题：传统用户画像依赖判别模型和手动特征工程，生成分散且不一致。 方法：研究生成式用户理解范式UserGPT。

---

## 热点趋势总结

1. **智能体系统持续火热**（18+篇）：从工具调用、多智能体协作到 GUI Agent，Agent 仍是 cs.CL 最活跃的方向
2. **LLM 训练优化**（27篇）：扩散语言模型、MoE 剪枝蒸馏、长上下文适配、记忆增强等基础训练方法仍是核心
3. **安全对齐**（20篇）：从越狱攻击、偏见审计到文化对齐、隐私保护，安全研究覆盖面广
4. **效率压缩**（17篇）：KV 缓存、推测解码、量化、剪枝——部署优化需求持续增长
5. **多模态**（18篇）：视觉语言、图表理解、视频推理等多模态方向论文量保持高位
6. **评估基准**（22篇）：新基准层出不穷，LLM-as-Judge 去偏、元认知校准等方法论反思增多
7. **可解释性/机制分析**（13篇）：涌现层、电路一致性、注意力学等 mechanistic interpretability 研究深入