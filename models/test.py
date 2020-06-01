
from models.qst import qstcal
from models.cosine import givKeywordsValue
from models.grammarcheck import grammarcal



def testcal(X,Y,Z):
    k=givKeywordsValue(Y,Z)
    g=grammarcal(Y,k)
    q=qstcal(X,Y)
    return [k,g,q]


