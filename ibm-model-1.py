## IBM Model 1

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


### Your implementation of the algorithm
### The algorithm should perform 5 iterations
### The output must look like the one showed in the exercise description :)
