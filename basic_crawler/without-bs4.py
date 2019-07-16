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

        for link in links:
            if link.startswith('mailto:') or link.startswith('tel:'):
                links.remove(link)

        return title[0], links, current_time, data


# URL to crawl
URL = 'https://stallman.org'

c = Crawler(URL)
title, links, current_time, source_code = c.crawl()

print('Title: {}'.format(title))

for link in links:
    print('Found URL: {} at {}'.format(link, current_time))

print('\nComplete source code: {}'.format(source_code))
