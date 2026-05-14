#!/usr/bin/env python3
"""
论文自动分类脚本

基于关键词匹配将论文分类到 TOPICS.md 中定义的 topic 类别。
分类结果保存为 *_classified.json，供后续翻译整理使用。

使用方法:
    python3 classify_papers.py <input_json>
    python3 classify_papers.py papers_cs.CL_2026-05-12.json

输出:
    papers_cs.CL_2026-05-12_classified.json (在输入文件同目录)
"""

import json
import sys
import os
from collections import defaultdict


def classify_paper(p):
    """
    基于标题和摘要关键词对论文进行分类。
    返回 (topic_id, should_exclude_medical)
    """
    title = p['title'].lower()
    abstract = p['abstract'].lower()
    text = title + ' ' + abstract

    # ===== 排除规则：医学/临床 =====
    medical_keywords = [
        'clinical', 'icu', 'mimic', 'diagnosis', 'cancer', 'breast cancer',
        'radiotherapy', 'radiation treatment', 'medical', 'patient', 'healthcare',
        'disease', 'drug', 'hospital', 'therapy', 'incidence', 'mortality',
        'morbidity', 'epidemiolog', 'pharma', 'symptom', 'treatment outcome',
        'doctor', 'nurse', 'clinical decision', 'psychotherapy', 'medicare',
        'ehr', 'health record', 'icd-10', 'side effects of', 'medical incident',
        'medical studies', 'inpatient clinical'
    ]
    is_medical = any(kw in text for kw in medical_keywords)

    # ===== Topic 分类（优先级从高到低）=====

    # --- Agent 相关 ---
    if any(kw in text for kw in [
        'multi-agent', 'multi agent system', 'agent system', 'agentic',
        'llm agent', 'coding agent', 'agent framew', 'agent collabor',
        'agent evaluat', 'mobile agent', 'agent memory', 'agent skill',
        'tool-use agent', 'tool use agent', 'agents that'
    ]):
        if any(kw in text for kw in ['multimodal', 'visual', 'vision', 'egocentric video', 'gui']):
            if any(kw in text for kw in ['reinforcement', ' rl ', 'reward', 'grpo', 'ppo', 'self-play', 'self-evolv']):
                return ('multimodal-agent-rl', is_medical)
            return ('multimodal-agent', is_medical)
        if any(kw in text for kw in [
            'reinforcement learn', ' rl ', 'reward', 'grpo', 'ppo',
            'policy optim', 'self-play', 'self-evolv', 'rlvr',
            'online learn', 'post-train'
        ]):
            return ('agent-rl', is_medical)
        if any(kw in text for kw in ['safety', 'jailbreak', 'adversarial', 'security', 'privacy', 'alignment']):
            return ('agent-safety', is_medical)
        return ('agent-design', is_medical)

    # --- Tool use (非 agent 场景) ---
    if any(kw in text for kw in ['tool call', 'tool-use', 'tool use', 'function call', 'api call', 'tool integrat', 'tool-augment', 'tool call prun']):
        return ('tool-use', is_medical)

    # --- GUI Agent ---
    if any(kw in text for kw in ['gui agent', 'visual agent']):
        if any(kw in text for kw in ['reinforcement', ' rl ', 'reward']):
            return ('multimodal-agent-rl', is_medical)
        return ('multimodal-agent', is_medical)

    # --- RLVR / RL for Reasoning ---
    if any(kw in text for kw in ['rlvr', 'reinforcement learning with verif']):
        if any(kw in text for kw in ['multimodal', 'visual', 'vision']):
            return ('multimodal-reasoning', is_medical)
        return ('rl-reasoning', is_medical)

    # --- General RL ---
    if any(kw in text for kw in [
        'reinforcement learn', ' rl ', 'reward', 'self-play', 'rlhf',
        'dpo', 'preference optim', 'rlvr', 'grpo', 'ppo', 'policy optim'
    ]):
        if any(kw in text for kw in ['reason', 'math', 'logic', 'chain-of-thought', 'cot', 'proof', 'verif']):
            if any(kw in text for kw in ['multimodal', 'visual', 'vision']):
                return ('multimodal-reasoning', is_medical)
            return ('rl-reasoning', is_medical)
        if any(kw in text for kw in ['multimodal', 'visual', 'vision']):
            return ('multimodal-agent-rl', is_medical)
        if any(kw in text for kw in ['align', 'safety', 'guardrail', 'jailbreak', 'harmful', 'red team', 'misalign']):
            return ('llm-alignment', is_medical)
        return ('agent-rl', is_medical)

    # --- RAG ---
    if any(kw in text for kw in ['retrieval-augment', ' rag ', ' rag,', ' rag:', 'retrieval augment']):
        return ('rag', is_medical)

    # --- Retrieval ---
    if any(kw in text for kw in [
        'retriev model', 'dense retriev', 'sparse retriev', 'rerank',
        'information retriev', 'lexical retriev', 'retrieval quality',
        'embedding model', 'text embed'
    ]):
        return ('retrieval-model', is_medical)

    # --- Code ---
    if any(kw in text for kw in [
        'code generat', 'text-to-sql', 'text2sql', 'code complet',
        ' coding', 'program synth', 'code understand', 'llm-generat code',
        'secure code', 'vulnerab'
    ]):
        return ('code-gen', is_medical)

    # --- VLM / Multimodal ---
    if any(kw in text for kw in ['vision-language', 'vlm', 'mllm', 'large vision-language']):
        if any(kw in text for kw in ['reason', 'chain-of-thought', 'cot', 'logic']):
            return ('multimodal-reasoning', is_medical)
        return ('vlm', is_medical)

    if any(kw in text for kw in ['multimodal reason', 'visual reason', 'video reason']):
        return ('multimodal-reasoning', is_medical)

    if any(kw in text for kw in [
        'text-to-image', 'text to image', 'video gen', 'image gen',
        'image edit', 'visual content cre', 'multimodal gen'
    ]):
        return ('multimodal-gen', is_medical)

    # --- LLM Reasoning (非 RL) ---
    if any(kw in text for kw in ['chain-of-thought', 'reason', 'math', 'proof', 'theorem', 'logic', 'planning']):
        if any(kw in text for kw in ['multimodal', 'visual', 'vision', 'image']):
            return ('multimodal-reasoning', is_medical)
        return ('llm-reasoning', is_medical)

    # --- Hallucination ---
    if 'hallucin' in text:
        return ('llm-alignment', is_medical)

    # --- Alignment / Safety ---
    if any(kw in text for kw in [
        'align', 'jailbreak', 'safety', 'guardrail', 'red team',
        'adversarial attack', 'harmful', 'misalign', 'sycophanc',
        'bias ', 'fairness', 'toxic'
    ]):
        return ('llm-alignment', is_medical)

    # --- Efficiency (量化/剪枝/蒸馏/加速) ---
    if any(kw in text for kw in [
        'quantiz', 'prun', 'speculat deco', 'kv cache',
        ' efficien', 'inference speed', 'inference cost', 'memory efficien'
    ]):
        return ('llm-efficiency', is_medical)

    if 'distill' in text or 'compress' in text:
        if any(kw in text for kw in ['lora', 'adapter', 'fine-tun']):
            return ('llm-training', is_medical)
        return ('llm-efficiency', is_medical)

    # --- Architecture ---
    if any(kw in text for kw in [
        'transformer', 'mixture-of-expert', 'moe', 'state space model',
        'ssm', 'mamba', 'diffusion language', 'masked diffusion',
        'recurrent', 'architect', 'looped'
    ]):
        return ('llm-architecture', is_medical)

    # --- Training / Fine-tuning ---
    if any(kw in text for kw in [
        'pretrain', 'pre-train', 'sft', 'supervised fine', 'fine-tun',
        'instruction tun', 'data select', 'data mix', 'curriculum',
        'lora', 'low-rank adapt', 'parameter-effici', 'adapter'
    ]):
        return ('llm-training', is_medical)

    # --- Knowledge / Memory / Long context ---
    if any(kw in text for kw in [
        'knowledge edit', 'long context', 'long-context', 'memory mechan',
        'continual learn', 'knowledge acquis', 'memory architect'
    ]):
        return ('llm-knowledge', is_medical)

    # --- Evaluation / Benchmark ---
    if any(kw in text for kw in ['benchmark', 'evaluat', 'assessment']):
        return ('llm-evaluation', is_medical)

    # --- Interpretability ---
    if any(kw in text for kw in [
        'interpret', 'mechanist', 'circuit', 'sparse autoencod',
        'neuron', 'activat steer', 'latent space', 'probe', 'probing'
    ]):
        return ('llm-interpret', is_medical)

    # --- Dialogue ---
    if any(kw in text for kw in ['dialogue', 'dialog system', 'conversational', 'spoken dialogue']):
        return ('dialogue', is_medical)

    # --- Machine Translation ---
    if any(kw in text for kw in ['machine translat', 'translat', 'bilingual']):
        return ('mt', is_medical)

    # --- Multilingual ---
    if any(kw in text for kw in ['multilingual', 'cross-lingual', 'low-resource']):
        return ('multilingual', is_medical)

    # --- Speech / Audio ---
    if any(kw in text for kw in ['speech recogn', 'asr', 'audio', 'spoken', 'voice']):
        return ('audio-speech', is_medical)

    # --- NER / RE ---
    if any(kw in text for kw in ['named entity', 'relation extract', 'event extract', 'information extract']):
        return ('ner-re', is_medical)

    # --- Knowledge Graph ---
    if any(kw in text for kw in ['knowledge graph', 'ontology', 'text2cypher', 'sparql']):
        return ('knowledge-graph', is_medical)

    # --- Data Quality ---
    if any(kw in text for kw in ['data synth', 'data augment', 'synthetic data', 'data quality', 'dedup']):
        return ('data-quality', is_medical)

    # --- NLU ---
    if any(kw in text for kw in ['semantic', 'intent', 'discourse', 'nlu']):
        return ('nlu', is_medical)

    # --- NLG ---
    if any(kw in text for kw in ['summariz', 'text gen', 'language gen']):
        return ('nlg', is_medical)

    # --- Prompt Engineering ---
    if any(kw in text for kw in ['prompt', 'in-context learn', 'icl', 'few-shot']):
        return ('prompt-engineering', is_medical)

    # --- LLM Application ---
    if any(kw in text for kw in [
        'legal', 'law', 'financ', 'education', 'scientific',
        'mathemat', 'physics', 'chemistry', 'molecular'
    ]):
        return ('llm-app', is_medical)

    # --- Sentiment ---
    if any(kw in text for kw in ['sentiment', 'emotion']):
        return ('nlu', is_medical)

    return ('other', is_medical)


def main():
    if len(sys.argv) < 2:
        print("使用方法: python3 classify_papers.py <input_json>")
        print("示例: python3 classify_papers.py papers_cs.CL_2026-05-12.json")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.replace('.json', '_classified.json')

    with open(input_file, 'r', encoding='utf-8') as f:
        papers = json.load(f)

    print(f"加载 {len(papers)} 篇论文...")

    # 分类
    for p in papers:
        topic_id, is_medical = classify_paper(p)
        p['topic_id'] = topic_id
        p['exclude'] = is_medical

    # 统计
    topic_papers = defaultdict(list)
    for p in papers:
        topic_papers[p['topic_id']].append(p)

    topic_order = [
        'agent-design', 'agent-rl', 'rl-reasoning', 'agent-safety',
        'llm-reasoning', 'tool-use', 'code-gen',
        'llm-training', 'llm-efficiency', 'llm-architecture',
        'llm-knowledge', 'llm-alignment', 'llm-evaluation', 'llm-interpret',
        'nlg', 'ner-re', 'nlu', 'mt', 'dialogue',
        'retrieval-model', 'rag', 'ir-evaluation',
        'vlm', 'multimodal-gen', 'multimodal-agent', 'multimodal-agent-rl',
        'multimodal-reasoning', 'audio-speech',
        'data-quality', 'knowledge-graph', 'benchmark',
        'prompt-engineering', 'llm-app', 'multilingual', 'other'
    ]

    excl_count = sum(1 for p in papers if p.get('exclude'))
    print(f"\n=== 分类统计 ===")
    print(f"总论文数: {len(papers)}")
    print(f"排除(医学): {excl_count}")
    print()

    for t in topic_order:
        if t in topic_papers:
            ps = topic_papers[t]
            exc = sum(1 for p in ps if p.get('exclude'))
            print(f"  {t}: {len(ps)}篇" + (f" (排除{exc})" if exc > 0 else ""))
            for p in ps[:3]:
                ex = " [排除]" if p.get('exclude') else ""
                print(f"    #{p['index']} {p['title'][:70]}{ex}")
            if len(ps) > 3:
                print(f"    ... 还有 {len(ps)-3} 篇")

    # 检查未在 order 中的 topic
    for t in sorted(topic_papers.keys()):
        if t not in topic_order:
            print(f"\n  [注意] 未在 topic_order 中的类别: {t}: {len(topic_papers[t])}篇")

    # 保存
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    print(f"\n分类结果已保存到: {output_file}")


if __name__ == '__main__':
    main()