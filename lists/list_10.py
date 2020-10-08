# QUESTION: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
#list1 = [5, 10, 15, 20, 25, 50, 20]
#Expected output: list1 = [5, 10, 15, 200, 25, 50, 20]

def numchange(list):
    x = list.index(20)
    list[x] = 200
    print(list)

list1 = [5, 10, 15, 20, 25, 50, 20]
numchange(list1)
