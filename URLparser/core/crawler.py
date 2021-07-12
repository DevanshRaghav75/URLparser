from URLparser.core.colors import GREEN, GRAY, RESET, YELLOW
from URLparser.core.Extractor import Extractor
total_urls_visited = 0

def crawl(url, max_urls=30):
    global total_urls_visited
    total_urls_visited += 1
    print(f"{YELLOW}[*] Crawling: {url}{RESET}")
    links = Extractor(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)
