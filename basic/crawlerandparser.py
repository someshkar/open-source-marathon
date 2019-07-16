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


class Parser:
    def __init__(self, links):
        self.links = links

    def parse(self):
        links_with_words = {}
        for link in self.links:
            r = requests.get(link)
            source = r.content

            title = re.findall(r'<title>(.*?)</title>', str(source))[0]
            meta_description = re.findall(
                r'<meta name="description" content="(.*?)"', str(source))[0]

            if meta_description is not None:
                def removeSpecialChars(s): return re.sub(
                    '[^A-Za-z0-9]+', ' ', s)

                title = removeSpecialChars(title)
                meta_description = removeSpecialChars(meta_description)

                words = title.split() + meta_description.split()

                print('found {} at {}'.format(words, link))

                links_with_words[link] = words

        return links_with_words


# URL to crawl
URL = 'https://techcrunch.com'

c = Crawler(URL)
title, links, current_time, _ = c.crawl()

print('Title: {}'.format(title))

for link in links:
    print('Found URL: {} at {}'.format(link, current_time))


p = Parser(links)
links_with_words = p.parse()
