#!/usr/bin/env python3
"""
Papers.cool 论文爬虫脚本
爬取指定日期的 arXiv 论文信息

使用方法:
    python papers_cool_crawler.py <URL>
    python papers_cool_crawler.py "https://papers.cool/arxiv/cs.IR?date=2026-04-08&show=50"
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import re
import sys


def crawl_papers_cool(url: str) -> list[dict]:
    """
    爬取 papers.cool 网站的论文列表
    
    Args:
        url: 目标网页 URL
        
    Returns:
        论文列表，每篇论文包含标题、作者、摘要、分类等信息
    """
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    
    print(f"正在请求：{url}")
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        response.encoding = 'utf-8'
    except requests.RequestException as e:
        print(f"请求失败：{e}")
        return []
    
    print(f"响应状态码：{response.status_code}")
    
    # 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    papers = []
    
    # 根据实际 HTML 结构，论文在 div.panel.paper 中
    paper_items = soup.find_all('div', class_='panel paper')
    
    print(f"找到 {len(paper_items)} 篇论文")
    
    for idx, item in enumerate(paper_items, 1):
        paper = parse_paper_item(item, idx)
        if paper and paper.get('title'):
            papers.append(paper)
    
    return papers


def parse_paper_item(item, index: int) -> dict:
    """
    解析单个论文条目
    
    HTML 结构示例:
    <div id="2604.06098" class="panel paper" keywords="...">
        <h2 class="title">
            <a href="https://arxiv.org/abs/2604.06098" target="_blank" title="2/35">
                <span class="index notranslate">#2</span>
            </a>
            <a id="title-2604.06098" class="title-link notranslate" href="/arxiv/2604.06098" target="_blank">
                论文标题
            </a>
            ...
        </h2>
        <p id="authors-2604.06098" class="metainfo authors notranslate">
            <strong>Authors</strong>:
            <a class="author notranslate" href="...">作者 1</a>,
            <a class="author notranslate" href="...">作者 2</a>,
            ...
        </p>
        <p id="summary-2604.06098" class="summary notranslate">摘要内容</p>
        <p id="subjects-2604.06098" class="metainfo subjects">
            <strong>Subjects</strong>:
            <span class="interact-item">
                <a class="subject-1" href="...">分类 1</a>
            </span>,
            ...
        </p>
        <p id="date-2604.06098" class="metainfo date">
            <strong>Publish</strong>: <span class="date-data">2026-04-07 17:10:54 UTC</span>
        </p>
    </div>
    
    Args:
        item: BeautifulSoup 元素
        index: 论文序号
        
    Returns:
        论文信息字典
    """
    paper = {
        'index': index,
        'title': '',
        'arxiv_id': '',
        'arxiv_url': '',
        'pdf_url': '',
        'authors': [],
        'abstract': '',
        'subjects': [],
        'publish_time': '',
    }
    
    # 获取论文 ID (从 div 的 id 属性)
    paper_id = item.get('id', '')
    if paper_id:
        paper['arxiv_id'] = paper_id
        paper['arxiv_url'] = f"https://arxiv.org/abs/{paper_id}"
        paper['pdf_url'] = f"https://arxiv.org/pdf/{paper_id}"
    
    # 提取标题 - 从 a.title-link 元素
    title_elem = item.find('a', class_='title-link')
    if title_elem:
        paper['title'] = title_elem.get_text(strip=True)
    else:
        # 备用方法：从 h2.title 中提取
        h2_title = item.find('h2', class_='title')
        if h2_title:
            # 获取第一个包含 arxiv.org/abs 的链接
            arxiv_link = h2_title.find('a', href=lambda x: x and 'arxiv.org/abs/' in x)
            if arxiv_link:
                paper['title'] = arxiv_link.get_text(strip=True)
                if not paper['arxiv_id']:
                    paper['arxiv_id'] = arxiv_link['href'].split('/abs/')[-1]
                    paper['arxiv_url'] = arxiv_link['href']
                    paper['pdf_url'] = paper['arxiv_url'].replace('/abs/', '/pdf/')
    
    # 提取作者列表 - 从 p.metainfo.authors 中的 a.author 元素
    authors_elem = item.find('p', class_=lambda x: x and 'authors' in x if x else False)
    if authors_elem:
        author_links = authors_elem.find_all('a', class_='author')
        paper['authors'] = [a.get_text(strip=True) for a in author_links]
    
    # 提取摘要 - 从 p.summary 元素
    summary_elem = item.find('p', class_='summary')
    if summary_elem:
        paper['abstract'] = summary_elem.get_text(strip=True)
    
    # 提取主题分类 - 从 p.metainfo.subjects 中的链接
    subjects_elem = item.find('p', class_=lambda x: x and 'subjects' in x if x else False)
    if subjects_elem:
        subject_links = subjects_elem.find_all('a')
        paper['subjects'] = [s.get_text(strip=True) for s in subject_links]
    
    # 提取发布时间 - 从 span.date-data 元素
    date_elem = item.find('span', class_='date-data')
    if date_elem:
        paper['publish_time'] = date_elem.get_text(strip=True)
    
    return paper


def save_to_json(papers: list[dict], filename: str):
    """保存论文列表到 JSON 文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    print(f"已保存 {len(papers)} 篇论文到 {filename}")


def save_to_markdown(papers: list[dict], filename: str):
    """保存论文列表到 Markdown 文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# arXiv 论文列表\n\n")
        f.write(f"爬取时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"论文总数：{len(papers)}\n\n")
        f.write("---\n\n")
        
        for paper in papers:
            f.write(f"## {paper['index']}. {paper['title']}\n\n")
            
            if paper['arxiv_id']:
                f.write(f"**arXiv ID**: [{paper['arxiv_id']}]({paper['arxiv_url']})\n\n")
            
            if paper['pdf_url']:
                f.write(f"**PDF**: [下载]({paper['pdf_url']})\n\n")
            
            if paper['authors']:
                f.write(f"**作者**: {', '.join(paper['authors'])}\n\n")
            
            if paper['abstract']:
                f.write(f"**摘要**: {paper['abstract']}\n\n")
            
            if paper['subjects']:
                f.write(f"**分类**: {', '.join(paper['subjects'])}\n\n")
            
            if paper['publish_time']:
                f.write(f"**发布时间**: {paper['publish_time']}\n\n")
            
            f.write("---\n\n")
    
    print(f"已保存 {len(papers)} 篇论文到 {filename}")


def main():
    """主函数"""
    # 从命令行参数获取 URL
    if len(sys.argv) < 2:
        print("使用方法：python3 papers_cool_crawler.py <URL>")
        print("示例：python3 papers_cool_crawler.py https://papers.cool/arxiv/cs.IR?date=2026-04-08&show=50")
        sys.exit(1)
    
    url = sys.argv[1]
    
    print("=" * 60)
    print("Papers.cool 论文爬虫")
    print("=" * 60)
    
    # 爬取论文
    papers = crawl_papers_cool(url)
    
    if not papers:
        print("未能获取到论文数据，请检查网络连接或页面结构是否发生变化")
        return
    
    print(f"\n成功爬取 {len(papers)} 篇论文")
    
    # 从 URL 中提取日期作为文件名的一部分
    # URL 格式：https://papers.cool/arxiv/cs.IR?date=2026-04-08&show=50
    import urllib.parse as urlparse
    parsed = urlparse.urlparse(url)
    params = urlparse.parse_qs(parsed.query)
    date_str = params.get('date', ['unknown'])[0]
    category = parsed.path.split('/')[-1] if parsed.path else 'papers'
    
    # 文件名使用日期和分类
    filename_prefix = f"papers_{category}_{date_str}"
    
    # 保存为 JSON
    json_file = f"{filename_prefix}.json"
    save_to_json(papers, json_file)
    
    # 保存为 Markdown
    md_file = f"{filename_prefix}.md"
    save_to_markdown(papers, md_file)
    
    # 打印前 5 篇论文预览
    print("\n" + "=" * 60)
    print("前 5 篇论文预览:")
    print("=" * 60)
    
    for paper in papers[:5]:
        print(f"\n[{paper['index']}] {paper['title']}")
        if paper['authors']:
            authors_str = ', '.join(paper['authors'][:3])
            if len(paper['authors']) > 3:
                authors_str += f" ... (共{len(paper['authors'])}人)"
            print(f"    作者：{authors_str}")
        if paper['arxiv_id']:
            print(f"    arXiv: {paper['arxiv_id']}")
        if paper['subjects']:
            print(f"    分类：{', '.join(paper['subjects'])}")


if __name__ == "__main__":
    main()
