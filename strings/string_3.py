# QUESTION: Given a list of numbers, return True if first and last number of a list is same.
def listt(list):
    if list[0] == list[- 1]:
        return True
    else:
        return False

list1 = input().split()

print("Given list is ", list1)
listt(list1)
