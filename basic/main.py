from crawler import Crawler
from parser import Parser
from indexer import Indexer
from pprint import PrettyPrinter

# URL to crawl
URL = 'https://techcrunch.com'

c = Crawler(URL)
title, links_and_data, current_time, main_source = c.crawl()

print('Title: {}\n'.format(title))

# for link in links:
#     print('Found URL: {} at {}'.format(link, current_time))

p = Parser(links_and_data)
links_with_words = p.parse()

i = Indexer(links_with_words)
inverted_index = i.index()

pp = PrettyPrinter(indent=4)
pp.pprint(inverted_index)
