# QUESTION: concatenate two lists index-wise
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]
# Expected output: ['My', 'name', 'is', 'Kelly']


def concatenate(a , b):
    List = list()
    length = max(len(a), len(b))
    for i in range(length) :
        List.append(a[i] + b[i])
    print (List)

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
concatenate(list1, list2)
