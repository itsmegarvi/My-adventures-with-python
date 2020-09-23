# QUESTION: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list
def listmerge(list1 , list2):
    result_list = list()
    for i in range(len(list1)):
        if list1[i] % 2 != 0:
            result_list.append(list1[i])
        else:continue
    for j in range(len(list2)):
        if list2[j] % 2 == 0:
            result_list.append(list2[j])
    print (result_list)

First_List = [10, 20, 23, 11, 17]
Second_List = [13, 43, 24, 36, 12]

listmerge(First_list , Second_list)
