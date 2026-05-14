#!/usr/bin/env python3
"""生成 Markdown 骨架文件，摘要翻译部分留占位符"""
import json
from datetime import datetime

with open('papers_cs.CL_2026-05-12.json', 'r') as f:
    data = json.load(f)

lines = []
lines.append("# arXiv cs.CL 论文列表 — 2026-05-12\n\n")
lines.append(f"- **日期**: 2026-05-12\n")
lines.append(f"- **分类**: Computation and Language (cs.CL)\n")
lines.append(f"- **论文总数**: {len(data)}\n\n")
lines.append("---\n\n")

for p in data:
    idx = p['index']
    title = p['title']
    arxiv_id = p.get('arxiv_id', '')
    arxiv_url = p.get('arxiv_url', '')
    pdf_url = p.get('pdf_url', '')
    authors = p.get('authors', [])
    abstract = p.get('abstract', '')
    subjects = p.get('subjects', [])
    publish_time = p.get('publish_time', '')

    lines.append(f"## {idx}. {title}\n\n")
    if arxiv_id:
        lines.append(f"**arXiv ID**: [{arxiv_id}]({arxiv_url})  |  ")
        lines.append(f"**PDF**: [下载]({pdf_url})\n\n")
    if authors:
        authors_str = ', '.join(authors[:5])
        if len(authors) > 5:
            authors_str += f" 等 (共{len(authors)}人)"
        lines.append(f"**作者**: {authors_str}\n\n")
    if subjects:
        lines.append(f"**分类**: {', '.join(subjects)}\n\n")
    if publish_time:
        lines.append(f"**发布时间**: {publish_time}\n\n")
    lines.append(f"**摘要 (英文)**: {abstract}\n\n")
    lines.append(f"**摘要 (中文)**: [待翻译]\n\n")
    lines.append("---\n\n")

content = ''.join(lines)
with open('papers_cs.CL_2026-05-12.md', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Generated stub markdown with {len(data)} papers")