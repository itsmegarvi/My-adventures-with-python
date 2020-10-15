# QUESTION:  Check if a value 200 exists in a dictionary
#sampleDict = {'a': 100, 'b': 200, 'c': 300}
#Expected output: True

def valcheck(dict , val):
    return val in dict.values()

sampleDict = {'a': 100, 'b': 200, 'c': 300}
valcheck(sampleDict , 200)
