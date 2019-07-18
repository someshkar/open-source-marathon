from crawler import Crawler
from parser import Parser
from indexer import Indexer
from ranker import Ranker
from pprint import PrettyPrinter
import json

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
inverted_index, original_words = i.index()

pp = PrettyPrinter(indent=4)
pp.pprint(inverted_index)

with open('db.json', 'w') as json_file:
    json.dump(inverted_index, json_file)

query = 'NASA'

r = Ranker(query, links_with_words, original_words, inverted_index)
r.rank()
