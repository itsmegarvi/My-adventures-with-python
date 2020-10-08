# QUESTION: Concatenate two lists in the following order
#list1 = ["Hello ", "take "] ; list2 = ["Dear", "Sir"]
#Expected output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def permlist(list1 , list2):
    output_list = list()
    for i in list1:
        for j in list2:
            output_list.append(i + j)

    print (output_list)


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

permlist(list1 , list2)

#shorter_version

#def permlist(list1 , list2):
#    output_list = list()
#    output_list = [i + j for i in list1 for j in list2]
#    print (output_list)
