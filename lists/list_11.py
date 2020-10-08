# QUESTION: Given a Python list, remove all occurrence of 20 from the list
#list1 = [5, 20, 15, 20, 25, 50, 20]
#Expected output: [5, 15, 25, 50]

def removevalue(list , num):
    return [item for item in list if item != num]

list1 = [5, 20, 15, 20, 25, 50, 20]
removevalue(list1,20)
    
