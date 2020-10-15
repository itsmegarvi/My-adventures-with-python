# QUESTION: Below are the two lists convert it into the dictionary
#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]

#The simpler code
def list_dic(l1 , l2):
    return dict(zip(l1 ,l2))

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

list_dic(keys , values)
#my first code
#def list_dic(l1 , l2):
#    dict = {}
#        for j in l2:
#            dict[i] = j
#    return dict
