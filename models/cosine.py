# Program to measure similarity between 
# two sentences using cosine similarity. 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.corpus import wordnet 
from nltk.stem import PorterStemmer 







def  givKeywordsValue(X,Y):
				
	# X answers
	# Y keywords

	ps = PorterStemmer() 

	# tokenization 
	X_list = word_tokenize(X)
	Y_list = word_tokenize(Y) 

	# sw contains the list of stopwords 
	sw = stopwords.words('english') 
	l1 =[];l2 =[] 

	# remove stop words from string 
	X_set = {w for w in X_list if not w in sw} 
	Y_set = {w for w in Y_list if not w in sw} 

	# syn_key=[]
				

	# for word in Y_set:
	# 	syn_key.append(word)
	# 	for syn in wordnet.synsets(word):
	# 		for l in syn.lemmas():
	# 			syn_key.append(ps.stem(l.name()))
				

	# syn_key=set(syn_key)     
	# # print("syn keys:",syn_key)                      

	# form a set containing keywords of both strings 
	rvector = Y_set
	print("idf:",rvector)
	print("length of idf",len(rvector))
	#Y_listing=list(Y_set)
	for i in range(len(rvector)):
		l2.append(1)
	for w in rvector: 
		print("w is:",w)
		if w in X_set: 
			print("appended 1 for:",w)
			l1.append(1) # create a vector 
		else:
			if len(wordnet.synsets(w))==0:
				l1.append(1)
				continue
			for syn in wordnet.synsets(w):
				for l in syn.lemmas():
					name=l.name()
					if name in X_set:
						l1.append(1)
						print("appended 1 for:",w,"and",name)
						break
					else:
						l1.append(0)
						print("appended 0 for:",w)
						break
				break
		
	
	print("l1:",l1)
	print("length of l1",len(l1))
	print("l2:",l2)
	print("length of l2",len(l2))
	c = 0
	# cosine formula 
	for i in range(len(rvector)): 
			c+= l1[i]*l2[i] 
	if sum(l1)==0:
		cosine=0		
	else:
		cosine = c / float((sum(l1)*sum(l2))**0.5) 
		cosine=cosine*100
	if cosine > 80:
			kval = 1
	elif cosine > 70:
			kval = 2
	elif cosine > 60:
			kval = 3
	elif cosine > 50:
			kval = 4
	elif cosine > 40:
			kval = 5
	else:
			kval = 6
				
	return kval





