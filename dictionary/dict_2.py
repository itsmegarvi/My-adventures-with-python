# QUESTION: Merge following two Python dictionaries into one
#dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

def dictmerge(dc1 , dc2):
    return {**dict1 , **dict2}

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dictmerge(dict1 , dict2)
