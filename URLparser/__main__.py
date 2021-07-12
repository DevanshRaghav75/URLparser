#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import requests
import argparse
import colorama
from urllib.parse import urlparse, urljoin
from URLparser.core.colors import GREEN, GRAY, RESET, YELLOW, RED, CYAN
from URLparser.core.crawler import crawl
from URLparser.core.Extractor import Extractor, internal_urls, external_urls
from URLparser.core.validator import is_valid

colorama.init()

print('''
   __  ______  __                                   
  / / / / __ \/ /   ____  ____ ______________  _____
 / / / / /_/ / /   / __ \/ __ `/ ___/ ___/ _ \/ ___/
/ /_/ / _, _/ /___/ /_/ / /_/ / /  (__  )  __/ /    
\____/_/ |_/_____/ .___/\__,_/_/  /____/\___/_/   v1.0  
                /_/                                 
                        Coded with <3 by HS_Devansh_Raghav 
''')

def main():
    try:
        parser = argparse.ArgumentParser(description="A Fast Link Extractor")
        parser.add_argument('-u', '--url', help="Specify the url")
        parser.add_argument("-m", "--max-urls", help="Number of max URLs to crawl, default is 30.", default=30, type=int)
    
        args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
        url = args.url
        max_urls = args.max_urls

        crawl(url, max_urls=max_urls)

        print('')
        print('------------------------------------------------------------')
        print("[+] Total Internal links:", len(internal_urls))
        print("[+] Total External links:", len(external_urls))
        print("[+] Total URLs:", len(external_urls) + len(internal_urls))
        print("[+] Total crawled URLs:", max_urls)
        print("------------------------------------------------------------")
        domain_name = urlparse(url).netloc

        with open(f"{domain_name}_internal_links.txt", "w") as f:
            for internal_link in internal_urls:
                print(internal_link.strip(), file=f)

        with open(f"{domain_name}_external_links.txt", "w") as f:
            for external_link in external_urls:
                print(external_link.strip(), file=f)

    except requests.exceptions.MissingSchema:
        print(RED + "[-] " + RESET + "Invalid URL: " + url + " | eg. : https://google.com, https://bing.com, http://example.com")
    except KeyboardInterrupt:
        quit()