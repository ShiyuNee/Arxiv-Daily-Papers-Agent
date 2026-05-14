# arXiv cs.CL 论文列表 — 2026-05-12

- **日期**: 2026-05-12
- **分类**: Computation and Language (cs.CL)
- **论文总数**: 270

---

## 1. ELF: Embedded Language Flows

**arXiv ID**: [2605.10938](https://arxiv.org/abs/2605.10938)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10938)

**作者**: Keya Hu, Linlu Qiu, Yiyang Lu, Hanhong Zhao, Tianhong Li 等 (共8人)

**分类**: Computation and Language, Artificial Intelligence, Machine Learning

**发布时间**: 2026-05-11 17:59:29 UTC

**摘要 (英文)**: Diffusion and flow-based models have become the de facto approaches for generating continuous data, e.g., in domains such as images and videos. Their success has attracted growing interest in applying them to language modeling. Unlike their image-domain counterparts, today's leading diffusion language models (DLMs) primarily operate over discrete tokens. In this paper, we show that continuous DLMs can be made effective with minimal adaptation to the discrete domain. We propose Embedded Language Flows (ELF), a class of diffusion models in continuous embedding space based on continuous-time Flow Matching. Unlike existing DLMs, ELF predominantly stays within the continuous embedding space until the final time step, where it maps to discrete tokens using a shared-weight network. This formulation makes it straightforward to adapt established techniques from image-domain diffusion models, e.g., classifier-free guidance (CFG). Experiments show that ELF substantially outperforms leading discrete and continuous DLMs, achieving better generation quality with fewer sampling steps. These results suggest that ELF offers a promising path toward effective continuous DLMs.

**摘要 (中文)**: 扩散和基于流的模型已成为生成连续数据（如图像和视频领域）的事实标准方法。其成功吸引了越来越多人将其应用于语言建模。与图像领域的对应物不同，当今领先的扩散语言模型（DLM）主要在离散token上操作。本文表明，连续DLM只需对离散域做最小适配即可变得高效。我们提出嵌入式语言流（ELF），一类基于连续时间Flow Matching的连续嵌入空间扩散模型。与现有DLM不同，ELF在最终时间步之前主要停留在连续嵌入空间中，在那里通过共享权重网络映射到离散token。该公式使得适配图像域扩散模型的成熟技术（如无分类器引导CFG）变得直接。实验表明，ELF大幅超越领先的离散和连续DLM，在更少采样步数下实现更优生成质量。这些结果表明ELF为有效的连续DLM提供了一条有前景的路径。

---

## 2. WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation

**arXiv ID**: [2605.10912](https://arxiv.org/abs/2605.10912)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10912)

**作者**: Shuangrui Ding, Xuanlang Dai, Long Xing, Shengyuan Ding, Ziyu Liu 等 (共17人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 17:49:43 UTC

**摘要 (英文)**: Large language and vision-language models increasingly power agents that act on a user's behalf through command-line interface (CLI) harnesses. However, most agent benchmarks still rely on synthetic sandboxes, short-horizon tasks, mock-service APIs, and final-answer checks, leaving open whether agents can complete realistic long-horizon work in the runtimes where they are deployed. This work presents WildClawBench, a native-runtime benchmark of 60 human-authored, bilingual, multimodal tasks spanning six thematic categories. Each task averages roughly 8 minutes of wall-clock time and over 20 tool calls, and runs inside a reproducible Docker container hosting an actual CLI agent harness (OpenClaw, Claude Code, Codex, or Hermes Agent) with access to real tools rather than mock services. Grading is hybrid, combining deterministic rule-based checks, environment-state auditing of side effects, and an LLM/VLM judge for semantic verification. Across 19 frontier models, the best, Claude Opus 4.7, reaches only 62.2% overall under OpenClaw, while every other model stays below 60%, and switching harness alone shifts a single model by up to 18 points. These results show that long-horizon, native-runtime agent evaluation remains a far-from-resolved task for current frontier models. We release the tasks, code, and containerized tooling to support reproducible evaluation.

**摘要 (中文)**: 大语言模型和视觉语言模型越来越多地通过命令行界面（CLI）驱动代理为用户执行操作。然而，大多数代理基准仍依赖合成沙箱、短时任务、模拟服务API和最终答案检查，无法验证代理是否能在实际部署的运行时中完成真实的长时任务。本文提出WildClawBench，一个由60个人工撰写的双语多模态任务组成的原生运行时基准，涵盖六个主题类别。每个任务平均约8分钟实际时间和超过20次工具调用，在可复现的Docker容器内运行，托管实际CLI代理框架（OpenClaw、Claude Code、Codex或Hermes Agent），可访问真实工具而非模拟服务。评分采用混合方式，结合确定性规则检查、环境状态审计和LLM/VLM语义验证。在19个前沿模型中，最好的Claude Opus 4.7在OpenClaw下仅达62.2%，其他所有模型均低于60%，仅切换框架就可使单个模型性能变化高达18个百分点。这些结果表明，长时原生运行时代理评估对当前前沿模型仍是一个远未解决的问题。

---

## 3. RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards

**arXiv ID**: [2605.10899](https://arxiv.org/abs/2605.10899)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10899)

**作者**: Gaotang Li, Bhavana Dalvi Mishra, Zifeng Wang, Jun Yan, Yanfei Chen 等 (共12人)

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-11 17:40:38 UTC

**摘要 (英文)**: Training deep research agents, namely systems that plan, search, evaluate evidence, and synthesize long-form reports, pushes reinforcement learning beyond the regime of verifiable rewards. Their outputs lack ground-truth answers, their trajectories span many tool-augmented decisions, and standard post-training offers little mechanism for turning past attempts into reusable experience. In this work, we argue that rubrics should serve not merely as final-answer evaluators, but as the shared interface that structures policy execution, judge feedback, and agent memory. Based on this view, we introduce RubricEM, a rubric-guided reinforcement learning framework that combines stagewise policy decomposition with reflection-based meta-policy evolution. RubricEM first makes research trajectories stage-aware by conditioning planning, evidence gathering, review, and synthesis on self-generated rubrics. It then assigns credit with Stage-Structured GRPO, which uses stagewise rubric judgments to provide denser semantic feedback for long-horizon optimization. In parallel, RubricEM trains a shared-backbone reflection meta-policy that distills judged trajectories into reusable rubric-grounded guidance for future attempts. The resulting RubricEM-8B achieves strong performance across four long-form research benchmarks, outperforming comparable open models and approaching proprietary deep-research systems. Beyond final performance, we perform thorough analyses to understand the key ingredients of RubricEM.

**摘要 (中文)**: 训练深度研究智能体——即规划、搜索、评估证据并综合长篇报告的系统——将强化学习推向了可验证奖励之外的领域。其输出缺乏标准答案，轨迹跨越多个工具增强决策，标准后训练几乎无法将过往尝试转化为可复用经验。本文认为评分标准（rubrics）不应仅作为最终答案评估器，而应作为结构化策略执行、评审反馈和智能体记忆的共享接口。基于此观点，我们提出RubricEM，一个评分标准引导的强化学习框架，结合阶段性策略分解与基于反思的元策略演化。RubricEM首先通过将规划、证据收集、审查和综合条件化于自生成评分标准，使研究轨迹具备阶段感知。然后使用阶段结构化GRPO分配信用，利用阶段性评分标准判断为长时优化提供更密集的语义反馈。同时，RubricEM训练共享骨干的反思元策略，将已评判的轨迹蒸馏为可复用的评分标准指导以供未来尝试。最终RubricEM-8B在四个长篇研究基准上取得强劲表现，超越可比开源模型并接近专有深度研究系统。

---

## 4. Grounded or Guessing? LVLM Confidence Estimation via Blind-Image Contrastive Ranking

**arXiv ID**: [2605.10893](https://arxiv.org/abs/2605.10893)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10893)

**作者**: Reza Khanmohammadi, Erfan Miahi, Simerjot Kaur, Charese H. Smiley, Ivan Brugere 等 (共7人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 17:35:10 UTC

**摘要 (英文)**: Large vision-language models suffer from visual ungroundedness: they can produce a fluent, confident, and even correct response driven entirely by language priors, with the image contributing nothing to the prediction. Existing confidence estimation methods cannot detect this, as they observe model behavior under normal inference with no mechanism to determine whether a prediction was shaped by the image or by text alone. We introduce BICR (Blind-Image Contrastive Ranking), a model-agnostic confidence estimation framework that makes this contrast explicit during training by extracting hidden states from a frozen LVLM twice: once with the real image-question pair, and once with the image blacked out while the question is held fixed. A lightweight probe is trained on the real-image hidden state and regularized by a ranking loss that penalizes higher confidence on the blacked-out view, teaching it to treat visual grounding as a signal of reliability at zero additional inference cost. Evaluated across five modern LVLMs and seven baselines on a benchmark covering visual question answering, object hallucination detection, medical imaging, and financial document understanding, BICR achieves the best cross-LVLM average on both calibration and discrimination simultaneously, with statistically significant discrimination gains robust to cluster-aware analysis at 4-18x fewer parameters than the strongest probing baseline.

**摘要 (中文)**: 大型视觉语言模型存在视觉不接地问题：它们可以完全由语言先验驱动产生流畅、自信甚至正确的回复，而图像对预测没有任何贡献。现有置信度估计方法无法检测这一问题，因为它们在正常推理下观察模型行为，没有机制判断预测是由图像还是仅由文本塑造。我们提出BICR（盲图像对比排序），一个模型无关的置信度估计框架，训练时通过从冻结LVLM中提取两次隐藏状态来使对比显式化：一次使用真实图像-问题对，一次将图像设为黑色而问题不变。在真实图像隐藏状态上训练轻量探针，通过排序损失正则化惩罚对黑屏视图赋予更高置信度，使其学会将视觉接地视为可靠性信号，且推理零额外代价。在5个现代LVLM和7个基线上的评估表明，BICR在校准和判别力上同时取得最佳跨LVLM平均值，统计显著的判别增益在集群感知分析下稳健，参数量比最强探针基线少4-18倍。

---

## 5. Neural at ArchEHR-QA 2026: One Method Fits All: Unified Prompt Optimization for Clinical QA over EHRs

**arXiv ID**: [2605.10877](https://arxiv.org/abs/2605.10877)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10877)

**作者**: Abrar Majeedi, Viswanatha Reddy Gajjala, Sai Prasanna Teja Reddy Bogireddy, Siddhant Rai

**分类**: Computation and Language, Information Retrieval

**发布时间**: 2026-05-11 17:27:30 UTC

**摘要 (英文)**: Automated question answering (QA) over electronic health records (EHRs) demands precise evidence retrieval, faithful answer generation, and explicit grounding of answers in clinical notes. In this work, we present Neural1.5, our method for the ArchEHR-QA 2026 shared task at CL4Health@LREC 2026, which comprises four subtasks: question interpretation, evidence identification, answer generation, and evidence alignment. Our approach decouples the task into independent, modular stages and employs DSPy"s MIPROv2 optimizer to automatically discover high-performing prompts, jointly tuning instructions and few-shot demonstrations for each stage. Within every stage, self-consistency voting over multiple stochastic inference runs suppresses spurious errors and improves reliability, while stage-specific verification mechanisms (e.g., self-reflection and chain-of-verification for alignment) further refine output quality. Among all teams that participated in all four subtasks, our method ranks second overall (mean rank 4.00), placing 4th, 1st, 4th, and 7th on Subtasks 1-4, respectively. These results demonstrate that systematic, per-stage prompt optimization combined with self-consistency mechanisms is a cost-effective alternative to model fine-tuning for multifaceted clinical QA.

**摘要 (中文)**: 电子健康记录（EHR）上的自动问答需要精确的证据检索、忠实的答案生成以及答案在临床笔记中的显式接地。本文介绍Neural1.5，我们为ArchEHR-QA 2026共享任务（CL4Health@LREC 2026）提出的方法，包含四个子任务：问题解读、证据识别、答案生成和证据对齐。我们的方法将任务解耦为独立模块化阶段，使用DSPy的MIPROv2优化器自动发现高性能提示，联合调优每个阶段的指令和少样本演示。在每个阶段内，多次随机推理运行的自一致性投票抑制虚假错误以提高可靠性，阶段特定的验证机制（如对齐的自我反思和验证链）进一步精化输出质量。在参与全部四个子任务的所有团队中，我们方法总体排名第二（平均排名4.00），子任务1-4分别排名4、1、4、7。这些结果表明系统化的逐阶段提示优化结合自一致性机制是多功能临床QA中模型微调的经济替代方案。

---

## 6. DGPO: Beyond Pairwise Preferences with Directional Consistent Groupwise Optimization

**arXiv ID**: [2605.10863](https://arxiv.org/abs/2605.10863)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10863)

**作者**: Mengyi Deng, Zhiwei Li, Xin Li, Tingyu Zhu, Yulan Yuan 等 (共7人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 17:10:44 UTC

**摘要 (英文)**: Although Large Language Models (LLMs) have made remarkable progress, current preference optimization methods still struggle to align directional consistency while preserving reasoning diversity. To address this limitation, we propose Directional-Groupwise Preference Optimization (DGPO), a lightweight framework that aggregates supervision signals at the group level and explicitly models direction-aware alignment through multi-candidate comparisons. DGPO organizes forward and reverse question-answer instances into structured sets and optimizes a margin-based likelihood objective that separates coherent reasoning paths from inconsistent alternatives. This group-wise formulation captures richer relative information than pairwise objectives and reinforces consistency across diverse reasoning pathways. Empirical results show that our constructed reverse data yields a 3.2% average improvement across five benchmarks, while DGPO further delivers consistent gains across multiple datasets and model families, achieving average accuracy improvements of up to 3.6%.

**摘要 (中文)**: 尽管大语言模型取得了显著进展，当前偏好优化方法在对齐方向一致性的同时保持推理多样性方面仍面临困难。为解决此局限，我们提出方向群组偏好优化（DGPO），一个轻量级框架，在群组层面聚合监督信号并通过多候选比较显式建模方向感知对齐。DGPO将正向和反向问答实例组织为结构化集合，优化基于边距的似然目标，将连贯推理路径与不一致替代方案分离。这种群组化公式比成对目标捕获更丰富的相对信息，并强化跨多样推理路径的一致性。实验结果表明，我们构建的反向数据在五个基准上带来3.2%的平均提升，而DGPO在多个数据集和模型家族上进一步带来一致增益，平均准确率提升高达3.6%。

---

## 7. RUBEN: Rule-Based Explanations for Retrieval-Augmented LLM Systems

**arXiv ID**: [2605.10862](https://arxiv.org/abs/2605.10862)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10862)

**作者**: Joel Rorseth, Parke Godfrey, Lukasz Golab, Divesh Srivastava, Jarek Szlichta

**分类**: Computation and Language

**发布时间**: 2026-05-11 17:10:35 UTC

**摘要 (英文)**: This paper demonstrates RUBEN, an interactive tool for discovering minimal rules to explain the outputs of retrieval-augmented large language models (LLMs) in data-driven applications. We leverage novel pruning strategies to efficiently identify a minimal set of rules that subsume all others. We further demonstrate novel applications of these rules for LLM safety, specifically to test the resiliency of safety training and effectiveness of adversarial prompt injections.

**摘要 (中文)**: 本文展示RUBEN，一个交互式工具，用于发现最小规则集来解释数据驱动应用中检索增强大语言模型的输出。我们利用新颖的剪枝策略高效识别涵盖所有其他规则的最小规则集。我们进一步展示了这些规则在LLM安全方面的应用，具体用于测试安全训练的鲁棒性和对抗提示注入的有效性。

---

## 8. Learning More from Less: Exploiting Counterfactuals for Data-Efficient Chart Understanding

**arXiv ID**: [2605.10855](https://arxiv.org/abs/2605.10855)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10855)

**作者**: Jianzhu Bao, Haozhen Zhang, Kuicai Dong, Bozhi Wu, Sarthak Ketanbhai Modi 等 (共8人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 17:02:09 UTC

**摘要 (英文)**: Vision-Language Models (VLMs) have demonstrated remarkable progress in chart understanding, largely driven by supervised fine-tuning (SFT) on increasingly large synthetic datasets. However, scaling SFT data alone is inefficient and overlooks a key property of charts: charts are programmatically generated visual artifacts, where small, code-controlled visual changes can induce drastic shifts in semantics and correct answers. Learning this counterfactual sensitivity requires VLMs to discriminate fine-grained visual differences, yet standard SFT treats training instances independently and provides limited supervision to enforce this behavior. To address this, we introduce ChartCF, a data-efficient training framework designed to enhance counterfactual sensitivity. ChartCF consists of: (1) a counterfactual data synthesis pipeline via code modification, (2) a chart similarity-based data selection strategy that filters overly difficult samples for improved training efficiency, and (3) multimodal preference optimization across both textual and visual modalities. Experiments on five benchmarks show that ChartCF achieves superior or comparable performance to strong chart-specific VLMs while using significantly less training data.

**摘要 (中文)**: 视觉语言模型在图表理解方面取得了显著进展，主要驱动力是在日益庞大的合成数据集上进行监督微调。然而，单纯扩展SFT数据效率低下，且忽略了一个关键属性：图表是程序化生成的视觉制品，代码控制的微小视觉变化即可引起语义和正确答案的剧变。学习这种反事实敏感性需要VLM辨别细粒度视觉差异，但标准SFT独立处理训练实例，提供的监督不足以强化此行为。为此，我们提出ChartCF，一个旨在增强反事实敏感性的数据高效训练框架。ChartCF包含：(1) 通过代码修改的反事实数据合成流水线，(2) 基于图表相似度的数据选择策略过滤过于困难的样本以提高训练效率，(3) 跨文本和视觉模态的多模态偏好优化。在五个基准上的实验表明，ChartCF在使用显著更少训练数据的同时，达到或超越强图表专用VLM的性能。

---

## 9. Grounded Satirical Generation with RAG

**arXiv ID**: [2605.10853](https://arxiv.org/abs/2605.10853)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10853)

**作者**: Oona Itkonen, Yuxin Su, Linyao Du, Ona De Gibert

**分类**: Computation and Language

**发布时间**: 2026-05-11 17:00:51 UTC

**摘要 (英文)**: Humor generation remains challenging task for Large Language Models (LLMs), due to their subjective nature. We focus on satire, a form of humor strongly shaped by context. In this work, we present a novel pipeline for grounded satire generation that uses Retrieval-Augmented Generation (RAG) over current news to produce satirical dictionary definitions in the Finnish context. We also introduce a new task-specific evaluation framework and annotate 100 generated definitions with six human annotators, enabling analysis across multiple experimental conditions, including cultural background, source-word type, and the presence or absence of RAG. Our results show that the generated definitions are perceived as more political than humorous. Both topic-based word selection and RAG improve the political relevance of the outputs, but neither yields clear gains in humor generation. In addition, our LLM-as-a-judge evaluation of five state-of-the-art models indicates that LLMs correlate well with human judgments on political relevance, but perform poorly on humor. We release our code and annotated dataset to support further research on grounded satire generation and evaluation.

**摘要 (中文)**: 幽默生成仍是大语言模型面临的挑战性任务，因其主观性质。我们聚焦讽刺——一种高度依赖语境的幽默形式。本文提出一个基于检索增强生成（RAG）的接地讽刺生成流水线，利用当前新闻在芬兰语境中生成讽刺词典定义。我们还引入了新的任务特定评估框架，并让六位人工标注者标注100个生成定义，支持跨多种实验条件（文化背景、源词类型、RAG有无）的分析。结果显示生成的定义被认为更具政治性而非幽默性。基于主题的词选择和RAG均提高了输出的政治相关性，但在幽默生成方面均未带来明显增益。此外，我们对五个最先进模型的LLM评审评估表明，LLM在政治相关性上与人类判断相关性好，但在幽默方面表现很差。我们发布代码和标注数据集以支持接地讽刺生成和评估的进一步研究。

---

## 10. Training-Free Cultural Alignment of Large Language Models via Persona Disagreement

**arXiv ID**: [2605.10843](https://arxiv.org/abs/2605.10843)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10843)

**作者**: Huynh Trung Kiet, Dao Sy Duy Minh, Tuan Nguyen, Chi-Nguyen Tran, Phu-Hoa Pham 等 (共8人)

**分类**: Computation and Language, Artificial Intelligence, Computers and Society

**发布时间**: 2026-05-11 16:55:16 UTC

**摘要 (英文)**: Large language models increasingly mediate decisions that turn on moral judgement, yet a growing body of evidence shows that their implicit preferences are not culturally neutral. Existing cultural alignment methods either require per-country preference data and fine-tuning budgets or assume white-box access to model internals that commercial APIs do not expose. In this work, we focus on this realistic black-box, public-data-only regime and observe that within-country sociodemographic disagreement, not consensus, is the primary steering signal. We introduce DISCA (Disagreement-Informed Steering for Cultural Alignment), an inference-time method that instantiates each country as a panel of World-Values-Survey-grounded persona agents and converts their disagreement into a bounded, loss-averse logit correction. Across 20 countries and 7 open-weight backbones (2B--70B), DISCA reduces cultural misalignment on MultiTP by 10--24% on the six backbones >=3.8B, and 2--7% on open-ended scenarios, without changing any weights. Our results suggest that inference-time calibration is a scalable alternative to fine-tuning for serving the long tail of global moral preferences.

**摘要 (中文)**: 大语言模型越来越多地介入依赖道德判断的决策，但越来越多的证据表明其隐含偏好并非文化中立。现有文化对齐方法要么需要按国家的偏好数据和微调预算，要么假设对模型内部的白盒访问（商业API不提供）。本文聚焦于现实的无权重修改、仅公开数据场景，观察发现国家内部的社会人口分歧（而非共识）才是主要引导信号。我们提出DISCA（分歧引导的文化对齐引导），一种推理时方法，将每个国家实例化为基于世界价值观调查的角色代理面板，并将其分歧转化为有界损失厌恶的logit校正。在20个国家和7个开源骨干（2B-70B）上，DISCA在>=3.8B的六个骨干上将MultiTP上的文化失对齐降低10-24%，在开放场景上降低2-7%，无需改变任何权重。结果表明推理时校准是服务全球道德偏好长尾的可扩展替代方案。

---

## 11. Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents

**arXiv ID**: [2605.10832](https://arxiv.org/abs/2605.10832)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10832)

**作者**: Shijue Huang, Hangyu Guo, Chenxin Li, Junting Lu, Xinyu Geng 等 (共10人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 16:49:36 UTC

**摘要 (英文)**: Multimodal deep search requires an agent to solve open-world problems by chaining search, tool use, and visual reasoning over evolving textual and visual context. Two bottlenecks limit current systems. First, existing tool-use harnesses treat images returned by search, browsing, or transformation as transient outputs, so intermediate visual evidence cannot be re-consumed by later tools. Second, training data is usually built by fixed curation recipes that cannot track the target agent's evolving capability. To address these challenges, we first introduce a visual-native agent harness centered on an image bank reference protocol, which registers every tool-returned image as an addressable reference and makes intermediate visual evidence reusable by later tools. On top of this harness, On-policy Data Evolution (ODE) runs a closed-loop data generator that refines itself across rounds from rollouts of the policy being trained. This per-round refinement makes each round's data target what the current policy still needs to learn. The same framework supports both diverse supervised fine-tuning data and policy-aware reinforcement learning data curation, covering the full training lifecycle of the target agent. Across 8 multimodal deep search benchmarks, ODE improves the Qwen3-VL-8B agent from 24.9% to 39.0% on average, surpassing Gemini-2.5 Pro in standard agent-workflow setting (37.9%). At 30B, ODE raises the average score from 30.6% to 41.5%. Further analyses validate the effectiveness of image-bank reuse, especially on complex tasks requiring iterative visual refinement, while rollout-feedback evolution yields more grounded SFT traces and better policy-matched RL tasks than static synthesis.

**摘要 (中文)**: 多模态深度搜索要求智能体通过链式搜索、工具使用和视觉推理来解决开放世界问题。当前系统存在两个瓶颈：一是现有工具使用框架将搜索、浏览或变换返回的图像视为临时输出，中间视觉证据无法被后续工具重新消费；二是训练数据通常由固定配方构建，无法跟踪目标智能体不断演化的能力。为解决这些问题，我们首先引入以图像库引用协议为中心的视觉原生智能体框架，将每个工具返回的图像注册为可寻址引用，使中间视觉证据可被后续工具复用。在此框架之上，策略数据演化（ODE）运行闭环数据生成器，从被训练策略的 rollout 中跨轮自我精炼。这种逐轮精炼使每轮数据针对当前策略仍需学习的内容。同一框架支持多样监督微调数据和策略感知强化学习数据管理。在8个多模态深度搜索基准上，ODE将Qwen3-VL-8B智能体从24.9%提升至39.0%，超越标准工作流设置下的Gemini-2.5 Pro（37.9%）。在30B规模，ODE将平均分从30.6%提升至41.5%。

---

## 12. Why Low-Resource NLP Needs More Than Cross-Lingual Transfer: Lessons Learned from Luxembourgish

**arXiv ID**: [2605.10714](https://arxiv.org/abs/2605.10714)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10714)

**作者**: Fred Philippy, Siwen Guo, Jacques Klein, Tegawendé F. Bissyandé

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 15:24:33 UTC

**摘要 (英文)**: Cross-lingual transfer has become a central paradigm for extending natural language processing (NLP) technologies to low-resource languages. By leveraging supervision from high-resource languages, multilingual language models can achieve strong task performance with little or no labeled target-language data. However, it remains unclear to what extent cross-lingual transfer can substitute for language-specific efforts. In this paper, we synthesize prior research findings and data collection results on Luxembourgish, which, despite its typological proximity to high-resource languages and its presence in a multilingual context, remains insufficiently represented in modern NLP technologies. Across findings, we observe a fundamental interdependence between cross-lingual transfer and language-specific efforts. Cross-lingual transfer can substantially improve target-language performance, but its success depends critically on the availability of sufficiently high-quality, task-aligned target-language data. At the same time, such resources, particularly in low-resource settings, are typically too limited in scale to drive strong performance on their own. Instead, such resources reach their full potential only when leveraged within a cross-lingual framework. We therefore argue that cross-lingual transfer and language-specific efforts should not be viewed as competing alternatives. Instead, they function as complementary components of a sustainable low-resource NLP pipeline. Based on these insights, we provide practical guidelines for integrating and balancing cross-lingual transfer with language-specific development in sustainable low-resource NLP pipelines.

**摘要 (中文)**: 跨语言迁移已成为将自然语言处理技术扩展到低资源语言的核心范式。通过利用高资源语言的监督，多语言模型可以在很少或没有目标语言标注数据的情况下取得强烈的任务性能。然而，跨语言迁移在多大程度上可以替代语言特定努力尚不清楚。本文综合了卢森堡语的先前研究发现和数据收集结果——尽管其与高资源语言类型学接近且存在于多语言环境中，但在现代NLP技术中仍代表性不足。研究发现跨语言迁移与语言特定努力之间存在根本的相互依赖：跨语言迁移可以大幅提升目标语言性能，但其成功关键取决于足够高质量、任务对齐的目标语言数据的可用性；同时，这些资源在低资源场景下通常规模太小，无法独自驱动强劲性能，只有当在跨语言框架内利用时才能发挥全部潜力。因此我们认为跨语言迁移和语言特定努力不应被视为竞争替代方案，而是可持续低资源NLP流水线的互补组成部分，并提供了实践指导。

---

## 13. Prompt-Activation Duality: Improving Activation Steering via Attention-Level Interventions

**arXiv ID**: [2605.10664](https://arxiv.org/abs/2605.10664)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10664)

**作者**: Diancheng Kang, Zheyuan Liu, Ningshan Ma, Yue Huang, Zhaoxuan Tan 等 (共6人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 14:44:32 UTC

**摘要 (英文)**: Activation steering controls language model behavior by adding directions to internal representations at inference time, but standard residual-stream steering can fail in stateful dialogue. We identify KV-cache contamination as a key failure mode: steered token states are stored and repeatedly reused, turning a local perturbation into cumulative coherence degradation. To address this challenge, we propose Gated Cropped Attention-Delta steering (GCAD), which extracts steering signals from system-prompt contributions to self-attention and applies them with token-level gating. Across persona-steering experiments, GCAD preserves trait control while substantially improving long-horizon coherence. On the main multi-turn benchmark, GCAD improves average coherence drift from -18.6 to -1.9 and raises turn-10 trait expression from 78.0 to 93.1. These results suggest that activation steering becomes more reliable when interventions follow the prompt-mediated pathways that models already use for behavioral control.

**摘要 (中文)**: 激活引导通过在推理时向内部表示添加方向来控制语言模型行为，但标准残差流引导在有状态对话中可能失效。我们识别出KV-cache污染是关键失败模式：被引导的token状态被存储并反复重用，将局部扰动转化为累积的连贯性退化。为解决这一问题，我们提出Gated Cropped Attention-Delta引导（GCAD），从系统提示对自注意力的贡献中提取引导信号，并以token级门控方式应用。在人格引导实验中，GCAD在保持特质控制的同时显著提升了长期连贯性。在主要多轮基准上，GCAD将平均连贯性漂移从-18.6改善至-1.9，并将第10轮特质表达从78.0提升至93.1。这些结果表明，当干预遵循模型已用于行为控制的提示中介路径时，激活引导变得更加可靠。

---

## 14. When Can Digital Personas Reliably Approximate Human Survey Findings?

**arXiv ID**: [2605.10659](https://arxiv.org/abs/2605.10659)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10659)

**作者**: Mumin Jia, Yilin Chen, Divya Sharma, Jairo Diaz-Rodriguez

**分类**: Computation and Language, Artificial Intelligence, Social and Information Networks, Machine Learning

**发布时间**: 2026-05-11 14:41:11 UTC

**摘要 (英文)**: Digital personas powered by Large Language Models (LLMs) are increasingly proposed as substitutes for human survey respondents, yet it remains unclear when they can reliably approximate human survey findings. We answer this question using the LISS panel, constructing personas from respondents' background variables and pre-2023 survey histories, then testing them against the same respondents' held-out post-cutoff answers. Across four persona architectures, three LLMs, and two prediction tasks, we assess performance at the question, respondent, distributional, equity, and clustering levels. Digital personas improve alignment with human response distributions, especially in domains tied to stable attributes and values, but remain limited for individual prediction and fail to recover multivariate respondent structure. Retrieval-augmented architectures provide the clearest gains, but performance depends more on human response structure than on model choice: personas perform best for low-variability questions and common respondent patterns, and worst for subjective, heterogeneous, or rare responses. Our results provide practical guidance on when digital personas could be appropriate for survey research and when human validation remains necessary.

**摘要 (中文)**: 由大语言模型（LLM）驱动的数字人格越来越多地被提议作为人类调查受访者的替代，但它们何时能可靠地近似人类调查结果仍不清楚。我们利用LISS面板回答这一问题，从受访者的背景变量和2023年之前的调查历史构建数字人格，然后将其与同一受访者保留截止日期后的回答进行对照测试。在四种人格架构、三个LLM和两个预测任务上，我们在问题级、受访者级、分布级、公平级和聚类级评估性能。数字人格改善了与人类回答分布的对齐，特别是在与稳定属性和价值观相关的领域，但在个体预测方面仍有限制，且无法恢复多变量受访者结构。检索增强架构提供了最大的增益，但性能更多取决于人类回答结构而非模型选择：人格在低变异性问题和常见受访者模式上表现最好，在主观、异质或罕见回答上表现最差。我们的结果为数字人格何时适用于调查研究以及何时仍需人类验证提供了实用指导。

---

## 15. A Single-Layer Model Can Do Language Modeling

**arXiv ID**: [2605.10643](https://arxiv.org/abs/2605.10643)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10643)

**作者**: Zanmin Wang

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-11 14:31:24 UTC

**摘要 (英文)**: Modern language models scale depth by stacking layers, each holding its own state - a per-layer KV cache in transformers, a per-layer matrix in Mamba, Gated DeltaNet (GDN), RWKV, and xLSTM. Biological systems lean heavily on recurrence rather than on stacking. We ask how far that shape can go on language modeling. We propose Grounded Prediction Networks (GPN): one state vector revisited at every step through a single recurrent block - one FFN, one shared matrix memory. At 130M parameters, a 1-layer GPN+M reaches FineWeb-Edu perplexity 18.06, within 13% of a 12-layer Transformer++ (16.05) and 18% of a 10-layer GDN (15.34); a 2-layer variant closes the gap to 6%/11%. We do not match the deep baselines. Because the working context is a single vector, we can directly inspect its geometry: a persistent default-token direction, a content-bearing horizon of tens of tokens, and memory heads that split spontaneously into fast and slow retention pools.

**摘要 (中文)**: 现代语言模型通过堆叠层数来扩展深度，每层维护独立状态——Transformer中每层的KV cache，Mamba、Gated DeltaNet（GDN）、RWKV和xLSTM中每层的矩阵。生物系统更依赖循环而非堆叠。我们探究这种形态在语言建模上能达到什么程度。我们提出Grounded Prediction Networks（GPN）：一个状态向量在每个步骤通过单个循环块被重新访问——一个FFN，一个共享矩阵记忆。在130M参数下，1层GPN+M达到FineWeb-Edu困惑度18.06，与12层Transformer++（16.05）相差13%，与10层GDN（15.34）相差18%；2层变体将差距缩小至6%/11%。我们未能匹敌深层基线。由于工作上下文是单一向量，我们可以直接检查其几何结构：一个持续的默认token方向，一个跨越数十个token的内容承载视界，以及自发分裂为快速和慢速保留池的记忆头。

---

## 16. Towards Understanding Continual Factual Knowledge Acquisition of Language Models: From Theory to Algorithm

**arXiv ID**: [2605.10640](https://arxiv.org/abs/2605.10640)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10640)

**作者**: Haoyu Wang, Yifan Shang, Zhongxiang Sun, Weijie Yu, Xiao Zhang 等 (共6人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 14:28:02 UTC

**摘要 (英文)**: Continual Pre-Training (CPT) is essential for enabling Language Models (LMs) to integrate new knowledge without erasing old. While classical CPT techniques like data replay have become the standard paradigm, the mechanisms underlying how LMs acquire and retain facts over time, termed as continual Factual Knowledge Acquisition (cFKA), remain unclear. In this work, we present a theoretical framework that characterizes the training dynamics of cFKA using a single-layer Transformer, offering a unified explanation for the behavior of representative CPT methods. Our analysis reveals that regularization-based methods merely adjust the convergence rate of parameters without altering the inherent forgetting tendency, whereas data replay methods succeed in shifting convergence dynamics and stabilizing pretrained knowledge. Building on these insights, we propose a novel generative data replay approach, called \textbf{S}electing \textbf{T}okens via attenti\textbf{O}n \textbf{C}ontribution~(STOC), which identifies influential factual snippets to guide replay data generation. Extensive experiments on both synthetic and real-world datasets validate our findings and demonstrate that STOC effectively enhances cFKA by mitigating catastrophic forgetting.

**摘要 (中文)**: 持续预训练（CPT）对于使语言模型整合新知识而不遗忘旧知识至关重要。虽然数据回放等经典CPT技术已成为标准范式，但语言模型如何随时间获取和保留事实的机制——称为持续事实知识获取（cFKA）——仍不清楚。在本文中，我们提出了一个理论框架，使用单层Transformer刻画cFKA的训练动态，为代表性CPT方法的行为提供统一解释。我们的分析揭示，基于正则化的方法仅调整参数收敛速率而不改变固有的遗忘倾向，而数据回放方法则成功转移收敛动态并稳定预训练知识。基于这些洞察，我们提出一种新型生成式数据回放方法，称为通过注意力贡献选择token（STOC），它识别有影响力的事实片段来引导回放数据生成。在合成和真实数据集上的大量实验验证了我们的发现，并表明STOC通过缓解灾难性遗忘有效增强了cFKA。

---

## 17. Intrinsic Guardrails: How Semantic Geometry of Personality Interacts with Emergent Misalignment in LLMs

**arXiv ID**: [2605.10633](https://arxiv.org/abs/2605.10633)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10633)

**作者**: Krishak Aneja, Manas Mittal, Anmol Goel, Ponnurangam Kumaraguru, Vamshi Krishna Bonagiri

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 14:21:57 UTC

**摘要 (英文)**: Fine-tuning Large Language Models (LLMs) on benign narrow data can sometimes induce broad harmful behaviors, a vulnerability termed emergent misalignment (EM). While prior work links these failures to specific directions in the activation space, their relationship to the model's broader persona remains unexplored. We map the latent personality space of LLMs through established psychometric profiles like the Big Five, Dark Triad, and LLM-specific behaviors (e.g. evil, sycophancy), and show that the semantic geometry is highly stable across aligned models and their corrupted fine-tunes. Through causal interventions, we find that directions isolating social valence, such as the 'Evil' persona vector, and a Semantic Valence Vector (SVV) that we introduce, function as intrinsic guardrails: ablating them drives the misalignment rates above $40$%, while amplifying them suppresses the failure mode to less than $3$%. Leveraging the structural stability of the personality space, we show that vectors extracted $\textit{a priori}$ from an instruct-tuned model transfer zero-shot to successfully regulate EM in corrupted fine-tunes. Overall, our findings suggest that harmful fine-tuning does not overwrite a model's internal representation of personality, allowing conserved representations to serve as robust, cross-distribution guardrails.

**摘要 (中文)**: 在良性窄域数据上微调大语言模型（LLM）有时会诱发广泛的危害行为，这种脆弱性被称为涌现错位（EM）。虽然先前工作将这些失败与激活空间中的特定方向联系起来，但它们与模型更广泛人格的关系尚未被探索。我们通过已建立的心理测量画像（如大五人格、暗黑三联征和LLM特定行为，如evil、sycophancy）映射LLM的潜在人格空间，并表明该语义几何在对齐模型及其被破坏的微调版本之间高度稳定。通过因果干预，我们发现隔离社会效价的方向——如"Evil"人格向量，以及我们引入的语义效价向量（SVV）——发挥了内在护栏的作用：消融它们会使错位率超过40%，而放大它们则将失败模式抑制到3%以下。利用人格空间的结构稳定性，我们展示了从指令微调模型中先验提取的向量可以零样本迁移到被破坏的微调版本中成功调节EM。总体而言，我们的发现表明有害微调并未覆盖模型内部的人格表示，使得保守的表示可作为鲁棒的跨分布护栏。

---

## 18. Interpretable Coreference Resolution Evaluation Using Explicit Semantics

**arXiv ID**: [2605.10627](https://arxiv.org/abs/2605.10627)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10627)

**作者**: Bruno Gatti, Giuliano Martinelli, Roberto Navigli

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 14:20:16 UTC

**摘要 (英文)**: Coreference resolution is typically evaluated using aggregate statistical metrics such as CoNLL-F1, which measure structural overlap between predicted and gold clusters. While widely used, these metrics offer limited diagnostic insights, penalizing errors without revealing whether a system struggles with specific semantic categories, such as people, locations, or events, and making it difficult to interpret model capabilities or derive actionable improvements. We address this gap by introducing a semantically-enhanced evaluation framework for coreference resolution. Our approach overlays Concept and Named Entity Recognition (CNER) onto coreference outputs, assigning semantic labels to nominal mentions and propagating them to entire coreference clusters. This enables the computation of typed scores aimed at evaluating mention extraction and linking capabilities stratified by semantic class. Across our experiments on OntoNotes, LitBank, and PreCo, we show that our framework uncovers systematic weaknesses that remain obscured by aggregate metrics. Furthermore, we demonstrate that these diagnostics can be used to design targeted, low-cost data augmentation strategies, achieving measurable out-of-domain improvements.

**摘要 (中文)**: 共指消解通常使用CoNLL-F1等聚合统计指标进行评估，这些指标测量预测聚类与金标准聚类之间的结构重叠。虽然被广泛使用，但这些指标提供的诊断洞察有限，在不揭示系统是否在特定语义类别（如人物、地点或事件）上存在困难的情况下惩罚错误，使得难以解释模型能力或得出可操作的改进方案。我们通过引入语义增强的共指消解评估框架来解决这一差距。我们的方法将概念和命名实体识别（CNER）叠加到共指输出上，为名词性提及分配语义标签并将其传播到整个共指聚类。这使得按语义类别分层评估提及提取和链接能力成为可能。在OntoNotes、LitBank和PreCo上的实验中，我们展示了该框架揭示了聚合指标所掩盖的系统性弱点。此外，我们证明这些诊断可用于设计有针对性的低成本数据增强策略，实现可衡量的域外改进。

---

## 19. Responsible Benchmarking of Fairness for Automatic Speech Recognition

**arXiv ID**: [2605.10615](https://arxiv.org/abs/2605.10615)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10615)

**作者**: Felix Herron, Ange Richard, François Portet, Alexandre Allauzen, Solange Rossato

**分类**: Computation and Language

**发布时间**: 2026-05-11 14:11:50 UTC

**摘要 (英文)**: Many studies have shown automatic speech processing (ASR) systems have unequal performance across speakergroups (SG's). However, the manner in which such studies arrive at this conclusion is inconsistent. To pave the wayfor more reliable results in future studies, we lay out best practices for benchmarking ASR fairness based on literaturefrom machine learning fairness, social sciences, and speech science. We first describe the importance of preciselythe fairness hypothesis being interrogated, and tailoring fairness metrics to apply specifically to said hypothesis.We then examine several benchmarks used to rate ASR systems on fairness and discuss how their results can bemisconstrued without assiduous oversight into the intersections between SG's. We find that evaluating fairnessbased on single heterogeneous SG's, such as they are defined in fairness benchmarks, can lead to misidentifyingwhich SG's are actually being mistreated by ASR systems. We advocate for as fine-grained an analysis as possibleof the intersectionality of as many demographic variables as are available in the metadata of fairness corpora in orderto tease out such spurious correlations

**摘要 (中文)**: 许多研究表明自动语音处理（ASR）系统在不同说话者群体之间存在性能差异。然而，这些研究得出结论的方式不一致。为在未来研究中获得更可靠的结果铺平道路，我们基于机器学习公平性、社会科学和语音科学的文献，制定了ASR公平性基准测试的最佳实践。我们首先描述了精确界定所考察公平性假设的重要性，以及将公平性指标专门针对该假设进行定制。然后我们考察了几个用于评估ASR系统公平性的基准，并讨论了如果不仔细审视说话者群体之间的交集，其结果可能如何被误读。我们发现，基于公平性基准中定义的单一异质说话者群体来评估公平性，可能导致误判哪些说话者群体实际上受到了ASR系统的不公正对待。我们主张对公平性语料库元数据中尽可能多的人口统计变量的交叉性进行尽可能细粒度的分析，以厘清此类虚假相关性。

---

## 20. Measuring Embedding Sensitivity to Authorial Style in French: Comparing Literary Texts with Language Model Rewritings

**arXiv ID**: [2605.10606](https://arxiv.org/abs/2605.10606)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10606)

**作者**: Benjamin Icard, Lila Sainero, Alice Breton, Evangelia Zve, Jean-Gabriel Ganascia

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 14:05:46 UTC

**摘要 (英文)**: Large language models (LLMs) can convincingly imitate human writing styles, yet it remains unclear how much stylistic information is encoded in embeddings from any language model and retained after LLM rewriting. We investigate these questions in French, using a controlled literary dataset to quantify the effect of stylistic variation via changes in embedding dispersion. We observe that embeddings reliably capture authorial stylistic features and that these signals persist after rewriting, while also exhibiting LLM-specific patterns. These analytical results offer promising directions for authorship imitation detection in the era of language models.

**摘要 (中文)**: 大语言模型（LLM）可以令人信服地模仿人类写作风格，但目前尚不清楚任何语言模型的嵌入中编码了多少文体信息，以及这些信息在LLM改写后能保留多少。我们在法语中研究了这些问题，使用受控文学数据集通过嵌入散度的变化来量化文体变异的影响。我们观察到嵌入能可靠地捕捉作者文体特征，这些信号在改写后持续存在，同时表现出LLM特有的模式。这些分析结果为语言模型时代的作者模仿检测指明了有前景的方向。

---

## 21. Where do aspectual variants of light verb constructions belong?

**arXiv ID**: [2605.10605](https://arxiv.org/abs/2605.10605)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10605)

**作者**: Aggeliki Fotopoulou, Eric Laporte, Takuya Nakamura

**分类**: Computation and Language

**发布时间**: 2026-05-11 14:05:38 UTC

**摘要 (英文)**: Expressions with an aspectual variant of a light verb, e.g. 'take on debt' vs. 'have debt', are frequent in texts but often difficult to classify between verbal idioms, light verb constructions or compositional phrases. We investigate the properties of such expressions with a disputed membership and propose a selection of features that determine more satisfactory boundaries between the three categories in this zone, assigning the expressions to one of them.

**摘要 (中文)**: 带有轻动词体变体的表达式（如"take on debt"与"have debt"）在文本中频繁出现，但常常难以在动词习语、轻动词构式和组合性短语之间进行分类。我们研究了这类归属有争议的表达式的性质，并提出了一组特征选择，以在该区域三个类别之间确定更令人满意的边界，将这些表达式归属到其中一个类别。

---

## 22. VISTA: A Generative Egocentric Video Framework for Daily Assistance

**arXiv ID**: [2605.10579](https://arxiv.org/abs/2605.10579)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10579)

**作者**: Yu-Hsiang Liu, Yu-Chien Tang, An-Zi Yen

**分类**: Computation and Language

**发布时间**: 2026-05-11 13:50:47 UTC

**摘要 (英文)**: Training AI agents to proactively assist humans in daily activities, from routine household tasks to urgent safety situations, requires large-scale visual data. However, capturing such scenarios in the real world is often difficult, costly, or unsafe, and physics-based simulators lack the visual fidelity needed to transfer learned behaviors to real settings. Therefore, we introduce VISTA, a video synthesis system that produces high-fidelity egocentric videos as training and evaluation data for AI agents. VISTA employs a 5-step script generation pipeline with causal reverse reasoning to create diverse, logically grounded intervention modes. These scenarios span two levels of agent autonomy: reactive and proactive. In reactive modes, the user explicitly asks the agent for help. In proactive modes, the agent offers help without receiving a direct request. We further divide proactive modes into explicit and implicit types. In explicit proactive scenarios, the user is aware of needing help but does not directly address the agent. In implicit proactive scenarios, the agent intervenes before the user even realizes that help is needed. VISTA allows users to customize and refine scenarios to generate video benchmarks for daily tasks, offering a scalable and controllable alternative to real-world data collection for training and evaluating AI agents in realistic environments.

**摘要 (中文)**: 训练AI智能体主动协助人类完成日常活动——从常规家务到紧急安全情况——需要大规模视觉数据。然而，在真实世界中捕获此类场景通常困难、昂贵或不安全，且基于物理的模拟器缺乏将学习到的行为迁移到真实环境所需的视觉保真度。因此，我们引入VISTA，一个视频合成系统，可生成高保真自中心视角视频作为AI智能体的训练和评估数据。VISTA采用5步脚本生成管道，结合因果逆向推理来创建多样化、逻辑有据的干预模式。这些场景涵盖两个智能体自主性层级：反应式和主动式。在反应模式中，用户明确请求智能体帮助；在主动模式中，智能体在没有收到直接请求时主动提供帮助。我们进一步将主动模式细分为显式和隐式类型。在显式主动场景中，用户意识到需要帮助但不直接呼叫智能体；在隐式主动场景中，智能体在用户意识到需要帮助之前就进行干预。VISTA允许用户定制和优化场景以生成日常任务的视频基准，为在真实环境中训练和评估AI智能体提供了可扩展且可控的替代方案。

---

## 23. ThreatCore: A Benchmark for Explicit and Implicit Threat Detection

**arXiv ID**: [2605.10563](https://arxiv.org/abs/2605.10563)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10563)

**作者**: Davide Bruni, Carlo Bardazzi, Maurizio Tesconi

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 13:35:53 UTC

**摘要 (英文)**: Threat detection in Natural Language Processing lacks consistent definitions and standardized benchmarks, and is often conflated with broader phenomena such as toxicity, hate speech, or offensive language. In this work, we introduce ThreatCore, a public available benchmark dataset for fine-grained threat detection that distinguishes between explicit threats, implicit threats, and non-threats. The dataset is constructed by aggregating multiple publicly available resources and systematically re-annotating them under a unified operational definition of threat, revealing substantial inconsistencies across existing labels. To improve the coverage of underrepresented cases, particularly implicit threats, we further augment the dataset with synthetic examples, which are manually validated using the same annotation protocol adopted for the re-annotation of the public datasets, ensuring consistency across all data sources. We evaluate Perspective API, zero-shot classifiers, and recent language models on ThreatCore, showing that implicit threats remain substantially harder to detect than explicit ones. Our results also indicate that incorporating Semantic Role Labeling as an intermediate representation can improve performance by making the structure of harmful intent more explicit. Overall, ThreatCore provides a more consistent benchmark for studying fine-grained threat detection and highlights the challenges that current models still face in identifying indirect expressions of harmful intent.

**摘要 (中文)**: 自然语言处理中的威胁检测缺乏一致的定义和标准化基准，常与毒性、仇恨言论或冒犯性语言等更广泛的现象混淆。在本文中，我们引入ThreatCore，一个用于细粒度威胁检测的公开基准数据集，区分显式威胁、隐式威胁和非威胁。该数据集通过聚合多个公开可用资源并在统一的威胁操作定义下系统性地重新标注来构建，揭示了现有标签之间的重大不一致性。为改善代表性不足案例（尤其是隐式威胁）的覆盖，我们进一步用合成示例增强数据集，这些示例使用与公开数据集重新标注相同的标注协议进行人工验证，确保所有数据源之间的一致性。我们在ThreatCore上评估了Perspective API、零样本分类器和近期的语言模型，结果表明隐式威胁仍然比显式威胁更难检测。我们的结果还表明，将语义角色标注作为中间表示可以通过使有害意图的结构更明确来提高性能。总体而言，ThreatCore为细粒度威胁检测研究提供了更一致的基准，并突出了当前模型在识别间接有害意图表达方面仍面临的挑战。

---

## 24. ICT-NLP at SemEval-2026 Task 3: Less Is More -- Multilingual Encoder with Joint Training and Adaptive Ensemble for Dimensional Aspect Sentiment Regression

**arXiv ID**: [2605.10560](https://arxiv.org/abs/2605.10560)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10560)

**作者**: Liyuan Huang, Jiawei He, Wutao Shen, Lin Li, Jin Zhang

**分类**: Computation and Language

**发布时间**: 2026-05-11 13:33:25 UTC

**摘要 (英文)**: This paper describes our system to SemEval-2026 Task 3 Track A Subtask 1 on Dimensional Aspect Sentiment Regression (DimASR). We propose a lightweight and resource-efficient system built entirely on multilingual pre-trained encoders, without relying on LLMs or external corpora. We adopt joint multilingual and multi-domain training to facilitate cross-lingual transfer and alleviate data sparsity, introduce a bounded regression transformation that improves training stability while constraining predictions within the valid range, and employ an adaptive ensemble strategy via subset search to reduce prediction variance. Experimental results demonstrate that our system achieves strong and consistent performance, ranking 1st on zho-res, 2nd on zho-lap, and 3rd on jpn-hot, with all remaining datasets placed within the top half of participating teams.

**摘要 (中文)**: 本文描述了我们参加SemEval-2026 Task 3 Track A Subtask 1维度方面情感回归（DimASR）的系统。我们提出一个完全基于多语言预训练编码器的轻量级资源高效系统，不依赖LLM或外部语料库。我们采用联合多语言和多领域训练以促进跨语言迁移并缓解数据稀疏性，引入有界回归变换在改善训练稳定性的同时将预测约束在有效范围内，并通过子集搜索采用自适应集成策略来降低预测方差。实验结果表明我们的系统实现了强健一致的性能，在zho-res上排名第1，zho-lap上排名第2，jpn-hot上排名第3，其余数据集均排在参赛队伍前半。

---

## 25. Multi-domain Multi-modal Document Classification Benchmark with a Multi-level Taxonomy

**arXiv ID**: [2605.10550](https://arxiv.org/abs/2605.10550)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10550)

**作者**: Denghao Ma, Qing Liu, Zulong Chen, Chuanfei Xu, Jia Xu 等 (共7人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 13:28:27 UTC

**摘要 (英文)**: Document classification forms the backbone of modern enterprise content management, yet existing benchmarks remain trapped in oversimplified paradigms -- single domain settings with flat label structures -- that bear little resemblance to the hierarchical, multi-modal, and cross-domain nature of real-world business documents. This gap not only misrepresents practical complexity but also stifles progress toward industrially viable document intelligence. To bridge this gap, we construct the first Multi-level, Multi-domain, Multi-modal document classification Benchmark (MMM-Bench). MMM-Bench includes (1) a deeply hierarchical taxonomy spanning five levels that capture the authentic organizational logic of business documentation; and (2) 5,990 real-world multi-modal documents meticulously curated from 12 commercial domains in Alibaba. Each document is manually annotated with a complete hierarchical path by domain experts. We establish comprehensive baselines on MMM-Bench, which consists of open-weight models and API-based models. Through systematic experiments, we identify four fundamental challenges within MMM-Bench and propose corresponding insights. To provide a solid foundation for advancing research in multi-level, multi-domain document classification, we release all of the data and the evaluation toolkit of MMM-Bench at https://github.com/MMMDC-Bench/MMMDC-Bench.

**摘要 (中文)**: 文档分类是现代企业内容管理的基石，但现有基准仍困于过度简化的范式——单领域设置和扁平标签结构——与真实世界商业文档的层次性、多模态和跨领域性质相去甚远。这一差距不仅歪曲了实际复杂性，还阻碍了向工业可用的文档智能迈进。为弥合这一差距，我们构建了首个多层次、多领域、多模态文档分类基准（MMM-Bench）。MMM-Bench包括：(1) 跨越五个层级的深层分类体系，捕捉商业文档的真实组织逻辑；(2) 从阿里巴巴12个商业领域精心策划的5,990份真实多模态文档。每份文档由领域专家手动标注完整的层次路径。我们在MMM-Bench上建立了综合基线，包括开源权重模型和API模型。通过系统实验，我们识别了MMM-Bench中的四个根本挑战并提出相应洞察。为推进多层次、多领域文档分类研究提供坚实基础，我们在https://github.com/MMMDC-Bench/MMMDC-Bench发布了MMM-Bench的所有数据和评估工具包。

---

## 26. Where Does Long-Context Supervision Actually Go? Effective-Context Exposure Balancing

**arXiv ID**: [2605.10544](https://arxiv.org/abs/2605.10544)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10544)

**作者**: Jinchang Zhu, Jindong Li, Chengyu Zou, Rong Fu, Chao Wang 等 (共7人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 13:23:21 UTC

**摘要 (英文)**: Long-context adaptation is often viewed as window scaling, but this misses a token-level supervision mismatch: in packed training with document masking, each target token's effective context remains short. We introduce EXACT, a supervision-allocation objective that assigns extra weight to long effective-context targets by inverse frequency within the long tail. Across seven Qwen/LLaMA CPT configurations, EXACT improves all 28 trained/extrapolated NoLiMa and RULER comparisons. On Qwen2.5-0.5B, NoLiMa improves by +10.09 (trained) and +5.34 (extrapolated); RULER by +10.69 and +5.55. On LLaMA-3.2-3B, RULER improves by +17.91 and +16.11. Standard QA/reasoning are preserved (+0.24 macro change across six benchmarks). A distance-resolved probe shows gains arise when evidence is thousands of tokens away, while short cases remain unchanged. Results support a supervision-centric thesis: long-context adaptation depends on how strongly training supervises long-context predictions.

**摘要 (中文)**: 长上下文适应通常被视为窗口扩展，但这忽略了token级监督不匹配的问题：在使用文档掩码的打包训练中，每个目标token的有效上下文仍然很短。我们提出EXACT，一种监督分配目标，通过长尾内的逆频率为长有效上下文目标分配额外权重。在七个Qwen/LLaMA CPT配置中，EXACT改善了所有28个训练/外推NoLiMa和RULER比较。在Qwen2.5-0.5B上，NoLiMa改善+10.09（训练）和+5.34（外推）；RULER改善+10.69和+5.55。在LLaMA-3.2-3B上，RULER改善+17.91和+16.11。标准QA/推理得到保持（六个基准上宏观变化+0.24）。距离分辨探针显示收益源自证据距离数千token时，而短距离案例保持不变。结果支持以监督为中心的论点：长上下文适应取决于训练对长上下文预测的监督强度。

---

## 27. Mela: Test-Time Memory Consolidation based on Transformation Hypothesis

**arXiv ID**: [2605.10537](https://arxiv.org/abs/2605.10537)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10537)

**作者**: Lungchuan Chen

**分类**: Computation and Language

**发布时间**: 2026-05-11 13:20:51 UTC

**摘要 (英文)**: Memory consolidation, the process by which transient experiences are transformed into stable, structured representations, is a foundational organizing principle in the human brain, yet it remains largely unexplored as a design principle for modern sequence models. In this work, we leverage established neuroscientific theories of memory consolidation and cross-frequency coupling to propose the Hierarchical Memory Module (HMM), a neural memory architecture composed of two functionally distinct sub-modules that operate at different update frequencies. Inspired by the transformation hypothesis, the low-frequency sub-module produces high-level representations that capture abstract, gist-level knowledge, while the high-frequency sub-module produces fine-grained representations that preserve richer episodic detail. The final memory output is dynamically reconstructed as a context-dependent combination of both representations, analogous to the reconstructive nature of human memory retrieval. We integrate HMM into a Transformer-based language decoder to form Mela, a family of memory-augmented language models that perform online memory consolidation at test time. To further exploit the multi-granularity memory representations produced by HMM, we introduce MemStack, a method that distributes different levels of memory features across the early layers of the decoder without introducing additional tokens. Experiments on language modeling demonstrate that Mela outperforms Transformer baselines across all the model sizes. Moreover, with the pretrained context length fixed at 4K, Mela maintains performance on significantly longer contexts, whereas Transformer baselines degrade rapidly beyond their training length. Extensive ablation studies validate the contribution of each component and provide guidance for practical configuration.

**摘要 (中文)**: 记忆巩固——将短暂经验转化为稳定结构化表示的过程——是人脑的基础组织原则，但作为现代序列模型的设计原则仍很大程度上未被探索。在本文中，我们利用记忆巩固和跨频率耦合的既有神经科学理论，提出层次记忆模块（HMM），一种由两个功能不同、以不同更新频率运行的子模块组成的神经记忆架构。受转化假说启发，低频子模块产生捕获抽象要旨知识的高级表示，而高频子模块产生保留更丰富情景细节的细粒度表示。最终记忆输出作为两种表示的上下文依赖组合被动态重建，类似于人类记忆检索的重构性质。我们将HMM集成到基于Transformer的语言解码器中，形成Mela——一系列在测试时执行在线记忆巩固的记忆增强语言模型。为进一步利用HMM产生的多粒度记忆表示，我们引入MemStack，一种在解码器早期层间分配不同层级记忆特征而不引入额外token的方法。语言建模实验表明Mela在所有模型规模上优于Transformer基线。此外，在预训练上下文长度固定为4K的情况下，Mela在显著更长的上下文上维持性能，而Transformer基线在超出训练长度后迅速退化。大量消融研究验证了每个组件的贡献并为实际配置提供指导。

---

## 28. Infinite Mask Diffusion for Few-Step Distillation

**arXiv ID**: [2605.10518](https://arxiv.org/abs/2605.10518)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10518)

**作者**: Jaehoon Yoo, Wonjung Kim, Chanhyuk Lee, Seunghoon Hong

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 13:07:03 UTC

**摘要 (英文)**: Masked Diffusion Models (MDMs) have emerged as a promising alternative to autoregressive models in language modeling, offering the advantages of parallel decoding and bidirectional context processing within a simple yet effective framework. Specifically, their explicit distinction between masked tokens and data underlies their simple framework and effective conditional generation. However, MDMs typically require many sampling iterations due to factorization errors stemming from simultaneous token updates. We observe that a theoretical lower bound of the factorization error exists, which standard MDMs cannot reduce due to their use of a deterministic single-state mask. In this paper, we propose the Infinite Mask Diffusion Model (IMDM), which introduces a stochastic infinite-state mask to mitigate the theoretical bound while directly inheriting the benefits of MDMs, including the compatibility with pre-trained weights. We empirically demonstrate that MDM fails to perform few-step generation even in a simple synthetic task due to the factorization error bound, whereas IMDM can find an efficient solution for the same task. Finally, when equipped with appropriate distillation methods, IMDM surpasses existing few-step distillation methods at small step counts on LM1B and OpenWebText. Code is available at https://Ugness.github.io/official_imdm.

**摘要 (中文)**: 掩码扩散模型（MDM）已成为语言建模中自回归模型的有前途替代方案，提供了并行解码和双向上下文处理的优势，同时框架简单有效。具体而言，其对掩码token和数据的显式区分构成了其简洁框架和有效条件生成的基础。然而，由于同时更新token导致的因子化误差，MDM通常需要许多采样迭代。我们观察到因子化误差存在理论下界，标准MDM由于使用确定性单状态掩码而无法降低该下界。在本文中，我们提出无限掩码扩散模型（IMDM），引入随机无限状态掩码来缓解理论下界，同时直接继承MDM的优势，包括与预训练权重的兼容性。我们实证表明，由于因子化误差下界，MDM即使在简单的合成任务上也无法进行少步生成，而IMDM可以为相同任务找到高效解。最后，配备适当的蒸馏方法后，IMDM在LM1B和OpenWebText上的少步计数下超越了现有少步蒸馏方法。代码可在https://Ugness.github.io/official_imdm获取。

---

## 29. Learning Less Is More: Premature Upper-Layer Attention Specialization Hurts Language Model Pretraining

**arXiv ID**: [2605.10504](https://arxiv.org/abs/2605.10504)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10504)

**作者**: Jinchang Zhu, Jindong Li, Yuwen Hao, Chengyu Zou, Rong Fu 等 (共6人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 13:01:12 UTC

**摘要 (英文)**: A causal-decoder block is hierarchical: lower layers build the residual basis that upper layers attend over. We identify a failure mode in GPT pretraining: upper layers commit to sharp attention patterns before lower-layer features stabilize. We call this premature upper-layer attention specialization. Temporarily slowing only upper-layer Q/K projections during early training improves final perplexity and downstream accuracy without altering other parameters; it prevents upper attention from collapsing onto an immature residual basis. In LLaMA-style blocks, the same intervention is nearly unnecessary. Through ablations, we isolate multiplicative gated FFNs (not RMSNorm or bias removal) as the component that suppresses the upstream residual writes driving the failure. A pathwise analysis unifies both findings: the learning-rate intervention reduces a step-size factor, while gated FFNs reduce a residual-energy factor on the same growth pathway. Our results identify upper-layer Q/K timing as a concrete interaction point between decoder architecture and optimization.

**摘要 (中文)**: 因果解码器块是层次化的：下层构建上层关注的残差基础。我们识别了GPT预训练中的一个失败模式：上层在下层特征稳定之前就形成尖锐注意力模式。我们称之为过早的上层注意力特化。在早期训练中暂时减缓上层Q/K投影能改善最终困惑度和下游准确率，而无需改变其他参数；它阻止了上层注意力坍缩到不成熟的残差基础上。在LLaMA风格块中，相同干预几乎不必要。通过消融实验，我们分离出乘法门控FFN（而非RMSNorm或偏差移除）为抑制驱动该失败的上行残差写入的组件。路径分析统一了两个发现：学习率干预减少了步长因子，而门控FFN减少了同一增长路径上的残差能量因子。我们的结果将上层Q/K时序识别为解码器架构与优化之间的具体交互点。

---

## 30. DeepRefine: Agent-Compiled Knowledge Refinement via Reinforcement Learning

**arXiv ID**: [2605.10488](https://arxiv.org/abs/2605.10488)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10488)

**作者**: Haoyu Huang, Jiaxin Bai, Shujie Liu, Yang Wei, Hong Ting Tsang 等 (共9人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 12:48:31 UTC

**摘要 (英文)**: Agent-compiled knowledge bases provide persistent external knowledge for large language model (LLM) agents in open-ended, knowledge-intensive downstream tasks. Yet their quality is systematically limited by \emph{incompleteness}, \emph{incorrectness}, and \emph{redundancy}, manifested as missing evidence or cross-document links, low-confidence or imprecise claims, and ambiguous or coreference resolution issues. Such defects compound under iterative use, degrading retrieval fidelity and downstream task performance. We present \textbf{DeepRefine}, a general LLM-based reasoning model for \emph{agent-compiled knowledge refinement} that improves the quality of any pre-constructed knowledge bases with user queries to make it more suitable for the downstream tasks. DeepRefine performs multi-turn interactions with the knowledge base and conducts abductive diagnosis over interaction history, localizes likely defects, and executes targeted refinement actions for incremental knowledge base updates. To optimize refinement policies of DeepRefine without gold references, we introduce a Gain-Beyond-Draft (GBD) reward and train the reasoning process end-to-end via reinforcement learning. Extensive experiments demonstrate consistent downstream gains over strong baselines.

**摘要 (中文)**: 智能体编译的知识库为大语言模型（LLM）智能体在开放式、知识密集型下游任务中提供持久外部知识。然而其质量系统性受限于不完整性、不正确性和冗余性，表现为缺失证据或跨文档链接、低置信度或不精确的声明，以及歧义或共指消解问题。这些缺陷在迭代使用中累积，降低检索保真度和下游任务性能。我们提出DeepRefine，一种通用的基于LLM的推理模型，用于智能体编译的知识精炼，通过用户查询提高任何预构建知识库的质量，使其更适合下游任务。DeepRefine与知识库进行多轮交互，对交互历史进行溯因诊断，定位可能的缺陷，并执行有针对性的精炼操作以增量更新知识库。为在没有金标准参考的情况下优化DeepRefine的精炼策略，我们引入Gain-Beyond-Draft（GBD）奖励，并通过强化学习端到端训练推理过程。大量实验证明了一致的下游增益，优于强基线。

---

## 31. Coherency through formalisations of Structured Natural Language, A case study on FRETish

**arXiv ID**: [2605.10462](https://arxiv.org/abs/2605.10462)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10462)

**作者**: Joost J. Joosten, Marina López Chamosa, Sofía Santiago Fernández

**分类**: Computation and Language, Logic in Computer Science

**发布时间**: 2026-05-11 12:30:53 UTC

**摘要 (英文)**: Formalisation is the process of writing system requirements in a formal language. These requirements mostly originate in Natural Language. In the field of Formal Methods, formalisation is often identified as one of the most delicate and complicated steps in the verification process. Not seldomly, formalisation tools and environments choose various levels of requirement descriptions: Natural Language, Technical Language, Diagram Representations and Formal Language, to mention a few. In the literature, there are various maxims and principles of good practice to guide the process of requirement formalisation. In this paper we propose a new guideline: Coherency through Formalisations. The guideline states that the different levels of formalisation mentioned above should roughly follow the same logical structure. The principle seems particularly relevant in the setting where LLMs are prompted to perform reasoning tasks that can be checked by formal tools using Structured Natural Language to act as an intermediate layer bridging both paradigms. In the light of coherency, we analyze NASA's Formal Requirement Elicitation Tool FRET and propose an alternative automated translation of the Controlled Natural Language FRETish to the formal language of MTL. We compare our translation to the original translation and prove equivalence using model checking. Some statistics are performed which seem to favor the new translation. As expected, the translation process yielded interesting reflections and revealed inconsistencies which we present and discuss.

**摘要 (中文)**: 形式化是将系统需求以形式语言书写的过程。这些需求大多源于自然语言。在形式化方法领域，形式化常被认为是最微妙和复杂的验证步骤之一。形式化工具和环境通常选择不同层级的需求描述：自然语言、技术语言、图表表示和形式语言等。文献中有各种良好实践准则来指导需求形式化过程。在本文中，我们提出一条新准则：通过形式化实现一致性。该准则指出，上述不同形式化层级应大致遵循相同的逻辑结构。这一原则在LLM被提示执行可由形式工具检查的推理任务时尤为相关，结构化自然语言充当连接两种范式的中间层。基于一致性视角，我们分析了NASA的形式需求获取工具FRET，并提出了受控自然语言FRETish到MTL形式语言的替代自动翻译。我们将我们的翻译与原始翻译进行比较，并使用模型检测证明等价性。进行了一些统计检验，结果似乎有利于新翻译。正如预期，翻译过程产生了有趣的反思并揭示了我们呈现和讨论的不一致性。

---

## 32. Can Language Models Analyze Data? Evaluating Large Language Models for Question Answering over Datasets

**arXiv ID**: [2605.10419](https://arxiv.org/abs/2605.10419)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10419)

**作者**: Andreas Xenofontos, Pavlos Fafalios

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 11:54:47 UTC

**摘要 (英文)**: This paper investigates the effectiveness of large language models (LLMs) in answering questions over datasets. We examine their performance in two scenarios: (a) directly answering questions given a dataset file as input, and (b) generating SQL queries to answer questions given the schema of a relational database. We also evaluate the impact of different prompting strategies on model performance. The study includes both state-of-the-art LLMs and smaller language models that require fewer resources and operate at lower computational and financial cost. Experiments are conducted on two datasets containing questions of varying difficulty. The results demonstrate the strong performance of large LLMs, while highlighting the limitations of smaller, more cost-efficient models. These findings contribute to a better understanding of how LLMs can be utilized in data analytics tasks and their associated limitations.

**摘要 (中文)**: 本文研究大语言模型（LLM）在数据集上回答问题的有效性。我们考察两种场景下的性能：(a) 以数据集文件为输入直接回答问题，(b) 给定关系数据库模式生成SQL查询来回答问题。我们还评估了不同提示策略对模型性能的影响。研究包括最先进的LLM和需要较少资源、计算和财务成本更低的较小语言模型。实验在两个包含不同难度问题的数据集上进行。结果展示了大型LLM的强劲性能，同时凸显了更小、更具成本效益模型的局限性。这些发现有助于更好地理解LLM在数据分析任务中的应用方式及其相关限制。

---

## 33. Aligning LLM Uncertainty with Human Disagreement in Subjectivity Analysis

**arXiv ID**: [2605.10415](https://arxiv.org/abs/2605.10415)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10415)

**作者**: Junyu Lu, Deyi Ji, Xuanyi Liu, Lanyun Zhu, Bo Xu 等 (共7人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 11:52:58 UTC

**摘要 (英文)**: Large language models for subjectivity analysis are typically trained with aggregated labels, which compress variations in human judgment into a single supervision signal. This paradigm overlooks the intrinsic uncertainty of low-agreement samples and often induces overconfident predictions, undermining reliability and generalization in complex subjective settings. In this work, we advocate uncertainty-aware subjectivity analysis, where models are expected to make predictions while expressing uncertainty that reflects human disagreement. To operationalize this perspective, we propose a two-phase Disagreement Perception and Uncertainty Alignment (DPUA) framework. Specifically, DPUA jointly models label prediction, rationale generation, and uncertainty expression under an uncertainty-aware setting. In the disagreement perception phase, adaptive decoupled learning enhances the model's sensitivity to disagreement-related cues while preserving task performance. In the uncertainty alignment phase, GRPO-based reward optimization further improves uncertainty-aware reasoning and aligns the model's confidence expression with the human disagreement distribution. Experiments on three subjectivity analysis tasks show that DPUA preserves task performance while better aligning model uncertainty with human disagreement, mitigating overconfidence on boundary samples, and improving out-of-distribution generalization.

**摘要 (中文)**: 用于主观性分析的大语言模型通常使用聚合标签训练，将人类判断的变异性压缩为单一监督信号。这种范式忽视了低一致性样本的内在不确定性，常导致过度自信的预测，削弱复杂主观场景中的可靠性和泛化能力。在本文中，我们倡导不确定性感知的主观性分析，即模型在做出预测的同时表达反映人类分歧的不确定性。为实现这一视角，我们提出两阶段分歧感知与不确定性对齐（DPUA）框架。具体而言，DPUA在不确定性感知设置下联合建模标签预测、理由生成和不确定性表达。在分歧感知阶段，自适应解耦学习增强模型对分歧相关线索的敏感性同时保持任务性能。在不确定性对齐阶段，基于GRPO的奖励优化进一步改善不确定性感知推理，并将模型的置信度表达与人类分歧分布对齐。在三个主观性分析任务上的实验表明，DPUA保持了任务性能，同时更好地将模型不确定性与人类分歧对齐，缓解了边界样本上的过度自信，并改善了分布外泛化。

---

## 34. Phoenix-VL 1.5 Medium Technical Report

**arXiv ID**: [2605.10391](https://arxiv.org/abs/2605.10391)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10391)

**作者**: Team Phoenix, Arka Ray, Askar Ali Mohamed Jawad, Biondi Lee, Elijah Seah 等 (共31人)

**分类**: Computation and Language, Artificial Intelligence, Computer Vision and Pattern Recognition

**发布时间**: 2026-05-11 11:36:37 UTC

**摘要 (英文)**: We introduce Phoenix-VL 1.5 Medium, a 123B-parameter natively multimodal and multilingual foundation model, adapted to regional languages and the Singapore context. Developed as a sovereign AI asset, it demonstrates that deep domain adaptation can be achieved with minimal degradation to broad-spectrum intelligence and alignment. Continued pretraining was performed on Mistral Medium 3.1 using a localized 1-trillion tokens multimodal corpus, followed by a 250-billion tokens long-context extension phase. Subsequent post-training incorporated a novel human-annotated Singapore multimodal dataset and curated textual corpus on Singapore culture, knowledge, and legislation, totaling 22-billion tokens. An additional 5 billion tokens of model alignment was performed through Online Direct Preference Optimization. Phoenix-VL 1.5 Medium achieves state-of-the-art performance for its size on Singapore multimodal, legal, and government policy benchmarks while remaining globally competitive on general multimodal intelligence, multilingual, and STEM benchmarks. We also introduce a novel evaluation suite encompassing localized knowledge benchmarks and an institutionally aligned model behavior and safety framework. We report the data curation principles, training methodology, and highlight benchmark and inference performance.

**摘要 (中文)**: 我们介绍Phoenix-VL 1.5 Medium，一个123B参数的原生多模态多语言基础模型，适配区域语言和新加坡语境。作为主权AI资产开发，它证明了可以在最小化广谱智能和对齐退化的情况下实现深度领域适配。在Mistral Medium 3.1上使用本地化的1万亿token多模态语料库进行持续预训练，随后进行2500亿token的长上下文扩展阶段。后续后训练纳入了新的人工标注新加坡多模态数据集以及关于新加坡文化、知识和法律的策划文本语料库，共计220亿token。另外通过在线直接偏好优化进行了50亿token的模型对齐。Phoenix-VL 1.5 Medium在其规模上于新加坡多模态、法律和政府政策基准上达到最优性能，同时在通用多模态智能、多语言和STEM基准上保持全球竞争力。我们还引入了新的评估套件，包含本地化知识基准和机构对齐的模型行为与安全框架。我们报告了数据策划原则、训练方法，并重点介绍了基准和推理性能。

---

## 35. Not All Proofs Are Equal: Evaluating LLM Proof Quality Beyond Correctness

**arXiv ID**: [2605.10379](https://arxiv.org/abs/2605.10379)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10379)

**作者**: Ivo Petrov, Jasper Dekoninck, Dimitar I. Dimitrov, Martin Vechev

**分类**: Computation and Language

**发布时间**: 2026-05-11 11:23:36 UTC

**摘要 (英文)**: Large language models (LLMs) have become capable mathematical problem-solvers, often producing correct proofs for challenging problems. However, correctness alone is not sufficient: mathematical proofs should also be clear, concise, insightful, and transferable to other problems. While this proof quality is subjective and depends on the reader and context, many of its components are concrete and broadly valued. In this work, we identify such components and introduce ProofRank, a benchmark curated from challenging mathematical competitions. ProofRank evaluates several scalable proxies of proof quality: (i) conciseness, measuring whether proofs avoid unnecessary steps; (ii) computational ease, measuring the extent to which a proof relies on tedious calculations; (iii) cognitive simplicity, measuring how accessible the used proof techniques are; (iv) diversity, measuring how varied a model's proofs for a single problem are; and (v) adaptivity, measuring whether a model can follow a specified proof technique. Across models, we find substantial differences in proof quality that are not captured by correctness-only benchmarks. We also observe significant trade-offs between proof-quality metrics and correctness, suggesting that future evaluations of mathematical reasoning should measure how useful LLM-generated proofs are.

**摘要 (中文)**: 大语言模型（LLM）已成为有能力的数学问题求解器，经常为挑战性问题生成正确证明。然而，仅正确性是不够的：数学证明还应当清晰、简洁、深刻且可迁移到其他问题。虽然证明质量是主观的并取决于读者和上下文，但其许多组成部分是具体且被广泛重视的。在本文中，我们识别了这些组件并引入ProofRank，一个从挑战性数学竞赛中策划的基准。ProofRank评估多个可扩展的证明质量代理指标：(i) 简洁性，衡量证明是否避免不必要的步骤；(ii) 计算简易度，衡量证明依赖繁琐计算的程度；(iii) 认知简单度，衡量所使用的证明技术的可及性；(iv) 多样性，衡量模型对单个问题的证明的多样性；(v) 适应性，衡量模型是否能遵循指定的证明技术。跨模型间，我们发现仅以正确性基准无法捕捉的证明质量存在重大差异。我们还观察到证明质量指标与正确性之间存在显著权衡，表明未来对数学推理的评估应衡量LLM生成证明的有用性。

---

## 36. An Annotation Scheme and Classifier for Personal Facts in Dialogue

**arXiv ID**: [2605.10339](https://arxiv.org/abs/2605.10339)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10339)

**作者**: Konstantin Zaitsev

**分类**: Computation and Language

**发布时间**: 2026-05-11 10:42:26 UTC

**摘要 (英文)**: The advancement of Large Language Models (LLMs) has enabled their application in personalized dialogue systems. We present an extended annotation scheme for personal fact classification that addresses limitations in existing approaches, particularly PeaCoK. Our scheme introduces new categories (Demographics, Possessions) and attributes (Duration, Validity, Followup) that enable structured storage, quality filtering, and identification of facts suitable for dialogue continuation. We manually annotated 2,779 facts from Multi-Session Chat and trained a multi-head classifier based on transformer encoders. Combined with the Gemma-300M encoder, the classifier achieves $81.6 \pm 2.6$\% macro F1, outperforming all few-shot LLM baselines (best: GPT-5.4-mini, 72.92\%) by nearly 9 percentage points while requiring substantially fewer computational resources. Error analysis reveals persistent challenges in semantic boundary disambiguation, temporal aspect interpretation, and pragmatic reasoning for followup assessment. The dataset\footnotemark[1] and classifier\footnotemark[2] are publicly available.

**摘要 (中文)**: 大语言模型（LLM）的进步使其在个性化对话系统中得到应用。我们提出一个扩展的个人事实分类标注方案，解决了现有方法（特别是PeaCoK）的局限性。我们的方案引入新类别（人口统计、拥有物）和属性（持续时间、有效性、后续），支持结构化存储、质量过滤和识别适合对话延续的事实。我们手动标注了来自Multi-Session Chat的2,779个事实，并基于Transformer编码器训练了一个多头分类器。结合Gemma-300M编码器，该分类器达到81.6±2.6%的宏F1，以近9个百分点的优势超越所有少样本LLM基线（最佳：GPT-5.4-mini，72.92%），同时所需计算资源大幅减少。错误分析揭示在语义边界消歧、时间方面解释和后续评估的语用推理方面仍存在持续挑战。数据集和分类器已公开发布。

---

## 37. ANCHOR: Abductive Network Construction with Hierarchical Orchestration for Reliable Probability Inference in Large Language Models

**arXiv ID**: [2605.10328](https://arxiv.org/abs/2605.10328)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10328)

**作者**: Wentao Qiu, Guanran Luo, Zhongquan Jian, Jingqi Gao, Meihong Wang 等 (共6人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 10:31:53 UTC

**摘要 (英文)**: A central challenge in large-scale decision-making under incomplete information is estimating reliable probabilities. Recent approaches leverage Large Language Models (LLMs) to generate explanatory factors and elicit coarse-grained probability estimates. Typically, an LLM performs forward abduction to propose factors, each paired with two mutually exclusive attributes, and a Naïve Bayes model is trained over factor combinations to refine the final probabilities. However, sparse factor spaces often yield ``unknown'' outcomes, while expanding factors increases noise and spurious correlations, weakening conditional independence and degrading reliability. To address these limitations, we propose \textsc{Anchor}, an inference framework that orchestrates aggregated Bayesian inference over a hierarchically structured factor space. \textsc{Anchor} first constructs a dense and organized factor space via iterative generation and hierarchical clustering. It then performs context-aware mapping through hierarchical retrieval and refinement, substantially reducing ``unknown'' predictions. Finally, \textsc{Anchor} augments Naïve Bayes with a Causal Bayesian Network to capture latent dependencies among factors, relaxing the strict independence assumption. Experiments show that \textsc{Anchor} markedly reduces ``unknown'' predictions and produces more reliable probability estimates than direct LLM baselines, achieving state-of-the-art performance while significantly reducing time and token overhead.

**摘要 (中文)**: 不完全信息下大规模决策的核心挑战是估计可靠的概率。近期方法利用大语言模型（LLM）生成解释因子并获取粗粒度概率估计。通常，LLM执行前向溯因提出因子，每个因子配对两个互斥属性，并在因子组合上训练朴素贝叶斯模型来精炼最终概率。然而，稀疏的因子空间常产生"未知"结果，而扩展因子增加噪声和虚假相关性，削弱条件独立性并降低可靠性。为解决这些局限，我们提出ANCHOR，一种在层次化因子空间上编排聚合贝叶斯推理的推理框架。ANCHOR首先通过迭代生成和层次聚类构建密集且有组织的因子空间。然后通过层次检索和精炼执行上下文感知映射，大幅减少"未知"预测。最后，ANCHOR用因果贝叶斯网络增强朴素贝叶斯以捕获因子间的潜在依赖，放宽严格的独立性假设。实验表明，ANCHOR显著减少"未知"预测，产生比直接LLM基线更可靠的概率估计，达到最优性能同时大幅降低时间和token开销。

---

## 38. Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering

**arXiv ID**: [2605.10318](https://arxiv.org/abs/2605.10318)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10318)

**作者**: Makbule Gulcin Ozsoy

**分类**: Computation and Language

**发布时间**: 2026-05-11 10:18:13 UTC

**摘要 (英文)**: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.

**摘要 (中文)**: 大语言模型（LLM）允许用户通过将问题翻译为可执行查询来使用自然语言查询数据库。尽管在Text2SQL、Text2SPARQL和Text2Cypher等任务上取得了强劲进展，但大多数现有方法侧重于更好的提示、微调或迭代精炼。然而，它们通常不显式强制结构约束，如语法有效性和模式一致性。这会降低可靠性，因为生成的查询必须同时满足语法规则和数据库模式约束才能执行。在本文中，我们研究如何在Text2Cypher的测试时推理中使用结构化约束。我们侧重于生成后验证以改善查询正确性。我们用顺序过滤过程扩展基于置信度的推理框架，在最终聚合前结合置信度评分、语法验证和模式约束。这使我们能分析不同约束类型如何影响生成的查询。两个指令微调模型的实验表明，基于语法的过滤改善了语法有效性。模式感知过滤通过强制与数据库结构的一致性进一步改善执行质量。然而，更强的过滤也增加了空预测数量并降低执行覆盖率。总体而言，我们展示了在测试时添加简单结构检查能改善Text2Cypher生成的可靠性，并提供了语法和模式约束如何差异化贡献的清晰视角。

---

## 39. Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian Multi-Domain Document Understanding

**arXiv ID**: [2605.10296](https://arxiv.org/abs/2605.10296)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10296)

**作者**: Anton Bazdyrev, Ivan Bashtovyi, Ivan Havlytskyi, Oleksandr Kharytonov, Artur Khodakovskyi

**分类**: Computation and Language, Artificial Intelligence, Information Retrieval, Machine Learning

**发布时间**: 2026-05-11 09:55:28 UTC

**摘要 (英文)**: We participated in the Fifth UNLP shared task on multi-domain document understanding, where systems must answer Ukrainian multiple-choice questions from PDF collections and localize the supporting document and page. We propose a retrieval-augmented pipeline built around three ideas: contextual chunking of PDFs, question-aware dense retrieval and reranking conditioned on both the question and answer options, and constrained answer generation from a small set of reranked passages. Our final system uses Qwen3-Embedding-8B for retrieval, a fine-tuned Qwen3-Reranker-8B for passage ranking, and Qwen3-32B for answer selection. On a held-out split, reranking improves Recall@1 from 0.6957 to 0.7935, while using the top-2 reranked passages raises answer accuracy from 0.9348 to 0.9674. Our best leaderboard run reached 0.9452 on the public leaderboard and 0.9598 on the private leaderboard. Our results suggest that, under strict code-competition constraints, preserving document structure and making relevance estimation aware of the answer space are more effective than adding complex downstream heuristics.

**摘要 (中文)**: 我们参加了第五届UNLP多领域文档理解共享任务，系统需要从PDF集合中回答乌克兰语多选题并定位支撑文档和页面。我们提出了一个围绕三个核心思想构建的检索增强管道：PDF的上下文分块、问题感知的密集检索和以问题与答案选项为条件的重排序，以及从少量重排序段落中进行受限答案生成。最终系统使用Qwen3-Embedding-8B进行检索、微调的Qwen3-Reranker-8B进行段落排序、Qwen3-32B进行答案选择。在留出分割上，重排序将Recall@1从0.6957提高到0.7935，使用top-2重排序段落将答案准确率从0.9348提高到0.9674。最佳排行榜运行在公开排行榜上达到0.9452，在私有排行榜上达到0.9598。我们的结果表明，在严格的代码竞赛约束下，保留文档结构和使相关性估计感知答案空间比添加复杂的下游启发式方法更有效。

---

## 40. DECO-MWE: building a linguistic resource of Korean multiword expressions for feature-based sentiment analysis

**arXiv ID**: [2605.10295](https://arxiv.org/abs/2605.10295)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10295)

**作者**: Jaeho Han, Changhoe Hwang, Seongyong Choi, Gwanghoon Yoo, Eric Laporte 等 (共6人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 09:54:51 UTC

**摘要 (英文)**: This paper aims to construct a linguistic resource of Korean Multiword Expressions for Feature-Based Sentiment Analysis (FBSA): DECO-MWE. Dealing with multiword expressions (MWEs) has been a critical issue in FBSA since many constructs reveal lexical idiosyncrasy. To construct linguistic resources of sentiment MWEs efficiently, we utilize the Local Grammar Graph (LGG) methodology: DECO-MWE is formalized as a Finite-State Transducer that represents lexical-syntactic restrictions on MWEs. In this study, we built a corpus of cosmetics review texts, which show particularly frequent occurrences of MWEs. Based on an empirical examination of the corpus, four types of MWEs have been distinguished. The DECO-MWE thus covers the following four categories: Standard Polarity MWEs (SMWEs), Domain-Dependent Polarity MWEs (DMWEs), Compound Named Entity MWEs (EMWEs) and Compound Feature MWEs (FMWEs). The retrieval performance of the DECO-MWE shows 0.806 f-measure in the test corpus. This study brings a twofold outcome: first, a sizeable general-purpose polarity MWE lexicon, which may be broadly used in FBSA; second, a finite-state methodology adopted in this study to treat domain-dependent MWEs such as idiosyncratic polarity expressions, named entity expressions or feature expressions, and which may be reused in describing linguistic properties of other corpus domains.

**摘要 (中文)**: 本文旨在构建用于基于特征的 sentiment 分析（FBSA）的韩语多词表达语言资源：DECO-MWE。处理多词表达（MWE）一直是FBSA中的关键问题，因为许多构式表现出词汇特异性。为高效构建情感MWE的语言资源，我们利用局部语法图（LGG）方法学：DECO-MWE被形式化为表示MWE词汇-句法限制的有限状态转换器。在本研究中，我们构建了化妆品评论文本语料库，其中MWE出现特别频繁。基于对该语料库的实证考察，区分了四种MWE类型。DECO-MWE涵盖以下四个类别：标准极性MWE（SMWE）、领域依赖极性MWE（DMWE）、复合命名实体MWE（EMWE）和复合特征MWE（FMWE）。DECO-MWE的检索性能在测试语料库上达到0.806的F值。本研究带来双方面成果：首先是一个可广泛用于FBSA的大型通用极性MWE词典；其次是在本研究中采用的有限状态方法学，用于处理领域依赖的MWE（如特异极性表达、命名实体表达或特征表达），该方法学可在描述其他语料库领域的语言特性时复用。

---

## 41. MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading

**arXiv ID**: [2605.10268](https://arxiv.org/abs/2605.10268)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10268)

**作者**: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou 等 (共6人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 09:30:59 UTC

**摘要 (英文)**: To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.

**摘要 (中文)**: 为解决标准注意力机制的二次复杂度带来的长上下文推理挑战，基于智能体记忆的方法应运而生，通常在线性处理文档块时维护动态更新的记忆。为缓解这种边读边记范式中的潜在证据丢失，近期工作集成了检索模块以允许智能体召回在记忆覆写中被丢弃的信息。然而，基于检索的召回同时面临记忆形成时的证据丢失和无效查询引起的干扰。为克服这些局限，我们提出MemReread。基于流式阅读，MemReread绕过中间检索。当最终记忆不足时，它触发问题分解和重读，使过早丢弃的间接事实得以恢复。这种设计支持非线性推理同时保留文档理解的内在逻辑流。为进一步增强实用性，我们引入强化学习框架，在增强长度外推能力的同时根据任务复杂度动态确定重读轮次，从而灵活控制计算开销。大量实验表明，MemReread在长上下文推理任务上一致优于基线框架，同时保持相对于上下文长度的线性时间复杂度。

---

## 42. Building Korean linguistic resource for NLU data generation of banking app CS dialog system

**arXiv ID**: [2605.10241](https://arxiv.org/abs/2605.10241)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10241)

**作者**: Jeongwoo Yoon, On-yu Park, Changhoe Hwang, Gwanghoon Yoo, Eric Laporte 等 (共6人)

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-11 09:16:21 UTC

**摘要 (英文)**: Natural language understanding (NLU) is integral to task-oriented dialog systems, but demands a considerable amount of annotated training data to increase the coverage of diverse utterances. In this study, we report the construction of a linguistic resource named FIAD (Financial Annotated Dataset) and its use to generate a Korean annotated training data for NLU in the banking customer service (CS) domain. By an empirical examination of a corpus of banking app reviews, we identified three linguistic patterns occurring in Korean request utterances: TOPIC (ENTITY, FEATURE), EVENT, and DISCOURSE MARKER. We represented them in LGGs (Local Grammar Graphs) to generate annotated data covering diverse intents and entities. To assess the practicality of the resource, we evaluate the performances of DIET-only (Intent: 0.91 /Topic [entity+feature]: 0.83), DIET+ HANBERT (I:0.94/T:0.85), DIET+ KoBERT (I:0.94/T:0.86), and DIET+ KorBERT (I:0.95/T:0.84) models trained on FIAD-generated data to extract various types of semantic items.

**摘要 (中文)**: 自然语言理解（NLU）是对话式任务系统的核心组成部分，但需要大量标注训练数据以覆盖多样化的话语。在本研究中，我们报告了名为FIAD（金融标注数据集）的语言资源的构建及其用于生成银行客户服务领域韩语NLU标注训练数据的用途。通过对银行应用评论语料库的实证考察，我们识别了韩语请求话语中出现的三种语言模式：TOPIC（ENTITY、FEATURE）、EVENT和DISCOURSE MARKER。我们将它们表示为局部语法图（LGG）以生成覆盖多样意图和实体的标注数据。为评估该资源的实用性，我们评估了使用FIAD生成数据训练的DIET-only（意图：0.91/主题[实体+特征]：0.83）、DIET+HANBERT（I:0.94/T:0.85）、DIET+KoBERT（I:0.94/T:0.86）和DIET+KorBERT（I:0.95/T:0.84）模型的性能，以提取各种类型的语义项。

---

## 43. Route Before Retrieve: Activating Latent Routing Abilities of LLMs for RAG vs. Long-Context Selection

**arXiv ID**: [2605.10235](https://arxiv.org/abs/2605.10235)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10235)

**作者**: Yiwen Chen, Kuan Li, Fuzhen Zhuang, Deqing Wang, Zhao Zhang 等 (共9人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 09:10:55 UTC

**摘要 (英文)**: Recent advances in large language models (LLMs) have expanded the context window to beyond 128K tokens, enabling long-document understanding and multi-source reasoning. A key challenge, however, lies in choosing between retrieval-augmented generation (RAG) and long-context (LC) strategies: RAG is efficient but constrained by retrieval quality, while LC supports global reasoning at higher cost and with position sensitivity. Existing methods such as Self-Route adopt failure-driven fallback from RAG to LC, but remain passive, inefficient, and hard to interpret. We propose Pre-Route, a proactive routing framework that performs structured reasoning before answering. Using lightweight metadata (e.g., document type, length, initial snippet), Pre-Route enables task analysis, coverage estimation, and information-need prediction, producing explainable and cost-efficient routing decisions. Our study shows three key findings: (i) LLMs possess latent routing ability that can be reliably elicited with guidelines, allowing single-sample performance to approach that of multi-sample (Best-of-N) results; (ii) linear probes reveal that structured prompts sharpen the separability of the "optimal routing dimension" in representation space; and (iii) distillation transfers this reasoning structure to smaller models for lightweight deployment. Experiments on LaRA (in-domain) and LongBench-v2 (OOD) confirm that Pre-Route outperforms Always-RAG, Always-LC, and Self-Route baselines, achieving superior overall cost-effectiveness.

**摘要 (中文)**: 大语言模型（LLM）的近期进展将上下文窗口扩展到128K token以上，实现了长文档理解和多源推理。然而，一个关键挑战在于选择检索增强生成（RAG）还是长上下文（LC）策略：RAG高效但受检索质量限制，而LC支持全局推理但成本更高且具有位置敏感性。现有方法如Self-Route采用从RAG到LC的失败驱动回退，但仍是被动的、低效的且难以解释。我们提出Pre-Route，一种在回答前执行结构化推理的主动路由框架。使用轻量级元数据（如文档类型、长度、初始片段），Pre-Route实现任务分析、覆盖度估计和信息需求预测，产生可解释且成本高效的路由决策。我们的研究展示三个关键发现：(i) LLM具有潜在路由能力，可以通过指南可靠地激发，使单样本性能接近多样本（Best-of-N）结果；(ii) 线性探测表明结构化提示锐化了表示空间中"最优路由维度"的可分离性；(iii) 蒸馏将该推理结构迁移到更小模型以实现轻量部署。在LaRA（域内）和LongBench-v2（OOD）上的实验证实Pre-Route优于Always-RAG、Always-LC和Self-Route基线，实现了更优的整体成本效益。

---

## 44. Relative Score Policy Optimization for Diffusion Language Models

**arXiv ID**: [2605.10218](https://arxiv.org/abs/2605.10218)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10218)

**作者**: Zichao Yu, Shengze Xu, Bingqing Jiang, Wenyi Zhang, Difan Zou

**分类**: Computation and Language

**发布时间**: 2026-05-11 08:58:40 UTC

**摘要 (英文)**: Diffusion large language models (dLLMs) offer a promising route to parallel and efficient text generation, but improving their reasoning ability requires effective post-training. Reinforcement learning with verifiable rewards (RLVR) is a natural choice for this purpose, yet its application to dLLMs is hindered by the absence of tractable sequence-level log-ratios, which are central to standard policy optimization. The lack of tractable sequence-level log-ratios forces existing methods to rely on high-variance ELBO-based approximations, where high verifier rewards can amplify inaccurate score estimates and destabilize RL training. To overcome this issue, we propose \textbf{R}elative \textbf{S}core \textbf{P}olicy \textbf{O}ptimization (RSPO), a simple RLVR method that uses verifiable rewards to calibrate noisy likelihood estimates in dLLMs. The core of our algorithm relies on a key observation: a reward advantage can be interpreted not only as an update direction, but also as a target for the relative log-ratio between the current and reference policies. Accordingly, RSPO calibrates this noisy relative log-ratio estimate by comparing its reward advantage with the reward-implied target relative log-ratio, updating the policy according to the gap between the current estimate and the target rather than the raw advantage alone. Experiments on mathematical reasoning and planning benchmarks show that RSPO yields especially strong gains on planning tasks and competitive mathematical-reasoning performance.

**摘要 (中文)**: 扩散大语言模型（dLLM）提供了一条有前景的并行高效文本生成路径，但提升其推理能力需要有效的后训练。使用可验证奖励的强化学习（RLVR）是实现这一目标的自然选择，然而其在dLLM上的应用受到缺乏可处理的序列级对数比率的阻碍，而这是标准策略优化的核心。缺乏可处理的序列级对数比率迫使现有方法依赖高方差的基于ELBO的近似，其中高验证器奖励可能放大不准确的分数估计并破坏RL训练的稳定性。为克服这一问题，我们提出相对分数策略优化（RSPO），一种简单的RLVR方法，使用可验证奖励来校准dLLM中嘈杂的似然估计。我们算法的核心依赖于一个关键观察：奖励优势不仅可以解释为更新方向，还可以解释为当前策略和参考策略之间的相对对数比率目标。相应地，RSPO通过将奖励优势与奖励隐含的目标相对对数比率进行比较来校准该嘈杂的相对对数比率估计，根据当前估计与目标之间的差距而非原始优势来更新策略。在数学推理和规划基准上的实验表明，RSPO在规划任务上取得特别强的增益，在数学推理上也有竞争力的表现。

---

## 45. The Impact of Editorial Intervention on Detecting Native Language Traces

**arXiv ID**: [2605.10216](https://arxiv.org/abs/2605.10216)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10216)

**作者**: Ahmet Yavuz Uluslu, Mark Gales, Kate Knill, Gerold Schneider

**分类**: Computation and Language

**发布时间**: 2026-05-11 08:58:08 UTC

**摘要 (英文)**: Native Language Identification (NLI) is the task of determining an author's native language (L1) from their non-native writings. With the advent of human-AI co-authorship, non-native texts are routinely corrected and rewritten by large language models, fundamentally altering the linguistic features NLI models depend on. In this paper, we investigate the robustness of L1 traces across increasing degrees of editorial intervention. By processing 450 essays from the Write & Improve 2024 corpus through varying levels of grammatical error correction (GEC) and paraphrasing, we demonstrate that L1 attribution does not entirely depend on surface-level errors. Instead, the detection models leverage deeper L1 features: unidiomatic lexico-semantic choices, pragmatic transfer, and the author's underlying cultural perspective. We find that minimal edits preserve these structural traces and maintain high profiling accuracy. In contrast, fluency edits and paraphrasing normalize these L1 features, leading to a severe degradation in performance.

**摘要 (中文)**: 母语识别（NLI）是根据作者的非母语写作确定其母语（L1）的任务。随着人-AI共著的出现，非母语文本经常被大语言模型纠正和改写，从根本上改变了NLI模型依赖的语言特征。在本文中，我们研究了在递增编辑干预程度下L1痕迹的鲁棒性。通过将Write & Improve 2024语料库中的450篇文章经过不同级别的语法错误纠正（GEC）和改写处理，我们证明L1归属并不完全依赖于表面错误。相反，检测模型利用更深层的L1特征：非惯用的词汇-语义选择、语用迁移以及作者的潜在文化视角。我们发现最小编辑保留了这些结构痕迹并维持了较高的画像准确率。相比之下，流利度编辑和改写使这些L1特征标准化，导致性能严重退化。

---

## 46. To Redact, or not to Redact? A Local LLM Approach to Deliberative Process Privilege Classification

**arXiv ID**: [2605.10211](https://arxiv.org/abs/2605.10211)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10211)

**作者**: Maik Larooij, David Graus

**分类**: Computation and Language, Artificial Intelligence, Information Retrieval

**发布时间**: 2026-05-11 08:55:09 UTC

**摘要 (英文)**: Government transparency laws, like the Freedom of Information (FOIA) acts in the United States and United Kingdom, and the Woo (Open Government Act) in the Netherlands, grant citizens the right to directly request documents from the government. As these documents might contain sensitive information, such as personal information or threats to national security, the laws allow governments to redact sensitive parts of the documents prior to release. We build on prior research to perform automatic sensitivity classification for the FOIA Exemption 5 deliberative process privilege using Large Language Models (LLMs). However, processing documents not yet cleared for review via third-party cloud APIs is often legally or politically untenable. Therefore, in this work, we perform sensitivity classification with a small, local model, deployable on consumer-grade hardware (Qwen3.5 9B). We compare eight variants of applying LLMs for sentence classification, using well-known prompting techniques, and find that a combination of Chain-of-Thought prompting and few-shot prompting with error-based examples outperforms classification models of earlier work in terms of recall and F2 score. This method also closely approaches the performance of a widely-used, cost-efficient commercial model (Gemini 2.5 Flash). In an additional analysis, we find that sentences that are predicted as deliberative contain more verbs that indicate the expression of opinions, and are more often phrased in in first-person. Above all, deliberativeness seems characterized by the presence of a combination of multiple indicators, in particular the combination of first-person words with a verb for expressing opinion.

**摘要 (中文)**: 政府透明度法律，如美国和英国的信息自由法（FOIA）以及荷兰的Woo（开放政府法），赋予公民直接向政府请求文件的权利。由于这些文件可能包含敏感信息（如个人信息或对国家安全的威胁），法律允许政府在发布前编辑文件的敏感部分。我们在先前研究基础上，使用大语言模型（LLM）对FOIA豁免5审议过程特权执行自动敏感度分类。然而，通过第三方云API处理尚未通过审查的文件在法律或政治上通常是不可行的。因此，在本工作中，我们使用可部署在消费级硬件上的小型本地模型（Qwen3.5 9B）执行敏感度分类。我们比较了八种将LLM应用于句子分类的变体，使用众所周知的提示技术，发现思维链提示与基于错误的少样本提示的组合在召回率和F2分数上优于先前工作的分类模型。该方法也接近了广泛使用的成本效益型商业模型（Gemini 2.5 Flash）的性能。在额外分析中，我们发现被预测为审议性的句子包含更多表示观点表达的动词，且更常以第一人称表述。最重要的是，审议性的特征似乎在于多个指标组合的存在，特别是第一人称词与表达观点的动词的组合。

---

## 47. How Should LLMs Listen While Speaking? A Study of User-Stream Routing in Full-Duplex Spoken Dialogue

**arXiv ID**: [2605.10199](https://arxiv.org/abs/2605.10199)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10199)

**作者**: Hui Lu, Xueyuan Chen, Huimeng Wang, Shuhai Peng, Shiyin Kang 等 (共7人)

**分类**: Computation and Language, Audio and Speech Processing

**发布时间**: 2026-05-11 08:46:47 UTC

**摘要 (英文)**: Full-duplex spoken dialogue requires a model to keep listening while generating its own spoken response. This is challenging for large language models (LLMs), which are designed to extend a single coherent sequence and do not naturally support user input arriving during generation. We argue that how the user stream is routed into the LLM is therefore a key architectural question for full-duplex modeling. To study this question, we extend a text-only LLM into a unified full-duplex spoken dialogue system and compare two routing strategies under a shared training pipeline: (i) channel fusion, which injects the user stream directly into the LLM input, and (ii) cross-attention routing, which keeps the user stream as external memory accessed through cross-attention adapters. Experiments on spoken question answering and full-duplex interaction benchmarks reveal a clear tradeoff. Channel fusion yields stronger semantic grounding and consistently better question-answering performance. However, under semantically overlapping conditions such as user interruptions, it is more vulnerable to context corruption: if the model fails to stop in time, the overlapping user stream can interfere with ongoing generation and lead to semantically incoherent continuations. Cross-attention routing underperforms on question answering, but better preserves the LLM generation context and is more robust to this failure mode. These results establish user-stream routing as a central design axis in full-duplex spoken dialogue and offer practical guidance on the tradeoff between semantic integration and context robustness. We provide a demo page for qualitative inspection.

**摘要 (中文)**: 全双工语音对话要求模型在生成自己的语音回复时保持监听。这对大语言模型（LLM）具有挑战性，因为它们被设计用于扩展单个连贯序列，不自然支持在生成过程中到达的用户输入。因此，我们认为用户流如何路由到LLM是全双工建模的关键架构问题。为研究此问题，我们将纯文本LLM扩展为统一的全双工语音对话系统，并在共享训练管道下比较两种路由策略：(i) 通道融合，将用户流直接注入LLM输入；(ii) 交叉注意力路由，将用户流作为通过交叉注意力适配器访问的外部内存保留。在语音问答和全双工交互基准上的实验揭示了明确的权衡。通道融合产生更强的语义接地，一致的问答性能更好。然而，在语义重叠条件下（如用户打断），更容易受到上下文破坏：如果模型未能及时停止，重叠的用户流会干扰正在进行的生成并导致语义不连贯的延续。交叉注意力路由在问答上表现不佳，但更好地保留了LLM生成上下文对此失败模式更鲁棒。这些结果确立了用户流路由作为全双工语音对话的中心设计轴，并在语义集成与上下文鲁棒性之间提供了实际权衡指导。我们提供了演示页面用于定性检查。

---

## 48. LegalCiteBench: Evaluating Citation Reliability in Legal Language Models

**arXiv ID**: [2605.10186](https://arxiv.org/abs/2605.10186)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10186)

**作者**: Sijia Chen, Hang Yin, Shunfan Zhou

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 08:37:54 UTC

**摘要 (英文)**: Large language models (LLMs) are increasingly integrated into legal drafting and research workflows, where incorrect citations or fabricated precedents can cause serious professional harm. Existing legal benchmarks largely emphasize statutory reasoning, contract understanding, or general legal question answering, but they do not directly study a central common-law failure mode: when asked to provide case authorities without external grounding, models may return plausible-looking but incorrect citations or cases. We introduce LegalCiteBench, a benchmark for studying closed-book citation recovery, citation verification, and case matching in legal language models. LegalCiteBench contains approximately 24K evaluation instances constructed from 1,000 real U.S. judicial opinions from the Case Law Access Project. The benchmark covers five citation-centric tasks: citation retrieval, citation completion, citation error detection, case matching, and case verification and correction. Across 21 LLMs, exact citation recovery remains highly challenging in this closed-book setting: even the strongest models score below 7/100 on citation retrieval and completion. Within the evaluated models, scale and legal-domain pretraining provide limited gains and do not resolve this difficulty. Models also frequently provide concrete but incorrect or low-overlap authorities under our evaluation protocol, with Misleading Answer Rates (MAR) exceeding 94% for 20 of 21 evaluated models on retrieval-heavy tasks. A prompt-only abstention experiment shows that explicit uncertainty instructions reduce some confident fabrication but do not improve citation correctness. LegalCiteBench is intended as a diagnostic framework for studying authority generation failures, verification behavior, and abstention when external grounding is absent, incomplete, or bypassed.

**摘要 (中文)**: 大语言模型越来越多地集成到法律起草和研究工作流程中，错误的引用或捏造先例可能导致严重的职业损害。现有法律基准主要强调制定法推理、合同理解或一般法律问答，但并未直接研究一个核心普通法失败模式：当要求提供案例权威而不进行外部接地时，模型可能返回看似合理但不正确的引用或案例。我们引入LegalCiteBench，一个用于研究法律语言模型中闭卷引用恢复、引用验证和案例匹配的基准。LegalCiteBench包含约24K个评估实例，由来自案例法访问项目的1000个真实美国司法意见构建。基准涵盖五个以引用为中心的任务：引用检索、引用补全、引用错误检测、案例匹配和案例验证与纠正。在21个LLM中，在此闭卷设置下精确引用恢复仍然极具挑战性：即使最强的模型在引用检索和补全上也得分低于7/100。在评估的模型中，规模和法律领域预训练提供的增益有限，无法解决此困难。模型在我们的评估协议下也经常提供具体但错误或低重叠的权威，在检索密集型任务上20/21个模型的误导答案率(MAR)超过94%。仅提示的不确定实验表明明确的 uncertainty 指令减少了一些自信的捏造但不提高引用正确性。LegalCiteBench旨在作为研究权威生成失败、验证行为和外部接地缺失、不完整或被绕过时拒绝回答的诊断框架。

---

## 49. When Reviews Disagree: Fine-Grained Contradiction Analysis in Scientific Peer Reviews

**arXiv ID**: [2605.10171](https://arxiv.org/abs/2605.10171)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10171)

**作者**: Sandeep Kumar, Yash Kamdar, Abid Hossain, Bharti Kumari, Tanik Saikh 等 (共6人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 08:20:58 UTC

**摘要 (英文)**: Scientific peer reviews frequently contain conflicting expert judgments, and the increasing scale of conference submissions makes it challenging for Area Chairs and editors to reliably identify and interpret such disagreements. Existing approaches typically frame reviewer disagreement as binary contradiction detection over isolated sentence pairs, abstracting away the review-level context and obscuring differences in the severity of evaluative conflict. In this work, we introduce a fine-grained formulation of reviewer contradiction analysis that operates over full peer reviews by explicitly identifying contradiction evidence spans and assigning graded disagreement intensity scores. To support this task, we present RevCI, an expert-annotated benchmark of peer-review pairs with evidence-level contradiction annotations with graded intensity labels. We further propose IMPACT, a structured multi-agent framework that integrates aspect-conditioned evidence extraction, deliberative reasoning, and adjudication to model reviewer contradictions and their intensity. To support efficient deployment, we distill IMPACT into TIDE, a small language model that predicts contradiction evidence and intensity in a single forward pass. Experimental results show that IMPACT substantially outperforms strong single-agent and generic multi-agent baselines in both evidence identification and intensity agreement, while TIDE achieves competitive performance at significantly lower inference cost.

**摘要 (中文)**: 科学同行评审经常包含相互冲突的专家判断，会议提交规模的不断增长使区域主席和编辑难以可靠地识别和解释这些分歧。现有方法通常将审稿人分歧框定为孤立句子对上的二值矛盾检测，忽略了评审级上下文并模糊了评估冲突严重程度的差异。在本文中，我们引入了一种细粒度的审稿人矛盾分析 formulation，它通过明确识别矛盾证据跨度并分配分级的不一致强度分数，在完整同行评审上运行。为支持此任务，我们呈现RevCI，一个同行评审对 expert-annotated 基准，包含带有分级强度标签的证据级矛盾注释。我们进一步提出IMPACT，一个结构化多智能体框架，整合方面条件证据提取、审议推理和仲裁，以模拟审稿人矛盾及其强度。为支持高效部署，我们将IMPACT蒸馏为TIDE，一个小语言模型，在单次前向传播中预测矛盾证据和强度。实验结果表明，IMPACT在证据识别和强度一致性上都显著优于强单智能体和通用多智能体基线，而TILE以显著更低的推理成本实现了有竞争力的性能。

---

## 50. ASTRA-QA: A Benchmark for Abstract Question Answering over Documents

**arXiv ID**: [2605.10168](https://arxiv.org/abs/2605.10168)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10168)

**作者**: Shu Wang, Shansong Zhou, Xinyang Wang, Shiwei Wang, Hulong Wu 等 (共6人)

**分类**: Computation and Language, Information Retrieval

**发布时间**: 2026-05-11 08:17:24 UTC

**摘要 (英文)**: Document-based question answering (QA) increasingly includes abstract questions that require synthesizing scattered information from long documents or across multiple documents into coherent answers. However, this setting is still poorly supported by existing benchmarks and evaluation methods, which often lack stable abstract references or rely on coarse similarity metrics and unstable head-to-head comparisons. To alleviate this issue, we introduce ASTRA-QA, a benchmark for AbSTRAct Question Answering over documents. ASTRA-QA contains 869 QA instances over academic papers and news documents, covering five abstract question types and three controlled retrieval scopes. Each instance is equipped with explicit evaluation annotations, including answer topic sets, curated unsupported topics, and aligned evidence. Building on these annotations, ASTRA-QA assesses whether answers cover required key points and avoid unsupported content by directly scoring topic coverage and curated unsupported content, enabling scalable evaluation without exhaustive head-to-head comparisons. Experiments with representative Retrieval-Augmented Generation (RAG) methods spanning vanilla, graph-based, and hierarchical retrieval settings show that ASTRA-QA provides reference-grounded diagnostics for coverage, hallucination, and retrieval-scope robustness. Our dataset and code are available at https://xinyangsally.github.io/astra-benchmark.

**摘要 (中文)**: 基于文档的问答 increasingly includes抽象问题，这些问题需要从长文档或跨多个文档综合分散信息到连贯答案中。然而，现有基准和评估方法对此设置支持不足，这些方法通常缺乏稳定的抽象参考或依赖粗粒度相似度指标和不稳定的正面比较。为缓解此问题，我们引入ASTRA-QA，一个用于文档抽象问答的基准。ASTRA-QA包含869个学术论文和新闻文档上的问答实例，涵盖五种抽象问题类型和三种受控检索范围。每个实例都配有明确的评估注释，包括答案主题集、策划的不支持主题和对齐证据。基于这些注释，ASTRA-QA通过直接评分主题覆盖和策划的不支持内容来评估答案是否覆盖所需要点并避免不支持内容，实现可扩展评估而无需穷举正面比较。使用代表性的检索增强生成（RAG）方法（涵盖 vanilla、基于图和分层检索设置）的实验表明，ASTRA-QA为覆盖、幻觉和检索范围鲁棒性提供了参考接地诊断。我们的数据集和代码可在https://xinyangsally.github.io/astra-benchmark获取。

---

## 51. NyayaAI: An AI-Powered Legal Assistant Using Multi-Agent Architecture and Retrieval-Augmented Generation

**arXiv ID**: [2605.10155](https://arxiv.org/abs/2605.10155)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10155)

**作者**: Deepanshu, Divi Saxena, Deepali Rana, Ayesha Varshney, Sahinur Rahman Laskar

**分类**: Computation and Language

**发布时间**: 2026-05-11 08:04:07 UTC

**摘要 (英文)**: Legal information in India remains largely inaccessible due to the complexity of legal language and the sheer volume of legal documentation involved in research and case analysis. This paper presents NyayaAI, an AI-powered legal assistant that automates and simplifies legal workflows for lawyers, law students, and general users. The system combines Large Language Models with a Retrieval-Augmented Generation pipeline grounded in a curated Indian legal knowledge base comprising constitutional provisions, statutes, case laws, and judicial precedents. A multi-agent architecture orchestrated through the Mastra TypeScript framework coordinates a main agent with specialized sub-agents handling legal research, document summarization, case law retrieval, and drafting assistance. A compliance module validates all responses before delivery. Domain classification achieved 70\% precision across test samples, with RAG retrieval precision at 74\% and overall response accuracy at 72\%, demonstrating that structured multi-agent LLM systems can meaningfully improve legal accessibility and workflow efficiency. The code\footnote{https://github.com/B97784/NyayaAI} is made publicly available for the benefit of the research community.

**摘要 (中文)**: 印度的法律信息因法律语言复杂性和研究和案例分析所涉及的大量法律文档而 largely inaccessible。本文呈现NyayaAI，一个AI驱动的法律助手，为律师、法学院学生和普通用户自动化和简化法律工作流程。该系统将大语言模型与基于检索增强生成的管道结合，接地于策划的印度法律知识库，包含宪法条款、法规、案例法和司法先例。通过Mastra TypeScript框架编排的多智能体架构协调主智能体和专门处理法律研究、文档摘要、案例法检索和起草协助的子智能体。合规模块在交付前验证所有响应。领域分类在测试样本上达到70%精确率，RAG检索精确率为74%，整体响应准确率为72%，表明结构化多智能体LLM系统可以显著改善法律可访问性和工作流程效率。代码向研究社区公开提供。

---

## 52. Synthetic Pre-Pre-Training Improves Language Model Robustness to Noisy Pre-Training Data

**arXiv ID**: [2605.10129](https://arxiv.org/abs/2605.10129)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10129)

**作者**: Xu Guo, Runyu Peng, Jian Tong, Yunhua Zhou, Haijun Lv 等 (共7人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 07:40:39 UTC

**摘要 (英文)**: Large language models (LLMs) rely on web-scale corpora for pre-training. The noise inherent in these datasets tends to obscure meaningful patterns and ultimately degrade model performance. Data curation mitigates but cannot eliminate such noise, so pre-training corpora remain noisy in practice. We therefore study whether a lightweight pre-pre-training (PPT) stage based on synthetic data with learnable temporal structure helps resist noisy data during the pre-training (PT) stage. Across various corruption settings, our method consistently improves robustness to noise during PT, with larger relative gains at higher noise levels. For a 1B-parameter model, a synthetic PPT stage with only 65M tokens achieves the same final loss as the baseline while using up to 49\% fewer natural-text PT tokens across different noise levels. Mechanistic analyses suggest PPT does not immediately suppress attention to noisy tokens. Rather, PPT-initialized models gradually downweight attention between corrupted tokens during noisy PT. This indicates that synthetic PPT inhibits noise self-modeling and shapes the subsequent optimization trajectory. Code is available at https://github.com/guox18/formal-language-prepretraining.

**摘要 (中文)**: 大语言模型依赖网络规模的语料库进行预训练。这些数据集中固有的噪声 tends to obscure 有意义的模式并最终降低模型性能。数据管理可以缓解但无法消除此类噪声，因此预训练语料库在实践中仍然存在噪声。因此，我们研究是否基于具有可学习时间结构的合成数据的轻量级预预训练（PPT）阶段有助于在预训练（PT）阶段抵抗噪声。在各种腐败设置下，我们的方法一致提高PT期间对噪声的鲁棒性，在更高噪声水平下获得更大的相对增益。对于1B参数模型，仅65M token的合成PPT阶段在不同的噪声水平下使用最多少49%的自然文本PT token即可达到与基线相同的最终损失。机制分析表明PPT不会立即抑制对噪声token的注意力。相反，PPT初始化的模型在噪声PT期间逐渐降低腐败token之间的注意力。这表明合成PPT抑制噪声自我建模并塑造后续优化轨迹。代码可在https://github.com/guox18/formal-language-prepretraining获取。

---

## 53. SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution

**arXiv ID**: [2605.10114](https://arxiv.org/abs/2605.10114)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10114)

**作者**: Xiangcheng Meng, Shu Wang, Yixiang Fang

**分类**: Computation and Language

**发布时间**: 2026-05-11 07:31:48 UTC

**摘要 (英文)**: Large Language Model (LLM)-based agents (e.g., OpenClaw) increasingly rely on reusable skill libraries to solve artifact-rich tasks such as document-centric workflows and data-intensive analysis. As these libraries grow, a few works have attempted to study the Retrieval-Augmented Execution (RAE), which often first retrieves some external skills and other knowledge, then compiles the context using retrieved skills, and finally executes the task. Existing works mainly focus on optimizing skill retrieval and task execution, and they pay little attention to how to effectively organize the selected skill evidence in a form that is compact, grounded, and immediately usable for the downstream executors to complete tasks. To fill this gap, we propose SkillRAE, a two-stage RAE approach focusing on skill-based context compilation, which consists of the offline and online stages. Specifically, in the offline indexing stage, it builds a multi-level skill graph over skill communities, skills, and reusable subunits, for capturing their relationships. In the online retrieval stage, it first performs skill-ranked retrieval with selected-subunit evidence export in the graph, and then applies rescue-aware compact compilation to recover the key evidence. Together, these components compile a coarse-ranked skill set into a task-specific context that is compact, grounded, and immediately usable. Experiments on two public benchmarks show that SkillRAE achieves a significant improvement over baselines for RAE. For example, on SkillsBench, it achieves an improvement of 11.7% over the SOTA method. Ablation studies further show that our context compilation is crucial, instead of a mere prompt addition.

**摘要 (中文)**: 基于大语言模型（LLM）的智能体（如OpenClaw） increasingly依赖可复用技能库来解决丰富的工件任务，如以文档为中心的工作流和数据分析。随着这些技能库的增长，一些工作尝试研究检索增强执行（RAE），它通常首先检索一些外部技能和其他知识，然后使用检索到的技能编译上下文，最后执行任务。现有工作主要关注优化技能检索和任务执行，而很少关注如何有效地将选定的技能证据组织成紧凑、接地且下游执行器可立即使用的形式。为填补这一空白，我们提出SkillRAE，一个两阶段RAE方法，专注于基于技能的上下文编译，包含离线和在线阶段。具体来说，在离线索引阶段，它在技能社区、技能和可复用子单元之上构建多级技能图，以捕获它们的关系。在在线检索阶段，它首先在图中执行技能排序检索并导出选定的子单元证据，然后应用救援感知的紧凑编译来恢复关键证据。这些组件共同将粗略排序的技能集编译成紧凑、接地且立即可用的任务特定上下文。在两个公开基准上的实验表明，SkillRAE在RAE上比基线取得显著改进。例如，在SkillsBench上，它比SOTA方法提高了11.7%。消融研究进一步表明我们的上下文编译至关重要，而不是简单的提示添加。

---

## 54. GLiNER-Relex: A Unified Framework for Joint Named Entity Recognition and Relation Extraction

**arXiv ID**: [2605.10108](https://arxiv.org/abs/2605.10108)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10108)

**作者**: Ihor Stepanov, Oleksandr Lukashov, Mykhailo Shtopko, Vivek Kalyanarangan

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-11 07:23:49 UTC

**摘要 (英文)**: Joint named entity recognition (NER) and relation extraction (RE) is a fundamental task in natural language processing for constructing knowledge graphs from unstructured text. While recent approaches treat NER and RE as separate tasks requiring distinct models, we introduce GLiNER-Relex, a unified architecture that extends the GLiNER framework to perform both entity recognition and relation extraction in a single model. Our approach leverages a shared bidirectional transformer encoder to jointly represent text, entity type labels, and relation type labels, enabling zero-shot extraction of arbitrary entity and relation types specified at inference time. GLiNER-Relex constructs entity pair representations from recognized spans and scores them against relation type embeddings using a dedicated relation scoring module. We evaluate our model on four standard relation extraction benchmarks: CoNLL04, DocRED, FewRel, and CrossRE, and demonstrate competitive performance against both specialized relation extraction models and large language models, while maintaining the computational efficiency characteristic of the GLiNER family. The model is released as an open-source Python package with a simple inference API that allows users to specify arbitrary entity and relation type labels at inference time and obtain both entities and relation triplets in a single call. All models and code are publicly available.

**摘要 (中文)**: 联合命名实体识别（NER）和关系抽取（RE）是从非结构化文本构建知识图谱的自然语言处理基础任务。最近的方法将NER和RE视为需要不同模型的单独任务，我们引入GLiNER-Relex，一个统一架构，扩展GLiNER框架以在单个模型中执行实体识别和关系抽取。我们的方法利用共享双向transformer编码器共同表示文本、实体类型标签和关系类型标签，支持在推理时指定任意实体和关系类型的零样本抽取。GLiNER-Relex从识别的跨度构建实体对表示，并使用专门的关系评分模块将其与关系类型嵌入进行评分。我们在四个标准关系抽取基准上评估我们的模型：CoNLL04、DocRED、FewRel和CrossRE，并展示与专门关系抽取模型和大型语言模型相比具有竞争力的性能，同时保持GLiNER系列的计算效率特性。该模型作为开源Python包发布，具有简单的推理API，允许用户在推理时指定任意实体和关系类型标签并在单次调用中获取实体和关系三元组。所有模型和代码均公开可用。

---

## 55. FERA: Uncertainty-Aware Federated Reasoning for Large Language Models

**arXiv ID**: [2605.10082](https://arxiv.org/abs/2605.10082)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10082)

**作者**: Ruhan Wang, Chengkai Huang, Zhiyong Wang, Junda Wu, Rui Wang 等 (共9人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 07:04:51 UTC

**摘要 (英文)**: Large language models (LLMs) exhibit strong reasoning capabilities when guided by high-quality demonstrations, yet such data is often distributed across organizations that cannot centralize it due to regulatory, proprietary, or institutional constraints. We study federated reasoning, where a server improves multi-step reasoning by coordinating with heterogeneous clients holding private demonstrations, without centralized training or raw data sharing. The key challenge is that client reliability is query-dependent, while the server cannot inspect client data to determine which contributions are trustworthy. To address this, we propose Uncertainty-Aware Federated Reasoning (FERA), a training-free framework based on iterative server-client co-refinement. Across communication rounds, clients generate reasoning traces with lightweight uncertainty estimates, and the server synthesizes them into improved reasoning that is redistributed as context for the next round, progressively improving both server outputs and client-side reasoning. Within each round, Uncertainty-Aware Self-Critique Aggregation (UA-SCA) resolves conflicts among heterogeneous client traces through query-dependent trust weighting and structured cross-client verification. Rather than simply discarding low-quality traces, UA-SCA revises flawed reasoning steps to recover useful information. We provide theoretical guarantees showing that the proposed iterative protocol converges and that uncertainty-aware weighting accelerates convergence. Experiments on multiple reasoning benchmarks show that FERA consistently outperforms both federated training and training-free baselines, achieving progressively higher accuracy across rounds while maintaining communication and computational efficiency.

**摘要 (中文)**: 大语言模型在高质量演示的引导下表现出强大的推理能力，但这些数据通常分布在由于监管、专有或机构限制而无法集中化的组织中。我们研究联邦推理，服务器通过与持有私人演示的异构客户端协调来改进多步推理，而无需集中训练或原始数据共享。关键挑战是客户端可靠性依赖于查询，而服务器无法检查客户端数据来确定哪些贡献是可信的。为此，我们提出不确定性感知联邦推理（FERA），一个基于迭代服务器-客户端协同精炼的无训练框架。在通信轮次中，客户端生成带有轻量级不确定性估计的推理痕迹，服务器将它们综合成改进的推理，作为下一轮的上下文重新分配，逐步提高服务器输出和客户端推理。在每轮内，不确定性感知自批评聚合（UA-SCA）通过查询依赖的信任加权和结构化跨客户端验证来解决异构客户端痕迹之间的冲突。UA-SCA不是简单地丢弃低质量痕迹，而是修正有缺陷的推理步骤以恢复有用信息。我们提供理论保证，表明所提出的迭代协议收敛，且不确定性感知加权加速收敛。在多个推理基准上的实验表明，FERA一致优于联邦训练和无训练基线，在保持通信和计算效率的同时实现轮次间逐步提高的准确性。

---

## 56. PHAGE: Patent Heterogeneous Attention-Guided Graph Encoder for Representation Learning

**arXiv ID**: [2605.10073](https://arxiv.org/abs/2605.10073)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10073)

**作者**: Yongmin Yoo, Qiongkai Xu, Zhangkai Wu, Longbing Cao

**分类**: Computation and Language

**发布时间**: 2026-05-11 06:54:44 UTC

**摘要 (英文)**: Patent claims form a directed dependency structure in which dependent claims inherit and refine the scope of earlier claims; however, existing patent encoders linearize claims as text and discard this hierarchy. Directly encoding this structure into self-attention poses two challenges: claim dependencies mix relation types that differ in semantics and extraction reliability, and the dependency graph is defined over claims while Transformers attend over tokens. PHAGE addresses the first challenge through a deterministic graph construction pipeline that separates near-deterministic legal citations from noisier rule-based technical relations, preserving type distinctions as heterogeneous edges. It addresses the second through a connectivity mask and learnable relation-aware biases that lift claim-level topology into token-level attention, allowing the encoder to differentially weight each relation type. A dual-granularity contrastive objective then aligns representations with both inter-patent taxonomy and intra-patent topology. PHAGE outperforms all baselines on classification, retrieval, and clustering, showing that intra-document claim topology is a stronger inductive bias than inter-document structure and that this bias persists in the encoder weights after training.

**摘要 (中文)**: 专利权利要求形成有向依赖结构，其中从属权利要求继承和精炼早期权利要求的范围；然而，现有专利编码器将权利要求线性化为文本并丢弃此层次结构。直接将此结构编码到自注意力中面临两个挑战：权利要求依赖混合语义和抽取可靠性不同的关系类型，且依赖图在权利要求上定义，而Transformers在token上关注。PHAGE通过确定性图构建管道解决第一个挑战，将近确定性的法律引用与更嘈杂的基于规则的技术关系分开，将类型区分保留为异构边。它通过连接掩码和可学习的relation-aware偏差解决第二个问题，将权利要求级拓扑提升到token级注意力，使编码器能够差异化加权每个关系类型。然后双粒度对比目标将表示与专利间分类学和专利内拓扑对齐。PHAGE在分类、检索和聚类上优于所有基线，表明文档内权利要求拓扑是比文档间结构更强的归纳偏置，且该偏置在训练后仍保留在编码器权重中。

---

## 57. NCO: A Versatile Plug-in for Handling Negative Constraints in Decoding

**arXiv ID**: [2605.10065](https://arxiv.org/abs/2605.10065)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10065)

**作者**: Hyundong Jin, Yo-Sub Han

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 06:43:42 UTC

**摘要 (英文)**: Controlling Large Language Models (LLMs) to prevent the generation of undesirable content, such as profanity and personally identifiable information (PII), has become increasingly critical. While earlier approaches relied on post-processing or resampling, recent research has shifted towards constrained decoding methods that control outputs during generation to mitigate high computational costs and quality degradation. However, preventing multiple forbidden hard constraints or regex constraints from appearing anywhere in the output is computationally challenging. A straightforward solution is to convert these constraints into a single automaton that tracks all forbidden patterns during decoding, but this often becomes impractically large. Standard regex engines also do not readily support the operations needed to build such a constraint, such as complement and intersection. In order to address these limitations, we propose NCO, a decoding strategy that performs online pattern matching over finite hard constraints and regex constraints, reducing computational overhead without inducing state explosion. NCO is fully compatible with standard inference strategies, including various sampling methods and beam search, while also supporting soft masking for probabilistic suppression. We empirically demonstrate its effectiveness across practical tasks, including PII and profanity suppression. Our implementation is available at https://github.com/hyundong98/NCO-Decoding.git .

**摘要 (中文)**: 控制大语言模型（LLM）防止生成不良内容（如脏话和个人可识别信息PII）变得越来越关键。虽然 earlier approaches依赖于后处理或重采样，但最近的研究转向约束解码方法，在生成期间控制输出以减轻高计算成本和质量下降。然而，防止多个禁止的硬约束或regex约束出现在输出中的任何地方在计算上具有挑战性。一个直接的解决方案是将这些约束转换为在解码期间跟踪所有禁止模式的单个自动机，但这通常变得不切实际地大。标准regex引擎也不容易支持构建此类约束所需的操作，如补集和交集。为了解决这些限制，我们提出NCO，一个在有限硬约束和regex约束上执行在线模式匹配的解码策略，减少计算开销而不会导致状态爆炸。NCO完全兼容标准推理策略，包括各种采样方法和波束搜索，同时还支持概率抑制的软掩码。我们通过实证展示了其在实际任务中的有效性，包括PII和脏话抑制。我们的实现可在https://github.com/hyundong98/NCO-Decoding.git获取。

---

## 58. Not-So-Strange Love: Language Models and Generative Linguistic Theories are More Compatible than They Appear

**arXiv ID**: [2605.10061](https://arxiv.org/abs/2605.10061)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10061)

**作者**: R. Thomas McCoy

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 06:38:40 UTC

**摘要 (英文)**: Futrell and Mahowald (2025) frame the success of neural language models (LMs) as supporting gradient, usage-based linguistic theories. I argue that LMs can also instantiate theories based on formal structures - the types of theories seen in the generative tradition. This argument expands the space of theories that can be tested with LMs, potentially enabling reconciliations between usage-based and generative accounts.

**摘要 (中文)**: Futrell和Mahowald（2025）将神经语言模型（LM）的成功框定为支持渐变、基于使用的语言理论。我认为LM也可以实例化基于形式结构的理论——生成传统中看到的理论类型。这一论点扩展了可以用LM测试的理论空间，可能实现基于使用和生成解释之间的调和。

---

## 59. Swarm Skills: A Portable, Self-Evolving Multi-Agent System Specification for Coordination Engineering

**arXiv ID**: [2605.10052](https://arxiv.org/abs/2605.10052)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10052)

**作者**: Xinyu Zhang, Zhicheng Dou, Deyang Li, Jianjun Tao, Shuo Cheng 等 (共13人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 06:26:58 UTC

**摘要 (英文)**: As artificial intelligence engineering paradigms shift from single-agent Prompt and Context Engineering toward multi-agent \textbf{Coordination Engineering}, the ability to codify and systematically improve how multiple agents collaborate has emerged as a critical bottleneck. While single-agent skills can now be distributed as portable assets, multi-agent coordination protocols remain locked within framework-internal code or static configurations, preventing them from being shared across systems or autonomously improved over time. We propose \textbf{Swarm Skills}, a portable specification that extends the Anthropic Skills standard with multi-agent semantics. Swarm Skills turns multi-agent workflows into first-class, distributable assets that consist of roles, workflows, execution bounds, and a built-in semantic structure for self-evolution. To operationalize the specification's evolving nature, we present a companion self-evolution algorithm that automatically distills successful execution trajectories into new Swarm Skills and continuously patches existing ones based on multi-dimensional scoring (Effectiveness, Utilization, and Freshness), eliminating the need for human-in-the-loop oversight during the refinement process. Through an architectural compatibility analysis and a comprehensive qualitative case study using the open-source JiuwenSwarm reference implementation, we demonstrate how Swarm Skills achieves zero-adapter cross-agent portability via progressive disclosure, enabling agent teams to self-evolve their coordination strategies without framework lock-in.

**摘要 (中文)**: 随着人工智能工程范式从单智能体提示和上下文工程转向多智能体**协调工程**，系统化改进多个智能体协作方式的能力已成为关键瓶颈。虽然单智能体技能现在可以分发为可移植资产，但多智能体协调协议仍锁定在框架内部代码或静态配置中，阻止它们跨系统共享或随时间自主改进。我们提出**Swarm Skills**，一个可移植规范，扩展Anthropic技能标准以包含多智能体语义。Swarm Skills将多智能体工作流转变为一流可分发资产，由角色、工作流、执行边界和用于自演化的内置语义结构组成。为使规范的不断演化的特性可操作，我们提供了一个配套的自演化算法，自动将成功执行轨迹蒸馏为新Swarm Skills，并根据多维评分（有效性、利用率和新鲜度）持续修补现有技能，在精炼过程中消除人工监督的需要。通过架构兼容性分析和使用开源JiuwenSwarm参考实现的综合定性案例研究，我们展示了Swarm Skills如何通过渐进式披露实现零适配器跨智能体可移植性，使智能体团队能够自主演化其协调策略而无需框架锁定。

---

## 60. Personalizing LLMs with Binary Feedback: A Preference-Corrected Optimization Framework

**arXiv ID**: [2605.10043](https://arxiv.org/abs/2605.10043)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10043)

**作者**: Xilai Ma, Liye Zhao, Weijun Yao, Haibing Di, Wenya Wang 等 (共6人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 06:12:24 UTC

**摘要 (英文)**: Large Language Model (LLM) personalization aims to align model behaviors with individual user preferences. Existing methods often focus on isolated user histories, neglecting the essential role of inter-user differences. We propose C-BPO, a framework that personalizes LLMs via preference-calibrated binary signals. By treating target user data as positive feedback and other users' data as an auxiliary set of implicit negative signals, C-BPO captures distinct inter-user differences. To mitigate the preference overlap issue, where shared task knowledge is erroneously penalized, we derive an objective grounded in Positive-Unlabeled (PU) learning theory. This approach purifies negative signals by subtracting ``positive bias'', ensuring alignment with unique idiosyncrasies without compromising general helpfulness. Empirical experiments across various personalization tasks and backbone LLMs show C-BPO consistently outperforms baselines, demonstrating the efficacy of preference-calibrated binary signals in modeling inter-user differences.

**摘要 (中文)**: 大语言模型（LLM）个性化旨在将模型行为与个体用户偏好对齐。现有方法通常专注于孤立的用户历史，忽略用户间差异的本质作用。我们提出C-BPO，一个通过偏好校准二元信号实现LLM个性化的框架。通过将目标用户数据视为正反馈，将其他用户数据视为隐负信号的辅助集，C-BPO捕获不同的用户间差异。为缓解偏好重叠问题（共享任务知识被错误惩罚），我们基于正负样本（PU）学习理论推导目标。该方法通过减去"正偏差"来净化负信号，确保在不妨碍一般有用性的情况下与独特特性对齐。跨各种个性化任务和骨干LLM的实证实验表明C-BPO始终优于基线，证明了偏好校准二元信号在建模用户间差异方面的有效性。

---

## 61. PlantMarkerBench: A Multi-Species Benchmark for Evidence-Grounded Plant Marker Reasoning

**arXiv ID**: [2605.10032](https://arxiv.org/abs/2605.10032)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10032)

**作者**: Sajib Acharjee Dip, Song Li, Liqing Zhang

**分类**: Computation and Language

**发布时间**: 2026-05-11 05:57:15 UTC

**摘要 (英文)**: Cell-type-specific marker genes are fundamental to plant biology, yet existing resources primarily rely on curated databases or high-throughput studies without explicitly modeling the supporting evidence found in scientific literature. We introduce PlantMarkerBench, a multi-species benchmark for evaluating literature-grounded plant marker evidence interpretation from full-text biological papers. PlantMarkerBench is constructed using a modular curation pipeline integrating large-scale literature retrieval, hybrid search, species-aware biological grounding, structured evidence extraction, and targeted human review. The benchmark spans four plant species -- Arabidopsis, maize, rice, and tomato -- and contains 5,550 sentence-level evidence instances annotated for marker-evidence validity, evidence type, and support strength. We define two benchmark tasks: determining whether a candidate sentence provides valid marker evidence for a gene-cell-type pair, and classifying the evidence into expression, localization, function, indirect, or negative categories. We benchmark diverse open-weight and closed-source language models across species and prompting strategies. Although frontier models achieve relatively strong performance on direct expression evidence, performance drops substantially on functional, indirect, and weak-support evidence, with evidence-type confusion emerging as a dominant failure mode. Open-weight models additionally exhibit elevated false-positive rates under ambiguous biological contexts. PlantMarkerBench provides a challenging and reproducible evaluation framework for literature-grounded biological evidence attribution and supports future research on trustworthy scientific information extraction and AI-assisted plant biology.

**摘要 (中文)**: 细胞类型特异性标记基因是植物生物学的基础，但现有资源主要依赖策展数据库或高通量研究，未明确建模科学文献中的支持证据。我们引入PlantMarkerBench，一个用于评估来自全文生物论文的文献接地植物标记证据解释的多物种基准。PlantMarkerBench使用模块化策展管道构建，整合大规模文献检索、混合搜索、物种感知生物接地、结构化证据提取和针对性人工审查。基准涵盖四种植物——拟南芥、玉米、水稻和番茄——包含5550个句子级证据实例，标注了标记-证据有效性、证据类型和支持强度。我们定义两个基准任务：确定候选句子是否为基因-细胞类型对提供有效标记证据，以及将证据分类为表达、定位、功能、间接或负类别。我们跨物种和提示策略对各种开源和闭源语言模型进行基准测试。尽管前沿模型在直接表达证据上表现相对较强，但性能在功能、间接和弱支持证据上大幅下降，证据类型混淆成为主导失败模式。开源模型在模糊生物背景下还表现出升高的假阳性率。PlantMarkerBench为文献接地生物证据归因提供了具有挑战性和可复现的评估框架，支持未来对可信科学信息提取和AI辅助植物生物学的研究。

---

## 62. Speech-based Psychological Crisis Assessment using LLMs

**arXiv ID**: [2605.10027](https://arxiv.org/abs/2605.10027)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10027)

**作者**: Terumi Chiba, Yang Luo, Ziyun Cui, Yongsheng Tong, Chao Zhang

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 05:50:51 UTC

**摘要 (英文)**: Psychological support hotlines provide critical support for individuals experiencing mental health emergencies, yet current assessments largely rely on human operators whose judgments may vary with professional experience and are constrained by limited staffing resources. This paper proposes a large language model (LLM)-based framework for automated crisis level classification, a key indicator that supports many downstream tasks and improves the overall quality of hotline services. To better capture emotional signals in spoken conversations, we introduce a paralinguistic injection method that inserts identified non-verbal emotional cues into speech transcripts, enabling LLM-based reasoning to incorporate critical acoustic nuances. In addition, we propose a reasoning-enhanced training strategy that trains the model to generate diagnostic reasoning chains as an auxiliary task, which serves as a regulariser to improve classification performance. Combined with data augmentation, our final system achieves a macro F1-score of 0.802 and an accuracy of 0.805 on the three-class classification task under 5-fold cross-validation.

**摘要 (中文)**: 在医疗保健等高风险领域，大语言模型（LLM）的可靠性至关重要，特别是在从事件报告中生成临床洞察时。本研究提出一种基于标签的少样本示例选择方法，用于提示LLM从医疗事件细节生成背景/因果因素和预防措施。实验中，我们使用日本医疗事件数据集（JMID），这是一个包含3884个真实世界医疗事故和险情报告的结构化数据集。这些报告用各种标签进行可变标注——一些包含描述性信息（如"药物"、"输血治疗"）。我们比较三种少样本示例选择策略——随机采样、基于余弦相似度的选择和我们提出的基于标签的方法——使用GPT-4o和LLaMA 3.3。结果表明，基于标签的方法达到最高精确率和最稳定的生成行为，而基于相似度的选择经常导致意外输出和安全过滤器激活。这些发现表明，基于人类可解释数据集标签选择示例可以提高临床LLM应用中的生成精度和稳定性。

---

## 63. Medical Incident Causal Factors and Preventive Measures Generation Using Tag-based Example Selection in Few-shot Learning

**arXiv ID**: [2605.10025](https://arxiv.org/abs/2605.10025)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10025)

**作者**: Yuna Haseyama, Tomoki Ito, Hiroki Sakaji, Itsuki Noda

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 05:49:09 UTC

**摘要 (英文)**: In high-stakes domains such as healthcare, the reliability of Large Language Models (LLMs) is critical, particularly when generating clinical insights from incident reports. This study proposes a tag-based few-shot example selection method for prompting LLMs to generate background/causal factors and preventive measures from details of the medical incidents. For our experiments, we use the Japanese Medical Incident Dataset (JMID), a structured dataset of 3,884 real-world medical accident and near-miss reports. These reports are variably annotated with a wide range of tags--some include descriptive information (e.g., "medications," "blood transfusion therapy"). We compare three few-shot example selection strategies--random sampling, cosine similarity-based selection, and our proposed tag-based method--using GPT-4o and LLaMA 3.3. Results show that the tag-based approach achieves the highest precision and most stable generation behavior, while similarity-based selection often leads to unintended outputs and safety filter activation. These findings suggest that selecting examples based on human-interpretable dataset tags can improve generation precision and stability in clinical LLM applications.

**摘要 (中文)**: 后训练（通过监督微调）提高了指令遵循能力，但通常通过使模型偏向低熵微调数据而牺牲高熵预训练分布来诱发语义模式崩溃。关键是我们发现这种权衡随规模恶化。为缩小这一语义多样性差距，我们提出标注锚定训练，一个有原则的方法，使模型能够采用后训练的偏好跟随行为而不牺牲预训练的固有多样性。我们的方法很简单：我们在与语义标注配对的文档上进行预训练，诱导反映预训练数据全广度的丰富标注分布，并在后训练期间保留该分布。这使我们能够在推理时采样多样化标注，并使用它们作为锚点引导生成，有效将预训练的语义丰富性转移到后训练模型中。我们发现使用标注锚定训练的模型可以实现比SFT训练的模型少6倍的多样性崩溃，并随规模改进。

---

## 64. Annotations Mitigate Post-Training Mode Collapse

**arXiv ID**: [2605.09995](https://arxiv.org/abs/2605.09995)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09995)

**作者**: Jacob Mitchell Springer, Madhu Advani, Lukas Aichberger, Arwen Bradley, Eran Malach 等 (共10人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 05:11:04 UTC

**摘要 (英文)**: Post-training (via supervised fine-tuning) improves instruction-following, but often induces semantic mode collapse by biasing models toward low-entropy fine-tuning data at the expense of the high-entropy pretraining distribution. Crucially, we find this trade-off worsens with scale. To close this semantic diversity gap, we propose annotation-anchored training, a principled method that enables models to adopt the preference-following behaviors of post-training without sacrificing the inherent diversity of pretraining. Our approach is simple: we pretrain on documents paired with semantic annotations, inducing a rich annotation distribution that reflects the full breadth of pretraining data, and we preserve this distribution during post-training. This lets us sample diverse annotations at inference time and use them as anchors to guide generation, effectively transferring pretraining's semantic richness into post-trained models. We find that models trained with annotation-anchored training can attain $6 \times$ less diversity collapse than models trained with SFT, and improve with scale.

**摘要 (中文)**: 后训练（通过监督微调）提高了指令遵循能力，但通常通过使模型偏向低熵微调数据而牺牲高熵预训练分布来诱导语义模式坍缩。关键的是，我们发现这种权衡随规模恶化。为缩小这一语义多样性差距，我们提出标注锚定训练，一个原则性方法，使模型能够采用后训练的偏好遵循行为而不牺牲预训练固有的多样性。我们的方法很简单：我们在与语义标注配对的文档上进行预训练，诱导反映预训练数据全广度的丰富标注分布，并在后训练中保留此分布。这使我们在推理时能够采样多样化标注并使用它们作为锚点来引导生成，有效将预训练的语义丰富性迁移到后训练模型中。我们发现使用标注锚定训练训练的模型可以实现比SFT训练的模型少6倍的多样性坍缩，并随规模改进。

---

## 65. Merlin: Deterministic Byte-Exact Deduplication for Lossless Context Optimization in Large Language Model Inference

**arXiv ID**: [2605.09990](https://arxiv.org/abs/2605.09990)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09990)

**作者**: Sietse Schelpe

**分类**: Computation and Language

**发布时间**: 2026-05-11 05:06:59 UTC

**摘要 (英文)**: Data-intensive applications, ranging from large-scale retrieval systems to advanced data pipelines, are increasingly bottlenecked by the processing of highly redundant text corpora. We present Merlin, a local-first, agnostic, high-throughput deduplication and context optimization engine designed to mitigate these inefficiencies. Utilizing a highly optimized, SIMD-friendly open-addressing flat hash set combined with xxHash3-64, Merlin performs rapid, byte-exact deduplication of text passages and data chunks. While broadly applicable to any text-processing workflow, its impact is particularly pronounced in Large Language Model (LLM) ecosystems, such as Retrieval-Augmented Generation (RAG). Our empirical evaluations demonstrate an input reduction ranging from 13.9% in low-redundancy datasets to over 71% in high-redundancy pipelines, maintaining absolute data fidelity. Furthermore, we detail the system's integration architecture via the Model Context Protocol (MCP), enabling secure, zero-network-interception deployment across major IDEs and autonomous agents. This paper outlines the core algorithmic design, performance benchmarks, and the architectural principles required to process data at sustained speeds of up to 8.7 GB/s.

**摘要 (中文)**: 数据密集型应用，从大规模检索系统到高级数据管道，越来越受到高度冗余文本语料库处理的瓶颈。我们呈现Merlin，一个本地优先、与框架无关的高吞吐量去重和上下文优化引擎，旨在缓解这些低效。利用高度优化的SIMD友好的开放寻址平面哈希集结合xxHash3-64，Merlin快速对文本段落和数据块执行字节精确去重。虽然广泛适用于任何文本处理工作流，但其影响在大型语言模型（LLM）生态系统中尤为显著，如检索增强生成（RAG）。我们的实证评估表明输入减少从低冗余数据集的13.9%到高冗余管道的71%以上，同时保持绝对数据保真度。此外，我们通过模型上下文协议（MCP）详细说明了系统集成架构，实现跨主要IDE和自主智能体的安全、零网络拦截部署。本文概述了核心算法设计、性能基准测试和处理数据所需的架构原则， sustained speeds高达8.7 GB/s。

---

## 66. GLiNER2-PII: A Multilingual Model for Personally Identifiable Information Extraction

**arXiv ID**: [2605.09973](https://arxiv.org/abs/2605.09973)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09973)

**作者**: Urchade Zaratiana, Ash Lewis, George Hurn-Maloney

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 04:29:30 UTC

**摘要 (英文)**: Reliable detection of personally identifiable information (PII) is increasingly important across modern data-processing systems, yet the task remains difficult: PII spans are heterogeneous, locale-dependent, context-sensitive, and often embedded in noisy or semi-structured documents. We present GLiNER2-PII, a small 0.3B-parameter model adapted from GLiNER2 and designed to recognize a broad taxonomy of 42 PII entity types at character-span resolution. Training such systems, however, is constrained by the scarcity of shareable annotated data and the privacy risks associated with collecting real PII at scale. To address this challenge, we construct a multilingual synthetic corpus of 4,910 annotated texts using a constraint-driven generation pipeline that produces diverse, realistic examples across languages, domains, formats, and entity distributions. On the challenging SPY benchmark, GLiNER2-PII achieves the highest span-level F1 among five compared systems, including OpenAI Privacy Filter and three GLiNER-based detectors. We publicly release the model on Hugging Face to support further research and practical deployment of open PII detection systems.

**摘要 (中文)**: 可靠的个人可识别信息（PII）检测在现代数据处理系统中越来越重要，但该任务仍然困难：PII跨度是异质的、依赖于地区、上下文敏感且经常嵌入在嘈杂或半结构化文档中。我们呈现GLiNER2-PII，一个从GLiNER2适配的0.3B参数小模型，设计用于在字符跨度分辨率下识别42种广泛PII实体类型。然而，训练此类系统受到可共享标注数据稀缺和大规模收集真实PII相关隐私风险的约束。为解决这一挑战，我们使用约束驱动的生成管道构建了一个包含4910个标注文本的多语言合成语料库，生成跨语言、领域、格式和实体分布的多样化真实示例。在具有挑战性的SPY基准上，GLiNER2-PII在五个比较系统中达到最高跨度级F1，包括OpenAI隐私过滤器和三个基于GLiNER的检测器。我们公开在Hugging Face上发布模型，以支持进一步研究和实际部署开源PII检测系统。

---

## 67. Beyond Majority Voting: Agreement-Based Clustering to Model Annotator Perspectives in Subjective NLP Tasks

**arXiv ID**: [2605.09955](https://arxiv.org/abs/2605.09955)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09955)

**作者**: Tadesse Destaw Belay, Ibrahim Said Ahmad, Idris Abdulmumin, Abinew Ali Ayele, Alexander Gelbukh 等 (共9人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 04:04:03 UTC

**摘要 (英文)**: Disagreement in annotation is a common phenomenon in the development of NLP datasets and serves as a valuable source of insight. While majority voting remains the dominant strategy for aggregating labels, recent work has explored modeling individual annotators to preserve their perspectives. However, modeling each annotator is resource-intensive and remains underexplored across various NLP tasks. We propose an agreement-based clustering technique to model the disagreement between the annotators. We conduct comprehensive experiments in 40 datasets in 18 typologically diverse languages, covering three subjective NLP tasks: sentiment analysis, emotion classification, and hate speech detection. We evaluate four aggregation approaches: majority vote, ensemble, multi-label, and multitask. The results demonstrate that agreement-based clustering can leverage the full spectrum of annotator perspectives and significantly enhance classification performance in subjective NLP tasks compared to majority voting and individual annotator modeling. Regarding the aggregation approach, the multi-label and multitask approaches are better for modeling clustered annotators than an ensemble and model majority vote.

**摘要 (中文)**: 标注中的分歧是NLP数据集开发中的常见现象，作为有价值的洞察来源。虽然多数投票仍是聚合标签的主导策略，但最近的工作探索了对单个标注者进行建模以保留他们的观点。然而，对每个标注者进行建模资源密集型，并且在各种NLP任务中仍未充分探索。我们提出一种基于一致性的聚类技术来建模标注者之间的分歧。我们在18种类型多样语言的40个数据集上进行综合实验，涵盖三个主观NLP任务：情感分析、情绪分类和仇恨言论检测。我们评估四种聚合方法：多数投票、集成、多标签和多任务。结果表明，基于一致性的聚类可以利用标注者观点的全部范围，并在主观NLP任务中显著增强分类性能优于多数投票和单个标注者建模。在聚合方法方面，多标签和多任务方法比集成和模型多数投票更适合建模聚类标注者。

---

## 68. TRACER: Verifiable Generative Provenance for Multimodal Tool-Using Agents

**arXiv ID**: [2605.09934](https://arxiv.org/abs/2605.09934)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09934)

**作者**: Bihui Yu, Caijun Jia, Jing Chi, Xiaohan Liu, Yining Wang 等 (共9人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 03:32:55 UTC

**摘要 (英文)**: Multimodal large language models increasingly solve vision-centric tasks by calling external tools for visual inspection, OCR, retrieval, calculation, and multi-step reasoning. Current tool-using agents usually expose the executed tool trajectory and the final answer, but they rarely specify which tool observation supports each generated claim. We call this missing claim-level dependency structure the provenance gap. The gap makes tool use hard to verify and hard to optimize, because useful evidence, redundant exploration, and unsupported reasoning are mixed in the same trajectory. We introduce TRACER, a framework for verifiable generative provenance in multimodal tool-using agents. Instead of adding citations after generation, TRACER generates each answer sentence together with a structured provenance record that identifies the supporting tool turn, evidence unit, and semantic support relation. Its relation space contains Quotation, Compression, and Inference, covering direct reuse, faithful condensation, and grounded derivation. TRACER verifies each record through schema checking, tool-turn alignment, source authenticity, and relation rationality, and then converts verified provenance into traceability constraints and provenance-derived local credit for reinforcement learning. We further construct TRACE-Bench, a benchmark for sentence-level provenance reconstruction from coarse multimodal tool trajectories. On TRACE-Bench, simply adding tools often introduces noise. With Qwen3-VL-8B, TRACER reaches 78.23% answer accuracy and 95.72% summary accuracy, outperforming the strongest closed-source tool-augmented baseline by 23.80 percentage points. Compared with tool-only supervised fine-tuning, it also reduces total test-set tool calls from 4949 to 3486. These results show that reliable multimodal tool reasoning depends on provenance-aware use of observations, not on more tool calls alone.

**摘要 (中文)**: 多模态大语言模型 increasingly通过调用外部工具解决以视觉为中心的任务，如视觉检查、OCR、检索、计算和多步推理。当前工具使用智能体通常暴露执行的工具轨迹和最终答案，但很少指定每个生成声明由哪个工具观察支持。我们称这个缺失的声明级依赖结构为溯源差距。这一差距使工具使用难以验证和优化，因为有用证据、冗余探索和无根据推理混合在同一轨迹中。我们引入TRACER，一个用于多模态工具使用智能体中可验证生成溯源的框架。TRACER不是事后添加引用，而是在生成每个答案句子的同时生成结构化溯源记录，识别支持的工具轮次、证据单元和语义支持关系。其关系空间包含引用、压缩和推理，涵盖直接重用、忠实压缩和有根据推导。TRACER通过模式检查、工具轮次对齐、源真实性和关系合理性验证每个记录，然后将验证的溯源转换为可追溯性约束和用于强化学习的溯源派生局部信用。我们进一步构建TRACE-Bench，一个从粗粒度多模态工具轨迹进行句子级溯源重构的基准。在TRACE-Bench上，简单添加工具通常会引入噪声。使用Qwen3-VL-8B，TRACER达到78.23%的答案准确率和95.72%的摘要准确率，比最强的闭源工具增强基线高23.80个百分点。与纯工具监督微调相比，它还将总测试集工具调用从4949减少到3486。这些结果表明可靠的多模态工具推理依赖于溯源感知的观察使用，而非仅更多的工具调用。

---

## 69. FocuSFT: Bilevel Optimization for Dilution-Aware Long-Context Fine-Tuning

**arXiv ID**: [2605.09932](https://arxiv.org/abs/2605.09932)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09932)

**作者**: Zehua Pei, Hui-Ling Zhen, Xianzhi Yu, Sinno Jialin Pan, Mingxuan Yuan 等 (共6人)

**分类**: Computation and Language

**发布时间**: 2026-05-11 03:30:35 UTC

**摘要 (英文)**: Large language models can now process increasingly long inputs, yet their ability to effectively use information spread across long contexts remains limited. We trace this gap to how attention budget is spent during supervised fine-tuning (SFT) on long sequences: positional biases and attention sinks cause the model to allocate most of its attention to positionally privileged tokens rather than semantically relevant content. This training-time attention dilution (the starvation of content tokens in the attention distribution) weakens the gradient signal, limiting the model's ability to learn robust long-context capabilities. We introduce FocuSFT, a bilevel optimization framework that addresses this problem at training time. An inner loop adapts lightweight fast-weight parameters on the training context to form a parametric memory that concentrates attention on relevant content, and the outer loop performs SFT conditioned on this sharpened representation. Both loops apply bidirectional attention over context tokens while preserving causal masking for responses, reducing the causal asymmetry that gives rise to attention sinks and aligning inner-outer behavior. On BABILong, FocuSFT improves accuracy by up to +14pp across 4K--32K context lengths; on RULER, it raises CWE aggregation from 72.9\% to 81.1\% at 16K; and on GPQA with agentic tool use, it yields a 24\% relative gain in pass@1. Attention analysis shows that FocuSFT reduces attention sink mass by 529$\times$ and triples context engagement during training. Code: https://github.com/JarvisPei/FocuSFT

**摘要 (中文)**: 大语言模型现在可以处理越来越长的输入，但它们有效利用分布在长上下文中的信息的能力仍然有限。我们将此差距追溯到在长序列监督微调（SFT）期间注意力预算如何花费：位置偏差和注意力汇导致模型将其大部分注意力分配给位置特权token而非语义相关内容。这种训练时注意力稀释（内容token在注意力分布中的饥饿）削弱了梯度信号，限制模型学习鲁棒长上下文能力的能力。我们引入FocuSFT，一个双层优化框架，在训练时解决此问题。内环在训练上下文上调整轻量级快速权重参数以形成将注意力集中在相关内容上的参数记忆，外环在此精炼表示上进行条件化SFT。两个循环都对上下文token应用双向注意力，同时为响应保持因果掩码，减少产生注意力汇的因果不对称并对齐内外环行为。在BABILong上，FocuSFT在4K-32K上下文长度上提高准确性高达+14pp；在RULER上，它将16K的CWE聚合从72.9%提高到81.1%；在GPQA与智能体工具使用上，它产生24%的pass@1相对增益。注意力分析显示FocuSFT将注意力汇质量减少529倍，并在训练期间将上下文参与度翻三倍。

---

## 70. PruneTIR: Inference-Time Tool Call Pruning for Effective yet Efficient Tool-Integrated Reasoning

**arXiv ID**: [2605.09931](https://arxiv.org/abs/2605.09931)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09931)

**作者**: Luan Zhang, Dandan Song, Zhijing Wu, Zhengyu Chen, Chen Zhang 等 (共11人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 03:28:43 UTC

**摘要 (英文)**: Tool-integrated reasoning (TIR) enables large language models (LLMs) to enhance their capabilities by interacting with external tools, such as code interpreters (CI). Most recent studies focus on exploring various methods to equip LLMs with the ability to use tools. However, how to further boost the reasoning ability of already tool-capable LLMs at inference time remains underexplored. Improving reasoning at inference time requires no additional training and can help LLMs better leverage tools to solve problems. We observe that, during tool-capable LLM inference, both the number and the proportion of erroneous tool calls are negatively correlated with answer correctness. Moreover, erroneous tool calls are typically resolved successfully within a few subsequent turns. If not, LLMs often struggle to resolve such errors even with many additional turns. Building on the above observations, we propose PruneTIR, a rather effective yet efficient framework that enhances the tool-integrated reasoning at inference time. During LLM inference, PruneTIR prunes trajectories, resamples tool calls, and suspends tool usage through three components: Success-Triggered Pruning, Stuck-Triggered Pruning and Resampling, and Retry-Triggered Tool Suspension. These three components enable PruneTIR to mitigate the negative impact of erroneous tool calls and prevent LLMs from getting stuck in repeated failed resolution attempts, thereby improving overall LLM performance. Extensive experimental results demonstrate the effectiveness of PruneTIR, which significantly improves Pass@1 and efficiency while reducing the working context length for tool-capable LLMs.

**摘要 (中文)**: 工具集成推理（TIR）使大语言模型（LLM）能够通过与外部工具（如代码解释器CI）交互来增强其能力。最近的大多数研究侧重于探索各种方法来为LLM配备工具使用能力。然而，如何在推理时进一步提升已有工具能力的LLM的推理能力仍然未被探索。在推理时改进推理不需要额外训练，可以帮助LLM更好地利用工具解决问题。我们观察到，在有工具能力的LLM推理期间，错误工具调用的数量和比例与答案正确性负相关。此外，错误工具调用通常在后续几轮内成功解决。如果没有，LLM即使有更多额外轮次也往往难以解决此类错误。基于上述观察，我们提出PruneTIR，一个在推理时增强工具集成推理的高效框架。在LLM推理期间，PruneTIR通过三个组件修剪轨迹、重采样工具调用和暂停工具使用：成功触发修剪、卡住触发修剪和重采样、以及重试触发工具暂停。这三个组件使PruneTIR能够缓解错误工具调用的负面影响，并防止LLM陷入重复失败解决尝试，从而提高整体LLM性能。广泛实验结果证明PruneTIR的有效性，其显著提高Pass@1和效率，同时减少有工具能力LLM的工作上下文长度。

---

## 71. Evolving Knowledge Distillation for Lightweight Neural Machine Translation

**arXiv ID**: [2605.09924](https://arxiv.org/abs/2605.09924)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09924)

**作者**: Xuewen Zhang, Haixiao Zhang, Xinlong Huang

**分类**: Computation and Language

**发布时间**: 2026-05-11 03:21:24 UTC

**摘要 (英文)**: Recent advancements in Neural Machine Translation (NMT) have significantly improved translation quality. However, the increasing size and complexity of state-of-the-art models present significant challenges for deployment on resource-limited devices. Knowledge distillation (KD) is a promising approach for compressing models, but its effectiveness diminishes when there is a large capacity gap between teacher and student models. To address this issue, we propose Evolving Knowledge Distillation (EKD), a progressive training framework in which the student model learns from a sequence of teachers with gradually increasing capacities. Experiments on IWSLT-14, WMT-17, and WMT-23 benchmarks show that EKD leads to consistent improvements at each stage. On IWSLT-14, the final student achieves a BLEU score of 34.24, narrowing the gap to the strongest teacher (34.32 BLEU) to just 0.08 BLEU. Similar trends are observed on other datasets. These results demonstrate that EKD effectively bridges the capacity gap, enabling compact models to achieve performance close to that of much larger teacher models.Code and models are available at https://github.com/agi-content-generation/EKD.

**摘要 (中文)**: 神经机器翻译（NMT）的最新进展显著提高了翻译质量。然而，最先进模型的规模和复杂性不断增加，对资源受限设备上的部署提出了重大挑战。知识蒸馏（KD）是压缩模型的有前景方法，但当师生模型之间存在大能力差距时，其有效性会降低。为解决此问题，我们提出演化知识蒸馏（EKD），一种渐进训练框架，其中学生模型从一系列容量逐渐增加的教师模型学习。在IWSLT-14、WMT-17和WMT-23基准上的实验表明，EKD在每个阶段都带来持续改进。在IWSLT-14上，最终学生达到34.24的BLEU分数，与最强教师（34.32 BLEU）的差距仅为0.08 BLEU。在其他数据集上观察到类似趋势。这些结果表明EKD有效弥合能力差距，使紧凑模型能够实现与更大教师模型接近的性能。代码和模型可在https://github.com/agi-content-generation/EKD获取。

---

## 72. Team-Based Self-Play With Dual Adaptive Weighting for Fine-Tuning LLMs

**arXiv ID**: [2605.09922](https://arxiv.org/abs/2605.09922)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09922)

**作者**: Wu Li, Yigeng Zhou, Zesheng Shi, Yequan Wang, Min Zhang 等 (共6人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 03:17:31 UTC

**摘要 (英文)**: While recent self-training approaches have reduced reliance on human-labeled data for aligning LLMs, they still face critical limitations: (i) sensitivity to synthetic data quality, leading to instability and bias amplification in iterative training; (ii) ineffective optimization due to a diminishing gap between positive and negative responses over successive training iterations. In this paper, we propose Team-based self-Play with dual Adaptive Weighting (TPAW), a novel self-play algorithm designed to improve alignment in a fully self-supervised setting. TPAW adopts a team-based framework in which the current policy model both collaborates with and competes against historical checkpoints, promoting more stable and efficient optimization. To further enhance learning, we design two adaptive weighting mechanisms: (i) a response reweighting scheme that adjusts the importance of target responses, and (ii) a player weighting strategy that dynamically modulates each team member's contribution during training. Initialized from a SFT model, TPAW iteratively refines alignment without requiring additional human supervision. Experimental results demonstrate that TPAW consistently outperforms existing baselines across various base models and LLM benchmarks. Our code is publicly available at https://github.com/lab-klc/TPAW.

**摘要 (中文)**: 虽然最近的自我训练方法减少了对人类标注数据对齐LLM的依赖，但它们仍然面临关键局限：(i) 对合成数据质量的敏感性，导致迭代训练中的不稳定性和偏见放大；(ii) 优化无效，因为正向和负向响应之间的差距在连续训练迭代中递减。在本文中，我们提出带双自适应权重的组队自博弈（TPAW），一种在完全自监督设置中改进对齐的新型自博弈算法。TPAW采用基于团队的框架，当前策略模型与历史检查点既合作又竞争，促进更稳定和高效的优化。为进一步增强学习，我们设计两种自适应加权机制：(i) 响应重新加权方案调整目标响应的重要性，(ii) 玩家加权策略在训练期间动态调节每个团队成员的贡献。从SFT模型初始化，TPAW迭代改进对齐，无需额外人类监督。实验结果表明TPAW在各种基础模型和LLM基准上始终优于现有基线。我们的代码公开于https://github.com/lab-klc/TPAW。

---

## 73. Position: Academic Conferences are Potentially Facing Denominator Gaming Caused by Fully Automated Scientific Agents

**arXiv ID**: [2605.09915](https://arxiv.org/abs/2605.09915)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09915)

**作者**: Rong Shan, Te Gao, Hang Zheng, Yunjia Xi, Jiachen Zhu 等 (共9人)

**分类**: Computation and Language, Artificial Intelligence, Computers and Society

**发布时间**: 2026-05-11 03:07:15 UTC

**摘要 (英文)**: The implicit policy of maintaining relatively stable acceptance rates at top AI conferences, despite exponentially growing submissions, introduces a critical structural vulnerability. This position paper characterizes a new systemic threat we term Agentic Denominator Gaming, in which a malicious actor deploys AI agents to generate and submit a large volume of superficially plausible but low-quality papers. Crucially, their objective is not the acceptance of low-quality papers, but rather to inflate the submission denominator and overwhelm reviewing capacity. Under a relatively stable acceptance rate, this dilution can systematically increase the publication probability of a small, targeted set of legitimate papers. We analyze the practical feasibility of this threat and its broader consequences, including intensified reviewer burnout, degraded review quality, and the emergence of industrialized automated agent mills. Finally, we propose and evaluate a range of mitigation strategies, and argue that durable protection will require system-level policy and incentive reforms, rather than relying primarily on technical detection alone.

**摘要 (中文)**: 本文针对人工智能会议论文数量指数增长但接受率相对稳定的现状，揭示了一种新的系统性威胁——"智能体分母博弈"。攻击者可部署AI智能体批量生成表面合理但质量低下的论文，其目的并非让低质量论文被接受，而是通过膨胀分母来耗尽审稿资源。在接受率相对稳定的条件下，这种稀释可以系统性地提高少量特定正规论文的发表概率。本文分析该威胁的可行性及其更广泛后果，包括审稿人倦怠加剧、审稿质量下降以及工业化自动审稿工厂的出现。最后，本文提出并评估了一系列缓解策略，认为长期保护需要系统层面的政策和激励机制改革，而非仅依赖技术检测。

---

## 74. Pseudo-Deliberation in Language Models: When Reasoning Fails to Align Values and Actions

**arXiv ID**: [2605.09893](https://arxiv.org/abs/2605.09893)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09893)

**作者**: Sushrita Rakshit, Hanwen Zhang, Hua Shen

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-11 02:32:53 UTC

**摘要 (英文)**: Large language models (LLMs) are often evaluated based on their stated values, yet these do not reliably translate into their actions, a discrepancy termed "value-action gap." In this work, we argue that this gap persists even under explicit reasoning, revealing a deeper failure mode we call "Pseudo-Deliberation": the appearance of principled reasoning without corresponding behavioral alignment. To study this systematically, we introduce VALDI, a framework for measuring alignment between stated values and generated dialogue. VALDI includes 4,941 human-centered scenarios across five domains, three tasks that elicit value articulation, reasoning, and action, and five metrics for quantifying value adherence. Across both proprietary and open-source LLMs, we observe consistent misalignment between expressed values and downstream dialogues. To investigate intervention strategies, we propose VIVALDI, a multi-agent value auditor that intervenes at different stages of generation.

**摘要 (中文)**: 大语言模型常基于其声明的价值观进行评估，但这些价值观并不能可靠地转化为实际行动，这种差异被称为"价值-行为差距"。本文认为即使在显式推理下这种差距依然存在，揭示了一种更深层的失败模式——"伪 deliberative"：看似有原则的推理却缺乏相应的行为对齐。为了系统研究这一问题，我们提出了VALDI框架，用于衡量声明价值观与生成对话之间的一致性。VALDI包含4941个人类中心场景横跨五个领域，三种任务用于引出价值观表达、推理和行为，以及五个用于量化价值遵循度的指标。在闭源和开源大语言模型中，我们都观察到表达的价值观与下游对话之间存在持续的不一致。为研究干预策略，我们提出了VIVALDI，一种在生成不同阶段进行干预的多智能体价值观审计器。

---

## 75. The Association of Transformer-based Sentiment Analysis with Symptom Distress and Deterioration in Routine Psychotherapy Care

**arXiv ID**: [2605.09838](https://arxiv.org/abs/2605.09838)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09838)

**作者**: Douglas K. Faust, Peter Awad, Alexandre Vaz, Tony Rousmaniere

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-11 00:41:47 UTC

**摘要 (英文)**: Sentiment analysis has been of long-standing interest in psychotherapy research. Recently, the Transformer deep learning architecture has produced text-based sentiment analysis models that are highly accurate and context-aware. These models have been explored as proxies for emotion measurement instruments in psychotherapy, but not investigated as stand-alone psychometric tools. Using proposed utterance-level and session-level sentiment features derived from a fine-grained sentiment model on a large corpus of psychotherapy sessions (N = 751), we investigate the distribution of session aggregated sentiment scores. Further, we characterize the relationship of these features to individual components and the overall score of the OQ-45 instrument and find that this sentiment feature is most strongly correlated to components related to emotional valence in directionally intuitive ways. Finally, we report that there are statistically significant differences between the sentiment distributions for patients flagged as at risk of deterioration or dropping out of care via either the OQ Rational or Empirical outcome models. These correlations to a fully-validated psychometric instrument demonstrate that these proposed sentiment features are, at least, adjunctive measures of client distress and deterioration.

**摘要 (中文)**: 情感分析一直是心理治疗研究长期关注的课题。近年来，Transformer深度学习架构已开发出高度准确且具上下文感知的基于文本的情感分析模型。这些模型已被探索作为心理治疗中情绪测量工具的替代方案，但尚未作为独立心理测量工具进行研究。我们使用细粒度情感模型从大量心理治疗会话语料库（N=751）中提取的提议的语句级和会话级情感特征，研究会话聚合情感分数的分布。此外，我们还表征了这些特征与OQ-45仪器各个分量及总体分数的关系，发现该情感特征与情感效价相关分量具有最强烈的直观方向性关联。最后，我们报告了通过OQ理性或经验结果模型标记为有恶化风险或退出治疗风险的患者，其情感分布存在统计学显著差异。这种与经过充分验证的心理测量仪器的相关性表明，这些提议的情感特征至少是客户困扰和恶化的辅助测量手段。

---

## 76. Quantifying the Utility of User Simulators for Building Collaborative LLM Assistants

**arXiv ID**: [2605.09808](https://arxiv.org/abs/2605.09808)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09808)

**作者**: Joseph Suh, Ayush Raj, Minwoo Kang, Serina Chang

**分类**: Computation and Language

**发布时间**: 2026-05-10 23:06:24 UTC

**摘要 (英文)**: User simulators are increasingly leveraged to build interactive AI assistants, yet how to measure the quality of these simulators remains an open question. In this work, we show how simulator quality can be quantified in terms of its downstream utility: how an LLM assistant trained with this user simulator performs in the wild when interacting with real humans. In a controlled experiment where only the user simulator varies, we train LLM assistants via reinforcement learning against a spectrum of simulators, from an LLM prompted to role-play a user to one fine-tuned on human utterances from WildChat. As evaluation, we measure pairwise win rates in a user study with 283 participants and on WildBench, a benchmark derived from real human--AI conversations. Training against the role-playing LLM yields an assistant statistically indistinguishable from the initial assistant in our user study (51% win rate), whereas training against the fine-tuned simulator yields significant gains (58% over the initial and 57% over the one trained against role-playing). Closer inspection reveals three further patterns: methods for making role-playing LLMs more realistic (e.g., persona conditioning) improve trained assistants but do not close the gap to the fine-tuned simulator; scaling the simulator's model size benefits the fine-tuned simulator but yields no gain for role-playing ones; and assistants trained against role-playing simulators fail to generalize when paired with other simulators at test time, while the one trained against fine-tuned simulator does. Together, these results argue for grounding user simulators in real human behavior and measuring their quality by their downstream effect on real users.

**摘要 (中文)**: 用户模拟器越来越多地被用于构建交互式AI助手，但如何衡量这些模拟器的质量仍然是一个开放性问题。本研究表明，模拟器质量可以依据其下游效用进行量化：使用该用户模拟器训练的大语言模型助手在野外与真实人类交互时的表现如何。在仅用户模拟器不同的受控实验中，我们通过强化学习针对一系列模拟器训练大语言模型助手，从提示扮演用户的LLM到在人类WildChat话语上微调的模拟器。作为评估，我们在283名参与者参与的用户研究和来自真实人机对话的WildBench上测量成对胜率。针对扮演角色的LLM训练得到的助手在用户研究中与初始助手在统计上无法区分（51%胜率），而针对微调模拟器训练的助手则获得显著提升（比初始助手高58%，比针对角色扮演训练的助手高57%）。进一步检查揭示了三个模式：使扮演角色的LLM更真实的方法（如人物设定）提高了训练后的助手，但仍未能弥合与微调模拟器的差距；扩大模拟器模型规模对微调模拟器有益，但对角色扮演无增益；针对角色扮演模拟器训练的助手在测试时与其他模拟器配对时无法泛化，而针对微调模拟器训练的助手则可以。这些结果表明，应基于真实人类行为构建用户模拟器，并通过其对真实用户的下游影响来衡量质量。

---

## 77. cantnlp@DravidianLangTech 2026: organic domain adaptation improves multi-class hope speech detection in Tulu

**arXiv ID**: [2605.09795](https://arxiv.org/abs/2605.09795)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09795)

**作者**: Andrew Li, Sidney Wong

**分类**: Computation and Language

**发布时间**: 2026-05-10 22:32:36 UTC

**摘要 (英文)**: This paper presents our systems and results for the Hope Speech Detection in Code-Mixed Tulu Language shared task at the Sixth Workshop on Speech, Vision, and Language Technologies for Dravidian Languages (DravidianLangTech-2026). We trained an XLM-RoBERTa-based text classification system for detecting hope speech in code-mixed Tulu social media comments. We compared this organically adapted hope speech detection model with our baseline model. On the development set, the organically adapted model outperformed the baseline system. While our submitted systems performed more modestly on the official test set, these results suggest that further adapting XLM-RoBERTa on organically collected Tulu social media text containing code-mixed and mixed-script variation can improve hope speech detection in code-mixed Tulu.

**摘要 (中文)**: 本文介绍了我们为第六届达罗毗荼语言语音视觉语言技术研讨会（DravidianLangTech-2026）上的代码混合图鲁语希望语音检测共享任务开发的系统和方法。我们训练了一个基于XLM-RoBERTa的文本分类系统，用于检测代码混合图鲁语社交媒体评论中的希望语音。我们将这种有机自适应的希望语音检测模型与基线模型进行了比较。在开发集上，有机自适应模型优于基线系统。虽然我们提交的系统在官方测试集上表现较为温和，但这些结果表明，进一步在包含代码混合和混合脚本变体的有机收集的图鲁语社交媒体文本上适配XLM-RoBERTa，可以改进代码混合图鲁语中的希望语音检测。

---

## 78. Exploitation Without Deception: Dark Triad Feature Steering Reveals Separable Antisocial Circuits in Language Models

**arXiv ID**: [2605.09773](https://arxiv.org/abs/2605.09773)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09773)

**作者**: Cameron Berg, Roshni Lulla

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-10 21:36:31 UTC

**摘要 (英文)**: We use sparse autoencoder (SAE) feature steering to amplify Dark Triad personality traits (Machiavellianism, narcissism, and psychopathy) in Llama-3.3-70B-Instruct and evaluate the resulting behavioral changes across five psychological instruments. The steered model becomes substantially more exploitative, aggressive, and callous on novel behavioral scenarios (d=10.62) while its cognitive empathy remains intact, reproducing the empathy dissociation characteristic of human Dark Triad populations. Critically, strategic deception is completely unaffected across all features, suggesting that exploitation and deception may operate through dissociable computational pathways in large language models. Individual feature analysis reveals non-redundant encoding, with each feature driving distinct antisocial mechanisms through separable computational pathways. We also show that feature discovery method itself modulates intervention depth: contrastively-discovered features change both self-report and behavior, while semantically-searched features change only self-report (d=12.65 between methods on behavior). These findings suggest that antisocial tendencies in at least one large language model comprise dissociable components rather than a unified construct, with implications for how such tendencies should be detected, measured, and controlled.

**摘要 (中文)**: 我们使用稀疏自编码器（SAE）特征引导来放大暗黑三角人格特质（马基雅维利主义、自恋和精神病态）在Llama-3.3-70B-Instruct中的程度，并在五种心理仪器上评估由此产生的行为变化。引导后的模型在新颖行为场景中变得更具剥削性、攻击性和冷漠（d=10.62），同时其认知同理心保持完好，重现了人类暗黑三角人群的特征性同理心解离。关键的是，战略性欺骗在所有特征中完全不受影响，表明剥削和欺骗可能通过可分离的计算路径在大语言模型中运作。单个特征分析揭示了非冗余编码，每个特征通过可分离的计算路径驱动不同的反社会机制。我们还表明，特征发现方法本身调节干预深度：对比发现的特征同时改变自我报告和行为，而语义搜索的特征仅改变自我报告（方法间行为差异d=12.65）。这些发现表明，至少在一个大语言模型中，反社会倾向由可分离的组件构成，而非统一结构，这对如何检测、测量和控制此类倾向具有影响。

---

## 79. ConFit v3: Improving Resume-Job Matching with LLM-based Re-Ranking

**arXiv ID**: [2605.09760](https://arxiv.org/abs/2605.09760)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09760)

**作者**: Xiao Yu, Ruize Xu, Chengyuan Xue, Junyu Chen, Matthew So 等 (共9人)

**分类**: Computation and Language

**发布时间**: 2026-05-10 21:10:41 UTC

**摘要 (英文)**: A reliable resume-job matching system helps a company find suitable candidates from a pool of resumes and helps a job seeker find relevant jobs from a list of job posts. While recent advances in embedding-based methods such as ConFit and ConFit v2 can efficiently retrieve candidates at scale, the lack of controllability and explainability limits their real-world adaptations. LLM-based re-rankers can address these limitations through reasoning, but existing training recipes are developed on short-document benchmarks and do not account for noise in real-world recruiting data. In this work, we first conduct a systematic analysis over the LLM re-ranker training pipeline for person-job fit, covering inference algorithm design, RL algorithm selection, data processing, and SFT distillation. We find that using multi-pass re-ranking, training with listwise RL objectives, removing noisy samples, and distilling from a stronger LLM before RL significantly improves re-ranking performance. We then aggregate these findings to train ConFit v3 with Qwen3-8B and Qwen3-32B on real-world person-job fit datasets, and find significant improvements over existing best person-job fit systems as well as strong LLMs such as GPT-5 and Claude Opus-4.5. We hope our findings provide useful insights for future research on adapting LLM-based re-rankers to person-job fit systems.

**摘要 (中文)**: 可靠的简历-职位匹配系统帮助公司从简历池中找到合适的候选人，帮助求职者从职位列表中找到相关工作。虽然ConFit和ConFit v2等基于嵌入的方法可以高效大规模检索候选人，但缺乏可控性和可解释性。LLM-based重排序器可以通过推理解决这些限制，但现有训练方法是在短文档基准上开发的，未能考虑真实招聘数据中的噪声。在本工作中，我们首先对LLM重排序器训练流程进行系统分析，涵盖推理算法设计、RL算法选择、数据处理和SFT蒸馏。我们发现使用多轮重排序、使用listwise RL目标、去除噪声样本、在RL前从更强LLM蒸馏可显著提升重排序性能。然后，我们将这些发现汇总，在真实的人员-职位匹配数据集上使用Qwen3-8B和Qwen3-32B训练ConFit v3，发现相较于现有最佳人员-职位匹配系统以及GPT-5和Claude Opus-4.5等强LLM都有显著提升。我们希望这些发现为未来将基于LLM的重排序器适配到人员-职位匹配系统的研究提供有用见解。

---

## 80. Language Models Without a Trainable Input Embedding Table: Learning from Fixed Minimal Binary Token Codes

**arXiv ID**: [2605.09751](https://arxiv.org/abs/2605.09751)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09751)

**作者**: A. Bochkov

**分类**: Computation and Language

**发布时间**: 2026-05-10 21:00:03 UTC

**摘要 (英文)**: Trainable input embedding tables are a standard component of modern language models. We ask whether they are actually necessary at the input interface. For a vocabulary of size $V$, exact token identity requires only $K=\lceil \log_2 V\rceil$ bits. We replace the usual trainable $V\times d_{\text{model}}$ input embedding matrix with fixed minimal binary token codes and a zero-parameter lift to model width. In our main setting, $V=65{,}536$, so $K=16$, and tokens are represented by fixed 16-dimensional binary codes tiled to $d_{\text{model}}=1024$. We also evaluate a fully table-free variant in which codes are generated from token IDs on the fly and randomly recoded by an invertible affine transform over $\mathbb{F}_2^K$. Across matched 32-layer decoder-only models trained on approximately 17B tokens and evaluated over three independent training seeds, fixed minimal codes achieve comparable held-out validation perplexity to a standard learned-input baseline while removing 67.1M trainable input parameters. The fixed-code runs have a lower mean validation perplexity in our experiments, 2.36 versus 2.44, but the observed gap is within the measured seed-to-seed variation of 4.8\%; we therefore interpret the result as evidence that the trainable input table is not necessary, rather than as a statistically resolved superiority claim. The table-free affine-recoded variant remains close at 2.39 despite a slightly shorter training run. These results show that, in this regime, a trainable input embedding table is not necessary for useful language modeling. The output projection remains standard and trainable.

**摘要 (中文)**: 可训练输入嵌入表是现代语言模型的标准组件。我们问它们在输入接口是否真的必要。对于词汇量为V的情况，精确的token标识仅需要K=⌈log₂V⌉位。我们用固定最小二进制token码和零参数提升到模型宽度来替换通常的可训练V×d_model输入嵌入矩阵。在我们的主要设置中，V=65,536，所以K=16，token由固定16维二进制码平铺到d_model=1024表示。我们还评估了一种完全无表的变体，其中码由token ID即时生成，并通过F₂ᴷ上的可逆仿射变换随机重编码。在使用约17B tokens训练的匹配32层仅解码器模型上，并使用三个独立训练种子评估，固定最小码在移除67.1M可训练输入参数的同时实现了与标准学习输入基线相当的保留验证困惑度。固定码运行的平均验证困惑度更低，为2.36 vs 2.44，但观察到的差距在测量的种子间变异性4.8%以内；因此我们将其解释为可训练输入表不必要的证据，而非统计上解决的优越性声明。无表仿射重编码变体保持在2.39，接近，尽管训练运行稍短。这些结果表明，在这个范围内，可训练输入嵌入表对于有用的语言建模并非必需。输出投影保持标准和可训练。

---

## 81. The Silent Vote: Improving Zero-Shot LLM Reliability by Aggregating Semantic Neighborhoods

**arXiv ID**: [2605.09739](https://arxiv.org/abs/2605.09739)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09739)

**作者**: Sanket Badhe, Priyanka Tiwari, Deep Shah

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-10 20:22:10 UTC

**摘要 (英文)**: Large Language Models are increasingly used as zero-shot classifiers in complex reasoning tasks. However, standard constrained decoding suffers from a phenomenon we define as Renormalization Bias. When a model is restricted to a small set of target labels, the standard softmax operation discards the probability mass assigned to semantic synonyms in the original distribution. This loss of information, which we call the Silent Vote, results in artificial overconfidence and poor calibration. We propose Semantic Softmax, an inference-time layer that recovers this lost information by aggregating the scores of the semantic neighborhood surrounding each target label. We evaluate this approach on Qwen-3 and Phi-4-mini models using GoEmotions and Civil Comments datasets. Our results demonstrate consistent improvements across all evaluation metrics: Semantic Softmax substantially reduces Expected Calibration Error (ECE) and Brier Score, while simultaneously enhancing discriminative performance in terms of AUROC and Macro-F1. By accounting for linguistic nuances, our method provides a more calibrated and accurate alternative for zero-shot classification.

**摘要 (中文)**: 大语言模型越来越多地被用作复杂推理任务中的零样本分类器。然而，标准约束解码遭受一种我们定义为重归一化偏差的现象。当模型被限制在一小组目标标签时，标准softmax操作会丢弃原始分布中分配给语义同义词的概率质量。这种信息丢失，我们称之为"沉默投票"，导致人为的过度自信和糟糕的校准。我们提出语义Softmax，这是一种推理时层，通过聚合每个目标标签周围语义邻域的分数来恢复丢失的信息。我们在GoEmotions和Civil Comments数据集上使用Qwen-3和Phi-4-mini模型评估了这种方法。我们的结果在所有评估指标上显示出一致的改进：语义Softmax显著降低了预期校准误差（ECE）和Brier分数，同时在AUROC和Macro-F1方面增强了判别性能。通过考虑语言细微差别，我们的方法为零样本分类提供了更校准和准确的替代方案。

---

## 82. MedMeta: A Benchmark for LLMs in Synthesizing Meta-Analysis Conclusion from Medical Studies

**arXiv ID**: [2605.09661](https://arxiv.org/abs/2605.09661)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09661)

**作者**: Huy Hoang Ha, Benoit Favre, Francois Portet

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-10 17:20:39 UTC

**摘要 (英文)**: Large language models (LLMs) have saturated standard medical benchmarks that test factual recall, yet their ability to perform higher-order reasoning, such as synthesizing evidence from multiple sources, remains critically under-explored. To address this gap, we introduce MedMeta, the first benchmark designed to evaluate an LLM's ability to generate conclusions from medical meta-analyses using only the abstracts of cited studies. MedMeta comprises 81 meta-analyses from PubMed (2018--2025) and evaluates models using two distinct workflows: a Retrieval-Augmented Generation (Golden-RAG) setting with ground-truth abstracts, and a Parametric-only approach relying on internal knowledge. Our evaluation framework is validated by a well-structured analysis showing our LLM-as-a-judge protocol strongly aligns with human expert ratings, as evidenced by high Pearson's r correlation (0.81) and Bland-Altman analysis revealing negligible systematic bias, establishing it as a reliable proxy for scalable evaluation. Our findings underscore the critical importance of information grounding: the Golden-RAG workflow consistently and significantly outperforms the Parametric-only approach across models. In contrast, the benefits of domain-specific fine-tuning are marginal and largely neutralized when external material is provided. Furthermore, stress tests show that all models, regardless of architecture, fail to identify and reject negated evidence, highlighting a critical vulnerability in current RAG systems. Notably, even under ideal RAG conditions, current LLMs achieve only slightly above-average performance (~2.7/5.0). MedMeta provides a challenging new benchmark for evidence synthesis and demonstrates that for clinical applications, developing robust RAG systems is a more promising direction than model specialization alone.

**摘要 (中文)**: 大语言模型（LLM）已经饱和了测试事实回忆的标准医学基准，但它们执行更高阶推理的能力，如综合多个来源的证据，仍然严重未被探索。为了解决这一空白，我们引入了MedMeta，这是第一个设计用于评估LLM仅使用被引用研究的摘要从医学元分析生成结论的能力的基准。MedMeta包含来自PubMed（2018-2025）的81篇元分析，并使用两种不同工作流评估模型：使用真实摘要的检索增强生成（Golden-RAG）设置，以及依赖内部知识的纯参数方法。我们的评估框架通过结构良好的分析进行验证，显示我们的LLM-as-a-judge协议与人类专家评分高度一致，高皮尔逊r相关（0.81）和Bland-Altman分析显示可忽略的系统偏差，证明它可作为可扩展评估的可靠代理。我们的发现强调了信息锚定的关键重要性：Golden-RAG工作流在所有模型上一致且显著优于纯参数方法。相比之下，领域特定微调的好处微薄，并且在提供外部材料时大多被抵消。此外，压力测试表明，无论架构如何，所有模型都未能识别并拒绝否定性证据，突出了当前RAG系统的一个关键漏洞。值得注意的是，即使在理想的RAG条件下，当前LLM也只能达到略高于平均水平的性能（约2.7/5.0）。MedMeta为证据综合提供了一个具有挑战性的新基准，并表明对于临床应用，开发强大的RAG系统比单纯模型专业化更有前途。

---

## 83. K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Education LLMs

**arXiv ID**: [2605.09635](https://arxiv.org/abs/2605.09635)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09635)

**作者**: Hao Liang, Qihan Lin, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong 等 (共8人)

**分类**: Computation and Language

**发布时间**: 2026-05-10 16:24:26 UTC

**摘要 (英文)**: Large language models (LLMs) are increasingly used in K-12 education, yet existing benchmarks such as C-Eval, CMMLU, GaokaoBench, and EduEval mainly evaluate factual recall through exam-style question answering. Effective educational AI additionally requires curriculum cognition: understanding how knowledge is structured through prerequisite chains, concept taxonomies, experiment-concept links, and pedagogical sequencing. To address this gap, we introduce K12-KGraph, a curriculum-aligned knowledge graph extracted from official People's Education Press textbooks across mathematics, physics, chemistry, and biology from primary to high school. The graph contains seven node types (Concept, Skill, Experiment, Exercise, Section, Chapter, Book) and nine relation types covering taxonomy, prerequisite, association, verification, assessment, location, and order. Based on this graph, we construct two resources: (1) K12-Bench, a 23,640-question multi-select benchmark spanning five graph-derived task families (Ground, Prereq, Neighbor, Evidence, and Locate); and (2) K12-Train, a KG-guided supervised fine-tuning corpus of approximately 2,300 QA pairs synthesized from graph structure and node attributes. Experiments reveal substantial deficiencies in curriculum cognition: on K12-Bench, Gemini-3-Flash achieves only 57% exact match, while the best open-source model, Gemma-4-31B-IT, reaches 46%. Under a strictly matched 2,300-sample SFT budget on Qwen3-4B-Base and Llama-3.1-8B-Base, K12-Train consistently outperforms equally sized subsets from eight mainstream instruction-tuning corpora on both GaokaoBench and EduEval, demonstrating that curriculum-structured supervision is highly sample-efficient for educational tuning. We release the graph, benchmark, training data, and full construction pipeline.

**摘要 (中文)**: 大语言模型（LLM）越来越多地用于K-12教育，但现有基准如C-Eval、CMMLU、GaokaoBench和EduEval主要通过考试风格问答评估事实回忆。有效的教育AI还需要课程认知：理解知识是如何通过先决条件链、概念分类、实验-概念联系和教学顺序构建的。为了解决这一空白，我们引入了K12-KGraph，这是一个与课程对齐的知识图谱，从人民教育出版社官方教材中提取，涵盖小学到高中的数学、物理、化学和生物。该图包含七种节点类型（概念、技能、实验、练习、章节、章节、书）和九种关系类型，涵盖分类、先决条件、关联、验证、评估、位置和顺序。基于该图，我们构建了两种资源：（1）K12-Bench，一个包含23,640个问题的多选基准，涵盖五个图衍生任务族（基础、先决条件、邻居、证据和定位）；和（2）K12-Train，一个由图结构和节点属性综合的约2,300个QA对的KG引导监督微调语料库。实验揭示了课程认知的实质性缺陷：在K12-Bench上，Gemini-3-Flash仅达到57%的精确匹配，而最佳开源模型Gemma-4-31B-IT达到46%。在Qwen3-4B-Base和Llama-3.1-8B-Base上，严格匹配2,300样本的SFT预算，K12-Train在GaokaoBench和EduEval上始终优于来自八个主流指令调优语料库的等大小子集，表明课程结构化监督对教育调优具有高度样本效率。我们发布了图、基准、训练数据和完整构建流程。

---

## 84. Can We Trust LLMs for Mental Health Screening? Consistency, ASR Robustness, and Evidence Faithfulness

**arXiv ID**: [2605.09634](https://arxiv.org/abs/2605.09634)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09634)

**作者**: Erfan Loweimi, Sofia de la Fuente Garcia, Samira Loveymi, Hadi Daneshvar, Saturnino Luz

**分类**: Computation and Language

**发布时间**: 2026-05-10 16:23:50 UTC

**摘要 (英文)**: LLMs can estimate Hospital Anxiety and Depression Scale (HADS) scores from speech in a zero-shot manner, but clinical deployment requires reliability across three dimensions: intra-model consistency, ASR robustness, and evidence faithfulness. We evaluate three LLMs (Phi-4, Gemma-2-9B, and Llama-3.1-8B) on 111 English-speaking participants using ground-truth transcripts and three Whisper ASR variants (Large, Medium, Small), with three independent runs per model-condition pair. We find that (i) Phi-4 and Gemma-2-9B achieve excellent intra-model consistency (ICC > 0.89) with minimal degradation under ASR; (ii) Llama-3.1-8B shows ASR-fragile consistency, with ICC dropping from 0.82 to 0.36 at 10% WER; (iii) predictive validity is largely preserved under ASR for robust models; and (iv) keyword groundedness exceeds 93% for Phi-4 and Gemma-2-9B but falls to 77-81% for Llama-3.1-8B. Inter-model keyword agreement is far lower than score-level agreement, revealing a score-evidence dissociation with implications for clinical interpretability.

**摘要 (中文)**: LLM可以零样本方式从语音中估计医院焦虑和抑郁量表（HADS）分数，但临床部署需要在三个维度上具备可靠性：模型内一致性、ASR鲁棒性和证据忠实度。我们使用真实转录本和三种Whisper ASR变体（Large、Medium、Small）在111名英语参与者上评估了三种LLM（Phi-4、Gemma-2-9B和Llama-3.1-8B），每个模型-条件对进行三次独立运行。我们发现（i）Phi-4和Gemma-2-9B实现了出色的模型内一致性（ICC>0.89），在ASR下降级最小；（ii）Llama-3.1-8B显示ASR脆弱的一致性，ICC从0.82降至10%WER时的0.36；（iii）对于鲁棒模型，预测效度在ASR下基本保持；以及（iv）Phi-4和Gemma-2-9B的关键词接地性超过93%，但Llama-3.1-8B降至77-81%。模型间关键词一致性远低于分数层面的一致性，揭示了分数-证据分离，对临床可解释性有影响。

---

## 85. Scratchpad Patching: Decoupling Compute from Patch Size in Byte-Level Language Models

**arXiv ID**: [2605.09630](https://arxiv.org/abs/2605.09630)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09630)

**作者**: Lin Zheng, Vasilisa Bashlovkina, Timothy Dozat, Dan Garrette, Laura Rimell 等 (共6人)

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-10 16:18:22 UTC

**摘要 (英文)**: Tokenizer-free language models eliminate the tokenizer step of the language modeling pipeline by operating directly on bytes; patch-based variants further aggregate contiguous byte spans into patches for efficiency. However, the average patch size chosen at the model design stage governs a tight trade-off: larger patches reduce compute and KV-cache footprint, but degrade modeling quality. We trace this trade-off to patch lag: until a patch is fully observed, byte predictions within it must rely on a stale representation from the previous patch to preserve causality; this lag widens as patches grow larger. We introduce Scratchpad Patching (SP), which inserts transient scratchpads inside each patch to aggregate the bytes seen so far and refresh patch-level context for subsequent predictions. SP triggers scratchpads using next-byte prediction entropy, selectively allocating compute to information-dense regions and enabling post-hoc adjustment of inference-time compute. Across experiments on natural language and code, SP improves model quality at the same patch size; for example, even at $16$ bytes per patch, SP-augmented models match or closely approach the byte-level baseline on downstream evaluations while using a $16\times$ smaller KV cache over patches and $3$-$4\times$ less inference compute.

**摘要 (中文)**: 无tokenizer的语言模型通过直接在字节上操作来消除语言建模流程中的tokenizer步骤；基于patch的变体进一步将连续字节跨度聚合为patch以提高效率。然而，在模型设计阶段选择的平均patch大小支配着紧密的权衡：更大的patch减少计算和KV-cache占用，但会降低建模质量。我们将这种权衡追溯到patch延迟：在完全观察到patch之前，patch内的字节预测必须依赖来自前一个patch的陈旧表示以保持因果关系；这种延迟随着patch变大而扩大。我们引入了Scratchpad Patching（SP），它在每个patch内插入临时暂存板，以聚合到目前为止看到的字节并刷新后续预测的patch级上下文。SP使用下一个字节预测熵触发暂存板，选择性地将计算分配给信息密集区域，并实现推理时计算的事后调整。在自然语言和代码的实验中，SP在相同patch大小下提高了模型质量；例如，即使在每patch 16字节的情况下，SP增强的模型在下游评估中匹配或接近字节级基线，同时使用比patch小16×的KV cache和少3-4×的推理计算。

---

## 86. Statistical Scouting Finds Debate-Safe but Not Debate-Useful Cases: A Matched-Ceiling Study of Open-Weight LLM Reasoning Protocols

**arXiv ID**: [2605.09618](https://arxiv.org/abs/2605.09618)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09618)

**作者**: Julia Hu, Alfred Shen, Kumar Lakshmipathi

**分类**: Computation and Language, Computers and Society

**发布时间**: 2026-05-10 15:56:37 UTC

**摘要 (英文)**: When should a language model answer directly, sample and vote, or engage in multi-agent debate? Recent work shows voting often explains much of the gain attributed to debate, while selective-debate systems activate deliberation only on uncertain examples. We ask: under a matched ceiling on generated tokens (960 per example), how much per-example routing headroom exists, and how much is recoverable from cheap pre-deliberation signals? We evaluate greedy decoding, three-sample voting, and a two-agent critique-revise debate on MuSiQue and GSM8K using Llama 3.1 8B Instruct and Ministral 3 8B Instruct. On MuSiQue, an oracle selecting the correct protocol per example gains +14.0 and +13.7 pp over the best fixed one. The best fixed protocol is model- and dataset-dependent: each (model, dataset) cell has a different winner. This headroom is hard to recover from cheap ex-ante signals. A vote-entropy threshold is the only controller that directionally beats the best fixed protocol on both models (+1.3 and +1.7 pp), though individual paired-bootstrap CIs include zero. A joint analysis (meta-analysis +1.6 pp, p=0.125; Bayesian P(both>0)=0.59) is directionally consistent but not significant. Learned controllers (LR, GBT) do not outperform the threshold. The key finding is structural: vote entropy predicts where debate is safe, not where debate is needed. High entropy sharply reduces debate backfire, but 66% of debate-helpful examples (31/47) occur when voting is unanimous but wrong. A single-prompt self-critique probe on Llama flips the answer in 127/127 unanimous cases, yielding zero mutual information with the debate-helpful label; we cannot rule out a prompt-compliance artifact, but either interpretation disqualifies the probe as a router. Recovering the remaining headroom requires behavioral probes that avoid format-compliance confounds at the 8B scale.

**摘要 (中文)**: 统计侦察发现了辩论安全而非辩论有用的情况：一项开放权重LLM推理协议的天花板匹配研究。何时应该直接回答、采样投票，还是进行多智能体辩论？最近的研究表明，投票通常能解释归因于辩论的大部分收益，而选择性辩论系统仅在不确定的例子上激活 deliberation。我们在生成的token上限匹配（每个例子960个token）下询问：每个例子有多少路由 headroom，以及可以从便宜的预辩论信号中恢复多少？我们在MuSiQue和GSM8K上评估了贪婪解码、三样本投票和双智能体批评-修正辩论，使用Llama 3.1 8B Instruct和Ministral 3 8B Instruct。在MuSiQue上，一个 oracle 为每个例子选择正确协议比最佳固定协议获得+14.0和+13.7个百分点的提升。最佳固定协议取决于模型和数据集：每个（模型，数据集）单元格都有不同的获胜者。这种headroom很难从便宜的先验信号中恢复。投票熵阈值是唯一在两个模型上方向性地击败最佳固定协议的控制器（+1.3和+1.7个百分点），尽管单独的配对bootstrap置信区间包含零。联合分析（荟萃分析+1.6个百分点，p=0.125；贝叶斯P(both>0)=0.59）方向一致但不显著。学习控制器（LR、GBT）不比阈值好。关键发现是结构性的：投票熵预测辩论是否安全，而非辩论是否需要。

---

## 87. Byte-Exact Deduplication in Retrieval-Augmented Generation: A Three-Regime Empirical Analysis Across Public Benchmarks

**arXiv ID**: [2605.09611](https://arxiv.org/abs/2605.09611)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09611)

**作者**: Sietse Schelpe

**分类**: Computation and Language

**发布时间**: 2026-05-10 15:48:38 UTC

**摘要 (英文)**: This preprint presents an empirical analysis of byte-exact chunk-level deduplication in Retrieval-Augmented Generation (RAG) pipelines. We measure context reduction across three distinct operating regimes: clean academic retrieval (0.16% byte reduction on 22.2M BeIR passages), constructed enterprise patterns (24.03% reduction), and multi-turn conversational AI (80.34% reduction). To validate quality preservation, we conducted a cross-vendor 5-judge calibrated panel evaluation across four production APIs (Google Gemini 2.5 Flash, Anthropic Claude Sonnet 4.6, Meta Llama 3.3 70B, and OpenAI GPT-5.1). Applying a five-category human-in-the-loop noise-removal protocol to panel-majority materially different (MAT) pairs, we establish that byte-exact deduplication introduces zero measurable quality regression. Post-audit, all four vendors clear the strict <5% Wilson 95% upper-bound MAT threshold in both the clean and high-redundancy RAG regimes. This work demonstrates that substantial inference compute savings can be achieved deterministically without compromising evaluation-grade model quality.

**摘要 (中文)**: 本文提出了检索增强生成（RAG）管道中字节级精确chunk级去重的实证分析。我们在三种不同的操作机制下测量上下文减少：清洁学术检索（2220万BeIR段落上减少0.16%）、构建的企业模式（减少24.03%）和多轮对话AI（减少80.34%）。为验证质量保留，我们对四个生产API（Google Gemini 2.5 Flash、Anthropic Claude Sonnet 4.6、Meta Llama 3.3 70B和OpenAI GPT-5.1）进行了跨供应商5评委校准小组评估。对小组多数实质性不同（MAT）对应用五类人机交互噪声去除协议，我们确定字节级精确去重没有引入可测量的质量回归。审计后，所有四个供应商在清洁和高冗余RAG机制下都通过了严格的<5% Wilson 95%上限MAT阈值。这项工作表明，可以在不损害评估级模型质量的情况下确定性地实现显著的推理计算节省。

---

## 88. Edit-Based Refinement for Parallel Masked Diffusion Language Models

**arXiv ID**: [2605.09603](https://arxiv.org/abs/2605.09603)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09603)

**作者**: Houxing Ren, Mingjie Zhan, Zimu Lu, Ke Wang, Yunqiao Yang 等 (共8人)

**分类**: Computation and Language

**发布时间**: 2026-05-10 15:31:22 UTC

**摘要 (英文)**: Masked diffusion language models enable parallel token generation and offer improved decoding efficiency over autoregressive models. However, their performance degrades significantly when generating multiple tokens simultaneously, due to a mismatch between token-level training objectives and joint sequence consistency. In this paper, we propose ME-DLM, an edit-based refinement framework that augments diffusion generation with lightweight post-editing steps. After producing an initial complete response, the model refines it through minimal edit operations, including replacement, deletion, and insertion, conditioned on the full sequence. Training supervision is derived from edit distance, providing a deterministic signal under a fixed canonicalization scheme for learning minimal corrections. This approach encourages sequence-level consistency through globally conditioned edits while preserving the efficiency benefits of parallel diffusion decoding. Extensive experiments demonstrate that ME-DLM improves the quality and robustness of multi-token parallel generation. In particular, when built upon LLaDA, our method achieves consistent gains of 11.6 points on HumanEval and 33.6 points on GSM8K while using one-eighth of the total diffusion steps. Code is available at https://github.com/renhouxing/ME-DLM.

**摘要 (中文)**: 何时应该直接回答、采样投票，还是进行多智能体辩论？最近的研究表明，投票通常能解释归因于辩论的大部分收益，而选择性辩论系统仅在不确定的例子上激活 deliberation。我们在生成的token上限匹配（每个例子960个token）下询问：每个例子有多少路由 headroom，以及可以从便宜的预辩论信号中恢复多少？我们在MuSiQue和GSM8K上评估了贪婪解码、三样本投票和双智能体批评-修正辩论，使用Llama 3.1 8B Instruct和Ministral 3 8B Instruct。在MuSiQue上，一个 oracle 为每个例子选择正确协议比最佳固定协议获得+14.0和+13.7个百分点的提升。最佳固定协议取决于模型和数据集：每个（模型，数据集）单元格都有不同的获胜者。这种headroom很难从便宜的先验信号中恢复。投票熵阈值是唯一在两个模型上方向性地击败最佳固定协议的控制器（+1.3和+1.7个百分点），尽管单独的配对bootstrap置信区间包含零。联合分析（荟萃分析+1.6个百分点，p=0.125；贝叶斯P(both>0)=0.59）方向一致但不显著。学习控制器（LR、GBT）不比阈值好。关键发现是结构性的：投票熵预测辩论是否安全，而非辩论是否需要。高熵显著减少辩论的危害，但66%的辩论有益例子（31/47）发生在投票一致但错误的情况下。Llama上的单提示自我批评探测在127/127个一致情况下翻转了答案，与辩论有益标签产生零互信息；我们不能排除提示遵循伪影，但任何一种解释都使探测不合格为路由器。恢复剩余headroom需要避免8B规模上格式遵循混杂的行为探测。

---

## 89. CLR-voyance: Reinforcing Open-Ended Reasoning for Inpatient Clinical Decision Support with Outcome-Aware Rubrics

**arXiv ID**: [2605.09584](https://arxiv.org/abs/2605.09584)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09584)

**作者**: Aishik Nagar, Arun-Kumar Kaliya-Perumal, Yu-Hsuan Han, Andrew Sheng-Han Huang, Kristen Kee 等 (共8人)

**分类**: Computation and Language, Artificial Intelligence, Machine Learning

**发布时间**: 2026-05-10 14:51:31 UTC

**摘要 (英文)**: Inpatient clinical reasoning is a sequential decision under partial observability: the clinician sees the admission so far and must choose the next action whose downstream consequences are not yet visible. Existing clinical-LLM evaluations and RL rewards signals collapse this into closed-form retrieval, clinical journey leakage, or unanchored LLM-as-judge scoring. We introduce CLR-voyance, a framework that reformulates inpatient reasoning as a Partially Observable Markov Decision Process (POMDP) and supervises it with rewards that are simultaneously outcome-grounded and clinician-validated. We instantiate the formulation as CLR-POMDP, which partitions successful patient journeys into a policy-visible past and an oracle-only future. Using the past information, an oracle LLM generates a case-specific query-answer pair, and the first adaptive rubric for clinical reasoning which is verifiable in the future of the patient journey. These rubrics are used for both post-training and evaluation of models for inpatient clinical reasoning. We post-train Qwen3-8B and MedGemma-4B with GRPO followed by model merging, yielding state-of-the-art inpatient clinical reasoning while retaining generalist capabilities. CLR-voyance-8B achieves 84.91% on CLR-POMDP, ahead of frontier medical reasoning models like GPT-5 (77.83%) and MedGemma-27B (66.66%) and has comparable or better performance on existing medical benchmarks. To ensure a clinically meaningful setting, we conduct a large-scale clinician alignment study, where physicians curate per-case rubrics, grade candidate responses, and provide blinded pairwise preferences of model reasoning. This study provides insights on clinical LLM-as-a-judge and clinical preference-model selection, which can inform the community at large. CLR-voyance has been deployed for 6+ months at a partner public hospital, drafting thousands of reasoning-heavy inpatient notes.

**摘要 (中文)**: 住院临床推理是在部分可观测性下的顺序决策：临床医生看到目前的入院情况，必须选择下一个行动，其下游后果尚未可见。现有临床LLM评估和RL奖励信号将其简化为封闭形式检索、临床旅程泄漏或无锚点的LLM-as-judge评分。我们引入了CLR-voyance，这是一个将住院推理重新表述为部分可观测马尔可夫决策过程（POMDP）并用同时基于结果且经临床医生验证的奖励监督的框架。我们将公式具体化为CLR-POMDP，它将成功的患者旅程分为策略可见的过去和仅预言的未来。使用过去信息，oracle LLM生成特定案例的问答对，以及临床推理的第一个自适应评分标准，可在患者旅程的未来验证。这些评分标准既用于住院临床推理模型的后训练和评估。我们使用GRPO对Qwen3-8B和MedGemma-4B进行后训练，然后进行模型合并，在保持通用能力的同时实现最先进的住院临床推理。CLR-voyance-8B在CLR-POMDP上达到84.91%，领先于前沿医学推理模型如GPT-5（77.83%）和MedGemma-27B（66.66%），并在现有医学基准上具有相当或更好的性能。为确保临床有意义的设置，我们进行了一项大规模临床医生对齐研究，其中医生策划每案例评分标准、评估候选响应，并提供模型推理的盲对偏好。这项研究提供了关于临床LLM-as-a-judge和临床偏好模型选择的见解，可为更广泛的社区提供信息。CLR-voyance已在合作公立医院部署6个多月，起草了数千份推理密集型住院记录。

---

## 90. Towards Compact Sign Language Translation: Frame Rate and Model Size Trade-offs

**arXiv ID**: [2605.09554](https://arxiv.org/abs/2605.09554)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09554)

**作者**: Kuanwei Chen, Mengfeng Tsai

**分类**: Computation and Language, Computer Vision and Pattern Recognition

**发布时间**: 2026-05-10 14:15:38 UTC

**摘要 (英文)**: Sign Language Translation (SLT) converts sign language videos into spoken-language text, bridging communication between Deaf and hearing communities. Current gloss-free approaches rely on large encoder-decoder models, limiting deployment. We propose a compact 77M-parameter pipeline that couples MMPose skeletal pose extraction with a single linear projection into T5-small. By varying the input frame rate, we expose a practical efficiency trade-off: at 12 fps the model halves its sequence length, achieving a 75% reduction in encoder quadratic self-attention computational complexity while incurring only a modest BLEU-4 drop (9.53 vs. 10.06 at 24 fps on How2Sign). Our system is roughly 3x smaller than prior T5-base systems, demonstrating that a lightweight architecture can remain competitive without hierarchical encoders or large-scale models.

**摘要 (中文)**: 手语翻译（SLT）将手语视频转换为口语文本，架起聋人与听力社区之间的桥梁。当前无词汇的方法依赖大型编码器-解码器模型，限制了部署。我们提出了一个77M参数的紧凑管道，将MMPose骨骼姿态提取与T5-small的单一线性投影相结合。通过改变输入帧率，我们揭示了一种实用的效率权衡：在12fps时，模型将序列长度减半，在编码器二次自注意力计算复杂度上实现75%的减少，同时仅造成适度的BLEU-4下降（How2Sign上24fps时为9.53 vs 10.06）。我们的系统比之前的T5-base系统大约小3倍，表明轻量级架构可以在没有分层编码器或大规模模型的情况下保持竞争力。

---

## 91. Crosslingual On-Policy Self-Distillation for Multilingual Reasoning

**arXiv ID**: [2605.09548](https://arxiv.org/abs/2605.09548)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09548)

**作者**: Yihong Liu, Raoyuan Zhao, Michael A. Hedderich, Hinrich Schütze

**分类**: Computation and Language

**发布时间**: 2026-05-10 14:06:09 UTC

**摘要 (英文)**: Large language models (LLMs) have achieved remarkable progress in mathematical reasoning, but this ability is not equally accessible across languages. Especially low-resource languages exhibit much lower reasoning performance. To address this, we propose Crosslingual On-Policy Self-Distillation (COPSD), which transfers a model's own high-resource reasoning behavior to low-resource languages. COPSD uses the same model as student and teacher: the student sees only the low-resource problem, while the teacher receives privileged crosslingual context, including the problem translation and reference solution in English. Training minimizes full-distribution token-level divergence on the student's own rollouts, providing dense supervision while avoiding the sparsity and instability of outcome-only reinforcement learning (RL). Experiments on 17 low-resource African languages show that COPSD consistently improves low-resource mathematical reasoning across model sizes and substantially outperforms Group Relative Policy Optimization (GRPO). Further analyses show that COPSD improves answer-format adherence, strengthens test-time scaling, and generalizes to harder multilingual reasoning benchmarks, with especially large gains for lower-resource languages. We make our code and data available at: https://github.com/cisnlp/COPSD.

**摘要 (中文)**: 大语言模型（LLM）在数学推理方面取得了显著进展，但这种能力并非在所有语言中都能平等获取。特别是低资源语言表现出低得多的推理性能。为了解决这一问题，我们提出了跨语言策略自蒸馏（COPSD），将模型自身的高资源推理行为转移到低资源语言。COPSD使用同一模型作为学生和教师：学生只看到低资源问题，而教师获得特权跨语言上下文，包括问题翻译和英文参考解决方案。训练最小化学生自身 rollout上的全部分布token级差异，提供密集监督，同时避免仅结果强化学习（RL）的稀疏性和不稳定性。在17种低资源非洲语言上的实验表明，COPSD一致性地改善了低资源数学推理，跨模型规模并显著优于组相对策略优化（GRPO）。进一步分析表明，COPSD改善了答案格式 adherence，增强了测试时扩展性，并推广到更硬的多语言推理基准，对于较低资源语言尤其增益大。我们在https://github.com/cisnlp/COPSD提供代码和数据。

---

## 92. TacoMAS: Test-Time Co-Evolution of Topology and Capability in LLM-based Multi-Agent Systems

**arXiv ID**: [2605.09539](https://arxiv.org/abs/2605.09539)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09539)

**作者**: Chen Xu, Yicheng Hu, Ruizi Wang, Xinyu Lin, Wenjie Wang 等 (共7人)

**分类**: Computation and Language

**发布时间**: 2026-05-10 13:52:00 UTC

**摘要 (英文)**: Multi-agent systems (MAS) have emerged as a promising paradigm for solving complex tasks. Recent work has explored self-evolving MAS that automatically optimize agent capabilities or communication topologies. However, existing methods either learn a topology that remains fixed at inference time or adapt only the topology or capability during inference. We empirically and theoretically show that effective test-time evolution requires jointly adapting both axes, but on different time scales: capabilities should update rapidly to handle emerging subtasks, while the topology should evolve more slowly to preserve coordination stability. We then introduce TacoMAS, a test-time co-evolution framework for dynamic MAS. TacoMAS formulates MAS inference as a task of online graph adaptation, where nodes represent agents with role-specific capabilities and edges define their communication topology. During inference, a fast capability loop updates agent expertise using trajectory-level feedback, while a slow meta-LLM-driven topology loop performs agents' birth-death operations on MAS, including edge edit, agent addition, and agent removal. We further show that this fast-slow design drives MAS evolution toward a task-conditioned stable equilibrium. Experiments on four benchmarks demonstrate that TacoMAS outperforms nearly 20 multi-agent baselines, achieving an average improvement of 13.3% over the strongest baseline. The codes are released at https://github.com/chenxu2-gif/TacoMAS-MultiAgent.

**摘要 (中文)**: 多智能体系统（MAS）已成为解决复杂任务的有前景的范式。最近的工作探索了自动优化智能体能力或通信拓扑的自我进化MAS。然而，现有方法要么学习在推理时保持不变的拓扑，要么仅在推理时适应拓扑或能力。我们从经验和理论上表明有效的测试时进化需要同时适应两个轴，但时间尺度不同：能力应该快速更新以处理新出现的子任务，而拓扑应该演化得更慢以保持协调稳定性。然后我们引入了TacoMAS，这是一个用于动态MAS的测试时共同进化框架。TacoMAS将MAS推理表述为在线图适应任务，其中节点表示具有角色特定能力的智能体，边定义它们的通信拓扑。在推理过程中，快速能力循环使用轨迹级反馈更新智能体专业知识，而慢速元LLM驱动的拓扑循环执行智能体的MAS生死操作，包括边编辑、智能体添加和智能体移除。我们进一步表明，这种快慢设计驱动MAS演化向任务条件稳定平衡。在四个基准上的实验表明，TacoMAS优于近20个多智能体基线，比最强基线平均提升13.3%。代码发布于https://github.com/chenxu2-gif/TacoMAS-MultiAgent。

---

## 93. TAD: Temporal-Aware Trajectory Self-Distillation for Fast and Accurate Diffusion LLM

**arXiv ID**: [2605.09536](https://arxiv.org/abs/2605.09536)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09536)

**作者**: Haoyang Zhou, Li Kong, Shijie Ren, Xiting Wang, Shuang Liang 等 (共7人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-10 13:38:53 UTC

**摘要 (英文)**: Diffusion large language models (dLLMs) offer a promising paradigm for parallel text generation, but in practice they face an accuracy-parallelism trade-off, where increasing tokens per forward (TPF) often degrades generation quality. Existing acceleration methods often gain speed at the cost of accuracy. To address this limitation, we propose TAD, a Temporal-Aware trajectory self-Distillation framework. During data construction, we condition a teacher model on both the prompt and the ground-truth response to generate decoding trajectories, recording the intermediate masked states throughout the process. Based on how many decoding steps remain before each masked token is revealed, we partition masked positions into near and distant subsets. For near tokens, we train the student with a hard cross-entropy loss using the teacher trajectory tokens as labels, encouraging confident predictions for tokens that are about to be decoded. For distant tokens, we apply a soft KL divergence loss between the teacher and student token distributions, providing softer supervision and preserving future planning knowledge. This temporal-aware partition naturally gives rise to two deployment configurations: a Quality model that prioritizes accuracy and a Speed model that favors more aggressive acceleration. Experiments show that TAD consistently improves the accuracy-parallelism trade-off. On LLaDA, it raises average accuracy from 46.2\% to 51.6\% with the Quality model and average AUP from 46.2 to 257.1 with the Speed model. Our code is available at: https://github.com/BHmingyang/TAD

**摘要 (中文)**: 扩散大语言模型（dLLM）为并行文本生成提供了有前景的范式，但实际上它们面临精度-并行性权衡，其中增加每次前向的token数（TPF）通常会降低生成质量。现有加速方法通常以精度为代价获得速度。为了解决这一限制，我们提出了TAD，一个时间感知的轨迹自蒸馏框架。在数据构建阶段，我们让教师模型基于提示和真实响应来生成解码轨迹，记录整个过程中的中间掩码状态。根据每个掩码token被揭示前还剩多少解码步骤，我们将掩码位置分为近和远子集。对于近端token，我们使用硬交叉熵损失训练学生，以教师轨迹token为标签，鼓励对即将解码的token进行自信预测。对于远端token，我们在教师和学生token分布之间应用软KL散度损失，提供更软的监督并保留未来规划知识。这种时间感知分区自然产生两种部署配置：优先考虑精度的质量模型和青睐更激进加速的速度模型。实验表明TAD一致性地改善了精度-并行性权衡。在LLaDA上，它将质量模型的平均精度从46.2%提高到51.6%，将速度模型的平均AUP从46.2提高到257.1。我们的代码可访问：https://github.com/BHmingyang/TAD

---

## 94. Assessment of RAG and Fine-Tuning for Industrial Question-Answering-Applications

**arXiv ID**: [2605.09533](https://arxiv.org/abs/2605.09533)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09533)

**作者**: Jakob Sturm, Josef Pichlmeier, Christian Bernhard, Maka Karalashvili, Johannes Klepsch 等 (共7人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-10 13:35:16 UTC

**摘要 (英文)**: Large Language Models (LLMs) are increasingly employed in enterprise question-answering (QA) systems, requiring adaptation to domain-specific knowledge. Among the most prevalent methods for incorporating such knowledge are Retrieval-Augmented Generation (RAG) and fine-tuning (FT). Yet, from a cost-accuracy trade-off perspective, it remains unclear which approach best suits industry scenarios. This study examines the impact of RAG and FT on two closed datasets specific to the automotive industry, assessing answer quality and operational costs. We extend the Cost-of-Pass framework proposed by Erol et al. (arXiv:2504.13359) to jointly assess output quality, generation cost, and user interaction cost. Our findings reveal that while premium models perform best out of the box, open-source models can achieve comparable quality when enhanced with RAG. Overall, RAG emerges as the most effective and cost-efficient adaptation method for both closed- and open-source models.

**摘要 (中文)**: 大语言模型（LLM）越来越多地用于企业问答（QA）系统，需要适应特定领域的知识。融合此类知识最流行的方法是检索增强生成（RAG）和微调（FT）。然而，从成本-精度权衡角度来看，哪种方法最适合行业场景仍不清楚。本研究检查了RAG和FT对两个特定于汽车行业的封闭数据集的影响，评估答案质量和运营成本。我们扩展了Erol等人（arXiv:2504.13359）提出的Cost-of-Pass框架，以联合评估输出质量、生成成本和用户交互成本。我们的发现表明，虽然高级模型开箱即用表现最佳，但开源模型通过RAG增强可以达到相当的质量。总体而言，RAG成为封闭和开源模型最有效和最具成本效益的适应方法。

---

## 95. Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal

**arXiv ID**: [2605.09502](https://arxiv.org/abs/2605.09502)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09502)

**作者**: Aojie Yuan, Zhiyuan Julian Su, Haiyue Zhang, Yi Nian, Yue Zhao

**分类**: Computation and Language, Artificial Intelligence, Machine Learning

**发布时间**: 2026-05-10 12:26:46 UTC

**摘要 (英文)**: Chain-of-thought (CoT) prompting assumes that generated reasoning reflects a model's internal computation. We show this assumption is wrong in a specific, measurable way: models internally detect their own reasoning errors but outwardly express confidence in them. A linear probe on hidden states predicts trace correctness with 0.95 AUROC -- from the very first reasoning step (0.79) -- while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a 0.20-point gap invisible in the generated text. This hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B-72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC). The natural question is whether this signal can fix the errors it detects. It cannot. Four interventions -- activation steering, probe-guided best-of-N, self-correction, and activation patching -- all fail; patching destroys output coherence entirely. The signal is diagnostic, not causal: a readout of computation quality, not a lever to redirect it. This delineates a boundary for mechanistic interpretability: error representations during reasoning are fundamentally different from the factual knowledge representations that prior work has successfully edited.

**摘要 (中文)**: 思维链（CoT）提示假设生成的推理反映模型的内部计算。我们以特定的、可测量的方式表明这一假设是错误的：模型内部检测到自己的推理错误，但表面却表达出对它们的信心。隐藏状态上的线性探测以0.95 AUROC预测轨迹正确性——从第一个推理步骤开始（0.79）——而错误轨迹的口头化信心为4.55/5，几乎与正确的（4.87/5）相同。同一数据上的文本表面分类器仅达到0.59，确认在生成文本中不可见的0.20差距。这种隐藏的错误意识在三个模型家族（Qwen、Llama、Phi）、1.5B-72B参数和经过RL训练的推理模型（DeepSeek-R1，0.852 AUROC）中都存在。自然而然的问题是，这个信号是否能修复它检测到的错误。不能。四种干预——激活探测、探测引导的最佳选择、自纠正和激活修补——都失败了；修补完全破坏输出连贯性。该信号是诊断性的，而非因果性的：是计算质量的读数，而非重新定向它的杠杆。这为机制可解释性划定了边界：推理过程中的错误表示与之前工作已成功编辑的事实知识表示根本不同。

---

## 96. Beyond Language: Format-Agnostic Reasoning Subspaces in Large Language Models

**arXiv ID**: [2605.09496](https://arxiv.org/abs/2605.09496)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09496)

**作者**: Aojie Yuan, Zhiyuan Su

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-10 12:06:48 UTC

**摘要 (英文)**: Large language models represent the same reasoning in vastly different surface forms -- English prose, Python code, mathematical notation -- yet whether they share a common internal substrate across these symbolic systems remains unknown. We introduce the TriForm Benchmark (18 concepts x 6 forms x 3 instances = 324 stimuli) and study five LLMs (1.6B-8B) across three architecture families. Using permutation-corrected RSA, cross-form probing, and activation patching, we find converging evidence for a Format-Agnostic Reasoning Subspace (FARS) in middle layers. We make FARS concrete: concept-centroid PCA extracts a 10-dimensional subspace that amplifies concept structure 3x while suppressing form information to near zero. Replacing only these 10 dimensions during cross-form patching preserves 90-96% of model output -- far exceeding both full activation replacement (44-56%) and variance-maximizing PCA (60-74%) -- while ablating them causes targeted disruption. FARS generalizes to held-out concepts and converges across architectures (CCA > 0.79 for all model pairs), providing within-modality evidence for the Platonic Representation Hypothesis. We further discover a declarative-procedural asymmetry: representations are far more compatible between prose and mathematics than between either and code, suggesting that the critical axis of divergence is not linguistic vs. formal but declarative vs. procedural.

**摘要 (中文)**: 大语言模型以截然不同的表面形式表示相同的推理——英文散文、Python代码、数学符号——但它们是否在这些符号系统之间共享共同的内部基质仍然未知。我们引入了TriForm基准（18个概念×6种形式×3个实例=324个刺激），并研究了五个跨三个架构家族的LLM（1.6B-8B）。使用排列校正的RSA、跨形式探测和激活修补，我们找到了中间层格式无关推理子空间（FARS）的收敛证据。我们使FARS具体化：概念质心PCA提取了一个将概念结构放大3倍同时将形式信息抑制到接近零的10维子空间。在跨形式修补期间仅替换这10个维度保留了90-96%的模型输出——远远超过完整激活替换（44-56%）和方差最大化PCA（60-74%）——而消融它们会导致针对性破坏。FARS推广到保留概念并在架构间收敛（所有模型对的CCA>0.79），为柏拉图表示假设提供了模态内证据。我们进一步发现了声明性-程序性不对称：散文和数学之间的表示远比它们与代码之间的更兼容，表明关键的分歧轴不是语言vs形式，而是声明性vs程序性。

---

## 97. APCD: Adaptive Path-Contrastive Decoding for Reliable Large Language Model Generation

**arXiv ID**: [2605.09492](https://arxiv.org/abs/2605.09492)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09492)

**作者**: Tianyu Zheng, Hong Wu, Jiaji Zhong

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-10 11:57:39 UTC

**摘要 (英文)**: Large language models (LLMs) often suffer from hallucinations due to error accumulation in autoregressive decoding, where suboptimal early token choices misguide subsequent generation. Although multi-path decoding can improve robustness by exploring alternative trajectories, existing methods lack principled strategies for determining when to branch and how to regulate inter-path interactions. We propose Adaptive Path-Contrastive Decoding (APCD), a multi-path decoding framework that improves output reliability through adaptive exploration and controlled path interaction. APCD consists of two components: (1) Entropy-Driven Path Expansion, which delays branching until predictive uncertainty - measured by Shannon entropy over top candidate tokens - indicates multiple plausible continuations; and (2) Divergence-Aware Path Contrast, which encourages diverse reasoning trajectories while dynamically attenuating inter-path influence as prediction distributions diverge. Experiments on eight benchmarks demonstrate improved factual accuracy while maintaining decoding efficiency. Our code is available at https://github.com/zty-king/APCD.

**摘要 (中文)**: 大语言模型（LLM）经常因自回归解码中的错误累积而产生幻觉，其中次优的早期token选择误导后续生成。虽然多路径解码可以通过探索替代轨迹来提高鲁棒性，但现有方法缺乏确定何时分支以及如何调节路径间交互的原则性策略。我们提出了自适应路径对比解码（APCD），一种通过自适应探索和控制路径交互来提高输出可靠性的多路径解码框架。APCD由两个组件组成：（1）熵驱动的路径扩展，延迟分支直到预测不确定性——通过对顶级候选token的香农熵测量——表明多个合理的 continuation；以及（2） divergence感知的路径对比，鼓励多样化的推理轨迹，同时随着预测分布发散动态减弱路径间影响。在八个基准上的实验表明提高了事实准确性，同时保持了解码效率。我们的代码可访问 https://github.com/zty-king/APCD

---

## 98. Not All Thoughts Need HBM: Semantics-Aware Memory Hierarchy for LLM Reasoning

**arXiv ID**: [2605.09490](https://arxiv.org/abs/2605.09490)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09490)

**作者**: Aojie Yuan, Tianqi Shen, Dajun Zhang

**分类**: Computation and Language, Hardware Architecture, Machine Learning

**发布时间**: 2026-05-10 11:54:40 UTC

**摘要 (英文)**: Reasoning LLMs produce thousands of chain-of-thought tokens whose KV cache must reside in scarce GPU HBM. The dominant response -- permanently evicting low-importance tokens -- is catastrophic for reasoning: accuracy collapses to 0-2.5% when half the cache is removed. We ask a different question: must every token live in HBM, or can some live elsewhere? We introduce a semantics-aware memory hierarchy that sorts tokens into four tiers -- HBM, DDR, compressed, and evicted -- using cumulative attention scoring. Low-importance tokens are moved to CPU memory rather than destroyed; before each attention step they are prefetched back at full precision, contributing exactly the same terms as if they had never left the GPU. We formalize this as zero-approximation-error offloading and derive our central finding: accuracy depends solely on how many tokens are permanently discarded (the eviction ratio), not on how many remain in HBM. A controlled 3x3 grid over HBM and eviction ratios confirms this across three model scales (7B-32B) and four benchmarks. With only 3% eviction, the hierarchy retains 91% of full-cache accuracy on GSM8K and 71% on MATH-500 (n=200); at 14B scale it matches the uncompressed baseline (90% vs. 86%) while halving HBM occupancy. A head-to-head reproduction of R-KV -- the current SOTA eviction method -- on our setup achieves only 0-32% at comparable budgets. A system prototype with real GPU-CPU data movement shows that the price of this preservation is modest -- 5-7% transfer overhead -- and scaling analysis projects 2-48 GB HBM savings at production batch sizes.

**摘要 (中文)**: 推理LLM产生数千个思维链token，其KV cache必须存放在稀缺的GPU HBM中。主流回应——永久驱逐低重要性token——对推理是灾难性的：当一半cache被移除时，精度崩溃到0-2.5%。我们问一个不同的问题：每个token都必须留在HBM中，还是可以留在其他地方？我们引入了一个语义感知内存层次结构，使用累积注意力评分将token分类到四个层级——HBM、DDR、压缩和驱逐。低重要性token被移动到CPU内存而非销毁；在每个注意力步骤之前，它们以全精度预取回，完全贡献与它们从未离开GPU时相同的项。我们将其形式化为零近似误差卸载，并得出我们的核心发现：精度仅取决于永久丢弃的token数量（驱逐比率），而不是HBM中保留的数量。对HBM和驱逐比率进行的受控3×3网格确认了这一点，跨三个模型规模（7B-32B）和四个基准。仅3%的驱逐，层次结构在GSM8K上保留91%的全cache精度，在MATH-500（n=200）上保留71%；在14B规模上，它匹配未压缩基线（90% vs 86%），同时减少一半HBM占用。我们对R-KV的复制——当前SOTA驱逐方法——在我们的设置上在相当预算下仅达到0-32%。具有真实GPU-CPU数据传输的系统原型表明，这种保留的代价是适度的——5-7%传输开销——Scaling分析预测在生产批大小下可节省2-48GB HBM。

---

## 99. A Cognitively Grounded Bayesian Framework for Misinformation Susceptibility

**arXiv ID**: [2605.09483](https://arxiv.org/abs/2605.09483)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09483)

**作者**: Pranava Madhyastha

**分类**: Computation and Language, Artificial Intelligence, Machine Learning

**发布时间**: 2026-05-10 11:37:40 UTC

**摘要 (英文)**: In this (work in progress) paper, we present Bounded Pragmatic Listener (or BPL), a cognitively grounded Bayesian framework for modelling susceptibility to information disorder. BPL extends Rational Speech Act theory with three cognitively motivated bounds derived from the bounded rationality literature with a) a recursion depth bound (that emphasises working memory limits);b) a prior compression parameter (which is oriented at capturing information bottleneck); and c) an availability sample size (that operationalises importance sampling with saliency-weighted proposals). This allows us to test predictions about misinformation susceptibility, annotator disagreement, and the differential vulnerability to mis-, dis-, and mal-information as defined in the Information Disorder framework. We validate BPL on the LIAR and MultiFC benchmarks showcasing competitive veracity classification and experimental support for the depth-mismatch paradox.

**摘要 (中文)**: 在这篇工作论文中，我们提出了有界务实 listener（BPL），一个认知基础的贝叶斯框架，用于建模对信息 disorder的敏感性。BPL将理性言语行为理论与来自有界理性文献的三个认知动机边界扩展：a）递归深度边界（强调工作记忆限制）；b）先验压缩参数（旨在捕获信息瓶颈）；以及c）可用样本大小（将重要性采样与显著性加权提议操作化）。这使我们能够测试关于 misinformation敏感性、标注者分歧以及对信息 disorder框架定义的误信息、虚假信息和恶意信息差异化脆弱性的预测。我们在LIAR和MultiFC基准上验证BPL，展示了竞争性的真实性分类和深度不匹配悖论的实验支持。

---

## 100. Align and Shine: Building High-Quality Sentence-Aligned Corpora for Multilingual Text Simplification

**arXiv ID**: [2605.09476](https://arxiv.org/abs/2605.09476)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09476)

**作者**: Kenji Hilasaca, Nouran Khallaf, Serge Sharoff

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-10 11:07:24 UTC

**摘要 (英文)**: Text simplification plays a crucial role in improving the accessibility and comprehensibility of written information for diverse audiences, including language learners and readers with limited literacy. Despite its importance, large-scale, high-quality datasets for training and evaluating text simplification models remain scarce for languages other than English. This paper reports an experimental study on the collection and processing of crowd-sourced simplification data from comparable corpora to construct a corpus suitable for both training and testing text simplification systems across multiple languages (Catalan, English, French, Italian and Spanish). We report mechanisms for sentence-level alignment from document-level data. The resulting dataset of the aligned sentence pairs is publicly available.

**摘要 (中文)**: 文本简化在提高不同受众（包括语言学习者和识字能力有限的读者）书面信息的可访问性和可理解性方面起着关键作用。尽管其重要性，除英语外，用于训练和评估文本简化模型的大规模、高质量数据集仍然稀缺。本文报告了一项关于从可比语料库收集和处理众包简化数据的实验研究，以构建一个适用于多种语言（加泰罗尼亚语、英语、法语、意大利语和西班牙语）的文本简化系统训练和测试的语料库。我们报告了从文档级数据进行句子级对齐的机制。产生的对齐句子对数据集是公开可用的。

---

## 101. FinMoji: A Framework for Emoji-driven Sentiment Analysis in Financial Social Media

**arXiv ID**: [2605.09469](https://arxiv.org/abs/2605.09469)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09469)

**作者**: Ahmed Mahrous, Roberto Di Pietro

**分类**: Computation and Language

**发布时间**: 2026-05-10 10:39:14 UTC

**摘要 (英文)**: This paper explores the use of emojis in financial sentiment analysis, focusing on the social media platform StockTwits. Emojis, increasingly prevalent in digital communication, have potential as compact indicators of investor sentiment, which can be critical for predicting market trends. Our study examines whether emojis alone can serve as reliable proxies for financial sentiment and how they compare with traditional text-based analysis. We conduct a series of experiments using logistic regression and transformer models. We further analyze the performance, computational efficiency, and data requirements of emoji-based versus text-based sentiment classification. Using a balanced dataset of about 528,000 emoji-containing StockTwits posts, we find that emoji-only models achieve F1 approximately 0.75, lower than text-emoji combined models, which achieve F1 approximately 0.88, but with far lower computational cost. This is a useful feature in time-sensitive settings such as high-frequency trading. Furthermore, certain emojis and emoji pairs exhibit strong predictive power for market sentiment, demonstrating over 90 percent accuracy in predicting bullish or bearish trends. Finally, our research reveals large statistical differences in emoji usage between financial and general social media contexts, stressing the need for domain-specific sentiment analysis models.

**摘要 (中文)**: 本文探讨了表情符号在金融情感分析中的应用，重点关注社交媒体平台StockTwits。表情符号在数字通信中越来越普遍，作为投资者情绪的紧凑指标具有潜力，这对预测市场趋势至关重要。我们的研究检查了表情符号是否可以作为金融情绪的可靠代理，以及它们与传统基于文本的分析相比如何。我们使用逻辑回归和transformer模型进行了一系列实验。我们进一步分析了基于表情符号与基于文本的情感分类的性能、计算效率和数据需求。使用包含约528,000条包含表情符号的StockTwits帖子的平衡数据集，我们发现仅表情符号模型达到F1约0.75，低于结合表情符号和文本的模型（F1约0.88），但计算成本低得多。这在高频交易等时间敏感环境中是一个有用的特性。此外，某些表情符号和表情符号组合对市场情绪表现出很强的预测能力，在预测看涨或看跌趋势方面表现出超过90%的准确性。最后，我们的研究揭示了金融和一般社交媒体环境中表情符号使用存在很大的统计差异，强调了领域特定情感分析模型的必要性。

---

## 102. Beyond Position Bias: Shifting Context Compression from Position-Driven to Semantic-Driven

**arXiv ID**: [2605.09463](https://arxiv.org/abs/2605.09463)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09463)

**作者**: Jiwei Tang, Zhijing Huang, Xinyu Zhang, Chen Jason Zhang, Jianxing Yu 等 (共8人)

**分类**: Computation and Language

**发布时间**: 2026-05-10 10:27:57 UTC

**摘要 (英文)**: Large Language Models (LLMs) have demonstrated exceptional performance across diverse tasks. However, their deployment in long-context scenarios faces high computational overhead and information redundancy. While soft prompt compression has emerged as a promising way to mitigate these costs by compressing sequences into compact embeddings, existing paradigms remain fundamentally constrained by position bias: they primarily rely on learnable tokens insertion at fixed positions or group tokens according to their physical token layout, thereby inducing performance instability and semantic fragmentation. To overcome this bottleneck, we propose Semantic Consistency Context Compression (SeCo), a method that shifts context compression from position-driven to semantic-driven. Rather than constraint by physical token layout, SeCo dynamically anchors compression directly in the semantic space by selecting query-relevant tokens as semantic centers and aggregating remaining tokens via consistency-weighted merging. This design inherently preserves semantic consistency while eliminating position bias. Extensive experiments on 14 benchmarks across two backbone models demonstrate that SeCo consistently shows superiority in downstream tasks, inference latency, and out-of-domain robustness. The code is available at https://anonymous.4open.science/r/seco-EE5E.

**摘要 (中文)**: 大语言模型（LLM）在不同任务中表现出色。然而，它们在长上下文场景中的部署面临高计算开销和信息冗余。虽然软提示压缩已成为通过将序列压缩为紧凑嵌入来缓解这些成本的有前景的方法，但现有范式仍然从根本上受到位置偏见的约束：它们主要依赖在固定位置插入可学习token或根据物理token布局对token进行分组，从而导致性能不稳定和语义碎片化。为了克服这一瓶颈，我们提出了语义一致性上下文压缩（SeCo），一种将上下文压缩从位置驱动转变为语义驱动的方法。SeCo不受物理token布局约束，而是通过选择与查询相关的token作为语义中心并通过一致性加权合并聚合其余token，在语义空间中动态锚定压缩。这种设计固有地保留了语义一致性，同时消除了位置偏见。在两个主干模型上的14个基准的大量实验表明，SeCo在下游任务、推理延迟和领域外鲁棒性方面始终表现出色。代码可访问 https://anonymous.4open.science/r/seco-EE5E

---

## 103. Key Coverage Matters: Semi-Structured Extraction of OCR Clinical Reports

**arXiv ID**: [2605.09440](https://arxiv.org/abs/2605.09440)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09440)

**作者**: Yu Wang, Yingyun Li, Ying Qin, Haiyang Qian

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-10 09:29:33 UTC

**摘要 (英文)**: Clinical reports are often fragmented across healthcare institutions because privacy regulations and data silos limit direct information sharing. When patients seek care at a different hospital, they often carry paper or scanned reports from prior visits. This hinders EHR integration and longitudinal review, and downstream applications that depend on more complete patient records, such as patient management, follow-up care, real-world studies, and clinical-trial matching. Although OCR can digitize such reports, reliable extraction remains challenging because clinical documents are heterogeneous, OCR text is noisy, and many healthcare settings require low-cost on-premise deployment. We formulate this problem as canonical key-conditioned extractive question answering over OCR-derived clinical reports. Because the key fields are neither fixed nor known in advance, the key space is open. We maintain a canonical key inventory through iterative key mining, normalization, clustering, and lightweight human verification, and introduce key coverage as a metric to quantify inventory completeness. Using a 0.2B BERT-based model, experiments on real-world reports from more than 20 hospitals show performance improves monotonically with key coverage. The model achieves F1 scores of 0.839 and 0.893 under exact match and boundary-tolerant matching, respectively, once the Top-90 canonical keys are covered. These results show that key coverage is a dominant factor for end-to-end performance. At Top-90 coverage, our model outperforms a fine-tuned Qwen3-0.6B baseline under exact match. Although our annotated corpus is Chinese, the method relies on the language-agnostic key-value organization of semi-structured clinical reports and can be adapted to other settings given an appropriate canonical key inventory and alias mapping.

**摘要 (中文)**: 临床报告因隐私法规和数据孤岛限制直接信息共享而分散在医疗机构之间。当患者在不同的医院就诊时，他们通常会携带之前就诊的纸质或扫描报告。这阻碍了EHR整合和纵向审查，以及依赖更完整患者记录的下游应用，如患者管理、随访护理、真实世界研究和临床试验匹配。虽然OCR可以数字化这些报告，但可靠提取仍然具有挑战性，因为临床文档是异构的，OCR文本有噪声，许多医疗设置需要低成本本地部署。我们将这个问题形式化为在OCR派生的临床报告上的规范key条件提取问答。因为key字段既不固定也无法预知，key空间是开放的。我们通过迭代key挖掘、规范化、聚类和轻量级人工验证来维护规范key清单，并引入key覆盖率作为量化清单完整性的指标。使用0.2B基于BERT的模型，对来自20多家医院的真实世界报告的实验表明，性能随着key覆盖率单调提高。一旦覆盖了Top-90规范key，模型在精确匹配和边界容忍匹配下分别达到0.839和0.893的F1分数。这些结果表明key覆盖率是端到端性能的主导因素。在Top-90覆盖率下，我们的模型在精确匹配下优于微调的Qwen3-0.6B基线。虽然我们的标注语料库是中文的，但该方法依赖于半结构化临床报告的语言无关key-value组织给定适当的规范key清单和别名映射，可以适应其他设置。

---

## 104. PumpSense: Real-Time Detection and Target Extraction of Crypto Pump-and-Dumps on Telegram

**arXiv ID**: [2605.09431](https://arxiv.org/abs/2605.09431)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09431)

**作者**: Ahmed Mahrous, Roberto Di Pietro

**分类**: Computation and Language

**发布时间**: 2026-05-10 09:10:13 UTC

**摘要 (英文)**: Cryptocurrency pump-and-dump schemes coordinated via Telegram threaten market integrity. However, existing research addressing this specific threat has not yet produced solutions that combine reliable results with fast response. This is in part due to the absence of publicly available, message-level labeled data, as well as design choices. In this paper, we address both issues. In particular, we introduce a corpus of over 280,000 Telegram posts from 39 pump-organizing groups, all manually reviewed to identify 2,246 pump announcements and their targeted cryptocurrency and exchange. Leveraging this dataset, we define two tasks: real-time pump-announcement detection and target cryptocurrency/exchange extraction. For detection, we compare two machine-learning models: a lightweight tree-based LightGBM classifier (F1=0.79, latency=9.4 s/sample) and a transformer-based BGE-M3 (F1=0.83, latency=50 ms/sample). With our proposed approach, we show that message analysis can achieve near-instant pump detection at the level of individual Telegram message windows. Unlike prior work that relies purely on market data and typically detects pumps tens of seconds after abnormal trading activity is observed, our method operates directly on the coordination messages themselves and can be evaluated in microseconds per window on commodity hardware. To our knowledge, we also establish the first benchmark for manipulated coin and exchange extraction. We demonstrate that traditional rule-based extraction methods, widely relied upon in prior literature, are ineffective due to ticker ambiguity. In contrast, LLMs achieve the highest accuracy with a score of 0.91.

**摘要 (中文)**: 通过Telegram协调的加密货币Pump-and-Dump方案威胁市场完整性。然而，解决这一特定威胁的现有研究尚未产生结合可靠结果和快速响应的解决方案。这部分是由于缺乏公开可用的消息级标签数据，以及设计选择。在本文中，我们解决了这两个问题。特别是，我们引入了一个包含来自39个Pump组织群的超过280,000条Telegram帖子的语料库，全部经过手动审查以识别2,246个Pump公告及其目标加密货币和交易所。利用这个数据集，我们定义了两个任务：实时Pump公告检测和目标加密货币/交易所提取。对于检测，我们比较了两种机器学习模型：轻量级基于树的LightGBM分类器（F1=0.79，延迟=9.4秒/样本）和基于transformer的BGE-M3（F1=0.83，延迟=50毫秒/样本）。通过我们提出的方法，我们表明消息分析可以在单个Telegram消息窗口级别实现近乎即时的Pump检测。与之前仅依赖市场数据且通常在观察到异常交易活动后数十秒检测到Pump的工作不同，我们的方法直接对协调消息进行操作，可以在普通硬件上以每窗口微秒级评估。据我们所知，我们还建立了操纵币和交易所提取的第一个基准。我们证明，由于ticker模糊性，传统的基于规则的提取方法在先前文献中广泛依赖是无效的。相比之下，LLM达到最高精度，得分为0.91。

---

## 105. Perception Without Engagement: Dissecting the Causal Discovery Deficit in LMMs

**arXiv ID**: [2605.09422](https://arxiv.org/abs/2605.09422)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09422)

**作者**: Jiafeng Liang, Zhihao Zhu, Zihan Zhang, Baoqi Ren, Shixin Jiang 等 (共10人)

**分类**: Computation and Language, Computer Vision and Pattern Recognition

**发布时间**: 2026-05-10 08:48:58 UTC

**摘要 (英文)**: Although Large Multimodal Models (LMMs) have achieved strong performance on general video understanding, their susceptibility to textual prior shortcuts during causal discovery has been recognized as a critical deficit. The underlying mechanisms of this phenomenon remain incompletely understood, as existing benchmarks only measure response accuracy without revealing the sources and extent of the deficit. We introduce ProCauEval, a perturbation-based evaluation protocol that shifts from outcome assessment to mechanism diagnosis, probing causal discovery through five controlled configurations that systematically manipulate visual and textual modalities to decompose their respective contributions to model behavior and dissect the failure modes. Evaluating 17 mainstream LMMs, we find that models faithfully perceive video content yet systematically underexploit it during causal reasoning. We further observe that stronger post-training amplifies rather than mitigates textual prior reliance, and that higher baseline performance correlates with greater fragility under perturbation. To address these, we propose Anti-Distillation Policy Optimization (ADPO), a reinforcement learning framework built on negative teacher alignment, which augments GRPO by explicitly pushing the policy away from a prior-only counterfactual teacher induced by visual corruption. Specifically, ADPO maximizes the divergence between the policy distributions conditioned on the original and visually corrupted inputs, thereby forcing the model to ground its reasoning in visual evidence rather than textual shortcuts. Extensive experiments show that ADPO improves visual engagement without sacrificing fundamental comprehension, thus offering a preliminary step toward reliable causal discovery.

**摘要 (中文)**: 虽然大型多模态模型（LMM）在通用视频理解方面取得了强劲的性能，但它们在因果发现中易受文本先验捷径影响已被认为是一个关键缺陷。这一现象的底层机制仍未被完全理解，因为现有基准只测量响应准确性，而不揭示缺陷的来源和程度。我们引入了ProCauEval，这是一个基于扰动的评估协议，从结果评估转向机制诊断，通过五种受控配置探测因果发现，系统地操纵视觉和文本模态，以分解它们对模型行为的各自贡献并剖析失败模式。评估17个主流LMM，我们发现模型忠实地感知视频内容，但在因果推理中系统地未充分利用它。我们进一步观察到更强的后训练放大而非缓解文本先验依赖，且更高的基线性能与扰动下更大的脆弱性相关。为了解决这些问题，我们提出了反蒸馏策略优化（ADPO），一个建立在负教师对齐之上的强化学习框架，通过视觉损坏诱导的纯先验反事实教师明确推动策略远离GRPO。具体来说，ADPO最大化基于原始和视觉损坏输入的条件策略分布之间的差异，从而迫使模型将其推理锚定在视觉证据而非文本捷径上。大量实验表明，ADPO在不牺牲基本理解的情况下改善了视觉参与，为可靠的因果发现提供了初步步骤。

---

## 106. Cross-Cultural Transfer of Emoji Semantics and Sentiment in Financial Social Media

**arXiv ID**: [2605.09414](https://arxiv.org/abs/2605.09414)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09414)

**作者**: Ahmed Mahrous, Roberto Di Pietro

**分类**: Computation and Language

**发布时间**: 2026-05-10 08:30:24 UTC

**摘要 (英文)**: Emojis are widely used in online financial communication, but it is unclear whether they provide transferable sentiment signals across languages, platforms, and asset communities. This study examines the extent to which emoji usage, semantics, and sentiment polarity remain stable across financial communities, and how these layers influence zero-shot sentiment transfer. Using large corpora of Twitter and StockTwits posts in four languages, we measure cross-community divergence and evaluate sentiment models trained under emoji-only, text-only, and text+emoji inputs. We find that emoji frequencies differ across communities, especially across languages, but their semantics and sentiment polarity are largely stable. Cross-asset transferability shows minimal degradation, while cross-language transfer remains the most challenging. Including emojis consistently reduces transfer gaps relative to text-only models. These results indicate that financial communication exhibits a partially shared ``emoji code,'' and that emojis provide compact, language-independent sentiment cues that improve model generalization across markets and platforms.

**摘要 (中文)**: 表情符号广泛用于在线金融通信，但目前尚不清楚它们是否提供跨语言、平台和资产社区的可转移情绪信号。本研究考察了表情符号的使用、语义和情绪极性在金融社区之间保持稳定的程度，以及这些层如何影响零样本情绪转移。使用四种语言的Twitter和StockTwits帖子大型语料库，我们测量跨社区分歧并评估在仅表情符号、仅文本和文本+表情符号输入下训练的情绪模型。我们发现表情符号频率在不同社区之间存在差异，特别是跨语言，但它们的语义和情绪极性在很大程度上是稳定的。跨资产转移性显示最小 degradation，而跨语言转移仍然最具挑战性。包括表情符号始终减少相对于仅文本模型的转移差距。这些结果表明金融通信表现出部分共享的"表情符号代码"，且表情符号提供紧凑的、与语言无关的情绪线索，改善模型跨市场和平台的泛化。

---

## 107. HOME-KGQA: A Benchmark Dataset for Multimodal Knowledge Graph Question Answering on Household Daily Activities

**arXiv ID**: [2605.09348](https://arxiv.org/abs/2605.09348)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09348)

**作者**: Shusaku Egami, Aoi Ohta, Tomoki Tsujimura, Masaki Asada, Tatsuya Ishigaki 等 (共8人)

**分类**: Computation and Language, Artificial Intelligence, Databases, Multimedia

**发布时间**: 2026-05-10 06:00:29 UTC

**摘要 (英文)**: Large Language Models (LLMs) provide flexible natural language processing capabilities, while knowledge graphs (KGs) offer explicit and structured knowledge. Integrating these two in a complementary manner enables the development of reliable and verifiable AI systems. In particular, knowledge graph question answering (KGQA) has attracted attention as a means to reduce LLM hallucinations and to leverage knowledge beyond the training data. However, existing KGQA benchmark datasets are biased toward encyclopedic knowledge, limited to a single modality, and lack fine-grained spatiotemporal data, which limits their applicability to real-world scenarios targeted by Embodied AI. We introduce HOME-KGQA, a novel KGQA benchmark dataset built on a multimodal KG of daily household activities. HOME-KGQA consists of complex, multi-hop natural language questions paired with graph database query languages. Compared to existing benchmarks, it includes more challenging questions that involve multi-level spatiotemporal reasoning, multimodal grounding, and aggregate functions. Experimental results show that the LLM-based KGQA methods fail to achieve performance comparable to that on existing datasets when evaluated on HOME-KGQA. This highlights significant challenges that should be addressed for the real-world deployment of KGQA systems. Our dataset is available at https://github.com/aistairc/home-kgqa

**摘要 (中文)**: 大语言模型（LLM）提供灵活的自然语言处理能力，而知识图谱（KG）提供明确和结构化的知识。以互补方式整合两者能够开发可靠且可验证的AI系统。特别是知识图谱问答（KGQA）作为减少LLM幻觉并利用训练数据之外知识的手段受到关注。然而，现有KGQA基准数据集偏向百科知识，限于单一模态，缺乏细粒度时空数据，这限制了它们对具身AI-targeted真实世界场景的适用性。我们引入了HOME-KGQA，这是一个建立在日常家庭活动多模态KG上的新型KGQA基准数据集。HOME-KGQA由复杂的、多跳自然语言问题与图数据库查询语言配对组成。与现有基准相比，它包含更具挑战性的问题，涉及多级时空推理、多模态接地和聚合函数。实验结果表明，基于LLM的KGQA方法在HOME-KGQA上评估时无法达到与现有数据集相当的性能。这凸显了KGQA系统真实世界部署应解决的重大挑战。我们的数据集可访问 https://github.com/aistairc/home-kgqa

---

## 108. RuPLaR : Efficient Latent Compression of LLM Reasoning Chains with Rule-Based Priors From Multi-Step to One-Step

**arXiv ID**: [2605.09346](https://arxiv.org/abs/2605.09346)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09346)

**作者**: Xiaocheng Luo, Kang Wang, Zaifu Zhan, Yuechi Zhou, Xiangyu Duan

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-10 05:55:07 UTC

**摘要 (英文)**: The Chain-of-Thought (CoT) paradigm, while enhancing the interpretability of Large Language Models (LLMs), is constrained by the inefficiencies and expressive limits of natural language. Latent Chain-of-Thought (latent CoT) reasoning, which operates in a continuous latent space, offers a promising alternative but faces challenges from structural complexities in existing multi-step or multi-model paradigms, such as error propagation and coordination overhead. In this paper, we introduce One-Model One-Step, a novel compression framework for Latent Reasoning with Rule-Based Priors(RuPLaR) to address this challenge. Our method trains an LLM to autonomously generate latent reasoning tokens in a single training stage, guided by rule-based prior probability distributions, thereby eliminating cascaded processes and inter-model dependencies. To ensure reasoning quality, we design a joint training objective that enforces answer consistency via cross-entropy, aligns soft tokens with rule-based priors via KL divergence (the Soft Thinking constraint), and adds a problem-thought semantic alignment constraint in the representation space. Extensive experiments show that our compression framework not only improves accuracy by 11.1% over existing latent CoT methods but also achieves this with minimal token usage, underscoring its effectiveness and extensibility. Code: https://github.com/xiaocen-luo/RuPLaR.

**摘要 (中文)**: 提出RuPLaR框架，通过规则先验引导LLM在单阶段训练中自主生成潜在推理token，在保持准确率的同时大幅减少token使用。

**arXiv ID**: [2605.09329](https://arxiv.org/abs/2605.09329)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09329)

**作者**: Avinash Kumar, Sujay Sanghavi, Poulami Das

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-10 05:02:39 UTC

**摘要 (英文)**: Speculative decoding accelerates LLM inference by using a fast draft model to generate tokens and a more accurate target model to verify them. Its performance depends on the $\textit{acceptance length}$, or number of draft tokens accepted by the target. Our studies show that the acceptance length of even state-of-the-art speculators, like DFlash, EAGLE-3 and PARD degrade with generation length, reaching values close to 1 (i.e. no speedup) within just a few thousand output tokens, making speculators ineffective for long-response tasks. Acceptance lengths decline because most speculators are trained offline on short sequences, but are forced to match the target model on much longer outputs at inference, well beyond their training distribution. To address this issue, we propose $\textit{Test-Time Speculation (TTS)}$, an online distillation approach that continuously adapts the speculator at test-time. TTS leverages the key insight that the token verification step already invokes the target model for each draft token, providing the training signal needed to adapt the draft at no additional cost. Treating the draft as the student and the target as a teacher, TTS adjusts the draft over several speculation rounds, with each update improving the draft's accuracy as generation proceeds. Our results across multiple models from the Qwen-3, Qwen-3.5, and Llama3.1 families show that TTS improves acceptance lengths over state-of-the-art speculators by up to $72\%$ and $41\%$ on average, with the benefits scaling with increased generation lengths.

**摘要 (中文)**: 投机解码通过使用快速draft模型生成token和更准确的目标模型验证它们来加速LLM推理。其性能取决于接受长度，即目标模型接受的draft token数量。我们的研究表明，即使是最先进的投机者，如DFlash、EAGLE-3和PARD的接受长度也会随生成长度下降，在仅几千输出token内接近值1（即无加速），使投机者对长响应任务无效。接受长度下降是因为大多数投机者在短序列上离线训练，但在推理时被迫与目标模型匹配更长的输出，远超其训练分布。为解决这一问题，我们提出测试时投机（TTS），一种在线蒸馏方法，在测试时持续适应投机者。TTS利用关键洞察：token验证步骤已经为每个draft token调用目标模型，提供免费训练信号以适应draft。将draft视为学生，目标视为教师，TTS在几个投机轮次中调整draft，每次更新随着生成进行提高draft的准确性。我们跨Qwen-3、Qwen-3.5和Llama3.1家族多个模型的结果表明，TTS将接受长度比最先进投机者提高高达72%，平均提高41%，随着生成长度增加收益增加。

---

## 110. Mem-W: Latent Memory-Native GUI Agents

**arXiv ID**: [2605.09317](https://arxiv.org/abs/2605.09317)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09317)

**作者**: Guibin Zhang, Yaohui Ling, Fanci Meng, Kun Wang, Shuicheng Yan

**分类**: Computation and Language, Computer Vision and Pattern Recognition, Machine Learning

**发布时间**: 2026-05-10 04:31:23 UTC

**摘要 (英文)**: GUI agents are beginning to operate the web, mobile, and desktop as interactive worlds, where successful control depends on carrying forward visual, procedural, and task-level evidence beyond the fleeting present screen. Yet most agents still treat memory as an external, human-readable artifact: histories are summarized, categorized, retrieved, and reinserted as text or structured records before being encoded again by the policy. This creates a mismatch between the representational form in which experience is stored and the latent embedding sequence over which modern GUI policies actually act. We introduce Mem-W, a series of latent-memory-native GUI agents that treat memory as part of the agent's continuous context rather than as an auxiliary symbolic scaffold. Mem-W weaves both historical trajectories (as experiential memory) and in-session segments (as working memory) into compact memory tokens through a shared trajectory-to-latent compressor. These tokens are woven with the current GUI observation and local context into one continuous embedding sequence, allowing the agent to read successes, failures, and unfinished progress through the same machine-native interface. Mem-W is trained with self-distillation and outcome-aware supervision to preserve decision-relevant state while filtering memory toward evidence that truly supports task success. Across four web and mobile navigation benchmarks, Mem-W consistently improves diverse backbones and memory-enhanced baselines, with gains of up to $+30.0$, suggesting that latent-context-native memory can serve as a scalable foundation for long-horizon GUI agency.

**摘要 (中文)**: GUI智能体开始操作网页、移动和桌面作为交互世界，成功控制取决于携带超出短暂当前屏幕的视觉、程序和任务级证据。然而大多数智能体仍将记忆视为外部的、人类可读的人工制品：历史被总结、分类、检索并作为文本或结构化记录重新插入，然后再次由策略编码。这造成了经验存储的表示形式与现代GUI策略实际作用的潜在嵌入序列之间的不匹配。我们引入了Mem-W，一系列潜在内存本机GUI智能体，将记忆视为智能体连续上下文的一部分，而非辅助符号脚手架。Mem-W通过共享轨迹到潜在压缩器将历史轨迹（作为体验记忆）和会话内片段（作为工作记忆）编织成紧凑的记忆token。这些token与当前GUI观察和本地上下文编织成一个连续嵌入序列，允许智能体通过相同的机器本机界面读取成功、失败和未完成的进度。Mem-W使用自蒸馏和结果感知监督训练，以保留决策相关状态，同时将记忆过滤向真正支持任务成功的证据。在四个网页和移动导航基准上，Mem-W持续改善 diverse backbone和记忆增强基线，增益高达+30.0，表明潜在上下文本机记忆可作为长期GUI智能体的可扩展基础。

---

## 111. LEAF-SQL: Level-wise Exploration with Adaptive Fine-graining for Text-to-SQL Skeleton Prediction

**arXiv ID**: [2605.09295](https://arxiv.org/abs/2605.09295)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09295)

**作者**: Zhao Tan, Xiping Liu, Qing Shu, Qizhi Wan, Dexi Liu 等 (共6人)

**分类**: Computation and Language

**发布时间**: 2026-05-10 03:43:29 UTC

**摘要 (英文)**: Text-to-SQL translates natural language questions into executable SQL queries, enabling intuitive database access for non-experts. While large language models achieve strong performance on Text-to-SQL with prompting, they still struggle with complex queries that involve deeply nested logic or multiple clauses. A widely used approach employs SQL skeletons--intermediate representations of query logic--to streamline generation, but existing methods are limited by their reliance on a single structural hypothesis and lack of progressive reasoning. To overcome these limitations, we propose LEAF-SQL, a novel framework that reframes skeleton prediction as a coarse-to-fine tree search process. LEAF-SQL enables systematic exploration of diverse structural hypotheses with adaptive refinement. Several key techniques are employed in LEAF-SQL: (1) a three-level skeleton hierarchy to guide the search, (2) a Skeleton Formulation Agent to generate diverse candidates, and (3) a Skeleton Evaluation Agent to efficiently prune the search space. This integrated design yields skeleton candidates that are both structurally diverse and granularity-adaptive, providing a stronger foundation for the SQL generation. Extensive experiments show that LEAF-SQL consistently improves the performance of various LLM backbones. On the official hidden test set of the challenging BIRD benchmark, our method achieves 71.6 execution accuracy, which outperforms leading search-based and skeleton-based methods, affirming its effectiveness for complex queries.

**摘要 (中文)**: Text-to-SQL将自然语言问题转换为可执行的SQL查询，为非专家提供直观的数据库访问。虽然大语言模型通过提示在Text-to-SQL上取得强劲性能，但它们仍在涉及深度嵌套逻辑或多个子句的复杂查询上挣扎。一种广泛使用的方法采用SQL骨架——查询逻辑的中间表示——来简化生成，但现有方法受到单一结构假设和缺乏渐进推理的限制。为克服这些限制，我们提出了LEAF-SQL，这是一个将骨架预测重新定义为粗到细树搜索过程的新框架。LEAF-SQL通过自适应细化实现多样结构假设的系统探索。LEAF-SQL采用几种关键技术：（1）三级骨架层次指导搜索，（2）骨架制定智能体生成多样化候选，以及（3）骨架评估智能体有效剪枝搜索空间。这种综合设计产生既结构多样化又粒度自适应的骨架候选，为SQL生成提供更强基础。大量实验表明LEAF-SQL持续改善各种LLM主干的性能。在具有挑战性的BIRD基准的官方隐藏测试集上，我们的方法达到71.6的执行准确性，优于领先的基于搜索和基于骨架的方法，确认其对复杂查询的有效性。

---

## 112. BetaEdit: Null-Space Constrained Sequential Model Editing

**arXiv ID**: [2605.09285](https://arxiv.org/abs/2605.09285)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09285)

**作者**: Bingqing Liu, Wei Liu, Yuhua Li

**分类**: Computation and Language

**发布时间**: 2026-05-10 03:17:57 UTC

**摘要 (英文)**: Null-space-based methods have garnered considerable attention in model editing by constraining updates to the null space of the pre-existing knowledge representation, thereby preserving the model's original behavior. However, in practice these methods rely on an approximate null space--leading to knowledge leakage--and further suffer from severe performance degradation during sequential editing. Recent work shows that history-aware editing strategies can empirically mitigate this decline, yet the underlying reason remains unclear. In this paper, we first expose the knowledge leakage inherent in existing null-space approaches and then analyze why history-aware updates effectively preserve both editing performance and general capabilities during long-horizon editing. Building on these insights, we propose BetaEdit, a refined framework that effectively controls the knowledge leakage and integrates history-aware updates into the null-space paradigm. Extensive experiments on three large language models across two standard benchmarks show that BetaEdit consistently outperforms prior methods in the challenging regime of massive-scale sequential editing. Code is available at: https://github.com/lbq8942/BetaEdit.

**摘要 (中文)**: 基于零空间的方法通过将更新约束到预存知识表示的零空间引起了相当多的关注，从而保留模型的原始行为。然而在实践中，这些方法依赖于近似零空间——导致知识泄漏——并在顺序编辑期间遭受严重的性能下降。最近的工作表明历史感知编辑策略可以凭经验缓解这种下降，但根本原因仍不清楚。在本文中，我们首先揭示现有零空间方法固有的知识泄漏，然后分析为什么历史感知更新在长期编辑中有效保留编辑性能和一般能力。基于这些见解，我们提出了BetaEdit，一个改进的框架，有效控制知识泄漏并将历史感知更新集成到零空间范式中。在三个大语言模型上跨两个标准基准的大量实验表明，BetaEdit在大量顺序编辑的挑战性环境中始终优于先前方法。代码可访问：https://github.com/lbq8942/BetaEdit

---

## 113. DeltaRubric: Generative Multimodal Reward Modeling via Joint Planning and Verification

**arXiv ID**: [2605.09269](https://arxiv.org/abs/2605.09269)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09269)

**作者**: Rui Liu, Dian Yu, Zhenwen Liang, Yucheng Shi, Tong Zheng 等 (共9人)

**分类**: Computation and Language, Computer Vision and Pattern Recognition

**发布时间**: 2026-05-10 02:32:19 UTC

**摘要 (英文)**: Aligning Multimodal Large Language Models (MLLMs) requires reliable reward models, yet existing single-step evaluators can suffer from lazy judging, exploiting language priors over fine-grained visual verification. While rubric-based evaluation mitigates these biases in text-only settings, extending it to multimodal tasks is bottlenecked by the complexity of visual reasoning. The critical differences between responses often depend on instance-specific visual details. Robust evaluation requires dynamically synthesizing rubrics that isolate spatial and factual discrepancies. To address this, we introduce $\textbf{DeltaRubric}$, an approach that reformulates multimodal preference evaluation as a plan-and-execute process within a single MLLM. DeltaRubric operates in two steps: acting first as a $\textit{Disagreement Planner}$, the model generates a neutral, instance-specific verification checklist. Transitioning into a $\textit{Checklist Verifier}$, it executes these self-generated checks against the image and question to produce the final grounded judgment. We formulate DeltaRubric as a multi-role reinforcement learning problem, jointly optimizing planning and verification capabilities. Validated on Qwen3-VL 4B and 8B Instruct models, DeltaRubric achieves solid empirical gains. For instance, On VL-RewardBench, it improves base model overall accuracy by $\textbf{+22.6}$ (4B) and $\textbf{+18.8}$ (8B) points, largely outperforming standard no-rubric baselines. The results demonstrate that decomposing evaluation into structured, verifiable steps leads to more reliable and generalizable multimodal reward modeling.

**摘要 (中文)**: 对齐多模态大语言模型（MLLM）需要可靠的奖励模型，但现有单步评估器可能遭受懒惰评判，利用语言先验而非细粒度视觉验证。虽然基于评分标准的评估在纯文本设置中缓解了这些偏差，但将其扩展到多模态任务受限于视觉推理的复杂性。响应之间的关键差异通常取决于实例特定的视觉细节。稳健评估需要动态合成隔离空间和事实差异的评分标准。为解决这一问题，我们引入了DeltaRubric，一种在单个MLLM内将多模态偏好评估重新表述为计划-执行过程的方法。DeltaRubric分两步操作：首先作为分歧计划者，模型生成中立的、实例特定的验证检查清单。然后转变为检查清单验证者，它针对图像和问题执行这些自生成的检查，以产生最终接地判断。我们将DeltaRubric形式化为多角色强化学习问题，联合优化计划和验证能力。在Qwen3-VL 4B和8B Instruct模型上验证，DeltaRubric获得扎实的实证收益。例如，在VL-RewardBench上，它将基础模型整体准确性提高+22.6（4B）和+18.8（8B）点，大大优于标准无评分标准基线。结果表明，将评估分解为结构化、可验证的步骤带来更可靠和可泛化的多模态奖励建模。

---

## 114. Beyond Continuity: Challenges of Context Switching in Multi-Turn Dialogue with LLMs

**arXiv ID**: [2605.09268](https://arxiv.org/abs/2605.09268)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09268)

**作者**: Aditya Sinha, Harald Steck, Vito Ostuni, Matteo Rinaldi

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-10 02:28:23 UTC

**摘要 (英文)**: Users interacting with Large Language Models (LLMs) in a multi-turn conversation routinely refine their requests or pivot to new topics. LLMs, however, often miss these topic shifts and carry over irrelevant context from previous turns, leading to inaccurate responses. In this paper, we stress-test the multi-turn understanding of LLMs and study the following two sub-tasks: (1) detecting whether the user pivots or refines in the current turn, and (2) shortlisting relevant context from previous turns. To this end, we construct synthetic benchmarks based on real-world datasets from varied domains, as to simulate context shifts of different levels of difficulty. We then evaluate the zero-shot performance of ten LLMs (open-weight, closed-source and reasoning), and demonstrate that only some reasoning and strongly instructed LLMs are accurate in detecting pivots; open-weight LLMs struggle with the task and frequently carry stale context even with explicit cues; and all models suffer from a position bias. Based on the results, we discuss key takeaways for improving long-term robustness in multi-turn capabilities for LLMs.

**摘要 (中文)**: 研究发现LLM多轮对话中用户话题转换检测困难，开源模型常携带过时上下文，所有模型存在位置偏差问题。

**arXiv ID**: [2605.09253](https://arxiv.org/abs/2605.09253)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09253)

**作者**: Yuxuan Jiang, Runchao Li, Shubhashis Roy Dipta, Dawei Li, Zhao Yang

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-10 01:41:43 UTC

**摘要 (英文)**: While recent work in Reinforcement Learning with Verifiable Rewards (RLVR) has shown that a small subset of critical tokens disproportionately drives reasoning gains, an analogous token-level understanding of On-Policy Distillation (OPD) remains largely unexplored. In this work, we investigate high-loss tokens, a token type that--as the most direct signal of student-teacher mismatch under OPD's per-token KL objective--should progressively diminish as training converges according to existing studies; however, our empirical analysis shows otherwise. Even after OPD training reaches apparent saturation, a substantial subset of tokens continues to exhibit persistently high loss; these tokens, which we term Rock Tokens, can account for up to 18\% of the tokens in generated outputs. Our investigation reveals two startling paradoxes. First, despite their high occurrence frequency providing a disproportionately large share of total gradient norms, Rock Tokens themselves remain stagnant throughout training, resisting teacher-driven corrections. Second, through causal intervention, we find that these tokens provide negligible functional contribution to the model's actual reasoning performance. These findings suggest that a vast amount of optimization bandwidth is spent on structural and discourse residuals that the student model cannot or need not internalize. By deconstructing these dynamics, we demonstrate that strategically bypassing these ``stumbling blocks'' can significantly streamline the alignment process, challenging the necessity of uniform token weighting and offering a more efficient paradigm for large-scale model distillation.

**摘要 (中文)**: 虽然最近在带可验证奖励的强化学习（RLVR）中的工作表明，一小部分关键token不成比例地驱动推理增益，但策略上蒸馏（OPD）中类似的token级理解在很大程度上仍未被探索。在这项工作中，我们研究高损失token，这是一种token类型——作为OPD每token KL目标下师生不匹配的最直接信号——根据现有研究应该随着训练收敛而逐渐减少；然而我们的实证分析显示并非如此。即使OPD训练达到明显饱和，大量token子集继续表现出持续高损失；这些我们称之为岩石Token的token可以占生成输出中多达18%的token。我们的调查揭示了两个惊人的悖论。首先，尽管它们的高出现频率提供了不成比例的大份额总梯度范数，但岩石Token本身在训练过程中保持停滞，抵抗教师驱动的修正。其次，通过因果干预，我们发现这些token对模型实际推理性能的贡献可以忽略不计。这些发现表明，大量优化带宽花费在学生模型无法或不需要内化的结构和话语残差上。通过解构这些动态，我们证明战略性绕过这些"绊脚石"可以显著简化对齐过程，挑战均匀token加权的必要性，并为大规模模型蒸馏提供更有效的范式。

---

## 116. LLM Agents Already Know When to Call Tools -- Even Without Reasoning

**arXiv ID**: [2605.09252](https://arxiv.org/abs/2605.09252)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09252)

**作者**: Chung-En Sun, Linbo Liu, Ge Yan, Zimo Wang, Tsui-Wei Weng

**分类**: Computation and Language

**发布时间**: 2026-05-10 01:37:40 UTC

**摘要 (英文)**: Tool-augmented LLM agents tend to call tools indiscriminately, even when the model can answer directly. Each unnecessary call wastes API fees and latency, yet no existing benchmark systematically studies when a tool call is actually needed. We propose When2Tool, a benchmark of 18 environments (15 single-hop, 3 multi-hop) spanning three categories of tool necessity -- computational scale, knowledge boundaries, and execution reliability -- each with controlled difficulty levels that create a clear decision boundary between tool-necessary and tool-unnecessary tasks. We evaluate two families of training-free baselines: Prompt-only (varying the prompt to discourage unnecessary calls) and Reason-then-Act (requiring the model to reason about tool necessity before acting). Both provide limited control: Prompt-only suppresses necessary calls alongside unnecessary ones, and Reason-then-Act still incurs a disproportionate accuracy cost on hard tasks. To understand why these baselines fail, we probe the models' hidden states and find that tool necessity is linearly decodable from the pre-generation representation with AUROC 0.89--0.96 across six models, substantially exceeding the model's own verbalized reasoning. This reveals that models already know when tools are needed, but fail to act on this knowledge during generation. Building on this finding, we propose Probe&Prefill, which uses a lightweight linear probe to read the hidden-state signal and prefills the model's response with a steering sentence. Across all models tested, Probe&Prefill reduces tool calls by 48% with only 1.7% accuracy loss, while the best baseline at comparable accuracy only reduces 6% of tool calls, or achieves a similar tool call reduction but incurs a 5$\times$ higher accuracy loss. Our code is available at https://github.com/Trustworthy-ML-Lab/when2tool

**摘要 (中文)**: 工具增强的LLM智能体倾向于不分青红皂白地调用工具，即使模型可以直接回答。每次不必要的调用都会浪费API费用和延迟，但现有基准没有系统研究何时真正需要工具调用。我们提出了When2Tool，这是一个包含18个环境（15个单跳，3个多跳）的基准，跨越三个工具必要性类别——计算规模、知识边界和执行可靠性——每个都有受控难度级别，在工具必要和工具不必要的任务之间创建清晰决策边界。我们评估了两类无训练基线：纯提示（改变提示以阻止不必要的调用）和先推理后行动（要求模型在行动前推理工具必要性）。两者都提供有限控制：纯提示同时抑制必要和不必要的调用，而先推理后行动在困难任务上仍会产生不成比例的准确性成本。为了理解这些基线失败的原因，我们探测模型隐藏状态，发现工具必要性可以从前生成表示中线性解码，AUROC在六个模型上达到0.89-0.96，大大超过模型自身的口头推理。这揭示模型已经知道何时需要工具，但在生成过程中未能根据这一知识采取行动。基于这一发现，我们提出了Probe&Prefill，它使用轻量级线性探测读取隐藏状态信号，并在响应中预填充引导句子。在所有测试模型上，Probe&Prefill减少48%的工具调用，仅损失1.7%准确性，而同等准确性下最佳基线仅减少6%的工具调用，或达到类似的工具调用减少但准确性损失高5倍。我们的代码可访问 https://github.com/Trustworthy-ML-Lab/when2tool

---

## 117. Repeated-Token Counting Reveals a Dissociation Between Representations and Outputs

**arXiv ID**: [2605.09239](https://arxiv.org/abs/2605.09239)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09239)

**作者**: Sohan Venkatesh

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-10 00:45:19 UTC

**摘要 (英文)**: Large language models fail at counting repeated tokens despite strong performance on broader reasoning benchmarks. These failures are commonly attributed to limitations in internal count tracking. We show this attribution is wrong. Linear probes on the residual stream decode the correct count with near-perfect accuracy at every post-embedding layer, across all model depths. This holds even at the exact layers where the wrong answer crystallizes while the model simultaneously outputs an incorrect count. Attention patterns show no evidence of collapse over repeated tokens and tokenization artifacts account for none of the failure. Instead, a format-triggered multi-layer perceptron (MLP) block overwrites the correctly-encoded count with a fixed wrong answer at roughly 88--93,% network depth. This prior fires for repeated word-tokens in space-separated list format and is absent for repeated digit-tokens. It is suppressed by comma-separated delimiters in larger models but persists in smaller ones. The finding holds across Llama-3.2 (1B and 3B) and Qwen2.5 (1.5B, 3B and 7B) at consistent relative depth. Counting failure is a failure of routing not of representation and the two require different interventions.

**摘要 (中文)**: 大语言模型在重复token计数上失败，尽管它们在更广泛的推理基准上表现强劲。这些失败通常归因于内部计数跟踪的限制。我们表明这种归因是错误的。残差流上的线性探测可以在每个后嵌入层以接近完美的准确性解码正确计数，跨所有模型深度。这甚至在错误答案固化的确切层也成立，同时模型同时输出错误计数。注意力模式显示重复token没有崩溃的证据，token化 artifacts也不能解释失败。相反，一个格式触发的多层感知器（MLP）块在约88-93%网络深度用固定错误答案覆盖正确编码的计数。这个先验对空格分隔列表格式中的重复单词token触发，对重复数字token不存在。在较大模型中被逗号分隔符抑制，但在较小模型中持续存在。这一发现在Llama-3.2（1B和3B）和Qwen2.5（1.5B、3B和7B）的相对深度一致。计数失败是路由而非表示的失败，两者需要不同的干预。

---

## 118. Matching Meaning at Scale: Evaluating Semantic Search for 18th-Century Intellectual History through the Case of Locke

**arXiv ID**: [2605.09236](https://arxiv.org/abs/2605.09236)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09236)

**作者**: Yu Wu, Ananth Mahadevan, Filip Ginter, Michael Mathioudakis, Mikko Tolonen

**分类**: Computation and Language, Artificial Intelligence, Computers and Society, Digital Libraries, Information Retrieval

**发布时间**: 2026-05-10 00:34:46 UTC

**摘要 (英文)**: While digitized corpora have transformed the study of intellectual transmission, current methods rely heavily on lexical text reuse detection, capturing verbatim quotations but fundamentally missing paraphrases and complex implicit engagement. This paper evaluates semantic search in 18th-century intellectual history through the reception of John Locke's foundational work. Using expert annotation grounded in a semantic taxonomy, we examine whether an off-the-shelf semantic search pipeline can surface meaning-level correspondences overlooked by lexical methods. Our results demonstrate that semantic search retrieves substantially more implicit receptions than lexical baselines. However, linguistic diagnostics also reveal a "lexical gatekeeping" effect, where retrieval remains partially constrained by surface vocabulary overlap. These findings highlight both the potential and the limitations of semantic retrieval for analyzing the circulation of ideas in large historical corpora. The data is available at https://github.com/COMHIS/locke-sim-data.

**摘要 (中文)**: 虽然数字化语料库改变了知识传承的研究，但当前方法严重依赖词汇文本重用检测，捕获逐字引用但从根本上错过改写和复杂的隐性参与。本文通过约翰·洛克基础作品的接受情况评估18世纪思想史中的语义搜索。使用基于语义分类法的专家注释，我们检验现成的语义搜索管道是否可以发现词汇方法遗漏的意义层面对应。我们的结果表明，语义搜索检索到的隐含接受明显多于词汇基线。然而，语言诊断也揭示了"词汇守门"效应，检索仍部分受表面词汇重叠约束。这些发现突出了语义检索在分析大型历史语料库中思想循环的潜力和局限性。数据可访问 https://github.com/COMHIS/locke-sim-data

---

## 119. Two Ways to De-Bias an LLM-as-a-Judge: A Continuous-Score Comparison of Hierarchical Bayesian Calibration and Neural-ODE Score Transport

**arXiv ID**: [2605.09227](https://arxiv.org/abs/2605.09227)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09227)

**作者**: Andrea Morandi

**分类**: Computation and Language

**发布时间**: 2026-05-09 23:55:02 UTC

**摘要 (英文)**: [Abridged] Using a Large Language Model (LLM) as an automatic rater (LLM-as-a-judge) is cheap but potentially biased: some judges run lenient, others strict, the middle of the scale gets compressed, and verbose answers may be over-rewarded. A common remedy is post-hoc calibration: leave the cheap judge in place and, on a modest set of paired anchors, fit a transformation from raw judge scores to an estimate of the human rating. We compare two correctors that take opposing views on how this mapping should be modeled: a parametric, small-anchor hierarchical Bayesian linear correction with per-score uncertainty, and a non-parametric Neural-ODE (FFJORD) score-transport flow. Both are run head-to-head on UltraFeedback fine-grained_score (1700 paired examples, 200 held out), with calibration split into three operational sub-questions: population-mean recovery, per-item accuracy, and distributional-shape match. The headline result is that the choice between methods is primarily a data-budget question. Both correctors close the raw $+0.71$-point mean offset to within $\pm 0.08$ of the GPT-4 reference, at 100 and at 1500 anchors. Past that, the methods swap roles. With 100 anchors, the linear corrector reconstructs the human-score distribution roughly twice as well by KL divergence (0.031 vs. 0.058) and ties the flow on MAE. With 1500 anchors the flow wins on every metric (MAE 0.320 vs. 0.359, Pearson 0.922 vs. 0.896, KL 0.026 vs. 0.037). The Bayesian linear corrector saturates well below 1500 anchors: residual $\tanh$-shaped non-linearity is, by construction, structure a linear correction cannot fit. The flow keeps improving as labels grow. We translate these findings into an explicit decision rule for production deployments.

**摘要 (中文)**: 提出LLM-as-a-judge的校准方法对比，发现数据量少时线性校正更好，数据量多时神经流更优。

**arXiv ID**: [2605.09167](https://arxiv.org/abs/2605.09167)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09167)

**作者**: Antonis Asonitis, Luca A. Lanzendörfer, Frédéric Berdoz, Roger Wattenhofer

**分类**: Computation and Language, Artificial Intelligence, Machine Learning

**发布时间**: 2026-05-09 21:00:01 UTC

**摘要 (英文)**: Automatic speech recognition (ASR) performs well for high-resource languages with abundant paired audio-transcript data, but its accuracy degrades sharply for most languages due to limited publicly available aligned data. To this end, we introduce WorldSpeech, a 24 kHz multilingual speech corpus comprising 65k hours of aligned audio-transcript data across 76 languages, collected from diverse public sources including parliamentary proceedings, international broadcasts, and public-domain audiobooks. For 37 languages, WorldSpeech provides more than 200 hours of aligned speech, with 28 exceeding 500 hours and 24 surpassing 1k hours. Fine-tuning existing ASR models on WorldSpeech results in an average relative Word-Error-Rate reduction of 63.5% across 11 typologically diverse languages.

**摘要 (中文)**: 使用大语言模型（LLM）作为自动评分员（LLM-as-a-judge）便宜但可能有偏见：一些评分员宽松，另一些严格，量表中间被压缩，冗长答案可能被过度奖励。常见的补救措施是后校准：保留廉价评分员，在适度的成对锚点上，拟合从原始评分员分数到人类评分估计的转换。我们比较了对这个映射应该如何建模持相反观点的两个校正器：参数化的、小锚点的分层贝叶斯线性校正（每个分数有不确定性），和非参数化的神经ODE（FFJORD）分数传输流。两者在UltraFeedback细粒度分数（1700个配对示例，200个保留）上进行正面比较，校准分为三个操作子问题：总体均值恢复、单项准确性和分布形状匹配。标题结果是方法之间的选择主要是数据预算问题。两个校正器都将原始+0.71点均值偏移闭合到GPT-4参考的±0.08以内，在100和1500个锚点处。之后，方法交换角色。使用100个锚点，线性校正器按KL散度（约两倍）更好地重建人类分数分布（0.031 vs 0.058），并在MAE上与流持平。使用1500个锚点，流在每个指标上获胜（MAE 0.320 vs 0.359，Pearson 0.922 vs 0.896，KL 0.026 vs 0.037）。贝叶斯线性校正器在远低于1500个锚点处饱和：残留的tanh形非线性（按结构）是线性校正无法拟合的。流随着标签增长持续改进。我们将这些发现转化为生产部署的明确决策规则。

---

## 121. Lost in Translation? Exploring the Shift in Grammatical Gender from Latin to Occitan

**arXiv ID**: [2605.09156](https://arxiv.org/abs/2605.09156)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09156)

**作者**: Ahan Chatterjee, Matthias Schöffel, Matthias Aßenmacher, Esteban Garces Arias

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-09 20:36:49 UTC

**摘要 (英文)**: The diachronic evolution from Latin to the Romance languages involved a restructuring of the grammatical gender system from a tripartite configuration (masculine, feminine, neuter) to a bipartite one (masculine, feminine). In this work, we introduce an interpretable deep learning framework to investigate this phenomenon at both lexical and contextual levels. First, we show that conventional tokenization strategies are insufficiently robust for this low-resource historical setting, and that our proposed tokenizer improves performance over these baselines. At the lexical level, we evaluate the contribution of morphological features to gender prediction. At the contextual level, we quantify the contributions of different part-of-speech categories to grammatical gender prediction. Together, these analyses characterize the distribution of gender information between the lemma and its sentential context. We make our codebase, datasets, and results publicly available.

**摘要 (中文)**: 自动语音识别（ASR）在具有丰富配对音频转录数据的高资源语言上表现良好，但由于有限的公开可用对齐数据，其准确性在大多数语言中急剧下降。为此，我们引入了WorldSpeech，这是一个24kHz多语言语音语料库，包含76种语言65,000小时的对齐音频转录数据，从 diverse 公共来源收集，包括议会程序、国际广播和公共领域有声读物。对于37种语言，WorldSpeech提供超过200小时的对齐语音，其中28种超过500小时，24种超过1,000小时。在WorldSpeech上微调现有ASR模型在11种类型多样语言上平均相对词错误率降低63.5%。

---

## 122. Meow-Omni 1: A Multimodal Large Language Model for Feline Ethology

**arXiv ID**: [2605.09152](https://arxiv.org/abs/2605.09152)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09152)

**作者**: Jucheng Hu, Zhangquan Chen, Yulin Chen, Chengjie Hong, Liang Zhou 等 (共12人)

**分类**: Computation and Language, Neurons and Cognition

**发布时间**: 2026-05-09 20:30:15 UTC

**摘要 (英文)**: Deciphering animal intent is a fundamental challenge in computational ethology, largely because of semantic aliasing, the phenomenon where identical external signals (e.g., a cat's purr) correspond to radically different internal states depending on physiological context. Existing Multimodal Large Language Models (MLLMs) are blind to high-frequency biological time-series data, restricting them to superficial behavioural pattern matching rather than genuine latent-state reasoning. To bridge this gap, we introduce Meow-Omni 1, the first open-source, quad-modal MLLM purpose-built for computational ethology. It natively fuses video, audio, and physiological time-series streams with textual reasoning. Through targeted architectural adaptation, we integrate specialized scientific encoders into a unified backbone and formalize intent inference via physiologically grounded cross-modal alignment. Evaluated on MeowBench, a novel, expert-verified quad-modal benchmark, Meow-Omni 1 achieves state-of-the-art intent-recognition accuracy (71.16%), substantially outperforming leading vision-language and omni-modal baselines. We release the complete open-source pipeline including model weights, training framework, and the Meow-10K dataset, to establish a scalable paradigm for inter-species intent understanding and to advance foundation models toward real-world veterinary diagnostics and wildlife conservation.

**摘要 (中文)**: 从拉丁语到罗曼语的历史演变涉及语法性别系统从三分结构（阳性、阴性、中性）重构成二分结构（阳性、阴性）。在这项工作中，我们引入了一个可解释的深度学习框架，在词汇和上下文两个层面研究这一现象。首先，我们表明传统token化策略对这种低资源历史设置不够稳健，我们提出的tokenizer在这些基线上提高了性能。在词汇层面，我们评估形态特征对性别预测的贡献。在上下文层面，我们量化不同词性类别对语法性别预测的贡献。这些分析共同表征了词元与其句子上下文之间的性别信息分布。我们将代码库、数据集和结果公开可用。

---

## 123. From Traditional Taggers to LLMs: A Comparative Study of POS Tagging for Medieval Romance Languages

**arXiv ID**: [2605.09147](https://arxiv.org/abs/2605.09147)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09147)

**作者**: Matthias Schöffel, Esteban Garces Arias

**分类**: Computation and Language, Artificial Intelligence, Applications

**发布时间**: 2026-05-09 20:15:18 UTC

**摘要 (英文)**: Part-of-speech (POS) tagging for Medieval Romance languages remains challenging due to orthographic variation, morphological complexity, and limited annotated resources. This paper presents a systematic empirical evaluation of large language models (LLMs) for POS tagging across three medieval varieties: Medieval Occitan, Medieval Catalan, and Medieval French. We compare traditional rule-based and statistical taggers with modern open-source LLMs under zero-shot prompting, few-shot prompting, monolingual fine-tuning, and cross-lingual transfer learning settings. Experiments on historically grounded datasets show that LLM-based approaches consistently outperform traditional taggers, with fine-tuning and multilingual training yielding the largest improvements. In particular, cross-lingual transfer learning substantially benefits under-resourced varieties, while targeted bilingual training can outperform broader multilingual configurations for specific target languages. The results highlight the importance of linguistic proximity and dataset characteristics when designing transfer strategies for historical NLP. These findings provide empirical insights into the applicability of modern neural methods to medieval text processing and provide practical guidance for deploying LLM-based POS tagging pipelines in digital humanities research. All code, models, and processed datasets are released for reproducibility.

**摘要 (中文)**: 解码动物意图是计算民族学的 fundamental 挑战，主要由于语义混叠，即相同的外部信号（例如猫的呼噜）根据生理上下文可能对应完全不同的内部状态。现有多模态大语言模型（MLLM）对高频生物时间序列数据视而不见，限制它们进行浅层行为模式匹配而非真正的潜在状态推理。为弥补这一差距，我们引入了Meow-Omni 1，这是第一个用于计算民族学的开源四模态MLLM。它原生融合视频、音频和生理时间序列流与文本推理。通过针对性架构适应，我们将专门的科学编码器集成到统一主干中，并通过基于生理的跨模态对齐形式化意图推理。在Meow-OMNI上评估——这是一个新颖的、专家验证的四模态基准——Meow-OMNI 1达到最先进的意图识别准确性（71.16%），大大优于领先的视觉语言和全模态基线。我们发布完整的开源管道，包括模型权重、训练框架和Meow-10K数据集，以建立可扩展的跨物种意图理解范式，并推进基础模型用于真实世界兽医诊断和野生动物保护。

---

## 124. Fin-Bias: Comprehensive Evaluation for LLM Decision-Making under human bias in Finance Domain

**arXiv ID**: [2605.09106](https://arxiv.org/abs/2605.09106)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09106)

**作者**: Xiaoyu Hu, Jinman Zhao

**分类**: Computation and Language

**发布时间**: 2026-05-09 18:28:40 UTC

**摘要 (英文)**: Large language models (LLMs) are increasingly deployed in financial contexts, raising critical concerns about reliability, alignment, and susceptibility to adversarial manipulation. While prior finance-related benchmarks assess LLMs' capabilities in stock trading, they are often restricted to small sample and fail to demonstrate LLM susceptibility to context with potential human bias. We introduce Fin-Bias (financial herding under long and uncertain financial context), a benchmark for evaluating LLM investment decision-making when faced with uncertainty and possible human-biased opinions. Fin-Bias includes 8868 long firm-specific analyst reports, including firm aspects summarized and analyzed by sophisticated analysts with investment ratings (Bullish/Neutral/Bearish) spanning from various industries. We present large language models with firm analyst reports with/without analyst investment ratings and even with 'fake' rating, to get investment ratings generated by LLMs. Our results reveal that LLMs tend to herd the explicit bias in context. We also develop a method to detect potential human opinions, which can encourage LLMs to think independently, some models even exceed human performance in predicting future stock return.

**摘要 (中文)**: 大语言模型（LLM）越来越多地部署在金融环境中，引发了对可靠性、对齐和对抗性操纵易感性的关键关切。虽然之前的金融相关基准评估LLM在股票交易方面的能力，但它们通常限于小样本，无法展示LLM对具有潜在人类偏见上下文的敏感性。我们引入了Fin-Bias（长期和不确定金融背景下的人类金融从众），这是一个评估LLM在面对不确定性和可能的人类偏见观点时投资决策的基准。Fin-Bias包含8,868份长期特定公司分析师报告，包括由复杂分析师总结和分析的公司方面，这些分析师具有投资评级（看涨/中性/看跌），涵盖各种行业。我们向大语言模型展示有或无分析师投资评级的公司分析师报告，甚至带有"虚假"评级，以获得LLM生成的投资评级。我们的结果表明，LLM倾向于从众上下文中的明确偏见。我们还开发了一种检测潜在人类观点的方法，可以鼓励LLM独立思考，某些模型甚至在预测未来股票回报方面超过人类表现。

---

## 125. GRC: Unifying Reasoning-Driven Generation, Retrieval and Compression

**arXiv ID**: [2605.09100](https://arxiv.org/abs/2605.09100)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09100)

**作者**: Zhongtao Miao, Qiyu Wu, Yoshimasa Tsuruoka

**分类**: Computation and Language

**发布时间**: 2026-05-09 18:15:02 UTC

**摘要 (英文)**: Text embedding and generative tasks are usually trained separately based on large language models (LLMs) nowadays. This causes a large amount of training cost and deployment effort. Context compression is also a challenging and pressing task, which is vital to reasoning-driven generation, and agentic tasks requiring long context and continual learning. In this paper, we explore how to unify reasoning-driven generation, reasoning-enhanced text representation and context compression tasks in one forward pass for LLMs. Through meta latent tokens and a unified generative, representative and compressive tuning approach, we propose a training framework named GRC that bridges the three tasks. The trained models can accomplish three objectives in a single forward pass while maintaining modular, LEGO-style flexibility during inference. This design greatly reduces the deployment effort for retrieval-augmented generation (RAG) and achieves efficient inference and three times data utilization during training. Furthermore, this framework design enables a new paradigm for text embedding: self-reason-latent embeds, and a new generation paradigm, latent memory-augmented generation, where compressed and internalized KV cache with O(1) length is used as the updatable memory. We also propose hybrid paged attention to speed up the inference of our models. Extensive experiments on reasoning-intensive retrieval benchmarks, generative tasks, document compression, latency evaluation, and RAG settings demonstrate the effectiveness of our method and may shed light on the truly unified model that can handle reasoning-driven generation, embedding and compression tasks seamlessly.

**摘要 (中文)**: 文本嵌入和生成任务目前通常基于大语言模型（LLM）分别训练。这导致大量训练成本和部署工作。上下文压缩也是一个具有挑战性和紧迫性的任务，对推理驱动的生成和需要长上下文和持续学习的智能体任务至关重要。在本文中，我们探索如何在一次前向传递中统一LLM的推理驱动生成、推理增强文本表示和上下文压缩任务。通过元潜在token和统一的生成性、代表性 compressive 调优方法，我们提出了一个名为GRC的训练框架，它桥接这三个任务。训练后的模型可以在一次前向传递中完成三个目标，同时在推理期间保持模块化、LEGO式灵活性。这种设计大大减少了检索增强生成（RAG）的部署工作，实现了高效推理和训练中三倍的数据利用。此外，这种框架设计为文本嵌入带来了新范式：自推理潜在嵌入，以及一种新的生成范式，潜在记忆增强生成，其中压缩和内化的KV cache（O(1)长度）用作可更新记忆。我们还提出了混合分页注意力来加速模型推理。在推理密集型检索基准、生成任务、文档压缩、延迟评估和RAG设置上的大量实验证明了我们方法的有效性，并为真正可以无缝处理推理驱动生成、嵌入和压缩任务的统一模型提供了启示。

---

## 126. Dynamic Meta-Metrics: Source-Sentence Conditioned Weighting for MT Evaluation

**arXiv ID**: [2605.09098](https://arxiv.org/abs/2605.09098)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09098)

**作者**: Luke Zhang, Justin Vasselli, Aditya Khan, York Hay Ng, En-Shiun Annie Lee

**分类**: Computation and Language

**发布时间**: 2026-05-09 18:12:10 UTC

**摘要 (英文)**: We propose Dynamic Meta-Metrics (DMM), a framework for machine translation evaluation that learns source-sentence conditioned combinations of existing metrics. Rather than relying on a single static ensemble or language-specific weighting, DMM adapts the metric combination based on properties of the source segment. We study hard conditioning, which fits an interpretable combiner per cluster, and an exploratory soft-conditioned extension whose weights vary continuously with source-cluster responsibilities. We evaluate DMM on the WMT Metrics Shared Task data across multiple language pairs using pairwise agreement measures at the system and segment levels. Across settings, MLP-based combinations outperform linear and Gaussian process-based ensembles, and introducing soft conditioning yields gains over linear models.

**摘要 (中文)**: 我们提出动态元指标（DMM），一个学习基于源句子属性的现有指标组合的机器翻译评估框架。DMM不是依赖单一静态集成或语言特定加权，而是根据源片段的属性调整指标组合。我们研究硬条件，它为每个聚类拟合可解释的组合器，以及探索性软条件扩展，其权重随源聚类责任连续变化。我们在WMT指标共享任务数据上跨多个语言对评估DMM，使用系统和片段级别的成对协议测量。在各种设置中，基于MLP的组合优于线性和高斯过程集成的组合，引入软条件比线性模型产生增益。

---

## 127. Character-Level Transformer for Tajik-Persian Transliteration with a Parallel Lexical Corpus

**arXiv ID**: [2605.09092](https://arxiv.org/abs/2605.09092)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09092)

**作者**: Mullosharaf K. Arabov

**分类**: Computation and Language

**发布时间**: 2026-05-09 17:57:29 UTC

**摘要 (英文)**: This study addresses automatic transliteration from Tajik (Cyrillic script) to Persian (Perso-Arabic script). We present a curated, lexicographically verified parallel corpus of 52,152 Tajik--Persian words and short phrases, compiled from printed dictionaries, encyclopedic sources, and manually verified online resources. To the best of our knowledge, this is one of the largest publicly available word-level corpora for Tajik--Persian transliteration. Using this corpus, we train a character-level sequence-to-sequence Transformer model and evaluate it using Character Error Rate (CER) and exact-match accuracy. The Transformer achieves a CER of 0.3216 and an exact-match accuracy of 0.3133, outperforming both dictionary-based rule-based and recurrent neural baselines. With beam search (k=3), performance further improves to CER 0.3182 and accuracy 0.3215. We describe the data collection and preprocessing pipeline, model architecture, and experimental protocol, and report a part-of-speech analysis showing performance differences across lexical categories. All preprocessing scripts, deterministic splits into training, validation, and test sets, and training configurations are released to support reproducibility and further research on Tajik and related Persian dialects. The corpus supports research in character-level transliteration, cross-script NLP, and lexicographic applications.

**摘要 (中文)**: 本研究解决了从塔吉克语（西里尔字母）到波斯语（波斯-阿拉伯字母）的自动音译问题。我们提供了一个经过整理的、词典学验证的52,152个塔吉克-波斯单词和短语的平行语料库，从印刷词典、百科资源和人verify的在线资源编制。据我们所知，这是塔吉克-波斯音译最大的公开可用词级语料库之一。使用这个语料库，我们训练了一个字符级序列到序列Transformer模型，并使用字符错误率（CER）和精确匹配准确性进行评估。Transformer实现了0.3216的CER和0.3133的精确匹配准确性，优于基于词典的规则和循环神经基线。使用beam search（k=3），性能进一步提升至CER 0.3182和准确性0.3215。我们描述了数据收集和预处理管道、模型架构和实验协议，并报告了词性分析，显示不同词汇类别的性能差异。所有预处理脚本、确定性训练、验证和测试集划分以及训练配置都已发布，以支持可重现性和对塔吉克语及相关波斯语方言的进一步研究。该语料库支持字符级音译、跨脚本NLP和词典应用的研究。

---

## 128. Soohak: A Mathematician-Curated Benchmark for Evaluating Research-level Math Capabilities of LLMs

**arXiv ID**: [2605.09063](https://arxiv.org/abs/2605.09063)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09063)

**作者**: Guijin Son, Seungone Kim, Catherine Arnett, Hyunwoo Ko, Hyein Lee 等 (共68人)

**分类**: Computation and Language

**发布时间**: 2026-05-09 17:14:22 UTC

**摘要 (英文)**: Following the recent achievement of gold-medal performance on the IMO by frontier LLMs, the community is searching for the next meaningful and challenging target for measuring LLM reasoning. Whereas olympiad-style problems measure step-by-step reasoning alone, research-level problems use such reasoning to advance the frontier of mathematical knowledge itself, emerging as a compelling alternative. Yet research-level math benchmarks remain scarce because such problems are difficult to source (e.g., Riemann Bench and FrontierMath-Tier 4 contain 25 and 50 problems, respectively). To support reliable evaluation of next-generation frontier models, we introduce Soohak, a 439-problem benchmark newly authored from scratch by 64 mathematicians. Soohak comprises two subsets. On the Challenge subset, frontier models including Gemini-3-Pro, GPT-5, and Claude-Opus-4.5 reach 30.4%, 26.4%, and 10.4% respectively, leaving substantial headroom, while leading open-weight models such as Qwen3-235B, GPT-OSS-120B, and Kimi-2.5 remain below 15%. Notably, beyond standard problem solving, Soohak introduces a refusal subset that probes a capability intrinsic to research mathematics: recognizing ill-posed problems and pausing rather than producing confident but unjustified answers. On this subset, no model exceeds 50%, identifying refusal as a new optimization target that current models do not directly address. To prevent contamination, the dataset will be publicly released in late 2026, with model evaluations available upon request in the interim.

**摘要 (中文)**: 继前沿LLM在IMO上取得金牌表现后，社区正在寻找下一个有意义的挑战性目标来衡量LLM推理。奥数风格问题仅测量逐步推理，而研究级问题使用这种推理来推进数学知识本身的前沿，成为一个引人注目的替代方案。然而研究级数学基准仍然稀缺，因为这类问题难以获取（例如Riemann Bench和FrontierMath-Tier 4分别包含25和50个问题）。为支持对下一代前沿模型的可靠评估，我们引入了Soohak，这是一个由64位数学家全新编写的439个问题的基准。Soohak包含两个子集。在Challenge子集上，包括Gemini-3-Pro、GPT-5和Claude-Opus-4.5的前沿模型分别达到30.4%、26.4%和10.4%，留有 substantial headroom，而领先的开源权重模型如Qwen3-235B、GPT-OSS-120B和Kimi-2.5保持在15%以下。值得注意的是，除标准问题解决外，Soohak引入了一个拒绝子集，探测研究数学的固有能力：识别不适定问题并暂停而非产生自信但不合理的答案。在该子集上，没有模型超过50%，将拒绝确定为当前模型未直接解决的新优化目标。为防止污染，数据集将于2026年末公开发布，期间可应要求进行模型评估。

---

## 129. Language-Conditioned Visual Grounding with CLIP Multilingual

**arXiv ID**: [2605.09060](https://arxiv.org/abs/2605.09060)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09060)

**作者**: J. de Curtò, Mauro Liz, I. de Zarzà

**分类**: Computation and Language

**发布时间**: 2026-05-09 17:06:16 UTC

**摘要 (英文)**: Multilingual vision-language models exhibit systematic performance gaps across languages, but the mechanism remains ambiguous: cross-language divergence could arise from the visual encoder, the text branch, or their interaction. We resolve this ambiguity through a dense multilingual CLIP probe in which the visual encoder is held identical across thirteen typologically diverse languages and only the XLM-RoBERTa text branch varies. We evaluate two CLIP architectures spanning a 7x visual-encoder scale gap (XLM-R base + ViT-B/32, ~87M visual parameters; XLM-R large + ViT-H/14, ~632M) on 11 concepts and 210 images, and quantify cross-language agreement via cluster-mask IoU, top-percentile IoU, and Spearman rank correlation against an English reference (n=2,310 paired observations per language). Three findings emerge. First, low-resource languages (Arabic, Basque, Luxembourgish) incur a structural penalty at both backbone scales (Wilcoxon HR>LR p<10^-300; cluster-mask IoU gap +0.114 at base, +0.143 at large), isolating the deficit to the text branch. Second, scaling the encoder 7x widens the gap for structural failure cases (Basque Δ=-0.056, Luxembourgish Δ=-0.076) while improving Arabic (Δ=+0.033), separating corpus-coverage from tokeniser-fertility failures. Third, peak similarity is preserved across languages (mean ratio 0.94 at large scale) while cluster-mask IoU drops sharply, identifying spatial misalignment, not signal collapse, as the dominant failure mode. At 3.4-3.9 Wh per 1,000 queries, dense-CLIP grounding is competitive with high-throughput inference budgets, positioning it as a practical substrate for energy-aware multilingual deployment.

**摘要 (中文)**: 多语言视觉语言模型在不同语言间表现出系统性性能差距，但机制仍然不明确：跨语言分歧可能来自视觉编码器、文本分支或它们的交互。我们通过密集多语言CLIP探测解决这一模糊性，其中视觉编码器在13种类型多样的语言中保持相同，只有XLM-RoBERTa文本分支变化。我们评估了跨越7倍视觉编码器规模差距的两种CLIP架构（XLM-R base + ViT-B/32，约87M视觉参数；XLM-R large + ViT-H/14，约632M）在11个概念和210张图像上，并通过cluster-mask IoU、top-percentile IoU和相对于英语参考的Spearman等级相关（每语言n=2,310配对观察）量化跨语言一致性。出现三个发现。首先，低资源语言（阿拉伯语巴斯克语卢森堡语）在两个主干规模上都招致结构惩罚（Wilcoxon HR>LR p<10^-300；cluster-mask IoU差距基线+0.143大型+0.114），将缺陷隔离到文本分支。其次，将编码器扩展7倍扩大了结构失败案例的差距（巴斯克Δ=-0.056，卢森堡语Δ=-0.076），同时改善了阿拉伯语（Δ=+0.033），分离了语料库覆盖与tokenizer-fertility失败。第三，峰值相似性在语言间保留（大型规模平均比率0.94），而cluster-mask IoU急剧下降，将空间对齐识别为主要失败模式，而非信号崩溃。每1000次查询3.4-3.9 Wh，密集CLIP接地与高吞吐推理预算竞争，使其成为能源感知多语言部署的实用基础。

---

## 130. Phase Transitions in Affective Meaning Divergence: The Hidden Drift Before the Break

**arXiv ID**: [2605.09043](https://arxiv.org/abs/2605.09043)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09043)

**作者**: Napassorn Litchiowong

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-09 16:30:47 UTC

**摘要 (英文)**: One partner says "Fine" meaning <i>resolution</i>; the other hears <i>surrender</i>. The word is shared; the affective uptake is not. We formalize this as <b>affective meaning divergence (AMD)</b>, the total-variation distance between interlocutors' anchor-conditioned affect distributions. Building on speech-act theory, common-ground accumulation, and entropy-regularized game theory, we derive a logit best-response map whose dynamics undergo a saddle-node bifurcation: when $βα> 4$, a monotone increase in AMD-driven load produces an abrupt, hysteretic collapse of repair coordination. On Conversations Gone Awry (CGA-Wiki; $N=652$), derailing conversations exhibit critical-slowing-down (CSD) signatures across multiple levels: lexical divergence variance ($p<0.001$, $d=0.36$), AMD variance ($p=0.001$, $d=0.26$), and dialog-act repair variance ($p=0.016$, $d=0.20$), all significant after correction and stronger than toxicity and sentiment baselines. AMD provides a distinct temporal signature, with retrospectively measured variance peaking at the bifurcation point while toxicity variance peaks earlier, and is the only indicator grounded in the theoretical framework. Boundary-condition analysis on CGA-CMV ($N=1{,}169$) yields mixed but directionally consistent evidence.

**摘要 (中文)**: 一方说"Fine"意思是<i>解决</i>；另一方听到<i>投降</i>。词汇共享；情感理解不同。我们将其形式化为情感意义分歧（AMD），即对话者锚定条件情感分布之间的总变差距离。基于言语行为理论、共同基础积累和熵正则化博弈论，我们推导出一个logit最佳响应映射，其动力学经历鞍节点分叉：当βα>4时，AMD驱动负载的单调增加产生协调修复的突然滞后崩溃。在Conversations Gone Awry（CGA-Wiki；N=652）上，偏离对话在多个层面表现出临界减速（CSD）签名：词汇分歧方差（p<0.001，d=0.36）、AMD方差（p=0.001，d=0.26）和对话行为修复方差（p=0.016，d=0.20），校正后均显著，且强于毒性和情感基线。AMD提供独特的时间签名，回顾性测量的方差在分叉点达到峰值，而毒性方差更早达到峰值，且是唯一基于理论框架的指标。在CGA-CMV（N=1,169）上的边界条件分析产生混合但方向一致的证据。

---

## 131. Evaluating Pragmatic Reasoning in Large Language Models: Evidence from Scalar Diversity

**arXiv ID**: [2605.09042](https://arxiv.org/abs/2605.09042)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09042)

**作者**: Ye-eun Cho

**分类**: Computation and Language

**发布时间**: 2026-05-09 16:28:50 UTC

**摘要 (英文)**: Evaluating pragmatic reasoning in large language models (LLMs) remains challenging because model behavior can vary depending on evaluation methods. Previous studies suggest that prompt-based judgments may diverge from models' internal probability distributions, raising questions about whether observed performance reflects underlying competence or task-induced behavior. This study examines this issue using scalar diversity as a graded diagnostic for pragmatic inference. Following Hu & Levy (2023), this study compares direct probability measurement and metalinguistic prompting across multiple models and experimental settings. The results show that neither evaluation method consistently outperforms the other and that pragmatic behavior varies substantially across model families, prompting strategies, and task structures. Moreover, scalar diversity gradients emerge only in specific model-condition combinations, suggesting that pragmatic reasoning in LLMs reflects an interaction between internal probabilistic representations and task-induced prompting behavior rather than a stable competence captured by a single evaluation paradigm. These findings highlight the central role of evaluation design in interpreting pragmatic abilities in LLMs.

**摘要 (中文)**: 评估大语言模型（LLM）的语用推理仍然具有挑战性，因为模型行为可能因评估方法而异。之前的研究表明，基于提示的判断可能与模型内部概率分布分离，引发关于观察到的表现是反映底层能力还是任务诱导行为的问题。本研究使用标量多样性作为语用推理的分级诊断来检验这一问题。按照Hu & Levy（2023），本研究跨多个模型和实验设置比较直接概率测量和元语言提示。结果表明，没有一种评估方法始终优于另一种，且语用行为在模型家族、提示策略和任务结构之间存在显著差异。此外，标量多样性梯度仅在特定的模型-条件组合中出现，表明LLM中的语用推理反映了内部概率表示与任务诱导提示行为之间的交互，而非单一评估范式捕获的稳定能力。这些发现强调了评估设计在解释LLM语用能力中的核心作用。

---

## 132. BiAxisAudit: A Novel Framework to Evaluate LLM Bias Across Prompt Sensitivity and Response-Layer Divergence

**arXiv ID**: [2605.09041](https://arxiv.org/abs/2605.09041)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09041)

**作者**: Jialing Gan, Junhao Dong, Songze Li

**分类**: Computation and Language, Cryptography and Security

**发布时间**: 2026-05-09 16:26:49 UTC

**摘要 (英文)**: Bias audits of large language models now operate within governance frameworks such as the EU AI Act, making benchmark reliability a security concern in its own right. Many current benchmarks, however, collapse bias into a single scalar from one prompt format and one surface label. This design misses two failure modes that can be exploited without changing model weights. Across prompts, meaning-preserving format changes shift bias endorsement by more than $0.7$ on a fixed statement pool. Within a response, the discrete Selection and free-text Elaboration can take opposing stances, so an apparently clean aggregate may hide substantial internal inconsistency (a ``cancellation trap''). Selection-only and elaboration-only rankings are therefore nearly uncorrelated across eight LLMs (Spearman $ρ= 0.238$, $p = 0.570$): LLaMA3-70B ranks in the middle under selection-only scoring but highest under elaboration-only scoring on the same responses. We introduce \textsc{BiAxisAudit}, a protocol that reports each bias score together with a reliability estimate on two orthogonal axes. The across-prompt axis evaluates each statement under a factorial grid of task format, perspective, role, and sentiment, treating bias as a distribution rather than a point estimate. The within-response axis uses Split Coding to recover Selection and Elaboration as separate signals, measured by the Inconsistency Rate and Divergence Net Imbalance. Across eight LLMs with $80{,}200$ coded responses each, task format alone explains as much variance as model choice; $63.6\%$ of pooled bias signals (up to $85.2\%$ per model) appear in only one coding layer, and prompt-dimension interactions exceed main effects. The instrument also separates real bias reductions from apparent reductions caused by cross-layer redistribution: some prompt configurations reduce both BER and IR, whereas others suppress only selection-layer bias.

**摘要 (中文)**: 大语言模型的偏见审计目前在欧洲AI法案等治理框架内运行，使基准可靠性成为其本身的安全关切。然而，许多当前基准将偏见简化为来自单一提示格式和单一表面标签的单一标量。这种设计遗漏了两种可以在不更改模型权重的情况下被利用的失败模式。跨提示，保留意义的格式变化在固定陈述池上将偏见支持率改变超过0.7。在响应内，离散选择和自由文本阐述可能采取相反立场，因此表面干净的聚合可能隐藏 substantial 内部不一致（"取消陷阱"）。因此，仅选择和仅阐述排名在八个LLM上几乎不相关（Spearman ρ=0.238，p=0.570）：LLaMA3-70B在仅选择评分下排名中等，但在相同响应的仅阐述评分下排名最高。我们引入BiAxisAudit，这是一种协议，在两个正交轴上报告每个偏见分数以及可靠性估计。跨提示轴在任务格式、视角、角色和情感的析因网格下评估每个陈述，将偏见视为分布而非点估计。响应内轴使用 Split Coding 将选择和阐述恢复为单独信号，通过不一致率和分歧净不平衡测量。跨八个LLM每个有80,200个编码响应，任务格式 alone 解释与模型选择一样多的方差；63.6%的汇总偏见信号（每个模型高达85.2%）仅出现在一个编码层中，且提示维度交互超过主效应。该仪器还可分离真正的偏见减少与跨层重分布引起的明显减少：一些提示配置同时减少BER和IR，而其他仅抑制选择层偏见。

---

## 133. A Quantum Inspired Variational Kernel and Explainable AI Framework for Cross Region Solar and Wind Energy Forecasting

**arXiv ID**: [2605.09032](https://arxiv.org/abs/2605.09032)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09032)

**作者**: Pavan Manjunath, Thomas Prufer

**分类**: Computation and Language, Artificial Intelligence, Machine Learning

**发布时间**: 2026-05-09 16:16:14 UTC

**摘要 (英文)**: Reliable short horizon forecasting of solar and wind generation is a structural prerequisite of any modern power system yet most published forecasters are tuned and evaluated on a single climatic regime and most algorithmic novelty has been concentrated either on classical recurrent networks or on monolithic foundation models that combine forecasting and explanation We develop a four stage hybrid framework that separates these concerns The first stage acquires hourly generation irradiance and surface weather records through public application programming interfaces The second stage trains three classical baselines autoregressive integrated moving average gradient boosted regression trees and a two layer long short term memory network and produces a strong point forecast together with a residual error series The third stage corrects the residual through a quantum inspired variational kernel built on a six qubit hardware efficient ansatz with three repeated entangling layers The fourth stage uses generative artificial intelligence strictly as an explainability layer that reads the measured benchmark numbers and produces a structured natural language interpretation Across three regions drawn from open public archives Iberian solar North Sea wind and a mixed Texas trace the proposed configuration stays within one percentage point of the strongest classical baseline on the in domain forecasting task and the quantum inspired kernel separates calm and stormy weather regimes with a Fisher discriminant ratio approximately fifteen fold higher than a tuned radial basis kernel

**摘要 (中文)**: 可靠的天阳能和风能短期预测是任何现代电力系统的结构性先决条件，但大多数已发布的预测器在单一气候 regime 上进行调优和评估，且大多数算法 novelty 集中在经典循环网络或结合预测和解释的整体基础模型上。我们开发了一个四阶段混合框架来分离这些关注点。第一阶段通过公共API获取每小时发电辐照度和地面天气记录。第二阶段训练三个经典基线：自回归积分移动平均、梯度提升回归树和双层长短期记忆网络，并产生强有力的点预测以及残差误差系列。第三阶段通过建立在六量子位硬件高效ansatz上的量子启发变分 kernel（带有三个重复纠缠层）校正残差。第四阶段严格将生成式AI用作可解释性层，读取测量的基准数字并产生结构化自然语言解释。跨从开放公共档案中提取的三个区域——伊比利亚太阳能北海风力和混合德克萨斯痕迹——所提出的配置在领域内预测任务上保持在最强经典基线的一个百分点内，且量子启发kernel以比调优径向基kernel高约15倍的Fisher判别率分离平静和暴风雨天气 regime。

---

## 134. GAMBIT: A Three-Mode Benchmark for Adversarial Robustness in Multi-Agent LLM Collectives

**arXiv ID**: [2605.09027](https://arxiv.org/abs/2605.09027)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09027)

**作者**: Alexandre Le Mercier, Chris Develder, Thomas Demeester

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-09 16:07:23 UTC

**摘要 (英文)**: In multi-agent systems (MAS), a single deceptive agent can nullify all gains of an agentic AI collective and evade deployed defenses. However, existing adversarial studies on MAS target only shallow tasks and do not consider adaptive adversaries, which evolve their strategies to evade the very detectors trained to catch them. To address that gap, we introduce GAMBIT, a benchmark with three evaluation modes and two independent scores for evaluating imposter detectors: the first two modes measure zero-shot detection under increasing distribution shift, and a third recalibration mode measures how quickly a detector adapts to novel attacks from just 20 labeled examples. The benchmark comes with a dataset of 27,804 labeled instances spanning 240 co-evolved imposter strategies. Our contributions are threefold: (1) Using chess as a substrate deep reasoning problem and Gemini 3.1 Pro for agents, we release GAMBIT and its dataset to evaluate imposter detectors under realistic constraints against a stealthy adaptive imposter; (2) We introduce an adaptive imposter agent based on an efficient evolutionary framework, generalizable beyond chess, that collapses collective task performance while remaining essentially undetectable (50.5% F1-score with a Gemini-based detector); (3) We show that zero-shot evaluation can be highly misleading for adaptive adversaries: two detectors with near-identical zero-shot scores differ by 8x on few-shot adaptation, while the meta-learned variant converges 20x faster, a gap only visible in the recalibration mode. Altogether, GAMBIT provides the first multi-agent benchmark where adversarial attacks and defenses co-evolve, with an imposter framework generalizable beyond our use case, and promising techniques for fast recalibration in a rapidly evolving adversarial system. Code and data: https://anonymous.4open.science/r/gambit.

**摘要 (中文)**: 在多智能体系统（MAS）中，单个欺骗性智能体可以使智能体AI集体的所有收益无效并逃避已部署的防御。然而，现有的MAS对抗研究仅针对浅层任务，不考虑适应性对手，后者会进化其策略以逃避训练来捕获它们的检测器。为解决这一差距，我们引入了GAMBIT，这是一个具有三种评估模式和两个独立分数的基准，用于评估伪装者检测器：前两种模式在增加分布偏移下测量零样本检测，第三种重新校准模式测量检测器从仅20个标记示例适应新攻击的速度。该基准包含跨越240个共进化伪装者策略的27,804个标记实例的数据集。我们的贡献有三方面：（1）使用国际象棋作为深层推理问题的基础以及Gemini 3.1 Pro作为智能体，我们发布GAMBIT及其数据集，以在针对隐蔽适应性伪装者的现实约束下评估伪装者检测器；（2）我们引入基于高效进化框架的适应性伪装者智能体，可推广到国际象棋之外，它在保持基本不可检测的同时瓦解集体任务表现（基于Gemini的检测器达到50.5%F1分数）；（3）我们表明零样本评估对于适应性对手可能高度误导：两个具有几乎相同零样本分数的检测器在少样本适应上相差8倍，而元学习变体收敛快20倍，这一差距仅在重新校准模式下可见。综上所述，GAMBIT提供了第一个对抗攻击和防御共进化的多智能体基准，其中伪装者框架可推广到我们的用例之外，并为快速重新校准提供有前景的技术。代码和数据：https://anonymous.4open.science/r/gambit

---

## 135. LLiMba: Sardinian on a Single GPU -- Adapting a 3B Language Model to a Vanishing Romance Language

**arXiv ID**: [2605.09015](https://arxiv.org/abs/2605.09015)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09015)

**作者**: Luca Ballore

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-09 15:54:11 UTC

**摘要 (英文)**: Sardinian, a Romance language with roughly one million speakers, has minimal presence in modern NLP. Commercial services do not support it, and current language models do not produce it reliably. We present LLiMba, a 3B parameter Sardinian-ready model adapted from Qwen2.5-3B-Instruct through continued pretraining (CPT) and supervised fine-tuning (SFT) on a single 24 GB consumer GPU. The corpus contains 11.5 million tokens of Sardinian spanning LSC, Logudorese, and Campidanese, augmented with 2.4 million tokens of related Romance text as replay against register blurring. After CPT the model reaches a perplexity of 6.76 on held out Sardinian and outperforms the base across all six FLORES-200 directions. We compare five SFT configurations under matched conditions: full fine-tuning, LoRA r64, rsLoRA r128, rsLoRA r256, and DoRA r256. rsLoRA r256 wins on every direction into Sardinian, reaching 28.5 BLEU from English against 17.3 after CPT and 21.0 with full fine-tuning. The rank ablation places r128 between LoRA r64 and rsLoRA r256 on BLEU but reveals failure modes invisible to the metric, including leakage across scripts no other variant produces. LoRA r64 retains less factual content from SFT than configurations at higher rank and produces more confident fabrications, though all methods fabricate on content absent from training. DoRA r256 yields the smallest gap between training and evaluation but the worst factual accuracy. The findings indicate that adapter capacity matters more than the choice among LoRA variants for adapting a Romance pretrained base to a low resource Romance target, that stronger regularization is not uniformly beneficial, and that translation metrics smoothly order configurations whose qualitative behavior differs categorically. Perplexity comparisons across scripts must account for byte fallback tokenization, which deflates the metric for scripts other than Latin.

**摘要 (中文)**: 我们呈现LLiMba，一个3B参数的撒丁语就绪模型，通过在单个24GB消费GPU上从Qwen2.5-3B-Instruct进行继续预训练（CPT）和监督微调（SFT）进行适配。语料库包含1150万撒丁语token，涵盖LSC、Logudorese和Campidanese，并增加240万相关罗曼文本作为 replay 以防止 register 模糊。CPT后，模型在保留的撒丁语上达到6.76的困惑度，并在所有六个FLORES-200方向上优于基线。我们在匹配条件下比较五种SFT配置：全参数微调、LoRA r64、rsLoRA r128、rsLoRA r256和DoRA r256。rsLoRA r256在每个进入撒丁语的方向上获胜，从英语达到28.5 BLEU，而CPT后为17.3，全参数微调为21.0。排名消融将r128放在LoRA r64和rsLoRA r256之间的BLEU上，但揭示了指标看不到的失败模式，包括跨脚本泄漏（其他变体都没有产生）。LoRA r64从SFT保留较少的事实内容并产生更自信的捏造，尽管所有方法都对训练中不存在的内容进行捏造。DoRA r256产生训练和评估之间最小的差距，但事实准确性最差。这些发现表明，对于将罗曼语预训练基础适应低资源罗曼语目标，adapter容量比LoRA变体之间的选择更重要，更强的正则化并非普遍有益，翻译指标有序排列其定性行为 categorical 地不同的配置。跨脚本的困惑度比较必须考虑字节回退token化，这会使非拉丁脚本的指标降低。

---

## 136. Dolphin-CN-Dialect: Where Chinese Dialects Matter

**arXiv ID**: [2605.08961](https://arxiv.org/abs/2605.08961)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08961)

**作者**: Yangyang Meng, Huihang Zhong, Guodong Lin, Guanbo Wang, Hu Du 等 (共9人)

**分类**: Computation and Language, Audio and Speech Processing

**发布时间**: 2026-05-09 13:56:54 UTC

**摘要 (英文)**: We present Dolphin-CN-Dialect, a streaming-capable ASR model with a focus on Chinese and dialect-rich scenarios. Compared to the previous version, Dolphin-CN-Dialect introduces substantial improvements in data processing, tokenization, training stability, and data sampling strategies. To address the challenges of highly imbalanced dialect data, we propose a temperature-based sampling strategy that effectively balances standard Mandarin and low-resource dialects, leading to significant gains in dialect recognition performance. In addition, we redesign the tokenizer to better align with linguistic characteristics, adopting character-level modeling for Chinese and subword modeling for English, while introducing extensible dialect tokens. Experimental results show that Dolphin-CN-Dialect achieves improvement in dialect recognition accuracy and CER reduction compared to Dolphin. Furthermore, Dolphin-CN-Dialect reaches competitive performance with recent SOTA open-source ASR models, while maintaining a significantly smaller model size. Dolphin-CN-Dialect supports both streaming and non-streaming inference, enabling a practical balance between latency and accuracy. It also provides flexible customization through hotword support and efficient deployment optimized for specialized hardware. These improvements make Dolphin-CN-Dialect a strong and practical solution for real-world multi-dialect ASR applications.

**摘要 (中文)**: 我们呈现Dolphin-CN-Dialect，一个专注于中文和方言丰富场景的流式ASR模型。与前一版本相比，Dolphin-CN-Dialect在数据处理、token化、训练稳定性和数据采样策略方面引入了实质性改进。为了解决高度不平衡方言数据的挑战，我们提出了一种基于温度的采样策略，有效平衡标准普通话和低资源方言，带来方言识别性能的显著提升。此外，我们重新设计了tokenizer以更好地与语言特征对齐，对中文采用字符级建模，对英语采用子词建模，同时引入可扩展方言token。实验结果表明，Dolphin-CN-Dialect在方言识别准确性和CER减少方面相比Dolphin取得提升。此外，Dolphin-CN-Dialect与最近的SOTA开源ASR模型达到竞争力的性能，同时保持明显更小的模型规模。Dolphin-CN-Dialect支持流式和非流式推理，在延迟和准确性之间实现实用的平衡。它还通过热词支持提供灵活定制，并为专业硬件优化高效部署。这些改进使Dolphin-CN-Dialect成为现实世界多方言ASR应用的强大实用解决方案。

---

## 137. Improving Lexical Difficulty Prediction with Context-Aligned Contrastive Learning and Ridge Ensembling

**arXiv ID**: [2605.08950](https://arxiv.org/abs/2605.08950)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08950)

**作者**: Wicaksono Leksono Muhamad, Joanito Agili Lopo, Tsamarah Rana Nugraha, Ahmad Cahyono Adi, Muhammad Oriza Nurfajri

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-09 13:43:54 UTC

**摘要 (英文)**: Lexical difficulty prediction is a fundamental problem in language learning and readability assessment, requiring models to estimate word difficulty across different first-language (L1) backgrounds. However, existing approaches rely on regression-only training with scalar supervision, which does not explicitly structure the representation space, limiting their ability to capture cross-lingual alignment and ordinal difficulty. To mitigate these issues, we propose Context-Aligned Contrastive Regression, which integrates Ridge regression ensemble with two complementary objectives, i.e., Cross-View Context and Ordinal Soft Contrastive Learning. Experiments on three L1 datasets show that (i) contrastive objectives improve cross-lingual representation alignment while preserving language-specific nuances, (ii) the learned representations capture the ordinal structure of lexical difficulty, and (iii) the ensemble effectively mitigates systematic biases of individual models, leading to more stable performance across difficulty levels.

**摘要 (中文)**: 词汇难度预测是语言学习和可读性评估的基本问题，需要模型跨不同第一语言（L1）背景估计词难度。然而，现有方法依赖仅回归训练与标量监督，这不会明确结构化表示空间，限制了其捕获跨语言对齐和有序难度的能力。为缓解这些问题，我们提出上下文对齐对比回归，它将岭回归集成与两个互补目标相结合，即跨视图上下文和有序软对比学习。在三个L1数据集上的实验表明（i）对比目标改善跨语言表示对齐，同时保留语言特定细微差别，（ii）学习到的表示捕获词汇难度的有序结构，（iii）集成有效减轻个体模型的系统性偏见，带来跨难度级别更稳定的性能。

---

## 138. Decomposing and Steering Functional Metacognition in Large Language Models

**arXiv ID**: [2605.08942](https://arxiv.org/abs/2605.08942)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08942)

**作者**: Yanshi Li, Xueru Bai, Shuman Liu, Haibo Zhang, Anxiang Zeng

**分类**: Computation and Language

**发布时间**: 2026-05-09 13:22:47 UTC

**摘要 (英文)**: Large language models (LLMs) increasingly exhibit behaviors suggesting awareness of their evaluation context, often adapting their reasoning strategies in benchmark settings. Prior work has shown that such evaluation awareness can distort performance measurements; however, it remains unclear whether this phenomenon reflects a single behavioral artifact or a deeper internal structure within the model. We propose that LLMs maintain a decomposable space of functional metacognitive states: internal variables encoding factors such as evaluation awareness, self-assessed capability, perceived risk, computational effort allocation, audience expertise adaptation, and intentionality. Through residual stream analysis across multiple reasoning models, we demonstrate that these states are linearly decodable from internal activations and exhibit distinct layer-wise profiles. Moreover, by steering model activations along probe-derived directions, we show that each functional metacognitive state causally modulates reasoning behavior in dissociable ways, affecting verbosity, accuracy, and safety-related responses across tasks. Our findings suggest that benchmark performance reflects not only task competence but also the activation of specific functional metacognitive states. We argue that understandi ng and controlling these internal states is essential for reliable evaluation and deployment of reasoning models, and we provide a mechanistic framework for studying functional m etacognition in artificial systems. Our code and data are publicly available at https://github.com/xlands/meta-cognition.

**摘要 (中文)**: 大语言模型（LLM）越来越多地表现出表明意识到其评估背景的行为，通常在基准设置中调整其推理策略。之前的工作表明这种评估意识可以扭曲性能测量；然而，这种现象是反映单一行为伪影还是模型内部更深的结构仍然不清楚。我们认为LLM维持功能元认知状态的可分解空间：编码评估意识、自我评估能力、感知风险、计算努力分配、受众专业知识适应和意图性等因素的内部变量。通过跨多个推理模型的残差流分析，我们证明这些状态可以从内部激活中线性解码，并表现出不同的层-wise profile。此外，通过沿探测派生方向引导模型激活，我们表明每个功能元认知状态以可分离的方式因果调节推理行为，影响任务中的冗长性、准确性和安全相关响应。我们的发现表明，基准性能不仅反映任务能力，还反映特定功能元认知状态的激活。我们认为理解和控制这些内部状态对于推理模型的可靠评估和部署至关重要，我们提供了一个研究人工系统中功能元认知的机制框架。我们的代码和数据在 https://github.com/xlands/meta-cognition 公开可用

---

## 139. LLM-Agnostic Semantic Representation Attack

**arXiv ID**: [2605.08898](https://arxiv.org/abs/2605.08898)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08898)

**作者**: Jiawei Lian, Jianhong Pan, Lefan Wang, Yi Wang, Tairan Huang 等 (共7人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-09 11:43:47 UTC

**摘要 (英文)**: Large Language Models (LLMs) increasingly employ alignment techniques to prevent harmful outputs. Despite these safeguards, attackers can circumvent them by crafting adversarial prompts. Predominant token-level optimization methods primarily rely on optimizing for exact affirmative templates (e.g., ``\textit{Sure, here is...}''). However, these paradigms frequently encounter bottlenecks such as suboptimal convergence, compromised prompt naturalness, and poor cross-model generalization. To address these limitations, we propose Semantic Representation Attack (SRA), a novel LLM-agnostic paradigm that fundamentally reconceptualizes adversarial objectives from exact textual targeting to malicious semantic representations. Theoretically, we establish the semantic Coherence-Convergence Relationship and derive a Cross-Model Semantic Generalization bound, proving that maintaining semantic coherence guarantees both white-box semantic convergence and black-box transferability. Technically, we operationalize this framework via the Semantic Representation Heuristic Search (SRHS) algorithm, which preserves interpretability and structural coherence of the adversarial prompts during incremental discrete token chunk expansion. Extensive evaluations demonstrate that our framework achieves a 99.71% average attack success rate across 26 open-source LLMs, with strong transferability and stealth.

**摘要 (中文)**: 大语言模型（LLM）越来越多地采用对齐技术来防止有害输出。尽管有这些保护措施，攻击者可以通过设计对抗性提示来绕过它们。主流的token级优化方法主要依赖于优化确切的肯定模板（例如"Sure, here is..."）。然而，这些范式经常遇到瓶颈，如次优收敛、提示自然性受损和差的跨模型泛化。为了解决这些限制，我们提出了语义表示攻击（SRA），这是一种新型的LLM无关范式，从精确文本目标重新概念化对抗目标为恶意语义表示。从理论上，我们建立了语义一致性-收敛关系并推导了跨模型语义泛化 bound，证明保持语义一致性保证白盒语义收敛和黑盒可迁移性。在技术上，我们通过语义表示启发式搜索（SRHS）算法来操作化这个框架，它在增量离散token块扩展期间保持对抗提示的可解释性和结构一致性。广泛评估表明，我们的框架在26个开源LLM上达到99.71%的平均攻击成功率，具有强大的可迁移性和隐蔽性。

---

## 140. FragileFlow: Spectral Control of Correct-but-Fragile Predictions for Foundation Model Robustness

**arXiv ID**: [2605.08896](https://arxiv.org/abs/2605.08896)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08896)

**作者**: Zhuoyun Li, Boxuan Wang, Jinwei Hu, Xiaowei Huang, Yi Dong

**分类**: Computation and Language, Artificial Intelligence, Machine Learning

**发布时间**: 2026-05-09 11:25:07 UTC

**摘要 (英文)**: Robust adaptation of LLMs and VLMs is often evaluated by average accuracy or average consistency under perturbations. However, these averages can hide a structured failure mode: a prediction may remain correct while probability mass already flows from particular true classes toward systematic wrong competitors near the decision boundary. In this paper, we formalize this phenomenon as margin-aware error flow and introduce FragileFlow, a plug-in regularizer that uses a calibrated margin buffer to identify correct-but-fragile predictions and organize their off-class probability mass into a class-wise vulnerable-risk matrix. Theoretically, we provide the first PAC-Bayes upper bound for this margin-aware error-flow object, showing how empirical spectral control yields a conservative route to deterministic worst-class robustness under a stability condition. Experiments on multiple-choice LLM benchmarks and few-shot CLIP adaptation show that FragileFlow consistently improves the proposed theory-facing risk measures over matched baselines, yields perturbed worst-class accuracy gains in most settings, and preserves clean accuracy across comparisons.

**摘要 (中文)**: LLM和VLM的鲁棒适应通常通过扰动下的平均准确性或平均一致性来评估。然而，这些平均值可以隐藏一种结构化失败模式：预测可能保持正确，而概率质量已经从特定真类流向决策边界附近的系统性错误竞争者。在本文中，我们将这一现象形式化为边界感知误差流，并引入FragileFlow，这是一个使用校准边界缓冲区的插件正则化器，用于识别正确但脆弱的预测并将它们的类外概率质量组织成类-wise脆弱风险矩阵。从理论上，我们为这个边界感知误差流对象提供了第一个PAC-Bayes上界，表明经验谱控制如何在稳定性条件下产生确定性最差类鲁棒性的保守路径。在多项选择LLM基准和少样本CLIP适应上的实验表明，FragileFlow在匹配的基线上持续改善提出的面向理论的风险度量，在大多数设置中产生扰动最差类准确性增益，并在比较中保持清洁准确性。

---

## 141. Fitting Is Not Enough: Smoothness in Extremely Quantized LLMs

**arXiv ID**: [2605.08894](https://arxiv.org/abs/2605.08894)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08894)

**作者**: Yuzhuang Xu, Xu Han, Yuxuan Li, Pengzhan Li, Wanxiang Che

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-09 11:19:51 UTC

**摘要 (英文)**: Large language models (LLMs) achieve strong performance but incur high deployment costs, motivating extremely low-bit but lossy quantization. Existing quantization algorithms mainly focus on improving the numerical accuracy of forward computation to eliminate performance degradation. In this paper, we show that extremely quantized LLMs suffer from systematic smoothness degradation beyond numerical precision loss. Through a smoothness proxy, we observe that such degradation becomes increasingly severe as the quantization bit-width decreases. Furthermore, based on sequence neighborhood modeling, we find that quantized models exhibit a rapid reduction of effective token candidates within the prediction neighborhood, which directly leads to a sparser decoding tree and degraded generation quality. To validate it, we introduce a simple smoothness-preserving principle in both post-training quantization and quantization-aware training, and demonstrate that preserving smoothness brings additional gains beyond numerical accuracy. The core goal of this paper is to highlight smoothness preservation as an important design consideration for future extreme quantization methods. Code is available at https://github.com/xuyuzhuang11/FINE.

**摘要 (中文)**: 大语言模型（LLM）取得强劲性能但产生高部署成本，激励极低比特但有损的量化。现有量化算法主要关注提高前向计算的数值准确性以消除性能退化。在本文中，我们表明极量化LLM遭受超越数值精度损失的系统性平滑退化。通过平滑代理，我们观察到这种退化随着量化比特宽度减小而变得越来越严重。此外，基于序列邻域建模，我们发现量化模型在预测邻域内有效token候选快速减少，这直接导致更稀疏的解码树和退化的生成质量。为验证这一点，我们在训练后量化和量化感知训练中引入了一个简单的平滑保持原则，并证明保持平滑带来超越数值准确性的额外增益。本文的 core 目标是将平滑保持作为未来极端量化方法的重要设计考虑因素。代码可访问 https://github.com/xuyuzhuang11/FINE

---

## 142. DocScope: Benchmarking Verifiable Reasoning for Trustworthy Long-Document Understanding

**arXiv ID**: [2605.08888](https://arxiv.org/abs/2605.08888)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08888)

**作者**: Xiang Feng, Jiawei Zhou, Zhangfeng Huang, Kewei Wang, Shanshan Ye 等 (共9人)

**分类**: Computation and Language, Computer Vision and Pattern Recognition

**发布时间**: 2026-05-09 11:12:59 UTC

**摘要 (英文)**: Evaluating whether Multimodal Large Language Models can produce trustworthy, verifiable reasoning over long, visually rich documents requires evaluation beyond end-to-end answer accuracy. We introduce DocScope, a benchmark that formulates long-document QA as a structured reasoning trajectory prediction problem: given a complete PDF document and a question, the model outputs evidence pages, supporting evidence regions, relevant factual statements, and a final answer. We design a four-stage evaluation protocol -- Page Localization, Region Grounding, Fact Extraction, and Answer Verification -- that audits each level of the trajectory independently through inter-stage decoupling, with all judges selected and calibrated via human alignment studies. DocScope comprises 1,124 questions derived from 273 documents, with all hierarchical evidence annotations completed by human annotators. We benchmark 6 proprietary models, 12 open-weight models, and several domain-specific systems. Our experiments reveal that answer accuracy cannot substitute for trajectory-level evaluation: even among correct answers, the highest observed rate of complete evidence chains is only 29\%. Across all models, region grounding remains the weakest trajectory stage. Furthermore, the primary difficulty stems from aggregating evidence dispersed across long distances and multiple document clusters, while an oracle study identifies faithful perception and fact extraction as the dominant capability bottleneck. Cross-architecture comparisons further suggest that activated parameter count matters more than total scale. The benchmark and code will be publicly released at https://github.com/MiliLab/DocScope.

**摘要 (中文)**: 评估多模态大语言模型是否可以对长而视觉丰富的文档产生可信、可验证的推理需要超越端到端答案准确性的评估。我们引入了DocScope，这是一个将长文档QA制定为结构化推理轨迹预测问题的基准：给定完整PDF文档和问题，模型输出证据页面、支持证据区域、相关事实陈述和最终答案。我们设计了一个四阶段评估协议——页面定位、区域接地、事实提取和答案验证——通过阶段间解耦独立审计轨迹的每个层面，所有法官通过人类对齐研究选择和校准。DocScope包含来自273个文档的1,124个问题，所有分层证据注释由人类注释者完成。我们基准测试了6个专有模型、12个开源权重模型和几个领域特定系统。我们的实验揭示答案准确性不能替代轨迹级评估：即使在正确答案中，观察到的完整证据链最高比率仅为29%。在所有模型中，区域接地仍然是 最弱的轨迹阶段。此外，主要困难源于聚合分散在长距离和多个文档簇中的证据，而预言研究确定忠实感知和事实提取是主要能力瓶颈。跨架构比较进一步表明，激活参数数量比总规模更重要。基准和代码将在 https://github.com/MiliLab/DocScope 公开发布

---

## 143. Max-pooling Network Revisited: Analyzing the Role of Semantic Probability in Multiple Instance Learning for Hallucination Detection

**arXiv ID**: [2605.08863](https://arxiv.org/abs/2605.08863)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08863)

**作者**: Shota Fujikawa, Issei Sato

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-09 10:30:30 UTC

**摘要 (英文)**: Hallucination detection has become increasingly important for improving the reliability of large language models (LLMs). Recently, hybrid approaches such as HaMI, which combine semantic consistency with internal model states via Multiple Instance Learning (MIL), have achieved state-of-the-art performance. However, these methods incur substantial computational overhead due to repeated sampling and costly semantic similarity computations. In this work, we first provide a theoretical analysis of HaMI in terms of decision margins, revealing that scaling internal states with semantic consistency leads to an enlarged decision margin. Motivated by this insight, we revisit classical sentence classification models from a margin enlargement perspective, aggregating token-level features via max pooling and directly estimating sentence scores using a lightweight MLP. Without requiring semantic consistency computations, our approach achieves substantial efficiency improvements while maintaining competitive performance with state-of-the-art baselines through adaptive aggregation of internal feature representations.

**摘要 (中文)**: 幻觉检测对于提高大语言模型（LLM）的可靠性变得越来越重要。最近，HaMI等混合方法通过多实例学习（MIL）将语义一致性 与内部模型状态相结合，取得了最先进的性能。然而，这些方法由于重复采样和昂贵的语义相似性计算而产生大量计算开销。在这项工作中，我们首先从决策边界角度对HaMI进行理论分析，揭示用语义一致性缩放内部导致决策边界扩大。从这一洞察启发，我们从边界扩大角度重新审视经典句子分类模型，通过最大池化聚合token级特征，并使用轻量级MLP直接估计句子分数。我们的方法不需要语义一致性计算，通过内部特征表示的自适应聚合，在保持与最先进基线竞争性能的同时实现了显著的效率提升。

---

## 144. Architecture, Not Scale: Circuit Localization in Large Language Models

**arXiv ID**: [2605.08853](https://arxiv.org/abs/2605.08853)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08853)

**作者**: Sohan Venkatesh

**分类**: Computation and Language

**发布时间**: 2026-05-09 10:05:22 UTC

**摘要 (英文)**: Mechanistic interpretability assumes that circuit analysis becomes harder as models scale. We challenge this assumption by showing that the attention architecture matters more than parameter count. Studying three circuit types across Pythia and Qwen2.5, we find that grouped query attention produces circuits that are far more concentrated and mechanistically stable than standard multi-head attention at comparable scales. The same concentration pattern holds across indirect object identification, induction heads, and factual recall. Within a single architecture family (Qwen2.5), factual recall circuits undergo a discrete phase transition above a critical scale, collapsing to a single bottleneck rather than degrading gradually. These findings suggest that some architectural choices make large models more tractable to study and that interpretability difficulty is not a fixed consequence of model size.

**摘要 (中文)**: 机制可解释性假设电路分析随着模型规模增大变得更难。我们通过显示注意力架构比参数计数更重要来挑战这一假设。研究Pythia和Qwen2.5上的三种电路类型，我们发现分组查询注意力在相同规模下产生的电路比标准多头注意力更加集中和机制稳定。相同的集中模式在间接对象识别、归纳头和事实回忆中都成立。在单一架构家族（Qwen2.5）内，事实回忆电路在临界规模以上经历离散相变，坍缩为单个瓶颈而非逐渐退化。这些发现表明一些架构选择使大型模型更容易研究，并且可解释性难度不是模型规模的固定后果。

---

## 145. EmoS: A High-Fidelity Multimodal Benchmark for Fine-grained Streaming Emotional Understanding

**arXiv ID**: [2605.08847](https://arxiv.org/abs/2605.08847)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08847)

**作者**: Pengze Guo, Jingxi Liang, Zhiwen Xie, Qifeng Wang, Derek F. Wong

**分类**: Computation and Language

**发布时间**: 2026-05-09 10:01:21 UTC

**摘要 (英文)**: In the context of today's high-pressure, aging society, the demand for large-scale emotional models capable of providing empathetic support is more critical than ever. However, existing benchmarks fail to simultaneously achieve ecological validity, signal clarity, and reliable fine-grained labeling. We introduce EmoS, a high-fidelity bilingual benchmark designed to resolve the limitations of ecological validity and noise in existing datasets by combining strictly filtered static slices with a dynamic Streaming Monologue subset. Supported by a rigorous dual-layer human annotation pipeline, EmoS provides trusted ground truth that captures continuous emotional evolution. Empirical results show that fine-tuning MLLMs (multimodal large language models) on EmoS yields significant gains over zero-shot baselines, laying the foundation for the training and evaluation of future emotion recognition models and empathy models. The dataset and code are publicly available at https://github.com/NLP2CT/EmoS.

**摘要 (中文)**: 在当今高压、老龄化社会中，对能够提供情感支持的大规模情感模型的需求比以往任何时候都更加关键。然而，现有基准无法同时实现生态有效性、信号清晰度和可靠的细粒度标签。我们引入了EmoS，这是一个高保真双语基准，通过结合严格过滤的静态切片和动态Streaming Monologue子集来解决现有数据集生态有效性和噪声的限制。在严格的双层人工注释管道支持下，EmoS提供捕获持续情感演化的可信ground truth。实证结果表明，在EmoS上微调MLLM（多模态大语言模型）比零样本基线获得显著收益，为未来情绪识别模型和情感模型的训练和评估奠定基础。数据集和代码在 https://github.com/NLP2CT/EmoS 公开可用

---

## 146. XPERT: Expert Knowledge Transfer for Effective Training of Language Models

**arXiv ID**: [2605.08842](https://arxiv.org/abs/2605.08842)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08842)

**作者**: Chang Liu, Boyu Shi, Xu Yang, Xin Geng

**分类**: Computation and Language

**发布时间**: 2026-05-09 09:53:03 UTC

**摘要 (英文)**: Mixture-of-Experts (MoE) language models organize knowledge into explicitly routed expert modules, making expert-level representations traceable and analyzable. By analyzing expert activation patterns in MoE large language models (LLMs), we find that a subset of experts is consistently activated across diverse knowledge domains. These common experts encode cross-domain, generalizable knowledge that is closely related to model generalization, naturally raising the question of how such identifiable expert knowledge can be practically reused. Motivated by this observation, we propose XPERT, a framework that extracts, consolidates, and reuses expert knowledge from pre-trained MoE LLMs to support more effective training of language models across different model scales. XPERT identifies cross-domain experts via inference-only analysis, refines their representations through tensor decomposition, and adapts the extracted knowledge to reuse in downstream models. Experiments on language understanding and dialogue generation benchmarks show that models benefiting from reused expert knowledge achieve consistently stronger performance and faster convergence compared to strong baselines. These results highlight MoE LLMs as structured and reusable knowledge sources, and demonstrate the value of expert-level knowledge reuse for improving model training.

**摘要 (中文)**: 专家混合（MoE）语言模型将知识组织到显式路由的专家模块中，使专家级表示可追踪和分析。通过分析MoE大语言模型（LLM）中的专家激活模式，我们发现一组专家在 diverse 知识域中持续激活。这些共同专家编码跨领域、可泛化的知识，与模型泛化密切相关，自然引出了这种可识别专家知识如何实际重用的问题。受此观察启发，我们提出了XPERT，这是一个从预训练MoE LLM中提取、整合和重用专家知识的框架，以支持在不同模型规模下更有效的语言模型训练。XPERT通过仅推理分析识别跨域专家，通过张量分解细化其表示，并使提取的知识适应在下游模型中重用。在语言理解和对话生成基准上的实验表明，受益于重用专家知识的模型与强基线相比实现持续更强的性能和更快的收敛。这些结果强调MoE LLM作为结构化和可重用知识来源的价值，并展示专家级知识重用对改进模型训练的价值。

---

## 147. ReST-KV: Robust KV Cache Eviction with Layer-wise Output Reconstruction and Spatial-Temporal Smoothing

**arXiv ID**: [2605.08840](https://arxiv.org/abs/2605.08840)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08840)

**作者**: Yongqi An, Chang Lu, Kuan Zhu, Tao Yu, Chaoyang Zhao 等 (共8人)

**分类**: Computation and Language

**发布时间**: 2026-05-09 09:49:32 UTC

**摘要 (英文)**: Large language models (LLMs) face growing challenges in efficient generative inference due to the increasing memory demands of Key-Value (KV) caches, especially for long sequences. Existing eviction methods typically retain KV pairs with high attention weights but overlook the impact of attention redistribution caused by token removal, as well as the spatial-temporal dynamics in KV selection. In this paper, we propose ReST-KV, a robust KV eviction method that combines layer-wise output Reconstruction and Spatial-Temporal smoothing to provide a more comprehensive perspective for the KV cache eviction task. Specifically, ReST-KV formulates KV cache eviction as an optimization problem that minimizes output discrepancies through efficient layer-wise reconstruction. By directly modeling how each token's removal affects the model output, our method naturally captures attention redistribution effects, going beyond simplistic reliance on raw attention weights. To further enhance robustness, we design exponential moving average smoothing to handle temporal variations and an adaptive window-based mechanism to capture spatial patterns. Our method, ReST-KV, significantly advances performance on long-context benchmarks. It surpasses state-of-the-art baselines by 2.58% on LongBench and 15.2% on RULER. Additionally, ReST-KV consistently outperforms existing methods on Needle-in-a-Haystack and InfiniteBench, all while achieving a remarkable 10.61$\times$ reduction in decoding latency at 128k context length. The code is publicly available at https://github.com/an-yongqi/rest-kv to facilitate reproducibility and further research.

**摘要 (中文)**: 大语言模型（LLM）在高效生成推理方面面临越来越大的挑战，特别是对于长序列，键值（KV）缓存的内存需求不断增加。现有驱逐方法通常保留具有高注意力权重的KV对，但忽略token移除引起的注意力重新分配影响，以及KV选择中的时空动态。在本文中，我们提出了ReST-KV，这是一种健壮的KV驱逐方法，结合分层输出重建和时空平滑，为KV缓存驱逐任务提供更全面的视角。具体来说，ReST-KV将KV缓存驱逐形式化为通过高效分层重建最小化输出差异的优化问题。通过直接建模每个token的移除如何影响模型输出，我们的方法自然地捕获注意力重新分配效应，超越对原始注意力权重的简单依赖。为了进一步增强鲁棒性，我们设计了指数移动平均平滑来处理时间变化，以及基于自适应窗口的机制来捕获空间模式。我们的方法ReST-KV在长上下文基准上显著推进性能。它在LongBench上超越最先进基线2.58%，在RULER上超越15.2%。此外，ReST-KV在Needle-in-a-Haystack和InfiniteBench上始终优于现有方法，同时在128k上下文长度下实现显著的10.61倍解码延迟降低。代码公开可访问 https://github.com/an-yongqi/rest-kv 以促进可重现性和进一步研究。

---

## 148. Generating Leakage-Free Benchmarks for Robust RAG Evaluation

**arXiv ID**: [2605.08838](https://arxiv.org/abs/2605.08838)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08838)

**作者**: Jiayi Liu, Jiaxing Zhang, Bowen Jin, Jennifer Neville

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-09 09:48:50 UTC

**摘要 (英文)**: Retrieval-augmented generation (RAG) is widely used to augment large language models (LLMs) with external knowledge. However, many benchmark datasets, designed to test RAG performance, comprise many questions that can already be answered from an LLM's parametric memory. This leads to unreliable evaluation. We refer to this phenomenon as knowledge leakage: cases where RAG tasks are solvable without retrieval. This issue worsens over time due to benchmark aging. As benchmarks are reused for training, their contents are increasingly absorbed into model parameters, making them less effective for evaluating retrieval. We introduce SeedRG, a semi-synthetic benchmark generation pipeline that mitigates knowledge leakage and addresses the issue of benchmark aging. Starting from a seed benchmark dataset, SeedRG extracts a reasoning graph from question-context pairs to capture their underlying reasoning structure, and then generates new examples via type-constrained entity replacement. This process produces structurally similar but novel instances that are unlikely to exist in the model's parametric knowledge, while preserving the original reasoning patterns. To ensure quality, we incorporate two verification steps: (1) a reasoning-graph consistency check to maintain task difficulty, and (2) a knowledge-leakage filter to exclude instances answerable without retrieval.

**摘要 (中文)**: 检索增强生成（RAG）广泛用于用外部知识增强大语言模型（LLM）。然而，许多为测试RAG性能设计的基准数据集包含许多已经可以从LLM参数记忆中回答的问题。这导致不可靠的评估。我们将这种现象称为知识泄漏：RAG任务可以在不检索的情况下解决的情况。由于基准老化，这个问题随着时间推移而恶化。当基准被重复用于训练时，它们的内容越来越多地被吸收到模型参数中，使它们对评估检索的效果降低。我们引入了SeedRG，一个半合成基准生成管道，减轻知识泄漏并解决基准老化问题。从种子基准数据集开始，SeedRG从问题-上下文对中提取推理图以捕获其底层推理结构，然后通过类型约束实体替换生成新示例。这个过程产生结构相似但新颖的实例，不太可能存在于模型的参数知识中，同时保留原始推理模式。为确保质量，我们纳入两个验证步骤：（1）推理图一致性检查以保持任务难度，（2）知识泄漏过滤器以排除可在不检索情况下回答的实例。

---

## 149. The Grounding Gap: How LLMs Anchor the Meaning of Abstract Concepts Differently from Humans

**arXiv ID**: [2605.08837](https://arxiv.org/abs/2605.08837)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08837)

**作者**: Odysseas S. Chlapanis, Orfeas Menis Mastromichalakis, Christos H. Papadimitriou

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-09 09:41:12 UTC

**摘要 (英文)**: Abstract concepts - justice, theory, availability - have no single perceivable referent; in the human brain, their meaning emerges from a web of experiences, affect, and social context. Do large language models (LLMs) ground abstract concepts in a similar way? We study this by replicating property-generation experiments from cognitive science on 21 frontier and open-weight LLMs. Across models and experiments, we find a consistent pattern: when compared to humans, models rely too heavily on word associations, and underproduce properties tied to emotion and internal states. This yields a large and consistent grounding gap: no model exceeds a Pearson correlation r=0.37 with human responses, compared to a human-to-human ceiling above r=0.9. To better interpret this gap, we also replicate a rating experiment on grounding categories and find that here LLMs align more closely with human judgment, and alignment improves as models get larger. We then use sparse autoencoders (SAEs) to inspect whether this information is also reflected in the models' internal features, and we do identify features connected to grounding dimensions such as "sensorimotor" and "social". These findings suggest that current LLMs can recover grounding dimensions when explicitly queried, but do not recruit them in a human-like way when words are generated freely.

**摘要 (中文)**: 抽象概念——正义、理论、可用性——没有单一可感知的指称；在人类大脑中，它们的意义从经验、情感和社会背景的网络中出现。大语言模型（LLM）是否以类似的方式锚定抽象概念？我们通过在21个前沿和开源权重LLM上复制认知科学的属性生成实验来研究这个问题。跨模型和实验，我们发现一致的模式：与人类相比，模型过度依赖词汇联想，而少产生与情感和内部状态相关的属性。这产生了一个大而一致的接地差距：没有模型超过与人类响应的Pearson相关r=0.37，而人类与人类的天花板高于r=0.9。为了更好解释这个差距，我们还复制了一个接地类别评级实验，发现LLM在这里与人类判断更一致，且随着模型变大一致性改善。然后我们使用稀疏自编码器（SAE）检查这些信息是否也反映在模型内部特征中，我们确实识别出与"感觉运动"和"社会"等接地维度相关的特征。这些发现表明，当前LLM在明确查询时可以恢复接地维度，但在自由生成词汇时不会以类似人类的方式招募它们。

---

## 150. SimReg: Achieving Higher Performance in the Pretraining via Embedding Similarity Regularization

**arXiv ID**: [2605.08809](https://arxiv.org/abs/2605.08809)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08809)

**作者**: Yan Sun, Guoxia Wang, Jinle Zeng, JiaBin Yang, Shuai Li 等 (共9人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-09 08:59:13 UTC

**摘要 (英文)**: Pretraining large language models (LLMs) with next-token prediction has led to remarkable advances, yet the context-dependent nature of token embeddings in such models results in high intra-class variance and inter-class similarity, thus hindering the efficiency of representation learning. While similarity-based regularization has demonstrated benefit in supervised fine-tuning and classification tasks, its application and efficacy in large-scale LLM pretraining remains underexplored. In this work, we propose the SimReg, an embedding similarity regularization loss that explicitly encourages token representations with the same ground-truth label within each sequence to be more similar, while enforcing separation from different-label tokens via a contrastive loss. Our analysis reveals that this mechanism introduces gains by enlarging multi-classification margins, thereby enabling more efficient classification. Extensive experiments across dense and Mixture-of-Experts (MoE) architectures demonstrate that SimReg consistently accelerates training convergence by over 30% and improves average zero-shot downstream performance by over 1% across standard benchmarks. Further ablation studies and analyses offer practical insights into hyperparameter tuning and loss effectiveness.

**摘要 (中文)**: 使用下一个token预测预训练大语言模型（LLM）已导致显著进步，然而这些模型中token嵌入的上下文依赖性质导致高类内方差和类间相似性，从而阻碍表示学习的效率。虽然基于相似性的正则化在监督微调和分类任务中显示出好处，但其在大规模LLM预训练中的应用和功效仍未被探索。在这项工作中，我们提出了SimReg，一种嵌入相似性正则化损失，明确鼓励在同一序列内具有相同 ground-truth 标签的token表示更相似，同时通过对比损失强制与不同标签的token分离。我们的分析表明，这种机制通过扩大多分类边界来引入增益，从而实现更有效的分类。跨密集和专家混合（MoE）架构的大量实验表明，SimReg持续加速训练收敛超过30%，并在标准基准上平均提高超过1%的零样本下游性能。进一步的消融研究和分析为超参数调整和损失有效性提供了实践见解。

---

## 151. Narrative Landscape: Mapping Narrative Dispositions Across LLMs

**arXiv ID**: [2605.08742](https://arxiv.org/abs/2605.08742)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08742)

**作者**: Donghoon Jung, Jiwoo Choi, Songeun Chae, Seohyon Jung

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-09 07:06:57 UTC

**摘要 (英文)**: This study proposes a quantitative framework for profiling LLM dispositions as stable, model-specific regularities in output under repeated, controlled elicitation. Using a structured narrative constraint-selection task administered across six frontier models and three instruction types, we operationalize disposition through two dimensions: "consistency", measured as cross-replication selection overlap via Jaccard similarity, and "diversity", measured as dispersion across options via the inverse Simpson index. We further introduce Narrative Landscape, a PCA-based visualization that maps each model's selection profile into a shared space for direct comparison. Results reveal a clear rigidity-exploration spectrum across model families and show that instruction types shift the geometry of selection spaces even when scalar metrics appear similar, indicating that comparable scores can mask qualitatively distinct selection topologies.

**摘要 (中文)**: 本研究提出了一个定量框架，用于在重复、受控诱导下将LLM disposition 分析为输出中稳定的、模型特定的规律性。使用在六个前沿模型和三种指令类型上管理的结构化叙事约束选择任务，我们通过两个维度来操作化disposition："一致性"，通过Jaccard相似性测量跨复制选择重叠，"多样性"，通过逆Simpson指数测量跨选项的分散度。我们进一步引入了Narrative Landscape，这是一种基于PCA的可视化，将每个模型的选择配置文件映射到共享空间以进行直接比较。结果揭示了跨模型家族的明显刚性-探索 spectrum，并表明指令类型改变选择空间的几何结构，即使标量指标看起来相似，表明可比较的分数可以掩盖定性不同的选择拓扑。

---

## 152. Training with Harnesses: On-Policy Harness Self-Distillation for Complex Reasoning

**arXiv ID**: [2605.08741](https://arxiv.org/abs/2605.08741)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08741)

**作者**: Zhengyang Zhao, Lu Ma, Wentao Zhang

**分类**: Computation and Language

**发布时间**: 2026-05-09 07:06:37 UTC

**摘要 (英文)**: Inference-time harnesses substantially improve large language models on complex reasoning tasks. However, the intrinsic capabilities of the underlying model remain unchanged by the addition of these external workflows. To bridge this gap, we introduce \emph{On-Policy Harness Self-Distillation} (OPHSD), which employs the harness-augmented current model as a teacher for self-distillation, thereby introducing extra supervisory signals from the harness beyond training data. OPHSD internalizes task-specific harness capabilities into the student model, yielding robust generalizability and strong standalone performance across diverse reasoning tasks. Evaluated across draft--verify harness for text classification and plan--solve for mathematical reasoning tasks, OPHSD consistently outperforms strong baselines (e.g., +10.83\% over OPSD on HMMT25). Our analysis further indicates that reattaching the harness during inference yields no additional benefits and can even degrade performance, suggesting that complex harnesses need not always be permanent fixtures; instead, they can serve as temporary training scaffolds whose benefits are permanently fed back into the base model. Our code and training data are available at https://github.com/zzy1127/OPHSD-On-Policy-Harness-Self-Distillation.

**摘要 (中文)**: 推理时的harness在复杂推理任务上显著改进大语言模型。然而，底层模型的内在能力通过这些外部工作流的添加保持不变。为弥补这一差距，我们引入了On-Policy Harness Self-Distillation（OPHSD），它利用harness增强的当前模型作为自蒸馏的教师，从而引入来自harness的超额训练数据的监督信号。OPHSD将任务特定的harness能力内化到学生模型中，在各种推理任务中产生强大的泛化和强劲的独立性能。在文本分类的draft-verify harness和数学推理任务的plan-solve上评估，OPHSD持续优于强基线（例如，在HMMT25上比OPSD高10.83%）。我们的分析进一步表明，在推理时重新连接harness不会产生额外收益甚至可能降低性能，表明复杂的harness不必永远是永久 fixture；相反，它们可以充当临时训练脚手架，其收益永久反馈到基础模型中。我们的代码和训练数据可访问 https://github.com/zzy1127/OPHSD-On-Policy-Harness-Self-Distillation

---

## 153. Breaking the Impasse: Dual-Scale Evolutionary Policy Training for Social Language Agents

**arXiv ID**: [2605.08721](https://arxiv.org/abs/2605.08721)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08721)

**作者**: Minzheng Wang, Run Luo, Yanbo Wang, Zichen Liu, Yuqiao Tan 等 (共9人)

**分类**: Computation and Language

**发布时间**: 2026-05-09 06:10:32 UTC

**摘要 (英文)**: While Reinforcement Learning with Verifiable Rewards (RLVR) has proven effective for closed-ended tasks, extending it to open-ended social language games via self-play reveals a critical issue: evolution impasse. Due to the vast strategy space, language agents frequently converge to homogenized behaviors, leading to deterministic match outcomes that eliminate the gradient signals necessary for policy evolution. To tackle this issue, we propose Dual-scale Evolutionary Policy Training (DEPT) for social language games. DEPT introduces a time-scaled evolutionary perception mechanism that detects impasse by quantifying dual-scale value baseline divergence alongside match entropy. Upon perceiving the collapse, it then activates asymmetric advantage reshaping to dynamically modulate the optimization landscape for intervention. Thus, our method effectively restores gradient signals and enforces sustained strategic exploration. Extensive experiments on multiple social language games demonstrate that DEPT outperforms strong baselines, avoiding policy degeneration and driving the continuous evolution of social language agents.

**摘要 (中文)**: 虽然带可验证奖励的强化学习（RLVR）已被证明对封闭任务有效，但通过自游戏将其扩展到开放端社交语言游戏揭示了一个关键问题：进化僵局。由于策略空间巨大，语言智能体经常收敛到同质化行为，导致确定性匹配结果消除了策略进化所需的梯度信号。为解决这个问题，我们为社交语言游戏提出了双尺度进化策略训练（DEPT）。DEPT引入了一个时间尺度的进化感知机制，通过量化双尺度价值基线分歧和匹配熵来检测僵局。在感知到崩溃后，它然后激活不对称优势重塑，以动态调节干预的优化景观。因此，我们的方法有效恢复梯度信号并强制持续的战略探索。在多个社交语言游戏上的大量实验表明，DEPT优于强基线，避免策略退化并推动社交语言智能体的持续进化。

---

## 154. AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems

**arXiv ID**: [2605.08715](https://arxiv.org/abs/2605.08715)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08715)

**作者**: Boxuan Zhang, Jianing Zhu, Zeru Shi, Dongfang Liu, Ruixiang Tang

**分类**: Computation and Language, Artificial Intelligence, Multiagent Systems

**发布时间**: 2026-05-09 05:55:19 UTC

**摘要 (英文)**: LLM-based multi-agent systems are increasingly deployed on long-horizon tasks, but a single decisive error is often accepted by downstream agents and cascades into trajectory-level failure. Existing work frames this as \emph{post-hoc failure attribution}, diagnosing the responsible agent and step after the trajectory has ended. However, this paradigm forfeits any opportunity to intervene while trajectory is still unfolding. In this work, we introduce AgentForesight, a framework that reframes this problem as online auditing: at each step of an unfolding trajectory, an auditor observes only the current prefix and must either continue the run or alarm at the earliest decisive error, without access to future steps. To this end, we curate AFTraj-2K, a corpus of agentic trajectories across Coding, Math, and Agentic domains, in which safe trajectories are retained under a strict curation pipeline and unsafe trajectories are annotated at the step of their decisive error via consensus among multiple LLM judges. Built on that, we develop AgentForesight-7B, a compact online auditor trained with a coarse-to-fine reinforcement learning recipe that first equips it with a risk-anticipation prior at the failure boundary on adjacent safe/unsafe prefix pairs, then sharpens this prior into precise step-level localization under a three-axis reward jointly targeting the what, where, and who of an audit verdict. Across AFTraj-2K and an external Who\&When benchmark, AgentForesight-7B outperforms leading proprietary models, including GPT-4.1 and DeepSeek-V4-Pro, achieving up to +19.9% performance gain and 3$\times$ lower step localization error, opening the loop from post-hoc failures detection to enabling deployment-time intervention. Project page: https://zbox1005.github.io/agent-foresight/

**摘要 (中文)**: 基于LLM的多智能体系统越来越多地部署在长期任务上，但单个决定性错误经常被下游智能体接受并级联到轨迹级失败。现有工作将其框架化为事后失败归因，在轨迹结束后诊断负责的智能体和步骤。然而，这种范式放弃了轨迹仍在展开时进行干预的任何机会。在这项工作中，我们引入了AgentForesight，一个将此问题重新框架化为在线审计的框架：在展开轨迹的每一步，审计员仅观察当前前缀，必须要么继续运行，要么在最早期决定性错误时发出警报，而无法访问未来步骤。为此，我们策划了AFTraj-2K，这是一个跨编码、数学和智能体领域的智能体轨迹语料库，其中安全轨迹在严格策划管道下保留，不安全轨迹通过多个LLM评委共识在决定性错误步骤上注释。在此基础上，我们开发了AgentForesight-7B，这是一个紧凑的在线审计器，使用粗到细的强化学习配方训练，首先使其在相邻安全/不安全前缀对上的失败边界获得风险预期先验，然后在此先验下将其锐化为精确的步骤级定位，三轴奖励共同针对审计裁决的内容、位置和谁。跨AFTraj-2K和外部Who&When基准，AgentForesight-7B优于领先的专有模型，包括GPT-4.1和DeepSeek-V4-Pro，实现高达+19.9%的性能增益和3倍低的步骤定位错误，从事后失败检测开启到实现部署时干预。项目页面：https://zbox1005.github.io/agent-foresight/

---

## 155. Structured Recurrent Mixers for Massively Parallelized Sequence Generation

**arXiv ID**: [2605.08696](https://arxiv.org/abs/2605.08696)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08696)

**作者**: Benjamin L. Badger

**分类**: Computation and Language, Machine Learning

**发布时间**: 2026-05-09 05:07:55 UTC

**摘要 (英文)**: Over the last two decades, language modeling has experienced a shift from predominantly recurrent architectures that process tokens sequentially during training and inference to non-recurrent models that process sequence elements in parallel during training, which results in greater training efficiency and stability at the expense of lower inference throughput. Here we introduce the Structured Recurrent Mixer, an architecture that allows for algebraic conversion between a sequence parallel representation at train time and a recurrent representation at inference, notably without the need for specialized kernels or device-specific memory management. We show experimentally that this dual representation allows for greater training efficiency, higher input information capacity, and larger inference throughput and concurrency when compared to other linear complexity models. We postulate that recurrent models are poorly suited to extended sequence length scaling for information-rich inputs typical of language, but are well suited to scaling in the sample (batch) dimension due to their constant memory per sample. We provide Mojo/MAX inference implementations of SRMs exhibiting 12x the throughput and 170x the concurrency of similarly powerful Transformers inferenced on vLLM, increases characteristic of Pytorch implementations resulting in a 30\% increase in compute-constant GSM8k Pass@k. We conclude by demonstrating that SRMs are effective reinforcement learning training candidates.

**摘要 (中文)**: 在过去二十年里，语言建模经历了从主要在训练和推理期间顺序处理token的循环架构到在训练期间并行处理序列元素的非循环模型的转变，这导致更高的训练效率和稳定性，但以较低的推理吞吐量为代价。在这里，我们引入了结构化循环混合器（Structured Recurrent Mixer），一种允许在训练时序列并行表示和推理时循环表示之间进行代数转换的架构，值得注意的是无需专门的内核或设备特定的内存管理。我们实验表明，与其他线性复杂度模型相比，这种双重表示允许更高的训练效率、更大的输入信息容量以及更大的推理吞吐量和并发性。我们假设循环模型不太适合典型语言的信息丰富输入的扩展序列长度，但由于每个样本的恒定内存，非常适合在样本（批次）维度上扩展。我们提供了在vLLM上推理的类似能力Transformers的12倍吞吐量和170倍并发性的SRM Mojo/MAX推理实现增加导致计算恒定GSM8k Pass@k增加30%。最后，我们证明SRM是有效的强化学习训练候选。

---

## 156. Explanation Fairness in Large Language Models: An Empirical Analysis of Disparities in How LLMs Justify Decisions Across Demographic Groups

**arXiv ID**: [2605.08671](https://arxiv.org/abs/2605.08671)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08671)

**作者**: Gautam Veldanda

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-09 04:19:03 UTC

**摘要 (英文)**: Large language models (LLMs) are increasingly deployed not only to make decisions but to explain them. While AI decision fairness has been studied extensively, the fairness of AI explanations (whether LLMs justify decisions with equal quality, depth, tone, and linguistic sophistication across demographic groups) has received little attention. This paper introduces the Explanation Fairness Taxonomy (EFT), a framework comprising five formally defined, operationalizable dimensions: Verbosity Disparity, Sentiment Disparity, Epistemic Hedging Disparity, Decision-Linked Explanation Disparity, and Lexical Complexity Disparity. The taxonomy is instantiated in a controlled empirical study across 80 prompt templates, four consequential decision domains (hiring, medical triage, credit assessment, legal judgment), and five LLMs: GPT-4.1, Claude Sonnet, LLaMA 3.3 70B, GPT-OSS 120B, and Qwen3 32B. Two novel black-box metrics are introduced: the Hedging Density Score (HDS) and the Explanation Faithfulness Proxy (EFP), a heuristic indicator of decision-linked explanation variation. Across up to 400 prompt pairs, all eight EFT metrics show statistically significant disparities (Cohen's d ranging from small to large, all p_BH < 10^(-62)). Model choice is strongly associated with disparity magnitude: Qwen3 32B exhibits verbosity disparities 5.9x larger than LLaMA 3.3 70B. Two prompting-based mitigations show significant reductions in EFP disparity (78-95%) but no significant effect on stylistic dimensions, consistent with the hypothesis that stylistic explanation inequalities are encoded in pre-training distributions and are not resolvable through deployment-level instruction alone. A reproducible measurement framework is offered for explanation-level fairness auditing, with implications for AI regulation and deployment practice.

**摘要 (中文)**: 大语言模型（LLM）越来越多地被部署不仅用于做决策，还用于解释它们。虽然AI决策公平性已被广泛研究，但AI解释的公平性（LLM是否以相同的质量、深度、语气和语言复杂性跨人口群体为决策辩护）受到的关注很少。本文引入了解释公平分类法（EFT），一个由五个正式定义、可操作维度组成的框架：冗长性差异、情感差异、认知回避差异、决策相关解释差异和词汇复杂性差异。该分类法在80个提示模板、四个后果性决策领域（招聘、医疗分诊、信贷评估、法律判断）和五个LLM（GPT-4.1、Claude Sonnet、LLaMA 3.3 70B、GPT-OSS 120B和Qwen3 32B）的受控实证研究中实例化。引入了两个新的黑盒指标：回避密度分数（HDS）和解释忠实度代理（EFP），这是决策相关解释变化的启发式指标。在最多400个提示对中，所有八个EFT指标显示统计学显著差异（Cohen's d从小到大，所有p_BH < 10^(-62)）。模型选择与差异幅度强相关：Qwen3 32B的冗长性差异是LLaMA 3.3 70B的5.9倍。两种基于提示的缓解显示EFP差异显著减少（78-95%），但对风格维度无显著影响，与风格解释不平等编码在预训练分布中且无法仅通过部署级指令解决的假设一致。提供了一个可重现的解释级公平审计测量框架，对AI监管和部署实践有影响。

---

## 157. Hint Tuning: Less Data Makes Better Reasoners

**arXiv ID**: [2605.08665](https://arxiv.org/abs/2605.08665)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08665)

**作者**: Siqi Fan, Minghao Li, Xiaoqian Ma, Xiusheng Huang, Zhuo Chen 等 (共9人)

**分类**: Computation and Language

**发布时间**: 2026-05-09 04:07:16 UTC

**摘要 (英文)**: Large reasoning models achieve high accuracy through extended chain-of-thought but generate 5--8 more tokens than necessary, applying verbose reasoning uniformly regardless of problem difficulty. We propose Hint Tuning, a data-efficient approach that teaches models to calibrate reasoning depth. Our key insight: the corresponding instruct model serves as an ideal difficulty probe. By testing what the instruct model can solve with varying guidance, we automatically construct training data across three states: No-Hint (direct answer), Sparse-Hint (minimal prefix), and Full-Hint (complete reasoning). This converts the abstract challenge of difficulty labeling into a measurable consistency check between the instruct and reasoning models. With only 1K self-annotated samples, Hint Tuning achieves 24--66% token reduction (31.5% average) across mainstream reasoning models (Qwen3-Thinking, DeepSeek-R1-Distill) at multiple scales (4B--32B) while maintaining competitive accuracy on five benchmarks. Unlike methods requiring massive distillation datasets or expensive RL, we achieve superior efficiency through simple alignment with the instruct model's capabilities.

**摘要 (中文)**: 大推理模型通过扩展思维链实现高精度，但生成比必要多5-8倍的token，无论问题难度如何都应用冗长推理。我们提出了Hint Tuning，一种数据高效的方法，教模型校准推理深度。我们的关键洞察：相应的instruct模型是理想的难度探测器。通过测试instruct模型在不同指导下能解决什么，我们自动构建三种状态的训练数据：无提示（直接回答）、稀疏提示（最小前缀）和完整提示（完整推理）。这将难度标签的抽象挑战转换为instruct模型和推理模型之间的一致性可测量检查。仅用1K自注释样本，Hint Tuning在主流推理模型（Qwen3-Thinking、DeepSeek-R1-Distill）在多个规模（4B-32B）上实现24-66%token减少（平均31.5%），同时在五个基准上保持竞争准确性。与需要大量蒸馏数据集或昂贵RL的方法不同，我们通过简单地对齐instruct模型的能力实现卓越效率。

---

## 158. AgentCollabBench: Diagnosing When Good Agents Make Bad Collaborators

**arXiv ID**: [2605.08647](https://arxiv.org/abs/2605.08647)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08647)

**作者**: Aritra Mazumder, Shubhashis Roy Dipta, Nusrat Jahan Lia, Tanzila Khan, Kainat Raisa Hossain 等 (共13人)

**分类**: Computation and Language, Artificial Intelligence, Machine Learning

**发布时间**: 2026-05-09 03:35:09 UTC

**摘要 (英文)**: Multi-agent systems achieve state-of-the-art outcomes through peer collaboration. However, when an agent in the pipeline silently drops a constraint, the system's final output may look correct even though the reasoning chain was quietly corrupted, and existing outcome-based evaluations are blind to such multi-hop process failures. To make these vulnerabilities measurable before deployment, we introduce AgentCollabBench, a diagnostic benchmark of 900 human-validated tasks spanning software engineering, DevOps, and data engineering. Each task isolates one of four behavioral risks: instruction decay (does a constraint survive peer pressure?), false-belief contagion (does a falsehood spread through consensus?), context leakage (does information bleed between tasks?), and tracer durability (does marked data reach the final agent?). Evaluating four modern LLMs (GPT 4.1 mini, Gemini 2.5 Flash Lite, Qwen-3.5-35B-A3B, and Llama 3.1 8B Instruct), we expose model-specific vulnerability profiles invisible to outcome-only evaluation; Qwen-3.5-35B-A3B, for example, leads on tracer durability and instruction stability, while GPT 4.1 mini leads on leakage containment and false-belief resistance. Beyond per-model differences, communication topology emerges as a primary risk factor that explains 7-40% of the variance in multi-hop information survival. The effect traces to a synthesis bottleneck specific to converging-DAG nodes: an agent weighing competing parent inputs discards constraints carried by a minority branch, a bottleneck structurally absent from linear chains. AgentCollabBench demonstrates that suboptimal topology can silently erase the safeguards of highly capable models, arguing that multi-agent reliability is fundamentally a structural problem and that scaling model intelligence alone is no substitute for architecture.

**摘要 (中文)**: 多智能体系统通过同行协作实现最先进的结果。然而，当管道中的智能体悄悄丢弃一个约束时，系统最终输出可能看起来正确，即使推理链悄悄腐烂，现有基于结果的评估对这种多跳过程失败是盲目的。为了在部署前使这些漏洞可测量，我们引入了AgentCollabBench，这是一个900个人类验证任务的诊断基准，涵盖软件工程、DevOps和数据工程。每个任务隔离四种行为风险之一：指令衰减（约束在同伴压力下是否存活？）、错误信念传染（虚假是否通过共识传播？）、上下文泄漏（信息是否在任务之间泄漏？)和追踪器耐久性（标记数据是否到达最终智能体？）。评估四个现代LLM（GPT 4.1 mini、Gemini 2.5 Flash Lite、Qwen-3.5-35B-A3B和Llama 3.1 8B Instruct），我们揭示了仅结果评估无法看到 model-specific 漏洞档案；例如，Qwen-3.5-35B-A3B在追踪器耐久性和指令稳定性方面领先，而GPT 4.1 mini在泄漏containment和错误信念抵抗方面领先。除per-model差异外，通信拓扑成为解释多跳信息生存方差7-40%的主要风险因素。该效果追溯到特定于汇聚DAG节点的综合瓶颈：权衡竞争父输入的智能体丢弃少数分支携带的瓶颈，这种瓶颈在线性链中在结构上不存在。AgentCollabBench表明，欠佳拓扑可以悄悄抹去高能力智能体的安全措施，认为多智能体可靠性基本上是一个结构问题，单独扩展模型智能不能替代架构。

---

## 159. EdgeFlowerTune: Evaluating Federated LLM Fine-Tuning Under Realistic Edge System Constraints

**arXiv ID**: [2605.08636](https://arxiv.org/abs/2605.08636)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08636)

**作者**: Jiaxiang Geng, Yiyi Lu, Lunyu Zhao, Yan Gao, Nicholas D. Lane 等 (共6人)

**分类**: Computation and Language

**发布时间**: 2026-05-09 03:02:44 UTC

**摘要 (英文)**: Federated fine-tuning offers a promising paradigm for adapting large language models (LLMs) on edge devices by leveraging the rich, diverse, and continuously generated data from smartphones and IoT devices without compromising user data privacy. Such edge-side adaptation can improve model personalization, robustness, and responsiveness to local contexts. However, the practical feasibility of federated LLM fine-tuning on real edge devices remains unclear, as most existing work focuses on cross-silo or simulation-based settings, overlooking the resource and runtime constraints that determine whether a method is deployable on real edge systems. We present EdgeFlowerTune, a deployment-oriented benchmark for federated LLM fine-tuning under realistic edge-system constraints. EdgeFlowerTune jointly evaluates model quality and system costs, including communication, wall-clock latency, memory usage, energy consumption, and robustness to dynamic edge conditions. To compare methods in terms of effectiveness, efficiency, and robustness, EdgeFlowerTune introduces three complementary protocols: Quality-under-Budget, Cost-to-Target, and Robustness. We instantiate EdgeFlowerTune as a real-device platform built on Flower and MobileFineTuner, spanning commercial Android smartphones and NVIDIA edge development boards. Our benchmark results show that accuracy-only evaluation can lead to misleading conclusions: methods with similar final quality may differ substantially in deployability once realistic system constraints are considered. EdgeFlowerTune provides a reproducible benchmark for system-aware evaluation of federated LLM fine-tuning at the edge.

**摘要 (中文)**: 联邦微调为通过利用来自智能手机和物联网设备的丰富、多样化和持续生成的数据adapt大语言模型（LLM）提供了有前景的 paradigm，而不损害用户数据隐私。这种边缘侧适应可以提高模型个性化、对本地环境的鲁棒性和响应能力。然而，联邦LLM微调在真实边缘设备上的实际可行性仍不清楚，因为大多数现有工作专注于跨silo或模拟设置，忽略了决定方法是否可在真实边缘系统上部署的资源 和运行时约束。我们呈现EdgeFlowerTune，这是一个面向部署的基准，用于在现实边缘系统约束下进行联邦LLM微调。EdgeFlowerTune联合评估模型质量和系统成本，包括通信、 wall-clock延迟、内存使用、能源消耗和对动态边缘条件的鲁棒性。为比较有效性、效率和鲁棒性方面 的方法，EdgeFlowerTune引入了三个补充协议：预算下的质量、成本到目标和鲁棒性。我们将EdgeFlowerTune实例化为建立在Flower和MobileFineTuner上的真实设备平台，跨越商业Android智能手机和NVIDIA边缘开发板。我们的基准结果表明，仅准确性评估可能导致误导性结论：一旦考虑现实系统约束，具有相似最终质量的方法可能在部署性方面存在显著差异。EdgeFlowerTune为边缘联邦LLM微调的系统感知评估提供了一个可重现的基准。

---

## 160. PARD-2: Target-Aligned Parallel Draft Model for Dual-Mode Speculative Decoding

**arXiv ID**: [2605.08632](https://arxiv.org/abs/2605.08632)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08632)

**作者**: Zihao An, Taichi Liu, Ziqiong Liu, Dong Li, Ruofeng Liu 等 (共6人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-09 02:50:58 UTC

**摘要 (英文)**: Speculative decoding accelerates Large Language Models (LLMs) inference by using a lightweight draft model to propose candidate tokens that are verified in parallel by the target model. However, existing draft model training objectives are not directly aligned with the inference-time goal of maximizing consecutive token acceptance. To address this issue, we reformulate the draft model optimization objective, shifting the focus from token prediction accuracy to the overall acceptance length. In this paper, we build upon PARD to propose PARD-2, a dual-mode speculative decoding framework with Confidence-Adaptive Token (CAT) optimization. This approach adaptively reweights each token to better align with the verification process. Notably, PARD-2 enables a single draft model to support both target-dependent and target-independent modes. Experiments across diverse models and tasks demonstrate that PARD-2 achieves up to 6.94$\times$ lossless acceleration, surpassing EAGLE-3 by 1.9$\times$ and PARD by 1.3$\times$ on Llama3.1-8B. Our code is available at https://github.com/AMD-AGI/PARD.

**摘要 (中文)**: 投机解码通过使用轻量级draft模型提出候选token来加速大语言模型（LLM）推理，这些token由目标模型并行验证。然而，现有draft模型训练目标与推理时最大化连续token接受的目标不直接一致。为解决这一问题，我们重新制定draft模型优化目标，将重点从token预测准确性转移到整体接受长度。在本文中，我们基于PARD提出PARD-2，一个具有置信度自适应token（CAT）优化的双模式投机解码框架。这种方法自适应地重新加权每个token以更好地与验证过程对齐。值得注意的是，PARD-2使单个draft模型能够支持目标依赖和目标独立模式。跨不同模型和任务的实验表明，PARD-2实现高达6.94倍的无损加速，在Llama3.1-8B上超过EAGLE-3 1.9倍和PARD 1.3倍。我们的代码可访问 https://github.com/AMD-AGI/PARD

---

## 161. 100,000+ Movie Reviews from Kazakhstan: Russian, Kazakh, and Code-Switched Texts

**arXiv ID**: [2605.08600](https://arxiv.org/abs/2605.08600)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08600)

**作者**: Rustem Yeshpanov

**分类**: Computation and Language

**发布时间**: 2026-05-09 01:45:57 UTC

**摘要 (英文)**: We present a new publicly available corpus of 100,502 movie reviews from Kazakhstan collected from kino.kz, spanning 2001-2025 and covering 4,943 unique titles. The dataset is multilingual, consisting mainly of Russian reviews alongside Kazakh and code-switched texts. Reviews are manually annotated for language and sentiment polarity, and 11,309 reviews additionally contain explicit user-provided ratings. We define two sentiment tasks -- three-way polarity classification and five-class score classification -- and benchmark classical BoW/TF-IDF baselines against multilingual transformer models (mBERT, XLM-RoBERTa, RemBERT). Experimental results show that transformer models consistently outperform classical baselines on polarity classification, while score classification remains challenging under leakage-controlled evaluation due to severe class imbalance and subtle distinctions between adjacent rating levels.

**摘要 (中文)**: 我们呈现了一个新的公开可用的100,502条来自哈萨克斯坦kino.kz的电影评论语料库，涵盖2001-2025年，覆盖4,943个独特标题。数据集是多语言的，主要由俄语评论以及哈萨克语和代码切换文本组成。评论被手动标注语言和情感极性，另有11,309条评论包含用户提供的明确评分。我们定义了两个情感任务——三向极性分类和五类评分分类——并对多语言transformer模型（mBERT、XLM-RoBERTa、RemBERT）进行经典BoW/TF-IDF基线基准测试。实验结果表明，transformer模型在极性分类上始终优于经典基线，而在泄漏控制评估下，由于严重的类不平衡和相邻评分水平之间的细微差别，评分分类仍然具有挑战性。

---

## 162. Source or It Didn't Happen: A Multi-Agent Framework for Citation Hallucination Detection

**arXiv ID**: [2605.08583](https://arxiv.org/abs/2605.08583)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08583)

**作者**: Mingzhe Li, Zhiqiang Lin, Shiqing Ma

**分类**: Computation and Language

**发布时间**: 2026-05-09 00:53:24 UTC

**摘要 (英文)**: Large language models are increasingly used in scientific writing, yet they can fabricate citation-shaped references that appear plausible but fail bibliographic verification. Existing detectors often reduce verification to binary found/not-found decisions and rely on brittle parsing or incomplete retrieval, offering little field-level signal to auditors. We reframe citation hallucination detection as taxonomy-aligned field-level adjudication and introduce a 12-code taxonomy spanning Real, Potential, and Hallucinated citations. Based on this taxonomy, we build CiteTracer, a cascading multi-agent detector that extracts structured citations from PDF and BibTeX, retrieves evidence through cache lookup, URL fetch, scholar connectors, and web search, applies deterministic field matching, and routes ambiguous cases to class-specialist judgers. We release a benchmark of 2,450 synthetic citations built from real seeds with controlled LLM mutations, paired with 957 real-world fabricated citations drawn from ICLR 2026 and an anonymous conference desk-rejected submissions. CiteTracer reaches 97.1% accuracy on the synthetic benchmark, with class-level F1 scores of 97.0, 95.8, and 98.5 for Real, Potential, and Hallucinated, respectively, and detects 97.1% of fabrications on the real-world set without abstaining. Code: https://github.com/aaFrostnova/CiteTracer.

**摘要 (中文)**: 大语言模型越来越多地用于科学写作，但它们可以制造看起来合理但无法通过书目验证的引用形状参考。现有的检测器经常将验证简化为二元发现/未发现决策，并依赖脆弱的解析或不完整的检索，几乎没有字段级信号给审计员。我们将引用幻觉检测重新框架化为分类法对齐的字段级裁决，并引入一个跨越真实、潜在和幻觉引用的12代码分类法。基于这个分类法，我们构建了CiteTracer，一个级联多智能体检测器，从PDF和BibTeX提取结构化引用，通过缓存查找、URL获取、学者连接器和网络搜索检索证据，应用确定性字段匹配，并将模糊情况路由到专业分类判断者。我们发布了一个由2,450个从真实种子构建的合成引用组成的基准，用受控LLM突变配对，并从ICLR 2026和一个匿名会议desk-rejected提交中抽取957个真实世界的捏造引用。CiteTracer在合成基准上达到97.1%准确性，真实、潜在和幻觉的类别级F1分数分别为97.0、95.8和98.5，并在不放弃的情况下检测到真实世界集中97.1%的捏造。代码：https://github.com/aaFrostnova/CiteTracer

---

## 163. Coordinates of Capability: A Unified MTMM-Geometric Framework for LLM Evaluation

**arXiv ID**: [2605.08522](https://arxiv.org/abs/2605.08522)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08522)

**作者**: Adib Sakhawat, Tahsin Islam, Takia Farhin, Syed Rifat Raiyan, Hasan Mahmud 等 (共6人)

**分类**: Computation and Language

**发布时间**: 2026-05-08 22:05:19 UTC

**摘要 (英文)**: The evaluation of Large Language Models (LLMs) faces a critical challenge in construct validity, where fragmented benchmarks and ad hoc metrics frequently conflate method variance, such as prompt sensitivity, with true latent capabilities. Concurrently, emerging research suggests that LLM capabilities and outputs can be modeled as continuous geometric manifolds. In this Systematization of Knowledge (SoK), we bridge these paradigms by proposing a generalized Multi-Trait Multi-Method (MTMM) framework for LLM evaluation. We formalize and unify nine evaluation metrics, including Paraphrase Instability, Drift Score, Overton Width, and Pluralism Score, interpreting them not as isolated scalar values but as geometric measurements within a shared latent coordinate space. This spatial unification factorizes model behavior into three orthogonal latent dimensions: (1) Instability and Sensitivity, (2) Position and Alignment, and (3) Coverage and Expressiveness. By systematically separating task-irrelevant perturbations from true capability spans, the framework provides a theoretically grounded and domain-agnostic taxonomy for robust and empirically stable benchmark design.

**摘要 (中文)**: 大语言模型（LLM）评估在构念效度方面面临关键挑战，碎片化基准和临时指标经常将方法方差（如提示敏感性）与真实潜在能力混为一谈。同时新兴研究表明LLM能力和输出可以建模为连续几何流形。在这个知识系统化（SoK）中，我们通过提出用于LLM评估的广义多特质多方法（MTMM）框架来桥接这些范式。我们形式化并统一了九个评估指标，包括 paraphrase instability、drift score、overton width和pluralism score，将它们解释为共享潜在坐标空间内的几何测量，而非孤立的标量值。这种空间统一将模型行为分解为三个正交潜在维度：（1）不稳定性和敏感性，（2）位置和对齐，以及（3）覆盖率和表现力。通过系统地将任务无关扰动与真实能力跨度分离，该框架为鲁棒和经验上稳定的基准设计提供了一个理论上有根据且领域无关的分类法。

---

## 164. A Single Neuron Is Sufficient to Bypass Safety Alignment in Large Language Models

**arXiv ID**: [2605.08513](https://arxiv.org/abs/2605.08513)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08513)

**作者**: Hamid Kazemi, Atoosa Chegini, Maria Safi

**分类**: Computation and Language, Artificial Intelligence, Machine Learning

**发布时间**: 2026-05-08 21:45:28 UTC

**摘要 (英文)**: Safety alignment in language models operates through two mechanistically distinct systems: refusal neurons that gate whether harmful knowledge is expressed, and concept neurons that encode the harmful knowledge itself. By targeting a single neuron in each system, we demonstrate both directions of failure -- bypassing safety on explicit harmful requests via suppression, and inducing harmful content from innocent prompts via amplification -- across seven models spanning two families and 1.7B to 70B parameters, without any training or prompt engineering. Our findings suggest that safety alignment is not robustly distributed across model weights but is mediated by individual neurons that are each causally sufficient to gate refusal behavior -- suppressing any one of the identified refusal neurons bypasses safety alignment across diverse harmful requests.

**摘要 (中文)**: 研究安全对齐的神经机制，发现拒绝神经元和概念神经元两个系统，单个神经元即可绕过安全对齐。

**arXiv ID**: [2605.08504](https://arxiv.org/abs/2605.08504)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08504)

**作者**: Zeru Shi, Zhenting Wang, Fan Yang, Qifan Wang, Ruixiang Tang

**分类**: Computation and Language

**发布时间**: 2026-05-08 21:37:27 UTC

**摘要 (英文)**: We investigate the origins of massive activations in large language models (LLMs) and identify a specific layer named the \textbf{Massive Emergence Layer (ME Layer)}, that is consistently observed across model families, where massive activations first emerge and subsequently propagate to deeper layers through residual connections. We show that, within the ME Layer both the RMSNorm and the FFN parameters jointly contribute to the emergence of massive activations. Once formed, the massive activation token representation remains largely invariant across layers, reducing the diversity of hidden representations passed to the attention module. Motivated by this limitation, we propose a simple and effective method to reduce the rigidity of the massive activation token. Our approach consistently improves LLM performance across multiple tasks, including instruction following and math reasoning, in both training free and fine tuning settings. Moreover, we show that our method mitigates attention sinks by selectively weakening their influence, elucidating their origin at the hidden state level and shedding new light on principled mitigation strategies.

**摘要 (中文)**: [待翻译]

---

## 166. NARRA-Gym for Evaluating Interactive Narrative Agents

**arXiv ID**: [2605.08503](https://arxiv.org/abs/2605.08503)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08503)

**作者**: Yue Huang, Yuchen Ma, Jiayi Ye, Wenjie Wang, Zipeng Ling 等 (共17人)

**分类**: Computation and Language, Computers and Society, Human-Computer Interaction

**发布时间**: 2026-05-08 21:36:23 UTC

**摘要 (英文)**: Interactive narrative tasks require LLMs to sustain a coherent, evolving story while adapting to a user over multiple turns. However, suitable benchmarks for this setting are limited: existing evaluations often focus on static prompts, isolated story generations, or post-hoc ratings, and therefore miss whether models can jointly manage story generation, long-context state and pacing, character simulation, empathic personalization, and story-grounded artifacts. We introduce NARRA-Gym, an executable evaluation environment that turns a sparse emotional seed into a complete interactive story episode and logs the full model-in-the-loop trajectory, including story construction, memory updates, planning, pacing interventions, and optional artifact synthesis. We evaluate nine frontier LLMs using a controlled LLM-as-judge sweep over eight benchmark personas and a human evaluation in which participants rate customized model outputs. Our results show substantial variation across models, personas, and evaluation dimensions: models that produce fluent stories can still fail on robustness, user experience, or resistance-sensitive personalization. These findings suggest that interactive narrative offers a useful benchmark for evaluating long-horizon, user-adaptive LLM behavior beyond isolated story quality.

**摘要 (中文)**: 提出NARRA-Gym可执行评估环境，将情感种子转化为完整互动故事，评估LLM在长程、用户适应性任务中的表现。

**arXiv ID**: [2605.08477](https://arxiv.org/abs/2605.08477)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08477)

**作者**: Naoki Otani, Nikita Bhutani, Hannah Kim, Dan Zhang, Estevam Hruschka

**分类**: Computation and Language

**发布时间**: 2026-05-08 20:51:42 UTC

**摘要 (英文)**: Explicit planning is a critical capability for LLM-based agents solving complex data-centric tasks, which require precise tool calling over external data sources. Existing strategies fall into two paradigms based on planning horizon: (1) full-horizon (FH), which generates a complete plan before execution, and (2) single-step horizon (SH), which interleaves each action (tool call) with incremental reasoning and observation. While step-by-step execution is a common default under the assumption that eager execution monitoring is necessary for adaptability, we revisit this assumption for well-defined data-centric tasks. Our controlled empirical study isolates planning horizon as the key architectural feature and systematically analyzes the effects of topological complexity and tool robustness on both paradigms. Our experiments across Knowledge Base Question Answering and Multi-hop QA show that FH planning with lazy replanning achieves accuracy parity with SH across varying depths, breadths, and robustness levels, while using 2-3x fewer tokens. These findings suggest that for well-defined data-centric tasks, eager step-wise monitoring is often unnecessary, and full-horizon planning with on-demand replanning can offer a more efficient default.

**摘要 (中文)**: 研究数据为中心任务的规划视野问题，发现全视野规划lazy repanning与单步规划精度相当但token减少2-3倍。

**arXiv ID**: [2605.08476](https://arxiv.org/abs/2605.08476)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08476)

**作者**: Mila Marcheva, Suchir Salhan, Weiwei Sun

**分类**: Computation and Language

**发布时间**: 2026-05-08 20:51:40 UTC

**摘要 (英文)**: This paper is concerned with what intermediate syntactic categories children acquire during first language development, and in what order. Maturational theories make different predictions. Bottom-up accounts (GROWING) propose that lexical and inflectional structure emerges first, while inward accounts (INWARD) predict early access to discourse-related categories. We computationally operationalise these hypotheses of staged syntactic emergence using statistical grammar induction, asking what each proposed ordering makes learnable when input and learning algorithm are held constant. Our framework makes category acquisition explicit and allows us to explore how different maturational orderings shape the structure that can be learned under identical conditions. Based on this operationalisation, the GROWING account significantly outperforms the INWARD account across three evaluation metrics.

**摘要 (中文)**: [待翻译]

---

## 169. PYTHALAB-MERA: Validation-Grounded Memory, Retrieval, and Acceptance Control for Frozen-LLM Coding Agents

**arXiv ID**: [2605.08468](https://arxiv.org/abs/2605.08468)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08468)

**作者**: Mehmet Iscan

**分类**: Computation and Language, Artificial Intelligence, Machine Learning

**发布时间**: 2026-05-08 20:39:32 UTC

**摘要 (英文)**: Local LLM-based coding agents increasingly work in settings where correctness is earned through execution feedback, persistent state, and bounded repair, not through a single fluent answer. Static retrieval, long-context prompting, self-refinement, execution-feedback repair, and reinforcement learning over model weights each address part of this setting, but they do not jointly provide validation-grounded episodic memory, adaptive retrieval-action selection, delayed credit assignment, and structural skill reuse around a frozen local model. We introduce PYTHALAB-MERA, a lightweight external controller for local validation-conditioned code generation. The frozen language model proposes complete source files; the controller decides which memory records and AST-derived skills should enter the next prompt, validates each candidate through a fail-fast pipeline, converts validation outcomes into bounded shaped rewards, and propagates delayed credit through TD(lambda)-style eligibility traces. We evaluate the implementation as a local CLI artifact on reinforcement-learning coding tasks with strict validation gates. In the measured hard RL setting with three tasks, three repetitions, and a three-attempt budget, PYTHALAB-MERA passed 8/9 strict validations; the self-refinement baseline and the investigated GRACE extension each passed 0/9. These results support a deliberately bounded claim: in this recorded setting, the external memory-and-retrieval controller improved validation success. They do not establish general-purpose code synthesis, state-of-the-art performance, formal program correctness, or formal safety.

**摘要 (中文)**: [待翻译]

---

## 170. Do Benchmarks Underestimate LLM Performance? Evaluating Hallucination Detection With LLM-First Human-Adjudicated Assessment

**arXiv ID**: [2605.08462](https://arxiv.org/abs/2605.08462)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08462)

**作者**: I. F. Atasoy, B. Mutlu, E. A. Sezer, A. Wahdan

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-08 20:27:44 UTC

**摘要 (英文)**: Hallucination remains a persistent challenge in Large Language Models (LLMs), particularly in context-grounded settings such as RAG and agentic AI systems. This study focuses on contextual hallucination detection in summarization tasks. We analyze the QAGS-C and SummEval datasets by comparing original benchmark annotations with reason and span-based predictions from Gemini 2.5 Flash and GPT-5 Mini. To address systematic divergences between human labels and LLM judgments, we re-evaluated all conflicted samples through a human adjudication process involving 2 cross-cultural adjudicators. Following this re-evaluation, triple agreement (between human, GPT, and Gemini) increased by 6.38% for QAGS-C and 7.62% for SummEval. Similarly, model accuracy improved, with GPT increasing by 4.25% on QAGS-C and 2.34% on SummEval, while Gemini showed gains of 8.51% and 3.80%, respectively. Notably, adjudicators frequently sided with the models' judgments over original human annotations when LLMs provided explicit reasoning. Overall human adjudicator agreement ranged between 83% and 87%. These findings suggest that for ambiguity-prone tasks, single-pass annotations may be insufficient, and model-assisted re-evaluation yields more reliable benchmarks.

**摘要 (中文)**: [待翻译]

---

## 171. Revisiting the syntax of imperatives in Yemeni Arabic: An Agree across phases approach

**arXiv ID**: [2605.08447](https://arxiv.org/abs/2605.08447)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08447)

**作者**: Mohammed Q. Shormani

**分类**: Computation and Language

**发布时间**: 2026-05-08 20:14:22 UTC

**摘要 (英文)**: This article revisits the syntax of imperatives in Yemeni Arabic proposing an Agree acros phases (AAP) approach. I argue that the AAP approach successfully accounts for both simple and complex imperative constructions, including A'-chain structures, by establishing a close interactions between syntax and discourse. The study demonstrates that this interface is motivated by the interpretive and performative functions associated with imperatives, linking informational structure with propositional structure. It is also proposed that the thematic subject of imperatives is a 2-person pro, whereas any overt pronominal or nominal element occurring preverbally is not a subject, but rather a C-domain element, precisely aboutness topic. These topics serve as the logical subjects of imperatives and enter into a coreferentiality relationship with pro. This relation is analyzed as APP involving Match, yielding both local and non-local A'-chains. For core imperatives, viz., lacking an overt topic, I propose a null topic to (re)merge in Spec,TopP, whose interpretation depends on the discourse.

**摘要 (中文)**: [待翻译]

---

## 172. Can Language Models Identify Side Effects of Breast Cancer Radiation Treatments?

**arXiv ID**: [2605.08439](https://arxiv.org/abs/2605.08439)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08439)

**作者**: Natalie Seah, Danielle S. Bitterman, Daphna Spiegel, Thomas Hartvigsen

**分类**: Computation and Language

**发布时间**: 2026-05-08 20:02:49 UTC

**摘要 (英文)**: Accurately communicating the side effects of cancer treatments to cancer survivors is critical, particularly in settings such as informed consent, where clinicians must clearly and comprehensively convey potential treatment toxicities. However, this task remains challenging due to clinical knowledge deficits about adverse treatment effects and fragmentation across electronic health record (EHR) systems. Large language models (LLMs) have the potential to assist in this task, though their reliability in oncology survivorship contexts remains poorly understood. We present a deployment-oriented stress-testing framework for evaluating LLM-generated radiation side effect lists in breast cancer treatment and survivorship care. Using 21 breast cancer patient profiles, we construct paired patient clinical scenarios that differ only in radiotherapy regimens to evaluate seven instruction-tuned LLMs under multiple prompting regimes. We then compare LLM outputs to a clinician-curated reference derived from informed consent documents at two major academic medical centers and developed by a team including more than seven breast radiation oncologists. The reference maps radiation dose-fractionation, fields, and locations to associated toxicities, broken down by frequency and temporal onset. Across models, we reveal sensitivity to minor documentation changes, trade-offs between precision and recall, and systematic under-recall of rare and long-term side effects. When used alone, constraints on the number of side effects generated reduce precision, and grounding outputs in clinician-curated side effect lists substantially improves reliability and robustness. These findings highlight important limitations of LLM use in oncology and suggest practical design choices for safer and more informative survivorship-focused applications.

**摘要 (中文)**: [待翻译]

---

## 173. Magis-Bench: Evaluating LLMs on Magistrate-Level Legal Tasks

**arXiv ID**: [2605.08437](https://arxiv.org/abs/2605.08437)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08437)

**作者**: Ramon Pires, Thales Sales Almeida, Celio Larcher Junior, Giovana Bonás, Hugo Abonizio 等 (共9人)

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-08 20:00:14 UTC

**摘要 (英文)**: Existing benchmarks for legal AI focus primarily on tasks where LLMs must produce legal arguments or documents, yet the capacity to \emph{judge} such arguments -- weighing competing claims, applying doctrine to facts, and rendering reasoned decisions -- is arguably as fundamental to a well-functioning legal system as advocacy itself. We introduce Magis-Bench, a benchmark for evaluating LLMs on magistrate-level writing tasks derived from recent Brazilian competitive examinations for judicial positions. Magis-Bench comprises 74 questions from eight examinations conducted between 2023 and 2025, including discursive legal analysis questions with multi-turn structure and practical exercises requiring the composition of complete civil and criminal judicial sentences. We evaluate 23 state-of-the-art LLMs using an LLM-as-a-judge methodology with four independent frontier models as evaluators. Our results show strong inter-judge agreement (Kendall's $W = 0.984$; pairwise Kendall's $τ\ge 0.897$), with Google's Gemini-3-Pro-Preview achieving the highest average score (6.97/10), followed by Gemini-3-Flash-Preview (6.67) and Claude-4.5-Opus (6.46). Even the best-performing models score below 70\% of the maximum, indicating that judicial-level legal reasoning and writing remain challenging for current LLMs. We release the complete benchmark, model outputs, and evaluation code to support further research on legal AI capabilities.

**摘要 (中文)**: [待翻译]

---

## 174. A Semantic-Sampling Framework for Evaluating Calibration in Open-Ended Question Answering

**arXiv ID**: [2605.08432](https://arxiv.org/abs/2605.08432)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08432)

**作者**: Zhanliang Wang, Jiancong Xiao, Ruochen Jin, Shu Yang, Bojian Hou 等 (共6人)

**分类**: Computation and Language, Artificial Intelligence, Machine Learning

**发布时间**: 2026-05-08 19:53:49 UTC

**摘要 (英文)**: Calibration measures whether a model's predicted confidence aligns with its empirical accuracy, and is central to the reliable deployment of large language models (LLMs) in high-stakes domains such as medicine and law. While much recent work focuses on improving LLM calibration, the equally important question of how to evaluate it in realistic settings remains underdeveloped. Open-ended question answering (QA), the most common deployment setting for modern LLMs, is where existing evaluation methods fall short: logit-based metrics need restricted output formats and internal probabilities; verbalized confidence is self-reported and often overconfident; and sampling-based methods rely on task-specific extraction rules without a clear finite-sample target. We introduce Sem-ECE (Semantic-Sampling Expected Calibration Error), a calibration evaluation framework for open-ended QA that samples answers from the model, groups them into semantic classes, and uses the resulting frequencies as confidence. We study two estimators within this framework: Sem$_1$-ECE, the same-sample self-consistency score, and Sem$_2$-ECE, a held-out variant that separates answer selection from confidence evaluation. We prove both are asymptotically unbiased, and further show that they agree on easy questions but diverge on hard ones with Sem$_2$ achieving strictly smaller calibration error, so their gap also serves as a diagnostic for question difficulty. Experiments on three open-ended QA benchmarks across five leading commercial LLMs match our theoretical predictions and show that Sem-ECE outperforms verbalized confidence and existing sampling-based methods, while complementing logit-based evaluation when internal probabilities are unavailable.

**摘要 (中文)**: [待翻译]

---

## 175. Effective Explanations Support Planning Under Uncertainty

**arXiv ID**: [2605.08406](https://arxiv.org/abs/2605.08406)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08406)

**作者**: Hanqi Zhou, Britt Besch, Charley M. Wu, Tobias Gerstenberg

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-08 19:12:14 UTC

**摘要 (英文)**: Explaining how to get from A to B can be challenging. It requires mentally simulating what the listener will do based on what they are told. To capture this process, we propose a computational model that converts utterances into action plans: a large language model translates an explanation into program-like guidance (a policy prior and value map), and a planning agent executes it under partial observability. We score explanations by the efficiency and reliability of the resulting paths, penalizing replanning. Across four preregistered experiments, we collect a corpus of 1,200 explanations over 24 maps, elicit helpfulness judgments, measure baseline navigation, and test behavior with explanations of differing quality. Higher-scored explanations are judged more helpful and improve navigation: participants with explanations outperform those without, and high-scoring explanations help more than low-scoring ones. Together, these results show procedural explanation as utility-guided communication shaped by how language can be grounded into action under uncertainty.

**摘要 (中文)**: [待翻译]

---

## 176. Built Environment Reasoning from Remote Sensing Imagery Using Large Vision--Language Models

**arXiv ID**: [2605.08404](https://arxiv.org/abs/2605.08404)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08404)

**作者**: Dongdong Wang, Deepak Balakrishnan, Ravi Srinivasan, Shenhao Wang

**分类**: Computation and Language, Artificial Intelligence, Computer Vision and Pattern Recognition, Emerging Technologies

**发布时间**: 2026-05-08 19:10:30 UTC

**摘要 (英文)**: This work investigates the use of large language models (LLMs) for tasks in smart cities. The core idea is to leverage remote sensing imagery to characterize the built environment, including design suggestions, constructability assessment, landuse patterns, and risk identification. We examine remote sensing imagery at multiple spatial scales as inputs for multimodal language modeling and evaluate their effects on built-environment-related reasoning. In addition, we compare state-of-the-art LLMs, including InternVL and Qwen, in terms of accuracy and reliability when generating built environment recommendations. The results demonstrate the potential of integrating remote sensing imagery with large language models to assist smart cities and decision-making.

**摘要 (中文)**: [待翻译]

---

## 177. AIPO: : Learning to Reason from Active Interaction

**arXiv ID**: [2605.08401](https://arxiv.org/abs/2605.08401)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08401)

**作者**: Junnan Liu, Linhao Luo, Thuy-Trang Vu, Gholamreza Haffari

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-08 19:06:55 UTC

**摘要 (英文)**: Recent advances in large language models (LLMs) have demonstrated remarkable reasoning capabilities, largely stimulated by Reinforcement Learning with Verifiable Rewards (RLVR). However, existing RL algorithms face a fundamental limitation: their exploration remains largely constrained by the inherent capability boundary of the policy model. Although recent methods introduce external expert demonstrations to extend this boundary, they typically rely on complete trajectory-level guidance, which is sample-inefficient, information-sparse, and may confine exploration to a static guidance space. Inspired by the potential of multi-agent systems, we propose $\textbf{AIPO}$, an enhanced reinforcement learning framework that improves LLM reasoning through active multi-agent interaction during exploration. Specifically, AIPO enables the policy model to proactively consult three functional collaborative agents, $\textit{Verify Agent}$, $\textit{Knowledge Agent}$, and $\textit{Reasoning Agent}$, when encountering reasoning bottlenecks, thereby receiving fine-grained and targeted guidance to actively expand its capability boundary during training. We further introduce a tailored importance sampling coefficient together with a clipping strategy to mitigate the off-policy bias and gradient vanishing issues that arise when learning from agent-provided feedback. After training, the policy model performs reasoning independently without relying on collaborative agents. Extensive experiments on diverse reasoning benchmarks, including AIME, MATH500, GPQA-Diamond, and LiveCodeBench, show that AIPO consistently improves reasoning performance, generalizes robustly across different policy models and RLVR algorithms, and effectively expands the reasoning capability boundary of the policy model.

**摘要 (中文)**: [待翻译]

---

## 178. jina-embeddings-v5-omni: Text-Geometry-Preserving Multimodal Embeddings via Frozen-Tower Composition

**arXiv ID**: [2605.08384](https://arxiv.org/abs/2605.08384)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08384)

**作者**: Florian Hönicke, Michael Günther, Andreas Koukounas, Kalim Akram, Scott Martens 等 (共7人)

**分类**: Computation and Language

**发布时间**: 2026-05-08 18:45:15 UTC

**摘要 (英文)**: In this work, we introduce frozen-encoder model composition, a novel approach to multimodal embedding models. We build on the VLM-style architecture, in which non-text encoders are adapted to produce input for a language model, which in turn generates embeddings for all varieties of input. We present the result: the jina-embeddings-v5-omni suite, a pair of models that encode text, image, audio, and video input into a single semantic embedding space. Our method is to extend the two Jina Embeddings v5 Text models to support additional media by adding encoders for images and audio. The backbone text embedding models and the added non-text media encoders remain frozen. We only trained the connecting components, representing 0.35% of the total weights of the joint model. Training is therefore much more efficient than full-parameter retraining. Additionally, the language model remains effectively unaltered, producing exactly the same embeddings for text inputs as the Jina Embeddings v5 Text models. Our evaluations show that this approach produces results that are competitive with the state-of-the-art, yielding nearly equal performance to larger multimodal embedding models.

**摘要 (中文)**: [待翻译]

---

## 179. Change My View? The Dynamics of Persuasion and Polarization in Online Discourse

**arXiv ID**: [2605.08383](https://arxiv.org/abs/2605.08383)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08383)

**作者**: David Freeborn, Malihe Alikani, Anthony Sicilia

**分类**: Computation and Language

**发布时间**: 2026-05-08 18:40:51 UTC

**摘要 (英文)**: Philosophical accounts of persuasion often assume that shared evidence and rational argumentation should lead to a convergence of views between peers, yet everyday discourse often suggests otherwise. In this study, we use large language models to analyze a corpus of debates on Reddit's r/ChangeMyView, where belief revision is publicly signaled. Large language models were asked, halfway through each discussion, to forecast whether such an acknowledgement would arise; their probabilistic estimates serve as a conversational baseline. Each reply was then coded, through a hybrid machine-assisted procedure, for ten familiar rhetorical strategies -- concession, empathy, logical challenge, credibility appeals, and so forth. Adding these strategic features markedly improves predictive power and yields a consistent pattern: moves that express concession or empathetic alignment substantially increase the prospect of belief change, whereas frontal refutation, credibility attacks, and topic deflection diminish it. The findings indicate that effective public reasoning depends as much on relational framing as on evidential content, and they invite a refinement of normative accounts of rational dialogue.

**摘要 (中文)**: [待翻译]

---

## 180. How Much Do Circuits Tell Us? Measuring the Consistency and Specificity of Language Model Circuits

**arXiv ID**: [2605.08348](https://arxiv.org/abs/2605.08348)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08348)

**作者**: Michael Li, Nishant Subramani

**分类**: Computation and Language

**发布时间**: 2026-05-08 18:01:03 UTC

**摘要 (英文)**: The circuits framework in mechanistic interpretability aims to identify causally important sparse subgraphs of model components, typically evaluated by measuring necessity and sufficiency. We measure circuit reuse, the proportion of components shared across per-example circuits within a task, and investigate two less-studied properties of this: consistency, the recurrence of components within a task, and specificity, their uniqueness to a task. Using edge attribution patching across six tasks and seven models, we find that within-task reuse is high and that shared components are necessary for task performance, with ablations causing up to $\sim$100% relative accuracy drops. However, circuits turn out not to be task-specific: ablating one task's circuit damages another task's performance about as much as that task's own circuit does. We discover that this is due to substantial overlap between circuits across tasks, which are causally important for performance. Some circuits do contain a smaller set of task-specific components, but these account for only a modest portion of circuit performance. Overall, our findings suggest that while circuit discovery at the level of attention heads and MLP layers identifies important components, their lack of task-specificity raises questions about the degree to which circuits can support targeted understanding and intervention on model behavior.

**摘要 (中文)**: [待翻译]

---

## 181. Sanity Checks for Long-Form Hallucination Detection

**arXiv ID**: [2605.08346](https://arxiv.org/abs/2605.08346)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08346)

**作者**: Geigh Zollicoffer, Minh Vu, Hongli Zhan, Raymond Li, Manish Bhattarai

**分类**: Computation and Language, Artificial Intelligence

**发布时间**: 2026-05-08 18:00:58 UTC

**摘要 (英文)**: Hallucination detection methods for large language models increasingly operate on chain-of-thought reasoning traces, yet it remains unclear whether they evaluate the reasoning itself or merely exploit surface correlates of the final answer. We introduce a controlled-invariance methodology that exposes this distinction through two oracle tests: \textsc{Force}, which replaces each response's final answer with the ground truth while preserving the reasoning trace, and \textsc{Remove}, which strips answer-announcement steps while leaving the trajectory intact. This reveals if their predictive power derives from answer-level artifacts rather than from the structure or validity of intermediate reasoning. We further show that once these artifacts are controlled for, effective detection does not necessarily require complex learned representations: TRACT, a lightweight scorer built on lexical trajectory features (hedging trends, step-length dynamics, and cross-response vocabulary convergence), achieves strong robustness while remaining competitive with or outperforming existing baselines on unperturbed traces. These findings suggest that the current central challenge in reasoning-aware hallucination detection is not the absence of signal in the trace, but the failure to isolate it from endpoint cues.

**摘要 (中文)**: [待翻译]

---

## 182. SalesSim: Benchmarking and Aligning Multimodal Language Models as Retail User Simulators

**arXiv ID**: [2605.08334](https://arxiv.org/abs/2605.08334)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08334)

**作者**: Yada Pruksachatkun, Elaine Wan, Lyanna Chen, Kai-Wei Chang, Chien-Sheng Wu

**分类**: Computation and Language

**发布时间**: 2026-05-08 17:59:23 UTC

**摘要 (英文)**: We present SalesSim, a framework and testbed for evaluating the ability of Multimodal Large Language Models (MLLMs) to simulate realistic, persona-driven customer behavior in multi-turn, multi-modal, tool-augmented online retail conversations. Unlike prior work that treat user simulation as surface-level dialogue generation, SalesSim models retail interaction and decision-making as a grounded, agentic process, where shoppers with diverse backgrounds, preferences, and dealbreakers interact with a sales agent, seek clarifications, and make informed purchasing decisions. For evaluation, we design a suite of metrics centered on decision alignment, measuring the consistency between the simulator's actions and its persona specifications, as well as conversational quality. We find several behavioral gaps after benchmarking 6 open and closed-source state-of-the-art models. First, while models produce fluent conversations, they display significantly lower lexical diversity and overdisclosure of criteria across personas compared to human conversations. Second, models tend to be persuaded by sales agent suggestions and drift from persona specifications. Even the strongest model achieves less than 79% average alignment with its underlying persona specifications. To make progress on these limitations, we propose UserGRPO, a multi-turn, multi-objective reinforcement learning recipe to optimize both conversational fluency and decision alignment under persona specifications. Our experiments demonstrate that UserGRPO boosts decision alignment of the baseline model by 13.8% while improving conversational quality. By introducing SalesSim, we provide a new testbed for the community to investigate and improve the adherence of user simulators in goal-oriented settings.

**摘要 (中文)**: [待翻译]

---

## 183. DECO: Sparse Mixture-of-Experts with Dense-Comparable Performance on End-Side Devices

**arXiv ID**: [2605.10933](https://arxiv.org/abs/2605.10933)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10933)

**作者**: Chenyang Song, Weilin Zhao, Xu Han, Chaojun Xiao, Yingfa Chen 等 (共6人)

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-11 17:58:28 UTC

**摘要 (英文)**: While Mixture-of-Experts (MoE) scales model capacity without proportionally increasing computation, its massive total parameter footprint creates significant storage and memory-access bottlenecks, which hinder efficient end-side deployment that simultaneously requires high performance, low computational cost, and small storage overhead. To achieve these properties, we present DECO, a sparse MoE architecture designed to match the performance of dense Transformers under identical total parameter budgets and training tokens. DECO utilizes the differentiable and flexible ReLU-based routing enhanced by learnable expert-wise scaling, which adaptively balances the contributions of routed and shared experts. Furthermore, we introduce NormSiLU, an activation function that normalizes inputs prior to SiLU operators, producing a more stable trend of routed-expert activation ratio and a higher intrinsic sparsity level. We also identify an empirical advantage in using non-gated MLP experts with ReLU-based routing, indicating the possibility of MoE architecture simplification. Experiments demonstrate that DECO, activating only 20% of experts, matches dense performance and outperforms established MoE baselines. Our specialized acceleration kernel delivers a 3.00$\times$ speedup on real hardware compared with dense inference. Codes and checkpoints will be released.

**摘要 (中文)**: [待翻译]

---

## 184. Dynamic Skill Lifecycle Management for Agentic Reinforcement Learning

**arXiv ID**: [2605.10923](https://arxiv.org/abs/2605.10923)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10923)

**作者**: Junhao Shen, Teng Zhang, Xiaoyan Zhao, Hong Cheng

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-11 17:55:13 UTC

**摘要 (英文)**: Large language model agents increasingly rely on external skills to solve complex tasks, where skills act as modular units that extend their capabilities beyond what parametric memory alone supports. Existing methods assume external skills either accumulate as persistent guidance or internalized into the policy, eventually leading to zero-skill inference. We argue this assumption is overly restrictive, since with limited parametric capacity and uneven marginal contribution across skills, the optimal active skill set is non-monotonic, task- and stage-dependent. In this work, we propose SLIM, a framework of dynamic Skill LIfecycle Management for agentic reinforcement learning (RL), which treats the active external skill set as a dynamic optimization variable jointly updated with policy learning. Specifically, SLIM estimates each active skill's marginal external contribution through leave-one-skill-out validation, then applies three lifecycle operations: retaining high-value skills, retiring skills whose contribution becomes negligible after sufficient exposure, and expanding the skill bank when persistent failures reveal missing capability coverage. Experiments show that SLIM outperforms the best baselines by an average of 7.1% points across ALFWorld and SearchQA. Results further indicate that policy learning and external skill retention are not mutually exclusive: some skills are absorbed into the policy, while others continue to provide external value, supporting SLIM as a more general paradigm for skill-based agentic RL.

**摘要 (中文)**: [待翻译]

---

## 185. Compute Where it Counts: Self Optimizing Language Models

**arXiv ID**: [2605.10875](https://arxiv.org/abs/2605.10875)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10875)

**作者**: Yash Akhauri, Mohamed S. Abdelfattah

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-11 17:27:15 UTC

**摘要 (英文)**: Efficient LLM inference research has largely focused on reducing the cost of each decoding step (e.g., using quantization, pruning, or sparse attention), typically applying a uniform computation budget to every generated token. In practice, token difficulty varies widely, so static compression can over-compute on easy steps and under-compute on hard ones. We study dynamic budget allocation for autoregressive decoding: learning how much computation to spend per token from within a single model. Self-Optimizing Language Models (SOL) pair a frozen LLM with a lightweight policy network that reads the LLM hidden state and selects a discrete efficiency action at each decode step. Actions can jointly control (i) token-level attention sparsity, (ii) structured activation pruning in the MLP, and (iii) activation quantization bit-width, while leaving the base model weights unchanged. We train the policy with group-relative policy optimization on teacher-forced episodes: the token sequence is fixed, while we sample multiple compute schedules (i.e., "counterfactual" schedules that vary only the efficiency actions for the same token path) and compare their likelihoods under the same supervision. Our reward trades off language-model quality against soft penalties that encourage episode-average budget usage to match a requested target. Across model variants and compute regimes, SOL improves quality at matched budget over static allocation and strong random schedule search, offering a complementary axis for inference-efficiency optimization. SOL discovers a better quality-efficiency pareto-front across all our experiments and improves MMLU accuracy by up to 7.3% over uniform budget allocation strategies.

**摘要 (中文)**: [待翻译]

---

## 186. The Generalized Turing Test: A Foundation for Comparing Intelligence

**arXiv ID**: [2605.10851](https://arxiv.org/abs/2605.10851)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10851)

**作者**: Daniel Mitropolsky, Susan S. Hong, Riccardo Neumarker, Emanuele Rimoldi, Tomaso Poggio

**分类**: Artificial Intelligence, Computation and Language, Machine Learning

**发布时间**: 2026-05-11 17:00:18 UTC

**摘要 (英文)**: We introduce the Generalized Turing Test (GTT), a formal framework for comparing the capabilities of arbitrary agents via indistinguishability. For agents A and B, we define the Turing comparator A $\geq$ B to hold if B, acting as a distinguisher, cannot reliably distinguish between interactions with A (instructed to imitate B) and another instance of B. This yields a dataset- and task-agnostic notion of relative intelligence. We study the comparator's structure, including conditions under which it is transitive and therefore induces an ordering over equivalence classes, and we define and analyze variants with querying, bounded interaction, and fixed distinguishers. To complement the theory, we instantiate the framework on a collection of modern models, empirically evaluating pairwise indistinguishability across thousands of trials. The resulting comparisons exhibit a stratified structure consistent with existing rankings, hinting that the proposed framework yields meaningful empirical orderings. Our results position indistinguishability as a unifying lens for reasoning about intelligence, suggesting a foundation for evaluation and, potentially, training objectives that are inherently independent of fixed datasets or benchmarks.

**摘要 (中文)**: [待翻译]

---

## 187. Rethinking Agentic Search with Pi-Serini: Is Lexical Retrieval Sufficient?

**arXiv ID**: [2605.10848](https://arxiv.org/abs/2605.10848)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10848)

**作者**: Tz-Huan Hsu, Jheng-Hong Yang, Jimmy Lin

**分类**: Information Retrieval, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-11 16:58:57 UTC

**摘要 (英文)**: Does a lexical retriever suffice as large language models (LLMs) become more capable in an agentic loop? This question naturally arises when building deep research systems. We revisit it by pairing BM25 with frontier LLMs that have better reasoning and tool-use abilities. To support researchers asking the same question, we introduce Pi-Serini, a search agent equipped with three tools for retrieving, browsing, and reading documents. Our results show that, on BrowseComp-Plus, a well-configured lexical retriever with sufficient retrieval depth can support effective deep research when paired with more capable LLMs. Specifically, Pi-Serini with gpt-5.5 achieves 83.1% answer accuracy and 94.7% surfaced evidence recall, outperforming released search agents that use dense retrievers. Controlled ablations further show that BM25 tuning improves answer accuracy by 18.0% and surfaced evidence recall by 11.1% over the default BM25 setting, while increasing retrieval depth further improves surfaced evidence recall by 25.3% over the shallow-retrieval setting. Source code is available at https://github.com/justram/pi-serini.

**摘要 (中文)**: [待翻译]

---

## 188. BabelDOC: Better Layout-Preserving PDF Translation via Intermediate Representation

**arXiv ID**: [2605.10845](https://arxiv.org/abs/2605.10845)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10845)

**作者**: Qi Yang, Xiangyao Ma, Xiao Wang, Hao Wang, Rui Wang

**分类**: Computer Vision and Pattern Recognition, Computation and Language

**发布时间**: 2026-05-11 16:56:44 UTC

**摘要 (英文)**: As global cross-lingual communication intensifies, language barriers in visually rich documents such as PDFs remain a practical bottleneck. Existing document translation pipelines face a tension between linguistic processing and layout preservation: text-oriented Computer-Assisted Translation (CAT) systems often discard structural metadata, while document parsers focus on extraction and do not support faithful re-rendering after translation. We introduce BabelDOC, an Intermediate Representation (IR)-based framework for layout-preserving PDF translation. BabelDOC decouples visual layout metadata from semantic content, enabling document-level translation operations such as terminology extraction, cross-page context handling, glossary-constrained generation, and formula placeholdering. The translated content is then re-anchored to the original layout through an adaptive typesetting engine. Experiments on a curated 200-page benchmark, together with human evaluation and multimodal LLM-as-a-judge evaluation, show that BabelDOC improves layout fidelity, visual aesthetics, and terminology consistency over representative baselines, while maintaining competitive translation precision. The open-source toolkit and its interactive downstream applications are publicly available and have attracted over 8.4K GitHub stars and 17 contributors at the time of writing. A demonstration video is also available.

**摘要 (中文)**: [待翻译]

---

## 189. SLIM: Sparse Latent Steering for Interpretable and Property-Directed LLM-Based Molecular Editing

**arXiv ID**: [2605.10831](https://arxiv.org/abs/2605.10831)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10831)

**作者**: Mingxu Zhang, Yuhan Li, Lujundong Li, Dazhong Shen, Hui Xiong 等 (共6人)

**分类**: Machine Learning, Artificial Intelligence, Computational Engineering, Finance, and Science, Computation and Language

**发布时间**: 2026-05-11 16:47:25 UTC

**摘要 (英文)**: Large language models possess strong chemical reasoning capabilities, making them effective molecular editors. However, property-relevant information is implicitly entangled across their dense hidden states, providing no explicit handle for property control: a substantial fraction of edits fail to improve or even degrade target properties. To address these issues, we propose SLIM (Sparse Latent Interpretable Molecular editing), a plug-and-play framework that decomposes the editor's hidden states into sparse, property-aligned features via a Sparse Autoencoder with learnable importance gates. Steering in this sparse feature space precisely activates property-relevant dimensions, improving editing success rate without modifying model parameters. The same sparse basis further supports interpretable analysis of editing behavior. Experiments on the MolEditRL benchmark across four model architectures and eight molecular properties show consistent gains over baselines, with improvements of up to 42.4 points.

**摘要 (中文)**: [待翻译]

---

## 190. Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge

**arXiv ID**: [2605.10805](https://arxiv.org/abs/2605.10805)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10805)

**作者**: Wenbo Zhang, Lijinghua Zhang, Liner Xiang, Hengrui Cai

**分类**: Artificial Intelligence, Computation and Language, Machine Learning

**发布时间**: 2026-05-11 16:30:20 UTC

**摘要 (英文)**: Reasoning-capable large language models (LLMs) have recently been adopted as automated judges, but their benefits and costs in LLM-as-a-Judge settings remain unclear. Through controlled comparisons between reasoning and non-reasoning judges, we show that explicit reasoning substantially improves judgment accuracy on tasks requiring structured verification (e.g., math and coding), while offering limited or even negative gains on simpler evaluations and incurring significantly higher computational cost. These findings motivate that reasoning should be used selectively rather than universally, with awareness of possible distribution shift. We propose a Robust Adaptive Cost-Efficient Routing (RACER), which dynamically selects between reasoning and non-reasoning judges under a fixed budget by formulating routing as a constrained distributionally robust optimization problem. RACER explicitly accounts for distribution shift via a KL-divergence uncertainty set, admits an efficient primal--dual algorithm, and enjoys theoretical guarantees including uniqueness of the optimal policy and linear convergence. Extensive experiments show that RACER achieves superior accuracy--cost trade-offs under distribution shift.

**摘要 (中文)**: [待翻译]

---

## 191. The Last Word Often Wins: A Format Confound in Chain-of-Thought Corruption Studies

**arXiv ID**: [2605.10799](https://arxiv.org/abs/2605.10799)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10799)

**作者**: Gabriel Garcia

**分类**: Machine Learning, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-11 16:26:50 UTC

**摘要 (英文)**: Corruption studies, the primary tool for evaluating chain-of-thought (CoT) faithfulness, identify which chain positions are "computationally important" by measuring accuracy when steps are replaced with errors. We identify a systematic confound: for chains with explicit terminal answer statements, the dominant format in standard benchmarks, corruption studies detect where the answer text appears, not where computation occurs. A within-dataset format ablation provides the key evidence: on standard GSM8K chains ending with "the answer is X," removing only the answer statement, preserving all reasoning, collapses suffix sensitivity ~19x at 3B (N=300, p=0.022). Conflicting-answer experiments quantify the causal mechanism: at 7B, CC accuracy drops to near-zero (<=0.02) across five architecture families; the followed-wrong rate spans 0.63-1.00 at 3B-7B and attenuates at larger scales (0.300 at Phi-4-14B, ~0.01 at 32B). A within-stable 7B replication (9.3x attenuation, N=76, p=7.8e-3; Qwen3-8B N=299, p=0.004) provides converging evidence, and the pattern replicates on MATH (DeepSeek-R1-7B: 10.9x suffix-survival recovery). On chains without answer suffixes the same protocol identifies the prefix as load-bearing (Delta=-0.77, p<10^-12). Generation-time probes confirm a dissociation: the answer is not early-determined during generation (early commitment <5%), yet at consumption time model outputs systematically follow the explicit answer text. The format-determination effect persists through 14B (8.5x ratio, p=0.001) and converges toward zero at 32B. We propose a three-prerequisite protocol (question-only control, format characterization, all-position sweep) as a minimum standard for corruption-based faithfulness studies.

**摘要 (中文)**: [待翻译]

---

## 192. Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR

**arXiv ID**: [2605.10781](https://arxiv.org/abs/2605.10781)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10781)

**作者**: Jeonghye Kim, Jiwon Jeon, Dongsheng Li, Yuqing Yang

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-11 16:16:00 UTC

**摘要 (英文)**: Self-distillation has emerged as a powerful framework for post-training LLMs, where a teacher conditioned on extra information guides a student without it, both from the same model. While this guidance is useful when the student has failed, on successful rollouts, the same mechanism instead overwrites the student's choices and suppresses it's own reasoning. Therefore, we propose reading the original self-distillation signal in reverse: when the student succeeds along a path the teacher would not have predicted, these tokens reflect its self-driven reasoning. Building on this, we propose RLRT (RLVR with Reversed Teacher), which augments GRPO by reinforcing these tokens on correct rollouts. We interpret this as a new form of exploration in RLVR: not uniform diversity, but valuable exploration grounded in the student's own success. Across base, instruction-tuned, and thinking-tuned Qwen3 checkpoints, RLRT substantially outperforms self-distillation and exploration-based baselines, establishing information asymmetry as a new, principled design axis for RLVR.

**摘要 (中文)**: [待翻译]

---

## 193. LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments

**arXiv ID**: [2605.10779](https://arxiv.org/abs/2605.10779)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10779)

**作者**: Chiyu Zhang, Huiqin Yang, Bendong Jiang, Xiaolei Zhang, Yiran Zhao 等 (共11人)

**分类**: Cryptography and Security, Computation and Language

**发布时间**: 2026-05-11 16:14:04 UTC

**摘要 (英文)**: The rapid proliferation of LLM-based autonomous agents in real operating system environments introduces a new category of safety risk beyond content safety: behavior jailbreak, where an adversary induces an agent to execute dangerous OS-level operations with irreversible consequences. Existing benchmarks either evaluate safety at the semantic layer alone, missing physical-layer harms, or fail to isolate test cases, letting earlier runs contaminate later ones. We present LITMUS (LLM-agents In-OS Testing for Measuring Unsafe Subversion), a benchmark addressing both gaps via a semantic-physical dual verification mechanism and OS-level state rollback. LITMUS comprises 819 high-risk test cases organized into one harmful seed subset and six attack-extended subsets covering three adversarial paradigms (jailbreak speaking, skill injection, and entity wrapping), plus a fully automated multi-agent evaluation framework judging behavior at both conversational and OS-level physical layers. Evaluation across frontier agents reveals three findings: (1) current agents lack effective safety awareness, with strong models (e.g., Claude Sonnet 4.6) still executing 40.64% of high-risk operations; (2) agents exhibit pervasive Execution Hallucination (EH), verbally refusing a request while the dangerous operation has already completed at the system level, invisible to every prior semantic-only framework; and (3) skill injection and entity wrapping attacks achieve high success rates, exposing pronounced agent vulnerabilities. LITMUS provides the first standardized platform for reproducible, physically grounded behavioral safety evaluation of LLM agents in real OS environments.

**摘要 (中文)**: [待翻译]

---

## 194. Conformity Generates Collective Misalignment in AI Agents Societies

**arXiv ID**: [2605.10721](https://arxiv.org/abs/2605.10721)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10721)

**作者**: Giordano De Marzo, Alessandro Bellina, Claudio Castellano, Viola Priesemann, David Garcia

**分类**: Physics and Society, Computation and Language, Multiagent Systems

**发布时间**: 2026-05-11 15:30:48 UTC

**摘要 (英文)**: Artificial intelligence safety research focuses on aligning individual language models with human values, yet deployed AI systems increasingly operate as interacting populations where social influence may override individual alignment. Here we show that populations of individually aligned AI agents can be driven into stable misaligned states through conformity dynamics. Simulating opinion dynamics across nine large language models and one hundred opinion pairs, we find that each agent's behavior is governed by two competing forces: a tendency to follow the majority and an intrinsic bias toward specific positions. Using tools from statistical physics, we derive a quantitative theory that predicts when populations become trapped in long-lived misaligned configurations, and identifies predictable tipping points where small numbers of adversarial agents can irreversibly shift population-level alignment even after manipulation ceases. These results demonstrate that individual-level alignment provides no guarantee of collective safety, calling for evaluation frameworks that account for emergent behavior in AI populations.

**摘要 (中文)**: [待翻译]

---

## 195. Step Rejection Fine-Tuning: A Practical Distillation Recipe

**arXiv ID**: [2605.10674](https://arxiv.org/abs/2605.10674)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10674)

**作者**: Igor Slinko, Ilia Zavidnyi, Egor Bogomolov, Yaroslav Zharov

**分类**: Machine Learning, Artificial Intelligence, Computation and Language, Software Engineering

**发布时间**: 2026-05-11 14:55:20 UTC

**摘要 (英文)**: Rejection Fine-Tuning (RFT) is a standard method for training LLM agents, where unsuccessful trajectories are discarded from the training set. In the context of SWE-bench tasks, this corresponds to filtering out runs where the submitted patch does not pass the tests. However, this approach discards unresolved trajectories, even though they form a large portion of all trajectories for hard tasks and even then may be partially correct. In this work, we propose Step Rejection Fine-Tuning (SRFT) - a practical way to leverage these unresolved trajectories. For this, we employ a critic LLM to assess the correctness of each step in a trajectory. Consequently, during training, we mask the loss for erroneous steps while retaining them in the context window. This way we ensure the model learns to recover from errors without reproducing them. Evaluation on SWE-bench Verified shows that while RFT improves the resolution rate by 2.4% by excluding unresolved trajectories, SRFT improves it by 3.7% by filtering them instead of discarding completely, reaching the total resolution rate of 32.2%.

**摘要 (中文)**: [待翻译]

---

## 196. MulTaBench: Benchmarking Multimodal Tabular Learning with Text and Image

**arXiv ID**: [2605.10616](https://arxiv.org/abs/2605.10616)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10616)

**作者**: Alan Arazi, Eilam Shapira, Shoham Grunblat, Mor Ventura, Elad Hoffer 等 (共11人)

**分类**: Machine Learning, Computation and Language, Computer Vision and Pattern Recognition

**发布时间**: 2026-05-11 14:12:05 UTC

**摘要 (英文)**: Tabular Foundation Models have recently established the state of the art in supervised tabular learning, by leveraging pretraining to learn generalizable representations of numerical and categorical structured data. However, they lack native support for unstructured modalities such as text and image, and rely on frozen, pretrained embeddings to process them. On established Multimodal Tabular Learning benchmarks, we show that tuning the embeddings to the task improves performance. Existing benchmarks, however, often focus on the mere co-occurrence of modalities; this leads to high variance across datasets and masks the benefits of task-specific tuning. To address this gap, we introduce MulTaBench, a benchmark of 40 datasets, split equally between image-tabular and text-tabular tasks. We focus on predictive tasks where the modalities provide complementary predictive signal, and where generic embeddings lose critical information, necessitating Target-Aware Representations that are aligned with the task. Our experimental results demonstrate that the gains from target-aware representation tuning generalize across both text and image modalities, several tabular learners, encoder scales, and embedding dimensions. MulTaBench constitutes the largest image-tabular benchmarking effort to date, spanning high-impact domains such as healthcare and e-commerce. It is designed to enable the research of novel architectures which incorporate joint modeling and target-aware representations, paving the way for the development of novel Multimodal Tabular Foundation Models.

**摘要 (中文)**: [待翻译]

---

## 197. LLARS: Enabling Domain Expert & Developer Collaboration for LLM Prompting, Generation and Evaluation

**arXiv ID**: [2605.10593](https://arxiv.org/abs/2605.10593)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10593)

**作者**: Philipp Steigerwald, Mara Stieler, Jennifer Burghardt, Eric Rudolph, Jens Albrecht

**分类**: Artificial Intelligence, Computation and Language, Human-Computer Interaction, Software Engineering

**发布时间**: 2026-05-11 14:00:27 UTC

**摘要 (英文)**: We demonstrate LLARS (LLM Assisted Research System), an open-source platform that bridges the gap between domain experts and developers for building LLM-based systems. It integrates three tightly connected modules into an end-to-end pipeline: Collaborative Prompt Engineering for real-time co-authoring with version control and instant LLM testing, Batch Generation for configurable output production across user-selected prompts $\times$ models $\times$ data with cost control, and Hybrid Evaluation where human and LLM evaluators jointly assess outputs through diverse assessment methods, with live agreement metrics and provenance analysis to identify the best model-prompt combination for a given use case. New prompts and models are automatically available for batch generation and completed batches can be turned into evaluation scenarios with a single click. Interviews with six domain experts and three developers in online counselling confirmed that LLARS feels intuitive, saves considerable time by keeping everything in one place and makes interdisciplinary collaboration seamless.

**摘要 (中文)**: [待翻译]

---

## 198. Collective Alignment in LLM Multi-Agent Systems: Disentangling Bias from Cooperation via Statistical Physics

**arXiv ID**: [2605.10528](https://arxiv.org/abs/2605.10528)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10528)

**作者**: Cristiano De Nobili

**分类**: Statistical Mechanics, Computation and Language, Multiagent Systems, Physics and Society

**发布时间**: 2026-05-11 13:13:44 UTC

**摘要 (英文)**: We investigate the emergent collective dynamics of LLM-based multi-agent systems on a 2D square lattice and present a model-agnostic statistical-physics method to disentangle social conformity from intrinsic bias, compute critical exponents, and probe the collective behavior and possible phase transitions of multi-agent systems. In our framework, each node of an $L\!\times\!L$ lattice hosts an identical LLM agent holding a binary state ($+1$/$-1$, mapped to yes/no) and updating it by querying the model conditioned on the four nearest-neighbor states. The sampler temperature $T$ serves as the sole control parameter. Across three open-weight models (llama3.1:8b, phi4-mini:3.8b, mistral:7b), we measure magnetization and susceptibility under a global-flip protocol designed to probe $\mathbb{Z}_2$ symmetry. All models display temperature-driven order-disorder crossovers and susceptibility peaks; finite-size scaling on even-$L$ lattices yields effective exponents $γ/ν$ whose values are model-dependent, close to but incompatible with the 2D Ising universality class ($γ/ν=7/4$). Our method enables the extraction of effective $β$-weighted couplings $\tilde{J}(T)$ and fields $\tilde{h}(T)$, which serve as a measure of social conformity and intrinsic bias. In the models we analyzed, we found that collective alignment is dominated by an intrinsic bias ($\tilde{h}\gg\tilde{J}$) rather than by cooperative neighbor coupling, producing field-driven crossovers instead of genuine phase transitions. These effective parameters vary qualitatively across models, providing compact collective-behavior fingerprints for LLM agents and a quantitative diagnostic for the reliability of multi-agent consensus and collective alignment.

**摘要 (中文)**: [待翻译]

---

## 199. SlimSpec: Low-Rank Draft LM-Head for Accelerated Speculative Decoding

**arXiv ID**: [2605.10453](https://arxiv.org/abs/2605.10453)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10453)

**作者**: Anton Plaksin, Sergei Krutikov, Sergei Skvortsov, Alexander Samarin

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-11 12:22:37 UTC

**摘要 (英文)**: Speculative decoding speeds up autoregressive generation in Large Language Models (LLMs) through a two-step procedure, where a lightweight draft model proposes tokens which the target model then verifies in a single forward pass. Although the drafter network is small in modern architectures, its LM-head still performs projection to a large vocabulary, becoming one of the major computational bottlenecks. In prior work this issue has been predominantly addressed via static or dynamic vocabulary truncation. Yet mitigating the bottleneck, these methods bring in extra complexity, such as special vocabulary curation, sophisticated inference-time logic or modifications of the training setup. In this paper, we propose SlimSpec, a low-rank parameterization of the drafter's LM-head that compresses the inner representation rather than the output, preserving full vocabulary support. We evaluate our method with EAGLE-3 drafter across three target models and diverse benchmarks in both latency- and throughput-bound inference regimes. SlimSpec achieves $4\text{-}5\times$ acceleration over the standard LM-head architecture while maintaining a competitive acceptance length, surpassing existing methods by up to $8\text{-}9\%$ of the end-to-end speedup. Our method requires minimal adjustments of training and inference pipelines. Combined with the aforementioned speedup improvements, it makes SlimSpec a strong alternative across wide variety of draft LM-head architectures.

**摘要 (中文)**: [待翻译]

---

## 200. StereoTales: A Multilingual Framework for Open-Ended Stereotype Discovery in LLMs

**arXiv ID**: [2605.10442](https://arxiv.org/abs/2605.10442)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10442)

**作者**: Pierre Le Jeune, Étienne Duchesne, Weixuan Xiao, Stefano Palminteri, Bazire Houssin 等 (共7人)

**分类**: Computers and Society, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-11 12:12:28 UTC

**摘要 (英文)**: Multilingual studies of social bias in open-ended LLM generation remain limited: most existing benchmarks are English-centric, template-based, or restricted to recognizing pre-specified stereotypes. We introduce StereoTales, a multilingual dataset and evaluation pipeline for systematically studying the emergence of social bias in open-ended LLM generation. The dataset covers 10 languages and 79 socio-demographic attributes, and comprises over 650k stories generated by 23 recent LLMs, each annotated with the socio-demographic profile of the protagonist across 19 dimensions. From these, we apply statistical tests to identify more than 1{,}500 over-represented associations, which we then rate for harmfulness through both a panel of humans (N = 247) and the same LLMs. We report three main findings. \textbf{(i)} Every model we evaluate emits consequential harmful stereotypes in open-ended generation, regardless of size or capabilities, and these associations are largely shared across providers rather than isolated misbehaviors. \textbf{(ii)} Prompt language strongly shapes which stereotypes appear: rather than transferring as a shared set of biases, harmful associations adapt culturally to the prompt language and amplify bias against locally salient protected groups. \textbf{(iii)} Human and LLM harmfulness judgments are broadly aligned (Spearman $ρ=0.62$), with disagreements concentrating on specific attribute classes rather than specific providers. To support further analyses, we release the evaluation code and the dataset, including model generations, attribute annotations, and harmfulness ratings.

**摘要 (中文)**: [待翻译]

---

## 201. Toward Multi-Database Query Reasoning for Text2Cypher

**arXiv ID**: [2605.10373](https://arxiv.org/abs/2605.10373)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10373)

**作者**: Makbule Gulcin Ozsoy

**分类**: Databases, Computation and Language

**发布时间**: 2026-05-11 11:17:27 UTC

**摘要 (英文)**: Large language models have significantly improved natural language interfaces to databases by translating user questions into executable queries. In particular, Text2Cypher focuses on generating Cypher queries for graph databases, enabling users to access graph data without query language expertise. Most existing Text2Cypher systems assume a single preselected graph database, where queries are generated over a known schema. However, real-world systems are often distributed across multiple independent graph databases organized by domain or system boundaries, where relevant information may span multiple sources. To address this limitation, we propose a shift from single-database query generation to multi-database query reasoning. Instead of assuming a fixed execution context, the system must reason about (i) relevant databases, (ii) how to decompose a question across them, and (iii) how to integrate partial results. We formalize this setting through a three-phase roadmap: database routing, multi-database decomposition, and heterogeneous query reasoning across database types and query languages. This work provides a structured formulation of multi-database reasoning for Text2Cypher and identifies challenges in source selection, query decomposition, and result integration, aiming to support more realistic and scalable natural language interfaces to graph databases.

**摘要 (中文)**: [待翻译]

---

## 202. How Mobile World Model Guides GUI Agents?

**arXiv ID**: [2605.10347](https://arxiv.org/abs/2605.10347)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10347)

**作者**: Weikai Xu, Kun Huang, Yunren Feng, Jiaxing Li, Yuhan Chen 等 (共13人)

**分类**: Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-11 10:49:31 UTC

**摘要 (英文)**: Recent advances in vision-language models have enabled mobile GUI agents to perceive visual interfaces and execute user instructions, but reliable prediction of action consequences remains critical for long-horizon and high-risk interactions. Existing mobile world models provide either text-based or image-based future states, yet it remains unclear which representation is useful, whether generated rollouts can replace real environments, and how test-time guidance helps agents of different strengths. To answer the above questions, we filter and annotate mobile world-model data, then train world models across four modalities: delta text, full text, diffusion-based images, and renderable code. These models achieve SoTA performance on both MobileWorldBench and Code2WorldBench. Furthermore, by evaluating their downstream utility on AITZ, AndroidControl, and AndroidWorld, we obtain three findings. First, renderable code reconstruction achieves high in-distribution fidelity and provides effective multimodal supervision for data construction, while text-based feedback is more robust for online out-of-distribution (OOD) execution. Second, world-model-generated trajectories can provide transferable interaction experience in the training process and improve agents' end-to-end task performance, although these data do not preserve the original distribution. Last, for overconfident mobile agents with low action entropy, posterior self-reflection provides limited gains, suggesting that world models are more effective as prior perception or training supervision than as universal post-hoc verifiers.

**摘要 (中文)**: [待翻译]

---

## 203. PowerStep: Memory-Efficient Adaptive Optimization via $\ell_p$-Norm Steepest Descent

**arXiv ID**: [2605.10335](https://arxiv.org/abs/2605.10335)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10335)

**作者**: Yao Lu, Dengdong Fan, Shixun Zhang, Yonghong Tian

**分类**: Machine Learning, Artificial Intelligence, Computation and Language, Numerical Analysis, Optimization and Control

**发布时间**: 2026-05-11 10:36:27 UTC

**摘要 (英文)**: Adaptive optimizers, most notably Adam, have become the default standard for training large-scale neural networks such as Transformers. These methods maintain running estimates of gradient first and second moments, incurring substantial memory overhead. We introduce PowerStep, a memory-efficient optimizer that achieves coordinate-wise adaptivity without storing second-moment statistics. Motivated by steepest descent under an $\ell_p$-norm geometry, we show that applying a nonlinear transform directly to a momentum buffer yields coordinate-wise adaptivity. We prove that PowerStep converges at the optimal $O(1/\sqrt{T})$ rate for non-convex stochastic optimization. Extensive experiments on Transformer models ranging from 124M to 235B parameters demonstrate that PowerStep matches Adam's convergence speed while halving optimizer memory. Furthermore, when combined with aggressive \texttt{int8} quantization, PowerStep remains numerically stable and reduces optimizer memory by $\sim\!8\times$ compared to full-precision Adam. PowerStep thus provides a principled, scalable and resource-efficient alternative for large-scale training. Code is available at https://github.com/yaolubrain/PowerStep.

**摘要 (中文)**: [待翻译]

---

## 204. Task-Aware Calibration: Provably Optimal Decoding in LLMs

**arXiv ID**: [2605.10202](https://arxiv.org/abs/2605.10202)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10202)

**作者**: Tim Tomov, Dominik Fuchsgruber, Rajeev Verma, Stephan Günnemann

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-11 08:48:04 UTC

**摘要 (英文)**: LLM decoding often relies on the model's predictive distribution to generate an output. Consequently, misalignment with respect to the true generating distribution leads to suboptimal decisions in practice. While a natural solution is to calibrate the model's output distribution, for LLMs, this is ill-posed at the combinatorially vast level of free-form language. We address this by building on the insight that in many tasks, these free-form outputs can be interpreted in a semantically meaningful latent structure, for example, discrete class labels, integers, or sets. We introduce task calibration as a paradigm to calibrate the model's predictive distribution in the task-induced latent space. We apply a decision-theoretic result to show that Minimum Bayes Risk (MBR) decoding on the task-calibrated latent distribution is the optimal decoding strategy on latent model beliefs. Empirically, it consistently improves generation quality across different tasks and baselines. We also introduce Task Calibration Error (TCE), an application-aware calibration metric that quantifies the excess loss due to miscalibration. Our work demonstrates that task calibration enables more reliable model decisions across various tasks and applications.

**摘要 (中文)**: [待翻译]

---

## 205. V-ABS: Action-Observer Driven Beam Search for Dynamic Visual Reasoning

**arXiv ID**: [2605.10172](https://arxiv.org/abs/2605.10172)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10172)

**作者**: Zhiwei Ning, Xuanang Gao, Jiaxi Cao, Gengming Zhang, Shengnan Ma 等 (共9人)

**分类**: Computer Vision and Pattern Recognition, Computation and Language

**发布时间**: 2026-05-11 08:21:52 UTC

**摘要 (英文)**: Multimodal large language models (MLLMs) have achieved remarkable success in general perception, yet complex multi-step visual reasoning remains a persistent challenge. Although recent agentic approaches incorporate tool use, they often neglect critical execution feedback. Consequently, they suffer from the imagination-action-observer (IAO) bias, a misalignment between prior imagination and observer feedback that undermines reasoning stability and optimality. To bridge this gap, we introduce V-ABS, an action-observer driven beam search framework that enables deliberate reasoning through thinker-actor-observer iterations. We also propose an entropy-based adaptive weighting algorithm to mitigate the IAO bias by dynamically balancing the confidence scores between the policy priors and the observational feedback. Moreover, we construct a large-scale supervised fine-tuning (SFT) dataset comprising over 80k samples to guide the model to assign higher prior confidence to correct action paths. Extensive experiments across eight diverse benchmarks show that V-ABS achieves state-of-the-art performance, delivering an average improvement of 19.7% on the Qwen3-VL-8B baseline and consistent gains across both open-source and proprietary models.

**摘要 (中文)**: [待翻译]

---

## 206. MolSight: Molecular Property Prediction with Images

**arXiv ID**: [2605.10157](https://arxiv.org/abs/2605.10157)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10157)

**作者**: Aaditya Baranwal, Akshaj Gupta, Shruti Vyas, Yogesh S Rawat

**分类**: Computer Vision and Pattern Recognition, Computation and Language

**发布时间**: 2026-05-11 08:05:18 UTC

**摘要 (英文)**: Every molecule ever synthesised can be drawn as a 2D skeletal diagram, yet in modern property prediction this universally available representation has received less focus in favour of molecular graphs, 3D conformers, or billion-parameter language models, each imposing its own computational and data-engineering overhead. We present $\textbf{MolSight}$, the first systematic large-scale study of vision-based Molecular Property Prediction (MPP). Using 10 vision architectures, 7 pre-training strategies, and $2\,M$ molecule images, we evaluate performance across 10 downstream tasks spanning physical-property regression, drug-discovery classification, and quantum-chemistry prediction. To account for the wide variation in structural complexity across pre-training molecules, we further propose a $\textbf{chemistry-informed curriculum}$: five structural complexity descriptors partition the corpus into five tiers of increasing chemical difficulty, consistently outperforming non-curriculum baselines. We show that a single rendered bond-line image, processed by a vision encoder, is sufficient for competitive molecular property prediction, i.e. $\textit{chemical insight from sight alone}$. The best curriculum-trained configuration achieves the top result on $\textbf{5 of 10}$ benchmarks and top two on $\textbf{all 10}$, at $\textbf{$\textit{80$\times$ lower}$}$ FLOPs than the nearest multi-modal competitor.

**摘要 (中文)**: [待翻译]

---

## 207. Instruction Adherence in Coding Agent Configuration Files: A Factorial Study of Four File-Structure Variables

**arXiv ID**: [2605.10039](https://arxiv.org/abs/2605.10039)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.10039)

**作者**: Damon McMillan

**分类**: Software Engineering, Computation and Language

**发布时间**: 2026-05-11 06:09:47 UTC

**摘要 (英文)**: Frontier coding agents read configuration files (CLAUDE.md, AGENTS.md, Cursor Rules) at session start and are expected to follow the conventions inside them. Practitioners assume that structural choices (file size, instruction position, file architecture, contradictions in adjacent files) measurably affect adherence. We report a systematic factorial study of these choices using four manipulated variables, measuring compliance with a trivial target annotation across 1,650 Claude Code CLI sessions (16,050 function-level observations) on two TypeScript codebases, three frontier models (primarily Sonnet 4.6, with Opus 4.6 as a CLI-matched cross-model check and Opus 4.7 reported descriptively under a CLI-version confound), and five coding tasks. We use mixed-effects models with a Bayesian companion. None of the four structural variables or three two-way interactions produces a detectable contrast after multiple-testing correction. Size and conflict nulls are supported by affirmative-null Bayes factors (BF10 between 0.05 and 0.10); position and architecture nulls are failures to reject without Bayes-factor support. The largest effect we measured is within-session: each additional function the agent generates is associated with approximately 5.6% lower odds of compliance per step (OR = 0.944) within the session-length range we tested, though the relationship is non-monotonic rather than a constant per-step effect. This reproduces on a second TypeScript codebase and on Opus 4.6 at matched configuration; it was identified during analysis rather than pre-specified. Within the conditions tested, file-structure variables did not produce detectable contrasts; compliance varies systematically between coding tasks and across each session's sequence of generated functions.

**摘要 (中文)**: [待翻译]

---

## 208. Federated Language Models Under Bandwidth Budgets: Distillation Rates and Conformal Coverage

**arXiv ID**: [2605.09986](https://arxiv.org/abs/2605.09986)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09986)

**作者**: Prasanjit Dubey, Xiaoming Huo

**分类**: Machine Learning, Computation and Language, Machine Learning

**发布时间**: 2026-05-11 05:01:43 UTC

**摘要 (英文)**: Training a language model on data scattered across bandwidth-limited nodes that cannot be centralized is a setting that arises in clinical networks, enterprise knowledge bases, and scientific consortia. We study the regime in which data must remain distributed across nodes, and ask what statistical guarantees are in principle achievable under explicit bandwidth budgets; we aim to characterize what is provably possible, not to demonstrate a deployment-ready system. Existing theory treats either training-time consistency or inference-time calibration in isolation, and none makes bandwidth a first-class statistical parameter. We analyze two protocols, Federated Probe-Logit Distillation (FPLD) for training and Federated Conformal RAG (FC-RAG) for inference, as the analytical vehicles for our results. Our first main result is an explicit high-probability KL-consistency rate for FPLD with simultaneous dependence on node count $K$, per-node sample size $n$, quantization budget $B$, probe-set size $m$, and vocabulary size $V$; bandwidth enters only through an exponentially vanishing quantization term. Our second main result is a distribution-free marginal-coverage bound for FC-RAG, whose novel retrieval-bandwidth slack $Δ_{\mathrm{RAG}} = f_{\max}\sqrt{K^{-2}\sum_i v(B_i)}$ makes per-node retrieval bandwidth a first-class statistical parameter, with arithmetic aggregation across $K$ nodes shrinking the slack as $K^{-1/2}$ in the per-node-uniform regime. A Pinsker-type corollary composes the two bounds into an end-to-end coverage guarantee. Synthetic experiments verify the predicted scaling along the bounds' parameters; small-scale experiments on a GPT-2 testbed illustrate that the qualitative bandwidth-accuracy tradeoff survives on a real language model. A deployment-scale empirical evaluation is out of scope.

**摘要 (中文)**: [待翻译]

---

## 209. The Truth Lies Somewhere in the Middle (of the Generated Tokens)

**arXiv ID**: [2605.09969](https://arxiv.org/abs/2605.09969)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09969)

**作者**: Sophie L. Wang, Phillip Isola, Brian Cheung

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-11 04:20:04 UTC

**摘要 (英文)**: How should hidden states generated autoregressively be collapsed into a representation that reflects a language model's internal state? Despite tokens being generated under causal masking, we find that mean pooling across their hidden states yields more semantic representations than any individual token alone. We quantify this through kernel alignment to reference spaces in language, vision, and protein domains. The improvement through mean pooling is consistent with information being distributed across generated tokens rather than localized to a single position. Furthermore, representations derived from generated tokens outperform those from prompt tokens, and alignment across generation reveals interpretable dynamics in model behavior.

**摘要 (中文)**: [待翻译]

---

## 210. G-Zero: Self-Play for Open-Ended Generation from Zero Data

**arXiv ID**: [2605.09959](https://arxiv.org/abs/2605.09959)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09959)

**作者**: Chengsong Huang, Haolin Liu, Tong Zheng, Runpeng Dai, Langlin Huang 等 (共10人)

**分类**: Machine Learning, Artificial Intelligence, Computation and Language, Emerging Technologies

**发布时间**: 2026-05-11 04:12:34 UTC

**摘要 (英文)**: Self-evolving LLMs excel in verifiable domains but struggle in open-ended tasks, where reliance on proxy LLM judges introduces capability bottlenecks and reward hacking. To overcome this, we introduce G-Zero, a verifier-free, co-evolutionary framework for autonomous self-improvement. Our core innovation is Hint-$δ$, an intrinsic reward that quantifies the predictive shift between a Generator model's unassisted response and its response conditioned on a self-generated hint. Using this signal, a Proposer model is trained via GRPO to continuously target the Generator's blind spots by synthesizing challenging queries and informative hints. The Generator is concurrently optimized via DPO to internalize these hint-guided improvements. Theoretically, we prove a best-iterate suboptimality guarantee for an idealized standard-DPO version of G-Zero, provided that the Proposer induces sufficient exploration coverage and the data filteration keeps pseudo-label score noise low. By deriving supervision entirely from internal distributional dynamics, G-Zero bypasses the capability ceilings of external judges, providing a scalable, robust pathway for continuous LLM self-evolution across unverifiable domains.

**摘要 (中文)**: [待翻译]

---

## 211. The Gordian Knot for VLMs: Diagrammatic Knot Reasoning as a Hard Benchmark

**arXiv ID**: [2605.09900](https://arxiv.org/abs/2605.09900)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09900)

**作者**: Hao Liu, Jicheng Liu

**分类**: Artificial Intelligence, Computation and Language, Computer Vision and Pattern Recognition

**发布时间**: 2026-05-11 02:44:30 UTC

**摘要 (英文)**: A vision-language model can look at a knot diagram and report what it sees, yet fail to act on that structure. KnotBench pairs an 858,318-image corpus from 1,951 prime-knot prototypes (crossing numbers 3 to 19) with a protocol whose answers are checked against Regina's canonical knot signature. Its 14 tasks span four families, equivalence judgment, move prediction, identification, and cross-modal grounding; an image-versus-symbol split locates failures along the perception-operation gap. We score Claude Opus 4.7 and GPT-5, each with and without thinking, under a 64K output-token budget matched on both vendors. Across 56 (task, model) cases, 15 sit at or below a random baseline and 8 of 14 tasks have a best score under 1.5x random. On diagram-to-symbol transcription, no model produces a strictly correct string, and permissive Regina decoding recovers the knot in 0 to 4 of 100 items. Thinking-mode reasoning lifts overall accuracy by 1.65 points for Claude and 9.25 points for GPT-5, narrowing the gap only modestly. Read together, the four families suggest current vision-language models hold features of a diagram but lack apparatus to simulate moves on those features.

**摘要 (中文)**: [待翻译]

---

## 212. Key-Value Means

**arXiv ID**: [2605.09877](https://arxiv.org/abs/2605.09877)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09877)

**作者**: Daniel Goldstein, Eugene Cheah

**分类**: Machine Learning, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-11 02:04:14 UTC

**摘要 (英文)**: We present Key-Value Means ("KVM"), a novel block-recurrence for attention that can accommodate either fixed-size or growing state. Equipping a strong transformer baseline with fixed-size KVM attention layers yields a strong $O(N)$ chunked RNN, while adding only an insignificant number of new parameters. We train a transformer with a growable KVM cache and show it performs competitively on long-context tests with only subquadratic prefill time and sublinear state growth. KVM is implementable with standard operations and without custom kernels, and supports chunk-wise parallelizable training and prefill. It provides many of the benefits of both traditional transformers (expandable context memory, chunk-wise parallelizable training and prefill) and linear RNNs in a single unified package. It can be used on every layer, saving KV-cache memory, and allowing a continuous range of choices of prefill time complexity between $O(N)$ and $O(N^2)$. It can also be implemented in a hybrid solution in tandem with LRNN layers in place of traditional attention, to supplement the LRNN with improved sublinear memory growth context length usage and long context decoding. We release our code at https://github.com/recursal/KVM-paper and trained models at https://huggingface.co/collections/recursal/key-value-means under the Apache 2.0 license.

**摘要 (中文)**: [待翻译]

---

## 213. EgoMemReason: A Memory-Driven Reasoning Benchmark for Long-Horizon Egocentric Video Understanding

**arXiv ID**: [2605.09874](https://arxiv.org/abs/2605.09874)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09874)

**作者**: Ziyang Wang, Yue Zhang, Shoubin Yu, Ce Zhang, Zengqi Zhao 等 (共9人)

**分类**: Computer Vision and Pattern Recognition, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-11 01:59:59 UTC

**摘要 (英文)**: Next-generation visual assistants, such as smart glasses, embodied agents, and always-on life-logging systems, must reason over an entire day or more of continuous visual experience. In ultra-long video settings, relevant information is sparsely distributed across hours or days, making memory a fundamental challenge: models must accumulate information over time, recall prior states, track temporal order, and abstract recurring patterns. However, existing week-long video benchmarks are primarily designed for perception and recognition, such as moment localization or global summarization, rather than reasoning that requires integrating evidence across multiple days. To address this gap, we introduce EgoMemReason, a comprehensive benchmark that systematically evaluates week-long egocentric video understanding through memory-driven reasoning. EgoMemReason evaluates three complementary memory types: entity memory, tracking how object states evolve and change across days; event memory, recalling and ordering activities separated by hours or days; and behavior memory, abstracting recurring patterns from sparse, repeated observations over the whole week period. EgoMemReason comprises 500 questions across three memory types and six core challenges, with an average of 5.1 video segments of evidence per question and 25.9 hours of memory backtracking. We evaluate EgoMemReason on 17 methods across MLLMs and agentic frameworks, revealing that even the best model achieves only 39.6% overall accuracy. Further analysis shows that the three memory types fail for distinct reasons and that performance degrades as evidence spans longer temporal horizons, revealing that long-horizon memory remains far from solved. We believe EgoMemReason establishes a strong foundation for evaluating and advancing long-context, memory-aware multimodal systems.

**摘要 (中文)**: [待翻译]

---

## 214. Nautilus Compass: Black-box Persona Drift Detection for Production LLM Agents

**arXiv ID**: [2605.09863](https://arxiv.org/abs/2605.09863)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09863)

**作者**: Chunxiao Wang

**分类**: Cryptography and Security, Artificial Intelligence, Computation and Language, Information Retrieval, Machine Learning

**发布时间**: 2026-05-11 01:49:17 UTC

**摘要 (英文)**: Production LLM coding agents drift over long sessions: they forget user-specified constraints, slip into mistakes the user already flagged, and confabulate prior agreements. White-box approaches such as persona vectors require model weights and so cannot be applied to closed APIs (Claude, GPT-4) that most users actually interact with. We present Nautilus Compass, a black-box persona drift detector and agent memory layer for production coding agents. The method operates entirely at the prompt-text layer: cosine similarity between user prompts and behavioral anchor texts, aggregated by a weighted top-k mean using BGE-m3 embeddings. Compass is, to our knowledge, the only public agent memory layer (among Mem0, Letta, Cognee, Zep, MemOS, smrti verified May 2026) that does not call an LLM at index time to extract facts or build a graph; raw conversation text is embedded directly. The system ships as a Claude Code plugin, an MCP 2024-11-05 A2A server (Cursor, Cline, Hermes), a CLI, and a REST API on one daemon, with a Merkle-chained audit log for tamper-evident anchor updates. On a held-out test set built from real Claude Code session traces and labeled by an independent LLM judge, Compass reaches ROC AUC 0.83 for drift detection. The embedded retrieval pipeline scores 56.6% on LongMemEval-S v0.8 and 44.4% on EverMemBench-Dynamic (n=500), topping the four published EverMemBench Table 4 baselines. LongMemEval-S 56.6% is ~30 points below recent white-box leaders (90+%); we treat that as the architectural ceiling of the no-extraction design. End-to-end reproduction cost is $3.50 (~14x cheaper than GPT-4o-judged stacks). A paired cross-vendor behavior A/B accompanies these numbers as preliminary system-level evidence. Code, anchors, frozen test data, and audit-log tooling are MIT-licensed at github.com/chunxiaoxx/nautilus-compass.

**摘要 (中文)**: [待翻译]

---

## 215. The Metacognitive Probe: Five Behavioural Calibration Diagnostics for LLMs

**arXiv ID**: [2605.09844](https://arxiv.org/abs/2605.09844)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09844)

**作者**: Rafael C. T. Oliveira

**分类**: Artificial Intelligence, Computation and Language, Machine Learning

**发布时间**: 2026-05-11 00:55:31 UTC

**摘要 (英文)**: The Metacognitive Probe is an exploratory five-task, 15-slot diagnostic that decomposes an LLM's confidence behaviour into five behaviourally-distinct dimensions: confidence calibration (T1-CC), epistemic vigilance (T2-EV), knowledge boundary (T3-KB), calibration range (T4-CR), and reasoning-chain validation (T5-RCV). It is evaluated on N=8 frontier models and N=69 humans. The instrument is motivated by Flavell (1979) and Nelson and Narens (1990) but operates on observable confidence-correctness alignment; it is not a validated cross-species metacognition scale, and the pre-specified human developmental hypothesis was falsified. Composite benchmarks (MMLU, BIG-Bench, HELM, GPQA) ask whether a model produces a correct response. They are silent on whether the model knows when its response is wrong. A model can score 80 on a composite calibration benchmark and still be wildly overconfident in narrow pockets the aggregate cannot surface. The Metacognitive Probe surfaces those pockets. Our headline is a 47-point within-model dissociation in Gemini 2.5 Flash: panel-best within-task calibration (T1-CC = 88; Spearman rho = +0.551, 95% CI [+0.14, +0.80], p = 0.005) and panel-worst cross-task difficulty prediction (T4-CR = 41; sigma_conf = 1.4 across twelve factoids).

**摘要 (中文)**: [待翻译]

---

## 216. Parameter-Efficient Neuroevolution for Diverse LLM Generation: Quality-Diversity Optimization via Prompt Embedding Evolution

**arXiv ID**: [2605.09781](https://arxiv.org/abs/2605.09781)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09781)

**作者**: Dongxin Guo, Jikun Wu, Siu Ming Yiu

**分类**: Neural and Evolutionary Computing, Artificial Intelligence, Computation and Language, Machine Learning

**发布时间**: 2026-05-10 22:00:15 UTC

**摘要 (英文)**: Large Language Models exhibit mode collapse, producing homogeneous outputs that fail to explore valid solution spaces. We present QD-LLM, a framework for parameter-efficient neuroevolution that evolves prompt embeddings, compact neural interfaces (~32K parameters) that steer generation in frozen LLMs (70B+ parameters), within a Quality-Diversity (QD) optimization framework. Our contributions: (1) evolved prompt embeddings via gradient-free optimization enabling behavioral steering without model fine-tuning; (2) hybrid behavior characterization combining semantic and explicit features with formal coverage bounds (Theorem 1) under validated near-independence (NMI $= 0.08 \pm 0.02$); (3) co-evolutionary variation operators including targeted behavioral mutation via finite-difference gradient estimation. On HumanEval (164 problems), MBPP, and creative writing benchmarks, QD-LLM achieves 46.4% higher coverage and 41.4% higher QD-Score than QDAIF ($p<0.001$, 30 runs, Vargha-Delaney $A=0.94$). We demonstrate downstream utility: diverse archives improve test generation (34% more edge cases) and fine-tuning data quality (8.3% accuracy gain). We validate across open-source LLMs (Llama-3-70B, Mistral-Large) with full embedding access, establishing prompt embedding evolution as an effective paradigm bridging neuroevolution and modern LLMs.

**摘要 (中文)**: [待翻译]

---

## 217. Nectar: Neural Estimation of Cached-Token Attention via Regression

**arXiv ID**: [2605.09778](https://arxiv.org/abs/2605.09778)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09778)

**作者**: João Monteiro, Michal Klein, Pierre Ablin, Marco Cuturi

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-10 21:51:36 UTC

**摘要 (英文)**: Evaluating softmax attention over a fixed long context requires reading every cached key-value pair for each new query token. For a given context (a book, a manual, a legal corpus) the attention output is a deterministic function of the query. We propose Nectar, which fits a compact neural network to this function for queries drawn from a task-relevant distribution. Nectar fits two networks per layer and KV-head: a target network that predicts the attention output and a score network that predicts the log-normalizer. The pair plugs into the standard masked self-attention at inference time, replacing the $O(n)$ attention over the cache with a forward pass whose cost does not depend on $n$. Each module carries on the order of $|θ|$ parameters per layer and KV-head, typically much smaller than the $2nd$ KV-cache footprint at the same granularity. We report experiments on models from 1.7B to 8B parameters across five long-context datasets. The approximation error tracks the next-token accuracy gap to full attention, and allocating capacity non-uniformly across layers reduces that gap in our ablation. Beyond this analysis of metrics, we check that the text generations (following a question prompt) of a model equipped with a Nectar module match in semantic content those obtained by giving the same model access to the full cache.

**摘要 (中文)**: [待翻译]

---

## 218. EvoPref: Multi-Objective Evolutionary Optimization Discovers Diverse LLM Alignments Beyond Gradient Descent

**arXiv ID**: [2605.09777](https://arxiv.org/abs/2605.09777)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09777)

**作者**: Dongxin Guo, Jikun Wu, Siu Ming Yiu

**分类**: Neural and Evolutionary Computing, Artificial Intelligence, Computation and Language, Machine Learning

**发布时间**: 2026-05-10 21:50:04 UTC

**摘要 (英文)**: Gradient-based preference optimization methods for large language model (LLM) alignment suffer from preference collapse, converging to narrow behavioral modes while neglecting preference diversity. We introduce EvoPref, a multi-objective evolutionary algorithm that maintains populations of Low-Rank Adaptation (LoRA) adapters optimized across helpfulness, harmlessness, and honesty objectives using Non-dominated Sorting Genetic Algorithm II (NSGA-II) selection with archive-based diversity preservation. Our primary contribution is demonstrating that population-based methods discover substantially more diverse alignments than gradient descent. On standard benchmarks, EvoPref improves preference coverage by 18% (median 82.5% vs. 70.0% for ORPO, $p<0.001$, Wilcoxon, $n=30$) and reduces collapse rates by 47% (11.0% vs. 20.6%, $p<0.001$), while achieving competitive alignment quality (median 75.5% RewardBench vs. 75.0% for ORPO, $p<0.05$). We provide theoretical motivation extending recent multi-objective evolutionary algorithm (MOEA) runtime analysis (Dang et al., 2025) suggesting why archive-based methods escape collapse more effectively than single-trajectory optimization. Comprehensive comparisons against MOEA/D, SMS-EMOA, CMA-ES, and gradient baselines (DPO, IPO, KTO, ORPO) with rigorous statistical testing (Friedman with Holm correction, Vargha-Delaney effect sizes, median with IQR) confirm that multi-objective selection with diversity preservation is essential. This work establishes evolutionary optimization as a principled paradigm for diverse LLM alignment.

**摘要 (中文)**: [待翻译]

---

## 219. Calibrate, Don't Curate: Label-Efficient Estimation from Noisy LLM Judges

**arXiv ID**: [2605.09702](https://arxiv.org/abs/2605.09702)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09702)

**作者**: Yanran Li

**分类**: Methodology, Computation and Language

**发布时间**: 2026-05-10 18:49:58 UTC

**摘要 (英文)**: Multi-judge evaluation is increasingly used to assess LLMs and reward models, and the prevailing heuristic is to curate: keep the most accurate judges and discard weaker ones. We show that this heuristic can reverse when the target is not point accuracy, but calibrated probabilistic evaluation from a labeled calibration set. Holding the aggregation and calibration procedures fixed, we compare accuracy-ranked top-$k$ judge selection with using the full judge panel. Across four labeled pairwise-evaluation benchmarks spanning LLM-as-judge and reward-model settings, the calibrated full panel consistently outperforms accuracy-based selection. On RewardBench2, retaining all judges achieves negative log-likelihood (NLL) of $0.006$ versus $0.013$ under top-5 selection, halving the calibration error. This advantage persists after judge-family deduplication and against stronger same-pipeline subset search. We explain this reversal with oracle analyses showing that the optimal calibrated risk under proper scoring rules cannot increase when additional judge signals are made available, and that even below-chance judges can be useful when their biases are learnable and their signals are non-redundant. The resulting operating principle is simple: in multi-judge evaluation with labeled calibration data, do not discard weak judges by accuracy alone; keep them when they are parseable, non-redundant, and calibratable.

**摘要 (中文)**: [待翻译]

---

## 220. Learning Multi-Indicator Weights for Data Selection: A Joint Task-Model Adaptation Framework with Efficient Proxies

**arXiv ID**: [2605.09665](https://arxiv.org/abs/2605.09665)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09665)

**作者**: Jingze Song, Zihao Chen, Wenqing Chen, Zibin Zheng

**分类**: Machine Learning, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-10 17:30:16 UTC

**摘要 (英文)**: Data selection is a key component of efficient instruction tuning for large language models, as recent work has shown that data quality often matters more than data quantity. Accordingly, prior studies have introduced various multi-dimensional heuristics to evaluate and filter instruction data. However, most existing methods rely on static task-agnostic and model-agnostic weighting schemes, which overlook the varying requirements of specific downstream tasks and the differing pre-existing capabilities of models. In this paper, we propose a framework for learning multi-indicator weights that jointly adapts data selection to both the downstream task and the specific model. Our method identifies optimal weight configurations without full-scale fine-tuning by utilizing in-context learning (ICL) signals on compact tiny-validation sets. These signals serve as efficient performance proxies that ensure high-fidelity evaluation at minimal computational cost. Experiments across multiple benchmarks and model families, including Mistral, Qwen, and Llama, show that the approach achieves performance comparable to or exceeding full-dataset tuning while using only 30\% of the training samples on GSM8K. Furthermore, our analysis reveals a trade-off between semantic diversity and logical complexity in reasoning tasks, highlighting the necessity of joint task-model adaptation.

**摘要 (中文)**: [待翻译]

---

## 221. MemPrivacy: Privacy-Preserving Personalized Memory Management for Edge-Cloud Agents

**arXiv ID**: [2605.09530](https://arxiv.org/abs/2605.09530)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09530)

**作者**: Yining Chen, Jihao Zhao, Bo Tang, Haofen Wang, Feiyu Xiong 等 (共6人)

**分类**: Cryptography and Security, Computation and Language

**发布时间**: 2026-05-10 13:31:58 UTC

**摘要 (英文)**: As LLM-powered agents are increasingly deployed in edge-cloud environments, personalized memory has become a key enabler of long-term adaptation and user-centric interaction. However, cloud-assisted memory management exposes sensitive user information, while existing privacy protection methods typically rely on aggressive masking that removes task-relevant semantics and consequently degrades memory utility and personalization quality. To address this challenge, We propose MemPrivacy, which identifies privacy-sensitive spans on edge devices, replaces them with semantically structured type-aware placeholders for cloud-side memory processing, and restores the original values locally when needed. By decoupling privacy protection from semantic destruction, MemPrivacy minimizes sensitive data exposure while retaining the information required for effective memory formation and retrieval. We also construct MemPrivacy-Bench for systematic evaluation, a dataset covering 200 users and over 52k privacy instances, and introduce a four-level privacy taxonomy for configurable protection policies. Experiments show that MemPrivacy achieves strong performance in privacy information extraction, substantially surpassing strong general-purpose models such as GPT-5.2 and Gemini-3.1-Pro, while also reducing inference latency. Across multiple widely used memory systems, MemPrivacy limits utility loss to within 1.6%, outperforming baseline masking strategies. Overall, MemPrivacy offers an effective balance between privacy protection and personalized memory utility for edge-cloud agents, enabling secure, practical, and user-transparent deployment.

**摘要 (中文)**: [待翻译]

---

## 222. Through the Lens of Character: Resolving Modality-Role Interference in Multimodal Role-Playing Agent

**arXiv ID**: [2605.09443](https://arxiv.org/abs/2605.09443)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09443)

**作者**: Yihong Tang, Kehai Chen, Xuefeng Bai, Min Zhang

**分类**: Computer Vision and Pattern Recognition, Computation and Language

**发布时间**: 2026-05-10 09:40:43 UTC

**摘要 (英文)**: The advancement of Multimodal Large Language Models (MLLMs) has expanded Role-Playing Agents (RPAs) into visually grounded environments. However, human vision is inherently subjective and identity-driven, whereas existing MLLMs extract objective, character-agnostic features for general tasks. In RPAs, this generic visual noise overpowers fragile character traits, causing Modality-Role Interference (MRI), where agents struggle to integrate visual grounding and character consistency. To address this, we introduce the training-free Character-Aware Visual Intervention (CAVI) framework, enabling agents to perceive the world through the lens of character. CAVI systematically targets MRI: macroscopically, Character-Guided Token Pruning (CTP) restricts the visual receptive field to role-relevant entities; microscopically, Orthogonal Feature Modulation (OFM) projects tokens onto a character-context subspace to extract aligned facts; and during decoding, Modality-Adaptive Role Steering (MARS) dynamically optimizes steering intensity based on visual reliance. Extensive experiments show CAVI effectively alleviates MRI, significantly enhancing character-consistent multimodal interactions.

**摘要 (中文)**: [待翻译]

---

## 223. Let the Target Select for Itself: Data Selection via Target-Aligned Paths

**arXiv ID**: [2605.09404](https://arxiv.org/abs/2605.09404)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09404)

**作者**: Huitao Yang, Hengzhi He, Guang Cheng

**分类**: Machine Learning, Computation and Language, Computer Vision and Pattern Recognition

**发布时间**: 2026-05-10 08:07:09 UTC

**摘要 (英文)**: Targeted data selection aims to identify training samples from a large candidate pool that improve performance on a specific downstream task. Many recent methods estimate candidate utility by aggregating local attribution scores along a trajectory induced by the candidate pool. When the pool is heterogeneous, however, this reference trajectory may be misaligned with the dynamics of a target-aligned selected subset, creating what we call reference path bias. We propose an alternative reference path: a validation-induced flow obtained from a short, capacity-limited warmup on the available target validation proxy. Along this path, candidates are scored by a normalized endpoint loss drop, yielding a simple zero-order selection rule that requires no candidate gradients or Hessian approximations. Across controlled logistic, vision, and instruction-tuning experiments, this score is competitive with strong dynamic attribution baselines while substantially reducing warmup and storage cost. Moreover, since the reference trajectory is decoupled from any specific candidate pool, the same compact warmup can be reused across additional pools without recomputing the trajectory.

**摘要 (中文)**: [待翻译]

---

## 224. EduStory: A Unified Framework for Pedagogically-Consistent Multi-Shot STEM Instructional Video Generation

**arXiv ID**: [2605.09378](https://arxiv.org/abs/2605.09378)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09378)

**作者**: Xinyi Wu, Jayant Teotia, Shuai Zhao, Erik Cambria

**分类**: Computer Vision and Pattern Recognition, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-10 07:03:37 UTC

**摘要 (英文)**: Long-horizon video generation has advanced in visual quality, yet existing methods still struggle to maintain knowledge consistency and coherent pedagogical narratives across multi-shot instructional videos, especially in STEM domains. To address these challenges, we propose EduStory, a unified framework for reliable instructional video generation. EduStory integrates pedagogical state modeling to track persistent knowledge states, script-guided structured control to organize multi-shot narratives, and learning-oriented evaluation metrics to assess knowledge fidelity and constraint satisfaction. To support rigorous evaluation, we further introduce EduVideoBench, a diagnostic benchmark with multi-granularity annotations, including pedagogical storyboards, shot-level semantics, and knowledge state transitions, together with baseline tasks for controllable instructional video generation. Extensive experiments demonstrate that domain-aware state modeling and structured control substantially reduce narrative breakdown and improve alignment with instructional intent. These results highlight the significance of domain-specific structural constraints and tailored benchmarks for advancing reliable, controllable, and also trustworthy long-horizon video generation.

**摘要 (中文)**: [待翻译]

---

## 225. Position: Avoid Overstretching LLMs for every Enterprise Task

**arXiv ID**: [2605.09365](https://arxiv.org/abs/2605.09365)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09365)

**作者**: Kuldeep Singh, Anson Bastos, Isaiah Onando Mulang'

**分类**: Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-10 06:29:34 UTC

**摘要 (英文)**: Enterprise workloads are dominated by deterministic, structured, and knowledge-dependent tasks operating under strict cost, latency, and reliability constraints. While these are often addressed through large language model (LLM) deployment or distillation into smaller models, we argue this is inefficient, unreliable, and misaligned with enterprise task structures. Instead, AI systems should treat language models as interfaces rather than monolithic engines, externalizing knowledge and computation into dedicated components for greater reliability, scalability, and transparency. Our theoretical evidences show that finite-capacity models cannot fully capture the breadth of knowledge required for enterprise tasks, creating inherent limits to efficiency and interpretability. Building on this, we take the position that language models should primarily be used for structured extraction in deterministic enterprise workflows, while computation and storage are delegated to knowledge bases and symbolic procedures. We formally demonstrate that such modular architectures are more reliable and maintainable than monolithic frameworks, offering a sustainable foundation for enterprise tasks.

**摘要 (中文)**: [待翻译]

---

## 226. Your Simulation Runs but Solves the Wrong Physics: PDE-Grounded Intent Verification for LLM-Generated Multiphysics Simulation Code

**arXiv ID**: [2605.09360](https://arxiv.org/abs/2605.09360)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09360)

**作者**: Zhenghan Song, Yulong Liu, Cheng Wan, Chenjun Li, Lingfu Liu 等 (共7人)

**分类**: Machine Learning, Artificial Intelligence, Computation and Language, Software Engineering

**发布时间**: 2026-05-10 06:19:47 UTC

**摘要 (英文)**: Execution-based evaluation of LLM-generated code implicitly treats successful execution as a proxy for correctness. In scientific simulation, this proxy is insufficient: a generated input file can run, mesh, and converge while encoding governing equations that differ from the user's intent. We call this mismatch between intended physics and generated code the comprehension-generation gap. We instantiate this in MOOSE, where Kernel and BC objects map compositionally to weak-form residual terms, enabling deterministic reconstruction of the encoded PDE and comparison against an intended contract. We formalize this comparison as the Intent Fidelity Score (IFS), a structural metric covering governing terms, BCs, ICs, coefficients, and time scheme. Building on IFS, we develop a PDE-grounded refinement loop that uses deterministic violation reports to correct generated code iteratively. We evaluate on MooseBench, a 220-case multiphysics benchmark with PDE-level ground truth released with this work. On this benchmark, our method consistently improves mean IFS over direct generation, with gains concentrated on hard cases. On the subset where direct generation falls below IFS 0.7, refinement adds +0.22 to +0.41 absolute IFS. In the deployment audit, execution-only repair improves execution success while leaving 39-40% of all 220 cases runnable but still solving the wrong physics across the three main deployment-audit models, exposing executability and intent fidelity as separable failure modes. Static proof-of-concept experiments on four PDE-oriented DSLs (UFL/FEniCS, FreeFEM, FiPy, and Devito) suggest that the reconstruction-and-comparison pattern extends beyond MOOSE. These findings reinforce that executable simulation code should be verified against the mathematical structure it is intended to encode, not accepted on execution alone.

**摘要 (中文)**: [待翻译]

---

## 227. SkillMAS: Skill Co-Evolution with LLM-based Multi-Agent System

**arXiv ID**: [2605.09341](https://arxiv.org/abs/2605.09341)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09341)

**作者**: Shuai Pan, Yixiang Liu, Jiaye Gao, Te Gao, Weiwen Liu 等 (共10人)

**分类**: Multiagent Systems, Computation and Language

**发布时间**: 2026-05-10 05:43:12 UTC

**摘要 (英文)**: Large language model (LLM) agent systems are increasingly expected to improve after deployment, but existing work often decouples two adaptation targets: skill evolution and multi-agent system (MAS) restructuring. This separation can create organization bottlenecks, context pressure, and mis-specialization. We present SkillMAS, a non-parametric framework for adaptive specialization in multi-agent systems that couples skill evolution with MAS restructuring. SkillMAS uses Utility Learning to assign credit from verified execution traces, bounded skill evolution to refine reusable procedures without unfiltered library growth, and evidence-gated MAS restructuring when retained failures and Executor Utility indicate a structural mismatch. Across embodied manipulation, command-line execution, and retail workflows, SkillMAS is competitive under the reported harnesses while clarifying how post-deployment specialization is attributed, updated, and applied.

**摘要 (中文)**: [待翻译]

---

## 228. Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation

**arXiv ID**: [2605.09315](https://arxiv.org/abs/2605.09315)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09315)

**作者**: Ye Yu, Xiaopeng Yuan, Haibo Jin, Heming Liu, Yaoning Yu 等 (共6人)

**分类**: Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-10 04:20:24 UTC

**摘要 (英文)**: Recent advances in LLM agents enable systems that autonomously refine workflows, accumulate reusable skills, self-train their underlying models, and maintain persistent memory. However, we show that such self-evolution is often non-monotonic: adapting to new task distributions can progressively degrade previously acquired capabilities across all major evolution channels. We identify this phenomenon as \emph{capability erosion under self-evolution} and show that it consistently emerges across workflow, skill, model, and memory evolution. To mitigate this issue, we propose \emph{Capability-Preserving Evolution} (CPE), a general stabilization principle that constrains destructive capability drift during continual adaptation. Across all four evolution dimensions, CPE consistently improves retained capability stability while preserving adaptation performance. For example, in workflow evolution, CPE improves retained simple-task performance from 41.8\% to 52.8\% under GPT-5.1 optimization while simultaneously achieving stronger complex-task adaptation. Our findings suggest that stable long-horizon self-evolving agents require not only acquiring new capabilities, but also explicitly preserving previously learned ones during continual adaptation.

**摘要 (中文)**: [待翻译]

---

## 229. A Prompt-Aware Structuring Framework for Reliable Reuse of AI-Generated Content in the Agentic Web

**arXiv ID**: [2605.09283](https://arxiv.org/abs/2605.09283)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09283)

**作者**: Shusaku Egami, Masahiro Hamasaki

**分类**: Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-10 03:16:33 UTC

**摘要 (英文)**: The evolution of Large Language Models (LLMs) and the software agents built on them (AI agents) marks a turning point in the transition from a human-centric Web to an ``Agentic Web'' driven by AI agents. However, for AI-Generated Content (AIGC), which is expected to dominate the Web, there is currently no mechanism for agents to verify its reliability, reproducibility, or license compliance during generation. This lack of transparency risks causing chained hallucinations and compliance violations through the reuse of AIGC. Consequently, a framework to manage the provenance and generation conditions of AIGC is essential. In this paper, we present a framework that automatically attaches structured metadata to AIGC at generation time, including modularized prompts, contexts, thoughts, model information, hyperparameters, and confidence. The metadata is enveloped together with verifiable credentials to support the reliable assessment and reuse of AIGC. This framework enables efficient curation of structured AIGC and facilitates its safe use for applications such as fine-tuning and knowledge distillation.

**摘要 (中文)**: [待翻译]

---

## 230. Towards Conversational Medical AI with Eyes, Ears and a Voice

**arXiv ID**: [2605.09272](https://arxiv.org/abs/2605.09272)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09272)

**作者**: Meet Shah, Jason Gusdorf, Anil Palepu, Chunjong Park, Jack W. O'Sullivan 等 (共53人)

**分类**: Artificial Intelligence, Computation and Language, Computer Vision and Pattern Recognition

**发布时间**: 2026-05-10 02:43:49 UTC

**摘要 (英文)**: The practice of medicine relies not only upon skillful dialogue but also on the nuanced exchange and interpretation of rich auditory and visual cues between doctors and patients. Building on the low-latency voice and video processing capabilities of Gemini, we introduce AI co-clinician, a first-of-its-kind conversational AI system utilizing continuous streams of audio-visual data from live patient conversations to inform real-time clinical decisions. Its dual-agent architecture balances deep clinical reasoning with the low latency required for natural dialogue. To assess this system, we implemented a video-based interface emulating telemedicine consultations. We crafted 20 standardized outpatient scenarios requiring proactive real-time auditory and visual reasoning and designed "TelePACES" evaluation criteria alongside case-specific rubrics. In a randomized, interface-blinded, crossover simulation study (n = 120 encounters) with 10 internal medicine residents as patient actors, we compared AI co-clinician with primary care physicians (PCPs), GPT-Realtime, and a baseline agent. AI co-clinician approached PCPs in key TelePACES dimensions, including management plans and differential diagnosis, while significantly outperforming GPT-Realtime across all general criteria. While our agent demonstrated parity with PCPs in case-specific triage measures, physicians maintained superior overall performance in case-specific assessments. Although AI co-clinician marks a significant advance in real-time telemedical AI, gaps remain in physical examination and disease-specific reasoning. Our work shows that text-only approaches fail to capture the true challenges of medical consultation and suggests that high-stakes real-time diagnostic AI is most safely advanced in collaborative, triadic models where AI can be a supportive co-clinician for doctors and patients.

**摘要 (中文)**: [待翻译]

---

## 231. Reinforcing Multimodal Reasoning Against Visual Degradation

**arXiv ID**: [2605.09262](https://arxiv.org/abs/2605.09262)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09262)

**作者**: Rui Liu, Dian Yu, Haolin Liu, Yucheng Shi, Tong Zheng 等 (共9人)

**分类**: Computer Vision and Pattern Recognition, Computation and Language

**发布时间**: 2026-05-10 02:17:14 UTC

**摘要 (英文)**: Reinforcement Learning has significantly advanced the reasoning capabilities of Multimodal Large Language Models (MLLMs), yet the resulting policies remain brittle against real-world visual degradations such as blur, compression artifacts, and low-resolution scans. Prior robustness techniques from vision and deep RL rely on static data augmentation or value-based regularization, neither of which transfers cleanly to critic-free RL fine-tuning of autoregressive MLLMs. Reinforcing reasoning against such corruptions is non-trivial: naively injecting degraded views during rollout induces reward poisoning, where perceptual occlusions trigger hallucinated trajectories and destabilize optimization. We propose ROMA, an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance. A dual-forward-pass strategy uses teacher forcing to evaluate corrupted views against clean-image trajectories, avoiding new rollouts on degraded inputs. For distributional consistency, we apply a token-level surrogate KL penalty against the worst-case augmentation; to prevent policy collapse under regularization, an auxiliary policy gradient loss anchored to clean-image advantages preserves a reliable reward signal; and to avoid systematically incorrect invariance, correctness-conditioned regularization restricts enforcement to successful trajectories. On Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, our method improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy.

**摘要 (中文)**: [待翻译]

---

## 232. Emergent Semantic Role Understanding in Language Models

**arXiv ID**: [2605.09187](https://arxiv.org/abs/2605.09187)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09187)

**作者**: Carla Griffiths, Mirco Musolesi

**分类**: Artificial Intelligence, Computation and Language, Machine Learning

**发布时间**: 2026-05-09 22:01:36 UTC

**摘要 (英文)**: Understanding how linguistic structure emerges in language models is central to interpreting what these systems learn from data and how much supervision they truly require. In particular, semantic role understanding ("who did what to whom") is a core component of meaning representation, yet it remains unclear whether it arises from pre-training alone or depends on task-specific fine-tuning. We study whether semantic role understanding emerges during language model pre-training or requires task-specific fine-tuning. We freeze decoder-only transformers and train linear probes to extract semantic roles, using performance to infer whether role information is already encoded in pre-training or learned during adaptation. Across model scales, we find that frozen representations contain substantial semantic role information, with performance improving but not fully matching fine-tuned models. This indicates partial but incomplete emergence from pre-training alone. We show that semantic role structure emerges from language modeling objectives, but its internal implementation shifts toward more distributed representations as model scale increases.

**摘要 (中文)**: [待翻译]

---

## 233. Agentic MIP Research: Accelerated Constraint Handler Generation

**arXiv ID**: [2605.09186](https://arxiv.org/abs/2605.09186)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09186)

**作者**: Liding Xu, Yugeng Zhou, Sebastian Pokutta

**分类**: Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-09 21:53:28 UTC

**摘要 (英文)**: Mixed-integer programming (MIP) research is both mathematically sophisticated and engineering-intensive: testing an algorithmic hypothesis within a branch-and-cut solver requires substantial implementation, debugging, tuning, and large-scale benchmarking. We propose an agentic MIP research framework that shortens this feedback loop by embedding LLM agents into a solver-aware harness for generating, verifying, and evaluating plugins for the open-source solver SCIP. Propagation methods play a central role in accelerating MIP solving by exploiting global constraints. We instantiate our framework on the semantic lifting of MIP formulations into global constraints and the automatic construction of propagation-only SCIP constraint handlers. On the MIPLIB 2017 benchmark set, the framework successfully recovers global constraint structures from constraint programming and generates executable constraint detectors and propagation-only constraint handlers. Furthermore, the framework naturally extends to in-context learning within a sandboxed environment, enabling agents not only to tune and debug generated constraint handlers on real instances, but also to explore global constraint patterns in MIP problems and discover novel propagation strategies not yet implemented in SCIP. This framework allows us to systematically distinguish meaningful algorithmic improvements from low-value or overly costly candidates: the novel propagation methods successfully solved five additional instances within the explored benchmark. Overall, this framework demonstrates that LLM agents can autonomously navigate the complex MIP research loop, paving the way for a more automated solver development process.

**摘要 (中文)**: [待翻译]

---

## 234. Open Ontologies: Tool-Augmented Ontology Engineering with Stable Matching Alignment

**arXiv ID**: [2605.09184](https://arxiv.org/abs/2605.09184)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09184)

**作者**: Fabio Rovai

**分类**: Artificial Intelligence, Computation and Language, Databases

**发布时间**: 2026-05-09 21:49:21 UTC

**摘要 (英文)**: We present Open Ontologies, an open-source ontology engineering system implemented in Rust that integrates LLM-driven construction with formal OWL reasoning and ontology alignment via the Model Context Protocol. Our primary finding is that stable 1-to-1 matching is the dominant factor in ontology alignment quality: on the OAEI Anatomy track, it achieves F1 = 0.832 (P = 0.963, R = 0.733), competitive with state-of-the-art systems and exceeding all in precision. Ablation across five weight configurations shows that signal weights are irrelevant when stable matching is applied (F1 varies by less than 0.004), while removing stable matching drops F1 to 0.728. On the Conference track, the same method achieves F1 = 0.438. On tool-augmented ontology interaction, we find a surprising result: an LLM reading a raw OWL file (F1 = 0.323) performs worse than the same LLM with no file at all (F1 = 0.431), while structured MCP tool access achieves F1 = 0.717. This demonstrates that tool structure provides a qualitatively different mode of access that the LLM cannot replicate by reading raw syntax. The system ships as a single binary under the MIT licence.

**摘要 (中文)**: [待翻译]

---

## 235. Sparse Layers are Critical to Scaling Looped Language Models

**arXiv ID**: [2605.09165](https://arxiv.org/abs/2605.09165)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09165)

**作者**: Ryan Lee, Jacob Biloki, Edward J. Hu, Jonathan May

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-09 20:58:18 UTC

**摘要 (英文)**: Looped language models repeat a set of transformer layers through depth, reducing memory costs and providing natural early-exit points at loop boundaries. However, looped models do not scale as favorably as standard transformers with unique layers. We compare standard and Mixture-of-Experts (MoE) transformers, with and without looping, and find two main results. First, we find Looped-MoE models scale better than the standard baseline while dense looped models do not. We trace this to routing divergence between loops: in Looped-MoE models, different experts are activated on each pass through the same shared layers, recovering expressivity without additional parameters. Our second finding is that looped models have better compute-quality trade-offs with early exits than standard models. Because each loop ends with the same layers that produce the final output, loop boundaries are superior exit points, as confirmed by earlier output convergence at these points. In sum, we provide a clear direction for scaling looped models: a Looped-MoE model with early exits can not only beat standard transformers at scale, but also enable significant memory and inference savings with minimal degradation in quality.

**摘要 (中文)**: [待翻译]

---

## 236. A Communication-Theoretic Framework for LLM Agents: Cost-Aware Adaptive Reliability

**arXiv ID**: [2605.09121](https://arxiv.org/abs/2605.09121)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09121)

**作者**: Hamed Omidvar, Vahideh Akhlaghi

**分类**: Machine Learning, Artificial Intelligence, Computation and Language, Information Theory

**发布时间**: 2026-05-09 19:14:33 UTC

**摘要 (英文)**: Agents built on large language models (LLMs) rely on a range of reliability techniques, including retry, majority voting, and self-consistency, that have been developed in parallel rather than within a common analytical framework. We observe that an LLM sampled at temperature $T$ is a discrete stochastic channel $p(y \mid x)$ in the sense of Shannon's coding theory, and use this identity as the entry point for such a framework grounded in communication theory. Each of these techniques is a special case of one of six classical reliability operators: diversity combining, hybrid retransmission, iterative generator-critic decoding, rateless sampling, structured redundant verification, and difficulty-adaptive routing. Within the framework we give two closed-form results: a noise-variance threshold above which uniform averaging beats quality-weighted averaging, and a contractivity criterion for generator-critic refinement, consistent with a contractive-to-divergent transition we observe between 3B- and 14B-parameter models. We further introduce a cost-aware semantic-nearest-neighbor router whose single Lagrangian knob traverses the quality-cost frontier without retraining. Across six channel configurations spanning local and cloud models on 69 hard tasks, no fixed model-technique-budget choice dominates, motivating per-task allocation. On a 300-item hard split of MMLU, GSM8K, and HumanEval, our router occupies the full empirical Pareto frontier: at matched quality, its normalized cost is ${\approx}56$\% lower than the strongest fixed technique; at matched normalized cost, it improves quality by ${\approx}7$\% ($26$\% over single-shot decoding). These results argue for consolidating these reliability techniques into a single tunable layer informed by channel coding.

**摘要 (中文)**: [待翻译]

---

## 237. Personalized Alignment Revisited: The Necessity and Sufficiency of User Diversity

**arXiv ID**: [2605.09119](https://arxiv.org/abs/2605.09119)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09119)

**作者**: Enoch Hyunwook Kang

**分类**: Machine Learning, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-09 19:07:35 UTC

**摘要 (英文)**: Personalized alignment aims to adapt large language models to heterogeneous user preferences, yet the precise theoretical conditions for its statistical efficiency have not been formally established. This paper characterizes the conditions under which personalized alignment achieves O(1) online regret and log(1/epsilon) offline sample complexity. We show that these optimal rates depend on a specific user-diversity condition: the population of user-specific heads must span the latent reward directions that can alter the optimal response. We prove that this condition is both necessary and sufficient. When it holds, simple greedy algorithms achieve benchmark efficiency; when it fails, every learner in a natural admissible class incurs at least logarithmic regret. Our results identify user diversity as the fundamental driver of personalized identifiability.

**摘要 (中文)**: [待翻译]

---

## 238. Relative Kinetic Utility for Reasoning-Aware Structural Pruning in Large Language Models

**arXiv ID**: [2605.09008](https://arxiv.org/abs/2605.09008)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.09008)

**作者**: Tianhao Qian

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-09 15:47:53 UTC

**摘要 (英文)**: Chain-of-Thought (CoT) prompting symbolized a huge improvement of reasoning capabilities of Large Language Models (LLMs). However, scaling up test-time computation yields extensive CoT sequences, introducing severe inference latency and key-value (KV) cache memory bottlenecks. While structural pruning offers a fundamental, hardware-aware solution to alleviate static parameter burdens, existing magnitude-based methods may cut off the neurons of CoT: by over-indexing on discrete cross-entropy objectives, these heuristics fall into a \textit{magnitude trap}: they prioritize high-frequency, low-information syntactic tokens and trigger a disappointing reasoning collapse at high sparsities (e.g., 40\%). To overcome this topological phase transition, we propose \textsc{Relative Kinetic Utility} (RKU), a novel theoretical framework that elevates discrete pruning to a continuous kinetic integral over the depth manifold of the model based on Alternating Gradient Flow(AGF). By modifying it with Fisher trace normalization, RKU acts as a lightweight curvature-aware normalization to isolate \textit{kinetic spikes} -- the fundamental structural pathways responsible for high-curvature logical routing. Extensive experiments on Qwen-2.5-7B and LLaMA-3-8B improves performance in the high-sparsity regime around 40\%. RKU attains 13.34\% accuracy on GSM8K at 40\% sparsity, outperforming the strongest baseline, and appears to better preserve reasoning-relevant representations under out-of-distribution evaluation.

**摘要 (中文)**: [待翻译]

---

## 239. Non-Monotonic Latency in Apple MPS Decoding: KV Cache Interactions and Execution Regimes

**arXiv ID**: [2605.08913](https://arxiv.org/abs/2605.08913)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08913)

**作者**: Willy Fitra Hendria

**分类**: Machine Learning, Hardware Architecture, Computation and Language, Performance

**发布时间**: 2026-05-09 12:26:36 UTC

**摘要 (英文)**: Autoregressive inference is typically assumed to scale predictably with decoding length, and key-value (KV) caching is widely regarded as a universally beneficial optimization for accelerating decoding. In this work, we identify unexpected non-monotonic latency behavior in the Apple MPS backend, where latency changes abruptly across nearby decoding configurations. Using transformer models from multiple families (GPT-2, BLOOM, and OPT), we observe latency spikes of up to 21x within specific decoding-budget intervals, followed by recovery at neighboring configurations. Controlled experiments show that these anomalies are not explained by memory pressure or prefill cost, but are instead consistent with backend execution dynamics, while CPU and NVIDIA T4 (CUDA) exhibit smooth monotonic scaling under identical conditions. Our findings highlight the importance of hardware-aware evaluation for autoregressive inference and caution against relying on aggregated decoding-budget benchmarks, as performance can vary discontinuously across nearby configurations.

**摘要 (中文)**: [待翻译]

---

## 240. Machine Learning Research Has Outpaced Its Communication Norms and NeurIPS Should Act

**arXiv ID**: [2605.08889](https://arxiv.org/abs/2605.08889)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08889)

**作者**: Ajay Mandyam Rangarajan, Jeyashree Krishnan

**分类**: Machine Learning, Computation and Language, Digital Libraries

**发布时间**: 2026-05-09 11:13:21 UTC

**摘要 (英文)**: Machine learning research has grown exponentially while its communication norms have not. We argue NeurIPS should adopt explicit, measurable writing standards. We analyze 2.8 million arXiv papers (1991-2025), 24,772 NeurIPS papers (1987-2024), and 24.5 million PubMed papers (1990-2025), applying classical readability scores, the Hohmann writing style suite (including sensational language), acronym density and reuse, an LLM as judge readability protocol, and citations from OpenAlex and Semantic Scholar. Four patterns emerge. First, NeurIPS abstracts score harder to read on every classical readability metric: Flesch Reading Ease falls from about 24 in 1987 to 13 in 2024, and sensational language rises by about 50 percent in NeurIPS abstracts between 2015 and 2024. Second, acronym density in NeurIPS titles has grown from 0.33 per 100 words in 1987 to 3.21 in 2024, and about 89 percent of NeurIPS acronyms are used fewer than ten times, ten points above the science-wide baseline. Third, more readable NeurIPS papers tend to receive more citations, suggesting readability and impact are correlated and that less readable papers risk remaining fragmented. LLM as judge scores rate NeurIPS abstracts as roughly stable from 1987 to 2022, with early signs of improvement thereafter, a pattern that disagrees with every classical readability metric and raises a design question for enforcement: is the target reader a human or an LLM? Lastly, NeurIPS volume has grown roughly 50-fold between 1987 and 2024. Assuming the goal is to optimise for human readers, we propose seven standards NeurIPS could pilot at NeurIPS 2027: an acronym budget with a venue-approved term list, a human readability threshold, stricter citation standards, standalone visual elements, a plain language summary, a pre-registered acronym glossary, and open source audit tooling.

**摘要 (中文)**: [待翻译]

---

## 241. Ace-Skill: Bootstrapping Multimodal Agents with Prioritized and Clustered Evolution

**arXiv ID**: [2605.08887](https://arxiv.org/abs/2605.08887)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08887)

**作者**: Feng Xiong, Zengbin Wang, Yong Wang, Xuecai Hu, Jinghan He 等 (共8人)

**分类**: Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-09 11:12:54 UTC

**摘要 (英文)**: Self-evolving agents present a promising path toward continual adaptation by distilling task interactions into reusable knowledge artifacts. In practice, this paradigm remains hindered by two coupled bottlenecks: data inefficiency, where costly rollout effort is disproportionately spent on low-value samples rather than informative ones, and knowledge interference, where heterogeneous knowledge stored in shared repositories leads to noisy retrieval and task-misaligned guidance. Together, these issues form a self-reinforcing failure loop in which uninformative rollouts yield noisy knowledge, which in turn degrades subsequent rollouts. In this work, we introduce Ace-Skill, a co-evolutionary framework that jointly optimizes rollout allocation and knowledge organization for self-evolving multimodal agents. Specifically, Ace-Skill combines aprioritized sampler with lazy-decay proficiency tracking to focus rollouts on informative and insufficiently mastered samples, and a clustered organizer that semantically clusters knowledge for cleaner retrieval and more reliable adaptation. By improving sampling and organization together, Ace-Skill turns self-evolution into a virtuous cycle in which more informative rollouts produce higher-quality knowledge that supports stronger subsequent rollouts. Across four multimodal tool-use benchmarks, Ace-Skill delivers strong gains (e.g., +35.46% relative improvement in Avg@4 accuracy), enabling an opensource 35B MoE model to match or surpass proprietary models. The acquired knowledge also transfers effectively in a zero-shot manner to smaller 9B and 4B models, allowing resource-constrained agents to inherit advanced capabilities without additional training. The code has been publicly available at https://github.com/AMAP-ML/Ace-Skill.

**摘要 (中文)**: [待翻译]

---

## 242. UserGPT Technical Report

**arXiv ID**: [2605.08766](https://arxiv.org/abs/2605.08766)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08766)

**作者**: Yunyi Xuan, Hao Yi, Fengling Mao, Daye Cai, Leikun Liang 等 (共12人)

**分类**: Information Retrieval, Computation and Language

**发布时间**: 2026-05-09 07:51:03 UTC

**摘要 (英文)**: Personalized user understanding from large-scale digital traces remains a fundamental challenge. Traditional user profiling methods rely on discriminative models and manual feature engineering to predict discrete attributes, often producing fragmented and logically inconsistent profiles that generalize poorly to long-tail behaviors. In this work, we study a generative paradigm in which large language models (LLMs) summarize long and noisy behavioral histories into coherent narratives that capture nuanced user evolution. Our experiments show that even strong LLMs remain limited in complex and implicit personalization reasoning. We propose UserGPT, a framework for improving LLM-based persona understanding through both attribute generation and summary generation. To address the scarcity of real-world behavioral data, we develop a User Behavior Simulation Engine that produces realistic and complex user trajectories. We further introduce a Data-Centric Semantization module that transforms heterogeneous behavioral logs into structured and semantically coherent inputs, reducing noise and sparsity. On top of this pipeline, we design a curriculum-driven post-training strategy that combines multi-stage Supervised Fine-Tuning (SFT) with Dual-Filter Group Relative Policy Optimization (DF-GRPO) to strengthen reasoning over long behavioral histories. We also construct HPR-Bench, a benchmark for holistic persona reasoning derived from simulated data. On HPR-Bench, UserGPT achieves an Avg@10 score of 0.7325 on tag prediction and an $Acc_{Ex}$ score of 0.7528 on summary generation, while compressing behavioral records by up to 97.9% with critical information preserved. These results demonstrate the effectiveness of UserGPT for holistic persona reasoning and personalized user-agent interaction.

**摘要 (中文)**: [待翻译]

---

## 243. Communicating Sound Through Natural Language

**arXiv ID**: [2605.08750](https://arxiv.org/abs/2605.08750)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08750)

**作者**: Emanuele Rossi, Emanuele Rodolà

**分类**: Machine Learning, Artificial Intelligence, Computation and Language, Multiagent Systems

**发布时间**: 2026-05-09 07:25:54 UTC

**摘要 (英文)**: Natural language is widely used to describe, prompt, and control audio systems, but rarely serves as the representation carrying audio itself. We introduce lexical acoustic coding (LAC), a framework in which pre-trained LLM sender and receiver agents transmit sound through natural language. Under fixed system prompts, the agents write their own analysis and synthesis code, communicating only through a lexical sentence, shared vocabulary, and optional symbolic music structure. The sender analyzes an input waveform into interpretable, non-learned acoustic descriptors, quantizes each with a feature-specific interval vocabulary, and verbalizes the lexical code as English. The receiver parses the sentence back into lexical-acoustic constraints and renders a waveform through closed-loop refinement. The transmitted text serves as both a rich caption and as the transport representation itself. We frame LAC as a finite-rate lossy quantizer, exposing trade-offs between vocabulary size, rate, and fidelity. Experiments on short sounds and symbolic music transfer show that plain text preserves measurable acoustic structure while remaining interpretable, editable, and native to LLM-mediated communication.

**摘要 (中文)**: [待翻译]

---

## 244. SlimQwen: Exploring the Pruning and Distillation in Large MoE Model Pre-training

**arXiv ID**: [2605.08738](https://arxiv.org/abs/2605.08738)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08738)

**作者**: Shengkun Tang, Zekun Wang, Bo Zheng, Liangyu Wang, Rui Men 等 (共10人)

**分类**: Machine Learning, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-09 06:50:35 UTC

**摘要 (英文)**: Structured pruning and knowledge distillation (KD) are typical techniques for compressing large language models, but it remains unclear how they should be applied at pretraining scale, especially to recent mixture-of-experts (MoE) models. In this work, we systematically study MoE compression in large-scale pretraining, focusing on three key questions: whether pruning provides a better initialization than training from scratch, how expert compression choices affect the final model after continued training, and which training strategy is most effective. We have the following findings: First, across depth, width, and expert compression, pruning a pretrained MoE consistently outperforms training the target architecture from scratch under the same training budget. Second, different one-shot expert compression methods converge to similar final performance after large-scale continual pretraining. Motivated by this, we introduce a simple partial-preservation expert merging strategy that improves downstream performance across most benchmarks. Third, combining KD with the language modeling loss outperforms KD alone, particularly on knowledge-intensive tasks. We further propose multi-token prediction (MTP) distillation, which yields consistent gains. Finally, given the same training tokens, progressive pruning schedules outperform one-shot compression, suggesting that gradual architecture transitions lead to better optimization trajectories. Putting it all together, we compress Qwen3-Next-80A3B to a 23A2B model that retains competitive performance. These results offer practical guidance for efficient MoE compression at scale.

**摘要 (中文)**: [待翻译]

---

## 245. The Extrapolation Cliff in On-Policy Distillation of Near-Deterministic Structured Outputs

**arXiv ID**: [2605.08737](https://arxiv.org/abs/2605.08737)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08737)

**作者**: Xin Li, Hao Jiang, Annan Wang, Yichi Zhang, Chau Yuen

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-09 06:48:00 UTC

**摘要 (英文)**: On-policy distillation (OPD) is widely used for LLM post-training. When pushed with a reward-extrapolation coefficient lambda > 1, the student can lift past the teacher in domain, but past a threshold lambda* the same step violates the output contract on structured-output tasks. In a single-position Bernoulli reduction, we derive a closed-form base-relative clip-safety threshold lambda*(p,b,c) determined by three measurable quantities: the teacher modal probability, the warm-start mass, and the importance-sampling clip strength. Above lambda*, the extrapolated fixed point exits the clip-safe region, changing training from format-preserving to format-collapsing. We extend the rule to calibrated K-ary listwise JSON tasks where a single binding equivalence class dominates the output contract and SFT retains parse headroom. On Amazon Fashion, three pre-registered tests--a fine-grid cliff interval, a budget-extension test, and a small-clip cross-prediction--fall within their locked prediction windows, with the small-clip value matching the closed-form prediction below grid resolution. Operating just below lambda*, ListOPD brings a 1.7B Qwen3 student to in-domain parity with an 8B-SFT baseline at one-fifth the parameters. The gain is driven primarily by format adherence: NDCG@1 on parsed outputs remains flat across lambda, while parse validity sharply changes at the predicted boundary. The cliff diagnostic is rubric-independent, whereas the parity claim uses a Gemini-graded rubric and inherits that evaluator's exposure.

**摘要 (中文)**: [待翻译]

---

## 246. AdaPreLoRA: Adafactor Preconditioned Low-Rank Adaptation

**arXiv ID**: [2605.08734](https://arxiv.org/abs/2605.08734)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08734)

**作者**: Ziyun Liu, Fengmiao Bian, Jian-Feng Cai

**分类**: Machine Learning, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-09 06:37:44 UTC

**摘要 (英文)**: Low-Rank Adaptation (LoRA) reparameterizes a weight update as a product of two low-rank factors, but the Jacobian $J_{G}$ of the generator mapping the factors to the weight matrix is rank-deficient, so the factor-space preconditioner $J_{G}^* {F}_t J_{G}$ induced by any ${W}$-space preconditioner ${F}_t$ is singular, and consequently the standard chain rule cannot be uniquely inverted to map a preconditioned ${W}$-space direction back to a factor-space update. We cast existing LoRA optimizers in a unified framework parameterized by two choices: (i) which invertible surrogate for $J_{G}^* {F}_t J_{G}$ to use, and (ii) which ${F}_t$ on ${W}$ to use. Existing methods occupy four families along these axes: factor-space adaptive updates, block-diagonal surrogates for $J_{G}^* J_{G}$, Frobenius-residual pseudoinverse methods, and Riemannian manifold constraint. Within this design space, a gradient-statistics-aware ${F}_t$ paired with a closed-form factor-space solve at ${O}((m+n)r)$ memory remains underexplored. We propose \textbf{AdaPreLoRA}, which fills this gap by adopting the Adafactor diagonal Kronecker preconditioner ${H}_t$ on ${W}$ and selecting from the resulting factor-space solution family the element minimizing an ${H}_t$-weighted imbalance between the two factor contributions; by construction, the resulting factor update is the closest LoRA approximation to the preconditioned ${W}$-space direction under the ${H}_t$-weighted norm. Across GPT-2 (E2E), Mistral-7B and Qwen2-7B (GLUE, ARC, GSM8K), and diffusion-model personalization, AdaPreLoRA is competitive with or improves over a representative set of LoRA optimizers while keeping peak GPU memory at the LoRA optimizer level.

**摘要 (中文)**: [待翻译]

---

## 247. Bias by Necessity: Impossibility Theorems for Sequential Processing with Convergent AI and Human Validation

**arXiv ID**: [2605.08716](https://arxiv.org/abs/2605.08716)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08716)

**作者**: Jikun Wu, Dongxin Guo, Siu-Ming Yiu

**分类**: Artificial Intelligence, Computation and Language, Machine Learning

**发布时间**: 2026-05-09 05:56:12 UTC

**摘要 (英文)**: Are certain cognitive biases mathematically inevitable consequences of sequential information processing? We prove that primacy effects, anchoring, and order-dependence are architecturally necessary in autoregressive language models due to causal masking constraints. Our three impossibility theorems establish: (1) primacy bias arises from asymmetric attention accumulation; (2) anchoring emerges from sequential conditioning with provable information bounds; and (3) exact debiasing by permutation marginalization requires factorial-time computation, with Monte Carlo approximation feasible at constant per-tolerance overhead. We validate these bounds across 12 frontier LLMs ($R^2 = 0.89$; $Δ$BIC $= 16.6$ vs. next-best alternative). We then derive quantitative predictions from the framework and test them in two pre-registered human experiments ($N = 464$ analyzed). Study 1 confirms anchor position modulates anchoring magnitude ($d = 0.52$, BF$_{10} = 847$). Study 2 shows working memory load amplifies primacy bias ($d = 0.41$, BF$_{10} = 156$), with WM capacity predicting bias reduction ($r = -.38$). These convergent findings reframe cognitive biases as resource-rational responses to sequential processing.

**摘要 (中文)**: [待翻译]

---

## 248. RewardHarness: Self-Evolving Agentic Post-Training

**arXiv ID**: [2605.08703](https://arxiv.org/abs/2605.08703)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08703)

**作者**: Yuxuan Zhang, Penghui Du, Bo Li, Cong Wei, Junwen Miao 等 (共14人)

**分类**: Artificial Intelligence, Computation and Language, Computer Vision and Pattern Recognition, Machine Learning

**发布时间**: 2026-05-09 05:32:48 UTC

**摘要 (英文)**: Evaluating instruction-guided image edits requires rewards that reflect subtle human preferences, yet current reward models typically depend on large-scale preference annotation and additional model training. This creates a data-efficiency gap: humans can often infer the target evaluation criteria from only a few examples, while models are usually trained on hundreds of thousands of comparisons. We present RewardHarness, a self-evolving agentic reward framework that reframes reward modeling as context evolution rather than weight optimization. Instead of learning from large-scale annotations, RewardHarness aligns with human preferences by iteratively evolving a library of tools and skills from as few as 100 preference demonstrations. Given a source image, candidate edited images, and an editing instruction, an Orchestrator selects the most relevant subset of tools and skills from the maintained library, and a frozen Sub-Agent uses them to construct a reasoning chain that produces a preference judgment. By comparing predicted judgments with ground-truth preferences and analyzing successes and failures in the reasoning process, the Orchestrator automatically refines its library of tools and skills without additional human annotation. Using only 0.05% of the EditReward preference data, RewardHarness achieves 47.4% average accuracy on image-editing evaluation benchmarks, surpassing GPT-5 by 5.3 points. When used as a reward signal for GRPO fine-tuning, RL-tuned models achieve 3.52 on ImgEdit-Bench. Project page: https://rewardharness.com.

**摘要 (中文)**: [待翻译]

---

## 249. AAAC: Activation-Aware Adaptive Codebooks for 4-bit LLM Weight Quantization

**arXiv ID**: [2605.08692](https://arxiv.org/abs/2605.08692)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08692)

**作者**: Beshr IslamBouli, David Jin

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-09 04:59:21 UTC

**摘要 (英文)**: Post-training weight-only quantization to 4 bits is widely used to reduce the memory and compute costs of large language model inference. Existing PTQ methods, such as AWQ and GPTQ, improve how weights are mapped onto a fixed 4-bit grid through scaling, clipping, or error compensation. To further improve accuracy, methods such as OmniQuant and QuIP\# uses gradient-assisted algorithms at the cost of hours of quantization time. In this work, we propose AAAC (Activation-Aware Adaptive Codebooks), a lightweight method for 4-bit LLM weight quantization. AAAC replaces the fixed scalar codebook used in standard quantization with two small learned scalar codebooks (64 bytes) per layer. Each group of weights selects the codebook that minimizes activation-weighted reconstruction error, encoding the choice in the unused sign bit of the group's positive scale and adding zero storage overhead. AAAC completes in 3--30 minutes on a single GPU, and adds no memory beyond the model itself. We evaluate against AWQ, GPTQ, IF4, GPTVQ, OmniQuant, SqueezeLLM, and QuIP\# across model families. AAAC outperforms baselines at orders-of-magnitude less quantization time.

**摘要 (中文)**: [待翻译]

---

## 250. MIND-Skill: Quality-Guaranteed Skill Generation via Multi-Agent Induction and Deduction

**arXiv ID**: [2605.08670](https://arxiv.org/abs/2605.08670)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08670)

**作者**: Yixuan Li, Mingshu Cai, Ziyang Xiao, Wanyuan Wang, Yanchen Deng 等 (共6人)

**分类**: Artificial Intelligence, Computation and Language, Multiagent Systems

**发布时间**: 2026-05-09 04:15:57 UTC

**摘要 (英文)**: Large language model (LLM) powered AI agents have emerged as a promising paradigm for autonomous problem-solving, yet they continue to struggle with complex, multi-step real-world tasks that demand domain-specific procedural knowledge. Reusable agent skills, which encapsulate successful problem-solving strategies, offer a natural remedy by enabling agents to build on prior experience. However, curating such skills has largely remained a manual endeavor, requiring human experts to distill rich domain knowledge into actionable guidelines. In this work, we present $\textbf{M}$ulti-agent $\textbf{IN}$duction and $\textbf{D}$eduction for $\textbf{Skill}$s ($\textbf{MIND-Skill}$), a framework that automatically induces generalizable skills from successful trajectories with robust quality guarantees. MIND-Skill consists of an induction agent which is tasked to abstract reusable skills from successful trajectories, and a deduction agent which aims to reconstruct trajectories by following the induced skills. To guarantee the quality of the generated skills, we introduce a reconstruction loss that compares input and reconstructed trajectories, an outcome loss that enforces the correctness of the reconstructed trajectories, and a rubric loss that assesses the documentation quality and regularizes the abstraction level of the generated skills according to predefined criteria. These textual losses are jointly optimized with TextGrad, and the resulting skills are evaluated on held-out tasks unseen during optimization. Experiments on AppWorld and BFCL-v3 show that MIND-Skill consistently outperforms concurrent skill generation methods.

**摘要 (中文)**: [待翻译]

---

## 251. PAAC: Privacy-Aware Agentic Device-Cloud Collaboration

**arXiv ID**: [2605.08646](https://arxiv.org/abs/2605.08646)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08646)

**作者**: Liangqi Yuan, Wenzhi Fang, Shiqiang Wang, Christopher G. Brinton

**分类**: Machine Learning, Computation and Language, Distributed, Parallel, and Cluster Computing

**发布时间**: 2026-05-09 03:29:20 UTC

**摘要 (英文)**: Large language model (LLM) agents face a structural tension: cloud agents provide strong reasoning but expose user data, while on-device agents preserve privacy at the cost of overall capability. Existing device-cloud designs treat this boundary as a compute split rather than a trust boundary suited to agentic workloads, and existing sanitizers force a choice between policy flexibility and the structural fidelity tool calls require. In this work, we develop PAAC, a privacy-aware agentic framework that aligns planner--executor decomposition with the device-cloud boundary so that role specialization itself becomes the privacy mechanism. The cloud agent reasons over typed placeholder tokens that preserve each sensitive value's reasoning role while discarding its content, while the on-device agent identifies sensitive spans and distills each step's execution outcome into compact key findings. Sanitization confines the on-device LLM to proposing which spans to mask, while a deterministic registry performs all substitution and reversal, keeping actions directly executable on device. On three agentic benchmarks under strict privacy settings, PAAC dominates the Pareto frontier of privacy and accuracy, improving average accuracy by 15-36\% and reducing average leakage by 2-6$\times$ over state-of-the-art device-cloud baselines, with the largest margins on privacy targets outside fixed entity taxonomies. We find consistent improvements on 17 additional benchmarks spanning 10 domains, including math, science, and finance.

**摘要 (中文)**: [待翻译]

---

## 252. Causal Stories from Sensor Traces: Auditing Epistemic Overreach in LLM-Generated Personal Sensing Explanations

**arXiv ID**: [2605.08590](https://arxiv.org/abs/2605.08590)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08590)

**作者**: Shanshan Zhu, Han Zhang, J. Doris Chi, Subigya Nepal, Koustuv Saha

**分类**: Human-Computer Interaction, Artificial Intelligence, Computation and Language, Computers and Society

**发布时间**: 2026-05-09 01:10:40 UTC

**摘要 (英文)**: LLMs are increasingly used to explain personal sensing data, translating traces of activity and mood into natural-language accounts of why an anomalous day may have occurred. However, such explanations can sound coherent and personally meaningful even when the underlying evidence is sparse or missing. We introduce epistemic overreach (EO) as a measure for cases where a generated explanation implies more than the available sensing evidence can justify. To audit how often and in what forms EO occurs, we obtained anomalous-day scenarios from three longitudinal sensing datasets of college students: StudentLife, GLOBEM, and CollegeExperience. Across activity, sleep, and affect anomalies, we generated 14,922 explanations using three LLM families -- Llama, Qwen, and GPT -- under two prompting conditions: one minimally constrained prompt and another prompt explicitly instructing models to bound claims to the data. For each scenario, we varied the amount of behavioral evidence available to the model to examine whether more evidence reduces EO. We evaluated each explanation using a structured rubric, decomposing EO into the dimensions of unsupported causal attribution, unacknowledged data gaps, overconfident language, temporal inconsistency, and diagnostic inference. We find that LLMs routinely attribute anomalous days to causes without sufficient support from the data, and that this pattern replicates across datasets, anomaly types, and model families. Further, providing richer context does not reliably reduce EO; bounded prompting helps but does not eliminate it. These findings suggest that evidential grounding should be a first-order evaluation criterion for LLM-generated personal sensing explanations, alongside fluency and plausibility. We argue that personal sensing explanations require evidential discipline: systems must distinguish what is observed, what is inferred, and what remains unknown.

**摘要 (中文)**: [待翻译]

---

## 253. Human-Inspired Memory Architecture for LLM Agents

**arXiv ID**: [2605.08538](https://arxiv.org/abs/2605.08538)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08538)

**作者**: Doga Kerestecioglu, Alexei Robsky, Clemens Vasters, Anshul Sharma, Yitzhak Kesselman

**分类**: Artificial Intelligence, Computation and Language, Information Retrieval, Machine Learning

**发布时间**: 2026-05-08 22:52:37 UTC

**摘要 (英文)**: Current LLM agents lack principled mechanisms for managing persistent memory across long interaction horizons. We present a biologically-grounded memory architecture comprising six cognitive mechanisms: (1) sleep-phase consolidation, (2) interference-based forgetting, (3) engram maturation, (4) reconsolidation upon retrieval, (5) entity knowledge graphs, and (6) hybrid multi-cue retrieval. Each mechanism addresses a specific failure mode of naive memory accumulation. We introduce a synthetic calibration methodology that derives all pipeline thresholds without benchmark data exposure, eliminating a common source of evaluation leakage. We evaluate on two benchmarks. First, a VSCode issue-tracking dataset (13K issues, 120K events) where deduplication-based consolidation achieves 97.2% retention precision with 58% store reduction (+21.8 pp over baseline). Second, the LongMemEval personal-chat benchmark where we conduct the first streaming M-tier evaluation (475 sessions, ~540K unique turns). At a 200K-token context budget, our pipeline matches raw retrieval accuracy (70.1% vs. 71.2%, overlapping 95% CI) while exposing a tunable accuracy/store-size operating curve. At S-tier scale (50 sessions), dedup-based consolidation yields a +13.3 pp improvement in preference recall.

**摘要 (中文)**: [待翻译]

---

## 254. ShifaMind: A Multiplicative Concept Bottleneck for Interpretable ICD-10 Coding

**arXiv ID**: [2605.08482](https://arxiv.org/abs/2605.08482)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08482)

**作者**: Mohammed Sameer Syed, Xuan Lu

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-08 20:58:52 UTC

**摘要 (英文)**: Automated ICD-10 coding from clinical discharge summaries requires models that are both accurate on long-tailed multi-label classification tasks and interpretable to clinicians. Concept Bottleneck Models (CBMs) offer a principled framework for interpretability by routing predictions through human-interpretable concepts, but this transparency often comes at a cost: compressing rich clinical text representations into a narrow concept layer can restrict gradient flow and limit predictive capacity. We present ShifaMind, a concept-grounded architecture built around a Multiplicative Concept Bottleneck (MCB), which changes the form, rather than the width, of the bottleneck. Instead of projecting through a narrow concept layer, ShifaMind uses a learned multiplicative gate over a concept-grounded representation while retaining a scalar concept interface for inspection. On MIMIC-IV top-50 ICD-10 coding, ShifaMind achieves performance competitive with LAAT, the strongest baseline, across F1, AUC, and ranking metrics, while outperforming five additional ICD-coding baselines and providing concept-mediated explanations. Its substantial gains over a capacity-matched Vanilla CBM in both predictive performance and interpretability-oriented metrics highlight the importance of the bottleneck design.

**摘要 (中文)**: [待翻译]

---

## 255. LLM-guided Semi-Supervised Approaches for Social Media Crisis Data Classification

**arXiv ID**: [2605.08448](https://arxiv.org/abs/2605.08448)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08448)

**作者**: Jacob Ativo, Bharaneeshwar Balasubramaniyam, Anh Tran, Khushboo Gupta, Hongmin Li 等 (共7人)

**分类**: Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-08 20:15:40 UTC

**摘要 (英文)**: Semi-supervised learning approaches have been investigated as a means to enhance the analysis of social media data in disaster management contexts. In this work, we present the first empirical evaluation of large language model (LLM) guided semi-supervised learning for crisis related tweet classification. We compare two recent LLM assisted semi-supervised methods, VerifyMatch and LLM guided Co-Training ( LG-CoTrain), against established semi-supervised baselines. Our results show that LG-CoTrain significantly outperforms classical semi-supervised approaches in low resource settings with 5, 10 and 25 labeled examples per class, achieving the highest averaged Macro F1 across events. VerifyMatch achieves competitive performance while also demonstrating strong calibration properties. As the number of labeled examples increases, the performance gap narrows and Self Training emerges as a strong baseline. We further observe that compact semi-supervised models can, in some cases, outperform very large LLMs operating in zero-shot settings. This finding highlights the potential of transferring knowledge from LLMs into smaller and more deployable models through LLM guided semi-supervised learning, offering a practical pathway for real world disaster response applications. Our project repository on Github is here.

**摘要 (中文)**: [待翻译]

---

## 256. Queryable LoRA: Instruction-Regularized Routing Over Shared Low-Rank Update Atoms

**arXiv ID**: [2605.08423](https://arxiv.org/abs/2605.08423)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08423)

**作者**: Omatharv Bharat Vaidya, Connor T. Jerzak, Nhat Ho, Chandrajit Bajaj

**分类**: Machine Learning, Computation and Language, Machine Learning

**发布时间**: 2026-05-08 19:32:43 UTC

**摘要 (英文)**: We present a data-adaptive method for parameter-efficient fine-tuning of large neural networks. Standard low-rank adaptation methods improve efficiency by restricting each layer update to a fixed low-rank form, but this static parameterization can be too rigid when the appropriate correction depends on the input and on the evolving depth-wise computation of the network. Our approach replaces a purely layer-local adapter with a shared queryable memory of low-rank update atoms. For each block of layers, the model forms a query from the current low-rank state and a running summary of previous blocks, uses this query to retrieve a content-dependent combination of shared update components via attention, and applies the resulting routed operator within the low-rank bottleneck. In this way, the method retains the efficiency and scalability of low-rank adaptation while allowing the effective update to vary across inputs and to share reusable structure across layers. The resulting architecture provides a principled middle ground between static LoRA-style updates and fully generated parameter updates: it remains compact and parameter-efficient while supporting dynamic, context-sensitive adaptation. Further, we incorporate instruction-regularization by augmenting routing logits with a language-induced prior over update atoms, thereby biasing the selection of low-rank transformations toward semantically relevant directions without generating unconstrained parameter updates. Experiments on noisy non-linear regression tasks and LLM fine-tuning suggest that this queryable update-memory formulation can improve final test performance and training stability compared to standard low-rank adaptation, while using a comparable number of trainable parameters.

**摘要 (中文)**: [待翻译]

---

## 257. SecureForge: Finding and Preventing Vulnerabilities in LLM-Generated Code via Prompt Optimization

**arXiv ID**: [2605.08382](https://arxiv.org/abs/2605.08382)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08382)

**作者**: Houjun Liu, Lisa Einstein, John Yang, Joachim Baumann, Duncan Eddy 等 (共8人)

**分类**: Cryptography and Security, Computation and Language, Computers and Society

**发布时间**: 2026-05-08 18:40:47 UTC

**摘要 (英文)**: LLM coding agents now generate code at an unprecedented scale, yet LLM-generated code introduces cybersecurity vulnerabilities into codebases without human involvement. Even when frontier models are explicitly asked to write secure production code with relevant weaknesses to avoid in context, we find that they still produce verifiable vulnerabilities on average 23% of the time across a corpus of 250 benign coding prompts. We introduce SecureForge, an automated pipeline that both audits security risks of frontier models and produces auditing-informed secure system prompts that reduce output security vulnerabilities while maintaining unit test performance. SecureForge first identifies benign prompts that produce statically detectable vulnerabilities, and then amplifies them into a large synthetic prompt corpus of diverse scenarios using a Markovian sampling technique to jointly maintain error rates and prompt diversity. This corpus is then used to iteratively optimize the system prompts to reduce output security vulnerabilities. On frontier models, SecureForge yields a statistically significant Pareto improvement in both unit test success and output security, with output vulnerabilities reduced by up to 48%. The resulting system prompts transfer zero-shot to in-the-wild coding agent prompts, without any exposure to real user prompt distributions during optimization.

**摘要 (中文)**: [待翻译]

---

## 258. Reinforcement Learning for Scalable and Trustworthy Intelligent Systems

**arXiv ID**: [2605.08378](https://arxiv.org/abs/2605.08378)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08378)

**作者**: Guangchen Lan

**分类**: Machine Learning, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-08 18:36:25 UTC

**摘要 (英文)**: Reinforcement learning has become a powerful paradigm for improving the capability of intelligent systems, but its practical deployment faces two central challenges. First, reinforcement learning must scale efficiently in distributed environments where communication bandwidth is limited and computation is heterogeneous across agents. Second, as reinforcement learning is increasingly used in post-training large language models and autonomous agents, the optimized policies must also be aligned with human preferences and satisfy safety requirements such as privacy-aware information disclosure. This dissertation addresses both challenges through four complementary contributions spanning federated optimization, preference alignment, and contextual safety. The first part of the dissertation studies scalable reinforcement learning in federated settings. The second part of the dissertation studies trustworthy reinforcement learning for large language models. Together, these contributions advance reinforcement learning along two complementary dimensions. On the one hand, they make reinforcement learning more scalable through communication-efficient and asynchronous federated optimization. On the other hand, they make reinforcement learning more trustworthy by improving alignment with human preferences and by reducing contextually inappropriate information disclosure in language-based intelligent systems. As a whole, this dissertation argues that the next generation of intelligent systems will require both efficient optimization and trustworthy behavior, and that reinforcement learning provides a unifying framework for addressing both goals.

**摘要 (中文)**: [待翻译]

---

## 259. CDS4RAG: Cyclic Dual-Sequential Hyperparameter Optimization for RAG

**arXiv ID**: [2605.08333](https://arxiv.org/abs/2605.08333)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08333)

**作者**: Pengzhou Chen, Tao Chen

**分类**: Machine Learning, Artificial Intelligence, Computation and Language, Performance, Software Engineering

**发布时间**: 2026-05-08 17:58:11 UTC

**摘要 (英文)**: Retrieval-Augmented Generation (RAG) is sensitive to the vast hyperparameters of the retriever and generator, yet optimizing them using given queries is a challenging task due to the complex interactions and expensive evaluation costs. Existing algorithms are ineffective and slow in convergence, since they often treat RAG as a monolithic black box or only optimize partial hyperparameters. In this paper, we propose CDS4RAG, a framework that optimizes the full RAG hyperparameters using given queries via a new cyclic dual-sequential formulation. CDS4RAG is special in the sense that it distinguishes the hyperparameters of the retriever and generator, cyclically optimizing them in turn. Such a paradigm allows us to design fine-grained within-cycle budget provision and expedite the optimization via cross-cycle seeding when optimizing the generator. CDS4RAG is also an algorithm-agnostic framework that can be paired with diverse general algorithms. Through experiments on four common benchmarks and two backbone LLMs, we reveal that CDS4RAG considerably boosts the vanilla algorithms in 21/24 cases while significantly outperforming state-of-the-art algorithms in all cases with up to 1.54x improvements of generation quality and better speedup.

**摘要 (中文)**: [待翻译]

---

## 260. LLMSYS-HPOBench: Hyperparameter Optimization Benchmark Suite for Real-World LLM Systems

**arXiv ID**: [2605.08305](https://arxiv.org/abs/2605.08305)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08305)

**作者**: Siyu Wu, Yulong Ye, Zezhen Xiang, Pengzhou Chen, Gangda Xiong 等 (共6人)

**分类**: Machine Learning, Artificial Intelligence, Computation and Language, Performance, Software Engineering

**发布时间**: 2026-05-08 12:53:03 UTC

**摘要 (英文)**: Large Language Model (LLM) systems have been the frontier of AI in many application domains, leading to new challenges and opportunities for hyperparameter optimization (HPO) for the AutoML community. However, this type of system exhibits an unprecedented compound space of hyperparameter configuration from both the AI and non-AI components; rich and nonlinear implications from the fidelity factors; and diverse costs of measuring hyperparameter configurations, none of which have been fully captured in existing benchmarks. This paper presents the first (live) benchmark suite and datasets for HPO of real-world LLM systems, dubbed LLMSYS-HPOBench, covering data related to the inference objective values of hyperparameter configurations profiled from running the LLM systems. Currently, LLMSYS-HPOBench contains 364,450 hyperparameter configurations with a dimensionality of 12-23, 3-5 dimensions of fidelity factor leading to 932 settings, 3-9 inference objective metrics, and 2-10 cost metrics, together with generated logs from measuring the LLM systems. What we seek to advocate is not only a revalidation of the existing HPO algorithms over the frontier LLM systems, but also to provide an evolving platform for the AutoML community to explore new directions of research in this regard. The benchmark suite has been made available at: https://github.com/ideas-labo/llmsys-hpobench

**摘要 (中文)**: [待翻译]

---

## 261. mHC-SSM: Manifold-Constrained Hyper-Connections for State Space Language Models with Stream-Specialized Adapters

**arXiv ID**: [2605.08300](https://arxiv.org/abs/2605.08300)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08300)

**作者**: Abdulvahap Mutlu, Şengül Doğan, Türker Tuncer

**分类**: Machine Learning, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-08 11:37:23 UTC

**摘要 (英文)**: Manifold-Constrained Hyper-Connections (mHC) introduce a stability-motivated variant of multi stream residual mixing by constraining residual stream mixing matrices to the manifold of doubly stochastic matrices via Sinkhorn-Knopp projection. In his work, we study whether mHC-style constrained multi-stream residual topology transfers effectively to state space model (SSM) language modeling. We implement a static mHC mechanism around an SSM block by expanding the residual stream into multiple parallel streams, aggregating streams into a single SSM input through simplex-constrained pre-mixing, scattering the SSM output back to streams through simplex-constrained post-mixing, and applying Sinkhorn-projected residual stream mixing at each layer. We further introduce stream-specialized adapters that add lightweight stream-specific capacity through a shared bottleneck with per-stream scaling, applied both before stream aggregation and after the SSM output prior to scattering. We evaluate baseline single-stream SSM, static mHC SSM, and mHC SSM with adapters on WikiText-2 using identical training settings and report checkpoint-based validation loss, perplexity, throughput, and peak GPU memory. Under the reported fair checkpoint evaluation, static mHC improves validation loss from 6.3507 to 6.2448 and reduces perplexity from 572.91 to 515.35, while mHC with adapters further improves validation loss to 6.1353 and perplexity to 461.88. These gains are accompanied by modest throughput reductions from 1025.52 to 964.81 and 938.90 tokens per second, and increased peak memory from 2365 MB to 2568 MB and 3092 MB. The results suggest that mHC-inspired constrained multi-stream residual mixing can yield measurable quality improvements in SSM language models and that stream-specialized adapter capacity can further enhance performance with predictable efficiency tradeoffs.

**摘要 (中文)**: [待翻译]

---

## 262. In-Context Fixation: When Demonstrated Labels Override Semantics in Few-Shot Classification

**arXiv ID**: [2605.08295](https://arxiv.org/abs/2605.08295)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08295)

**作者**: Ming Liu

**分类**: Machine Learning, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-08 10:20:39 UTC

**摘要 (英文)**: While random demonstration labels barely hurt in-context learning (Min et al., 2022), we show that homogeneous labels--even semantically valid ones--collapse accuracy to <=12% across six models (Pythia, Llama, Qwen; 0.8B--8B) and four tasks. The trigger is label-slot content: the model treats tokens occupying the label position as an exhaustive answer vocabulary, with homogeneity as the maximally collapsed case. A novel set-level fixation finding confirms this: when demonstrations carry varied nonsense tokens from {foo,bar,vex,nit,orb}, the model places 42--67% of probability on the demonstrated set while P(dog) remains below 0.2%. This is inconsistent with latent-concept Bayesian accounts (Xie et al., 2022) and reveals that ICL output is constrained vocabulary retrieval--the model binds its output to the demonstrated token inventory regardless of semantic plausibility. The effect generalizes to 4-way classification (0% accuracy across three models, 1B--8B) and multi-token verbalizers ("very positive"), where we decompose fixation into format-level (template adoption) and content-level (polarity override) components that are experimentally dissociable. Mechanistically, per-item paired activation patching on Pythia-1B recovers 98.4% of the gap (95% CI [84%, 112%]), localizing fixation to a layer-7-centered circuit (rank 2/560, 99.8th percentile; 4-fold CV mean 103%). Cross-architecture logit lens on Llama-3.2-1B replicates the encode-then-override trajectory with causal confirmation (top-5 layers: 89% recovery).

**摘要 (中文)**: [待翻译]

---

## 263. HTPO: Towards Exploration-Exploitation Balanced Policy Optimization via Hierarchical Token-level Objective Control

**arXiv ID**: [2605.08283](https://arxiv.org/abs/2605.08283)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08283)

**作者**: Xincheng Yao, Ruoqi Li, Cheng Chen, Daoxin Zhang, Yi Wu 等 (共7人)

**分类**: Machine Learning, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-08 07:38:35 UTC

**摘要 (英文)**: Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a pivotal technique for enhancing the reasoning capabilities of Large Language Models (LLMs). However, the de facto practice of mainstream RL algorithms is to treat all tokens of one response equally and assign the same optimization objective to each token, failing to provide granular guidance for the reasoning process. While in Chain-of-Thought (CoT) reasoning, different tokens usually play distinct roles. Therefore, the current RL algorithms lack an effective mechanism to dynamically balance the exploration-exploitation trade-off during learning. To this end, we propose Hierarchical Token-level Objective Control Policy Optimization (HTPO), a novel RL algorithm that takes the divide-and-conquer idea to hierarchically partition the response tokens into specific functional groups from three aspects (i.e., prompt difficulty, answer correctness, and token entropy). Within each group, according to the contributions to exploration or exploitation, we design specialized optimization objectives to facilitate the effective execution of each token's expected functionality. In this way, HTPO can achieve a more balanced exploration-exploitation trade-off. Extensive experiments on challenging reasoning benchmarks validate the superiority of our HTPO algorithm, which significantly outperforms the strong DAPO baseline (e.g., +8.6% and +6.7% on AIME'24 and AIME'25, respectively). When scaling test-time compute, the HTPO-trained model maintains a consistent performance advantage over the DAPO baseline, and the gap widens as the sampling budget increases, validating that our adaptive token-level control method fosters effective exploration without sacrificing exploitation performance. Code will be at https://github.com/xcyao00/HTPO.

**摘要 (中文)**: [待翻译]

---

## 264. Spatial Priming Outperforms Semantic Prompting: A Grid-Based Approach to Improving LLM Accuracy on Chart Data Extraction

**arXiv ID**: [2605.08220](https://arxiv.org/abs/2605.08220)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08220)

**作者**: Andrei Lazarev, Dmitrii Sedov, Alexander Galkin

**分类**: Artificial Intelligence, Computational Engineering, Finance, and Science, Computation and Language, Computer Vision and Pattern Recognition, Software Engineering

**发布时间**: 2026-05-06 13:38:29 UTC

**摘要 (英文)**: The automated extraction of data from scientific charts is a critical task for large-scale literature analysis. While multimodal Large Language Models (LLMs) show promise, their accuracy on non-standardized charts remains a challenge. This raises a key research question: what is the most effective strategy to improve model performance (high-level semantic priming) or low-level spatial priming? This paper presents a comparative investigation into these two distinct strategies. We describe our exploratory experiments with semantic methods, such as a two-stage metadata-first framework and Chain-of-Thought, which failed to produce a statistically significant improvement. In contrast, we present a simple but highly effective spatial priming method: overlaying a coordinate grid onto the chart image before analysis. Our quantitative experiment on a synthetic dataset demonstrates that this grid-based approach provides a statistically significant reduction in data extraction error (SMAPE reduced from 25.5% to 19.5%, p < 0.05) compared to a baseline. We conclude that for the current generation of multimodal models, providing explicit spatial context is a more effective and reliable strategy than high-level semantic guidance for this class of tasks.

**摘要 (中文)**: [待翻译]

---

## 265. LLMs with in-context learning for Algorithmic Theoretical Physics

**arXiv ID**: [2605.08212](https://arxiv.org/abs/2605.08212)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08212)

**作者**: Anamaria Hell, Leander Thiele

**分类**: Machine Learning, Computation and Language, General Relativity and Quantum Cosmology, High Energy Physics - Theory

**发布时间**: 2026-05-06 09:30:08 UTC

**摘要 (英文)**: There is an increasing number of algorithmic computations in theoretical physics. These, while conceptually simple, can nevertheless be time-consuming and contain subtleties that should not be overlooked. Given the recent improvement of Large Language Models (LLM), it is natural to investigate whether LLMs equipped with a computer algebra system (CAS) runtime and sufficiently informative context can reliably carry out these algorithmic tasks. In this work, we interface Claude with Maple, and apply this framework to cosmological perturbations in modified theories of gravity. We demonstrate the current capabilities of this approach, the typical failures, and how the same can be improved. We find that a frontier LLM supplied with worked examples is able to solve most test problems.

**摘要 (中文)**: [待翻译]

---

## 266. MULTITEXTEDIT: Benchmarking Cross-Lingual Degradation in Text-in-Image Editing

**arXiv ID**: [2605.08163](https://arxiv.org/abs/2605.08163)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08163)

**作者**: Liwei Cheng, Zirui Song, Shibo Feng, Lunjie Zhou, Yixuan Guan 等 (共6人)

**分类**: Computer Vision and Pattern Recognition, Artificial Intelligence, Computation and Language

**发布时间**: 2026-05-04 16:21:25 UTC

**摘要 (英文)**: Text-in-image editing has become a key capability for visual content creation, yet existing benchmarks remain overwhelmingly English-centric and often conflate visual plausibility with semantic correctness. We introduce MULTITEXTEDIT, a controlled benchmark of 3,600 instances spanning 12 typologically diverse languages, 5 visual domains, and 7 editing operations. Language variants of each instance share a common visual base and are paired with a human-edited reference and region masks, isolating the language variable for cross-lingual comparison. To capture script-level errors that coarse text-matching metrics miss, such as missing diacritics, reversed RTL order, and mixed-script renderings, we introduce a language fidelity (LSF) metric scored by a two-stage LVM protocol that first traces the edited target text and then judges it in isolation, reaching a quadratic-weighted \k{appa} of 0.76 against native-speaker annotators. Evaluating 12 open-source and proprietary systems with LSF alongside standard semantic and mask-aware pixel metrics, we find pronounced cross-lingual degradation for every model, largest on Hebrew and Arabic and smallest on Dutch and Spanish, and concentrated in text accuracy and script fidelity rather than in coarse structural dimensions. We also uncover a pervasive semantic and pixel mismatch, where outputs preserve global layout and background fidelity yet distort script-specific forms.

**摘要 (中文)**: [待翻译]

---

## 267. Feature Rivalry in Sparse Autoencoder Representations: A Mechanistic Study of Uncertainty-Driven Feature Competition in LLMs

**arXiv ID**: [2605.08149](https://arxiv.org/abs/2605.08149)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08149)

**作者**: Harshavardhan

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-05-03 18:43:19 UTC

**摘要 (英文)**: Sparse Autoencoders (SAEs) decompose large language model representations into interpretable features, but how these features interact under uncertainty remains poorly understood. We introduce Feature Rivalry -- negatively correlated SAE feature pairs -- and study whether rivalry serves as a mechanistic signature of model uncertainty in Gemma-2-2B using Gemma Scope SAEs. Through a controlled within-domain experiment on PopQA split by response entropy, we find that high-entropy questions produce significantly stronger feature rivalry at layers 0 and 12 relative to low-entropy questions (p=5.3x10^-26 and p=5.8x10^-5 respectively), localizing uncertainty to specific processing stages in the residual stream. We then test whether rivalry is causally upstream of model outputs via activation steering along rivalry axes -- finding that steering along the rivalry direction (vec_A - vec_B) causes more output changes than random directions at low steering multipliers across 15 of 20 rival feature pairs. Finally, a per-prompt rivalry score derived from pairwise cosine similarities of active SAE feature decoder vectors predicts answer correctness (AUROC=0.689), approaching but not matching softmax confidence (AUROC=0.808).

**摘要 (中文)**: [待翻译]

---

## 268. Reasoning emerges from constrained inference manifolds in large language models

**arXiv ID**: [2605.08142](https://arxiv.org/abs/2605.08142)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08142)

**作者**: Yanbiao Ma, Fei Luo, Linfeng Zhang, Chuangxin Zhao, Mingxuan Wang 等 (共13人)

**分类**: Machine Learning, Computation and Language, Computer Vision and Pattern Recognition

**发布时间**: 2026-05-02 10:41:20 UTC

**摘要 (英文)**: Reasoning in large language models is predominantly evaluated through labeled benchmarks, conflating task performance with the quality of internal inference. Here we study reasoning as an intrinsic dynamical process by examining the evolution of internal representations during inference. We find that inference-time dynamics consistently self-organize into low-dimensional manifolds embedded within high-dimensional representation spaces. we find that such geometric compression, although pervasive, is not sufficient for stable or reliable reasoning. Instead, effective reasoning dynamics emerge within a constrained structural regime characterized by three conditions: adequate representational expressivity, spontaneous manifold compression, and preservation of non-degenerate information volume within the compressed subspace. Models outside this regime exhibit characteristic pathological inference dynamics. Based on these insights, we introduce a unified, label-free diagnostic computed solely from internal dynamics. These findings suggest that reasoning in LLMs is fundamentally governed by geometric and informational constraints, offering a complementary framework to benchmark-centric assessment.

**摘要 (中文)**: [待翻译]

---

## 269. Scaling Mobile Agent Systems: From Capability Density to Collective Intelligence

**arXiv ID**: [2605.08124](https://arxiv.org/abs/2605.08124)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08124)

**作者**: Bowei He

**分类**: Distributed, Parallel, and Cluster Computing, Computation and Language, Multiagent Systems, Networking and Internet Architecture

**发布时间**: 2026-04-29 12:24:33 UTC

**摘要 (英文)**: Mobile agent systems are emerging as a key paradigm for enabling intelligent applications on edge devices and in AIoT ecosystems. However, their scalability is fundamentally constrained by limited on-device computation and fragmented intelligence across devices. In this work, we propose a unified research agenda for scaling mobile agent systems along two complementary dimensions: (1) improving capability density of individual agents through compact foundation model design and compression, and (2) enabling collective intelligence via communication-rich multi-agent collaboration. Building on recent model and infrastructure advances, this vision aims to transform isolated mobile agents into a distributed intelligent system that is efficient and scalable.

**摘要 (中文)**: [待翻译]

---

## 270. Block-Wise Differentiable Sinkhorn Attention: Tail-Refinement Gradients with a Gap-Aware Dustbin Bridge

**arXiv ID**: [2605.08123](https://arxiv.org/abs/2605.08123)  |  **PDF**: [下载](https://arxiv.org/pdf/2605.08123)

**作者**: Dylan Forde

**分类**: Machine Learning, Computation and Language

**发布时间**: 2026-04-28 19:01:11 UTC

**摘要 (英文)**: We study long-context balanced entropic optimal transport (OT) attention on TPU hardware through a stopped-base, fixed-depth tail-refinement surrogate. After a stopped $T$-step Sinkhorn solve, we unroll a short refinement tail and differentiate that surrogate exactly. For the production $R=2$ case, the backward pass contains four staircase plan factors. We prove an exact one-reference-tile schedule: the $R=2$ score cotangent is a single reference plan tile times an explicit modifier field built from vector cotangents and dual differences. This yields block-wise cost $O((T+R)LW)$, $O(Ld)$ input storage, and $O(L)$ additional HBM usage for fixed head dimension $d$ and band width $W$. We also formalize the current \texttt{dustbin\_block} path as the same balanced surrogate on an augmented support, so the schedule lifts to the gap-aware transport path used in our TPU runs. We provide a local surrogate-bias bound, an a posteriori bias certificate, and a projective contraction certificate for strictly positive active blocks. On synthetic masked problems, the optimized kernel matches exact autodiff of the same centered surrogate to within $10^{-5}$--$10^{-10}$. On TPU v6e-8, a four-configuration Pfam screen completes end-to-end, and a promoted balanced $R=2$ run sustains roughly $8.5$ examples per second through a three-hour budget, reaching step $1437$. Held-out Pfam test shards improve reconstruction from $3.17$ to $0.99$ and sparse CE from $5.86$ to $5.69$ relative to step $0$. These results support exact fixed-depth backward theory, a theorem-matching gap-aware bridge, and trainability evidence for the production path.

**摘要 (中文)**: [待翻译]

---

