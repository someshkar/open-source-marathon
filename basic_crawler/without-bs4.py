import re
import requests
from datetime import datetime


class Crawler:
    def __init__(self, url):
        self.url = url

    def crawl(self):
        r = requests.get(self.url)
        data = r.content

        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')

        title = re.findall(r'<title>(.*?)</title>', str(data))
        links = re.findall(r'<a href="(.*?)"', str(data))

        return title[0], links, current_time


# URL to crawl
URL = 'https://stallman.org'

c = Crawler(URL)
title, links, current_time = c.crawl()

print('Title: {}'.format(title))

for link in links:
    print('Found URL: {} at {}'.format(link, current_time))
