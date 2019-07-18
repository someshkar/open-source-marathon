import math


class Ranker:
    def __init__(self, query,
                 links_with_words, original_words, inverted_index):
        self.query = query
        self.links_with_words = links_with_words
        self.original_words = original_words
        self.inverted_index = inverted_index

    def TF(self, query, link):
        query_count = 0
        total_words = len(link.get('words'))

        for word in link['words']:
            if word == query:
                query_count = query_count + 1

        return query_count/total_words

    def IDF(self, query):
        total_links = len(self.links_with_words)
        total_links_with_query = len(self.inverted_index[query])
        return math.log(total_links/total_links_with_query)

    def rank(self):
        if self.query not in self.inverted_index:
            print('Query not found in index')
            return False

        ranked_links = {}

        for i in self.inverted_index[self.query]:
            for link in self.links_with_words:
                tf = self.TF(self.query, link)
                idf = self.IDF(self.query)
                ranked_links[link] = tf*idf

        print(ranked_links)
