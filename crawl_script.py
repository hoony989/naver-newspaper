
import sys
import os
from datetime import datetime

# Add current directory to path so we can import app
sys.path.append(os.getcwd())

from app import crawl_naver_news

def run_crawl():
    query = "AX"
    print(f"Crawling Naver News for '{query}'...")
    results = crawl_naver_news(query, max_items=20)
    
    if not results:
        print("No results found.")
        return

    now = datetime.now()
    filename = f"ax_news_report_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"네이버 뉴스 검색 결과: '{query}'\n")
        f.write(f"수집 일시: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 50 + "\n\n")
        
        for item in results:
            f.write(f"제목: {item['title']}\n")
            f.write(f"출처: {item.get('source', 'Unknown')}\n")
            f.write(f"내용: {item.get('snippet', '')}\n")
            f.write(f"링크: {item['link']}\n")
            f.write("-" * 30 + "\n")
            
    print(f"Saved to {filename}")

if __name__ == "__main__":
    run_crawl()
