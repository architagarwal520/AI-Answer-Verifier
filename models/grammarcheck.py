import requests
from models.cosine import givKeywordsValue
from models.qst import qstcal




def grammarcal(Y,k):
    req = requests.get("https://api.textgears.com/check.php?text=" + Y + "&key=JmcxHCCPZ7jfXLF6")
    no_of_errors = len(req.json()['errors'])


    if no_of_errors > 5 or k == 6:
            g = 0
    else:    
        no_words=len(Y.split())
        if no_words<15:
                g=0
        else: 
                g = 1

    return g




