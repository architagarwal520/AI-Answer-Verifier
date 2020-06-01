import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from models.test import testcal


data = pd.read_csv('models/finaldataset.csv')

model = GaussianNB()


xf = data[['keyword', 'grammar', 'qst']]
x = np.array(xf.values)

yf = data[['class']]
y = np.array(yf.values).ravel()

##x_train,y_train,x_test,y_test=train_test_split(x,y,test_size=0.25,random_state=42)

model.fit(x,y)




def calc(X,Y,Z):
	predicted=model.predict([testcal(X,Y,Z)]) 
	print("keywords:",Z)
	print("Solution by student:",Y)
	val=int(predicted[0])*5/9
	predicted[0]=val
	sol=str(predicted[0])
	return sol


