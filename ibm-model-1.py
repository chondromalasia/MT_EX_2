#!/usr/bin/python


"""
In which we try to implement the IBM Model 1 algorithm
"""

import itertools

## Trivial example
f_sentences = ["das Haus", "das Buch", "ein Buch"]
e_sentences = ["the house", "the book", "a book"]

## See whether word order has any effect on the result
# f_sentences = ["klein ist das Haus", "ein Haus ist gut"]
# e_sentences = ["the house is small", "a house is good"]

## Simulate lemmatization and see whether the probabilities change. Compare
#f_sentences = ["er kann sein neues Auto fahren", "das Auto kann neu sein"]
#e_sentences = ["he can drive his new car", "the car can be new"]
## to
#f_sentences = ["er koennen sein neu Auto fahren", "das Auto koennen neu sein"]
#e_sentences = ["he can drive his new car", "the car can be new"]

## Initialize the dictionaries
## 'count' holds the sum of all translation probabilities t[e_f] for each pair e_f 
##    normalized with the current s_total for the e_word
count = {}
## 'total' holds the sum of all translation probabilities t[e_f] for each f_word 
##    normalized with the current s_total for the e_word
total = {}
## 's_total' holds the sum of all translation probabilities t[e_f] for each e_word
s_total = {}	
## 't' holds the translation probability for each pair e_f
t = {} 
## the e_ and f_vocabularies
e_vocab = {}
f_vocab = {}

## collect the e_vocabulary in a dictionary
for e_sent in e_sentences:
	e_word_list = e_sent.split()
	## collect the e_vocabulary
	for e_word in e_word_list:
		e_vocab[e_word] = 1

## collect the f_vocabulary in a dictionary
for f_sent in f_sentences:
	f_word_list = f_sent.split()
	## collect the f_vocabulary
	for f_word in f_word_list:
		f_vocab[f_word] = 1
		## initialize total keys for each f_word 
		total[f_word] = 0

# initialize t(e|f) uniformly
for e_word in e_vocab.keys():
	for f_word in f_vocab.keys():
		e_f = e_word + f_word
		t[e_f] = 0.5
		## initialize count keys for all word pairs
		count[e_f] = 0

# i_counter counts the number of iterations
i_counter = 1

while i_counter <= 5:
        i_counter += 1
        print 'sentence'

        # intialize count
        for pair in count:
                count[pair] = 0

        # initialize total
        for word in total:
                total[word] = 0

        # now I mash up the sentances
        all_sents = itertools.izip(f_sentences, e_sentences)

        # and iterate through it
        for sent in all_sents:

                # go through all words e
                for e_word in sent[1].split():
                        # initialize e
                        s_total[e_word] = 0

                        # go through all foreign words
                        for f_word in sent[0].split():
                                s_total[e_word] += t[e_f]
                                
                #get counts
                for e_word in sent[1].split():
                       for f_word in sent[0].split():
                               e_f = e_word + f_word
                               count[e_f] += (t[e_f]/s_total[e_word])
                               total[word] += (t[e_f]/s_total[e_word])

        # do the probabilities
        for f_word in sent[0].split:
                for e_word in sent[1].split():
                        e_f = e_word + f_word
                        t[e_f] = (count[e_f] / total[word])
                        print e_f, t[e_f]
                               
