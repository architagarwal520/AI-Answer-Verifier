# Program to measure similarity between 
# two sentences using cosine similarity. 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 








def  givKeywordsValue(X,Y):

    # tokenization 
    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y) 

    # sw contains the list of stopwords 
    sw = stopwords.words('english') 
    l1 =[];l2 =[] 

    # remove stop words from string 
    X_set = {w for w in X_list if not w in sw} 
    Y_set = {w for w in Y_list if not w in sw} 

    # form a set containing keywords of both strings 
    rvector = X_set.union(Y_set) 
    for w in rvector: 
	    if w in X_set: l1.append(1) # create a vector 
	    else: l1.append(0) 
	    if w in Y_set: l2.append(1) 
	    else: l2.append(0) 
    c = 0

    # cosine formula 
    for i in range(len(rvector)): 
		    c+= l1[i]*l2[i] 
    cosine = c / float((sum(l1)*sum(l2))**0.5) 
    cosine=cosine*100
    if cosine > 90:
            kval = 1
    elif cosine > 80:
            kval = 2
    elif cosine > 60:
            kval = 3
    elif cosine > 40:
            kval = 4
    elif cosine > 20:
            kval = 5
    else:
            kval = 6
    
    return kval





