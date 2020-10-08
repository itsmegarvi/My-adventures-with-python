# QUESTION: Given a Python list. Turn every item of a list into its square
#aList = [1, 2, 3, 4, 5, 6, 7]
#Expected output: [1, 4, 9, 16, 25, 36, 49]

def listsquare(list1):
    list1 = [x**2 for x in list1]
    print(list1)

aList = [1, 2, 3, 4, 5, 6, 7]
listsquare(aList)
