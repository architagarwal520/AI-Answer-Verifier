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

model.fit(x,y)




def calc(X,Y):
    predicted=model.predict([testcal(X,Y)])
    sol=str(predicted[0])
    return sol


