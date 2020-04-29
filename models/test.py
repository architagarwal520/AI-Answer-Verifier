
from models.qst import qstcal
from models.cosine import givKeywordsValue
from models.grammarcheck import grammarcal



def testcal(X,Y):
    k=givKeywordsValue(X,Y)
    g=grammarcal(Y,k)
    q=qstcal(X,Y)
    return [k,g,q]


