import re


class Indexer:
    def __init__(self, links_with_words):
        self.links_with_words = links_with_words

    def index(self):
        for words in self.links_with_words:
            for word in words:
                print('Word: ', word)
