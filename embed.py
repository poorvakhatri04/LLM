import gensim.downloader as api
import numpy as np
model = api.load("glove-wiki-gigaword-100")  # ~350 MB
word_vectors=model
#print(word_vectors['computer'])
print(word_vectors['cat'].shape) #100
print(word_vectors.most_similar(positive=['king','woman'],negative=['man'],topn=10))
print(word_vectors.similarity('woman','man'))
print(word_vectors.most_similar("tower",topn=5))
word1='is'
word2='the'
vec_diff=model[word1]-model[word2]
mag=np.linalg.norm(vec_diff)
print("The magnitude of the difference between '{}' and '{}' is {:.2f}".format(word1,word2,mag))