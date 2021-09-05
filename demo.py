# -*- coding: utf-8 -*-
from gensim.models import word2vec
from gensim import models
import logging
def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = models.Word2Vec.load('word2vec.model')
    print("input one word to find the most relationship word")
    print("input two word to find the relationship of this two word")
    print("input three word to analog")
    while True:
        try:
            query = input()
            q_list = query.split()
            if len(q_list) == 1:
                print("the most relationship wiki keyword")
                res = model.wv.most_similar(q_list[0],topn = 12)
                for item in res:
                    print(item[0])
            elif len(q_list) == 2:
                print("the most relationship wiki keyword")
                res = model.wv.most_similar(q_list[0])
                for item in res:
                    print(item[0])
            else:
                print("under is the most relationship wiki keyword")
                res = model.wv.most_similar([q_list[0],q_list[1]], [q_list[2]],topn= 12)
                for item in res:
                    print(item[0])
        except Exception as e:
            print(repr(e))
if __name__ == "__main__":
	main()