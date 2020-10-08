# QUESTION: Given a Python list you should be able to display Python list in the following order
# aLsit = [100, 200, 300, 400, 500]
# Expected output: [500, 400, 300, 200, 100]

alist = [100 ,200 ,300 ,400 ,500 ]
output = alist[ : : -1]
print (output)
