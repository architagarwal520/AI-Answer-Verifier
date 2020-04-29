from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
import math



def qstcal(X,Y):
    dict={1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    # Token Sort Ratio 
    qstval=fuzz.token_sort_ratio(X,Y) 
    qstval= math.ceil(qstval * 6 / 100)
    qstval=dict[qstval]
    return qstval




