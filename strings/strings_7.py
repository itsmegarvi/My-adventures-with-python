# QUESTION: String characters balance Test
#We’ll say that a String s1 and s2 is balanced if all the chars in the s1 are there in s2. characters position doesn’t matter.

def stringbalance(s1 , s2):
    count = 0
    for char in s1:
        if char not in s2:
            print(False)
            break
        else:
            count += 1
    if count == len(s1):
        print(True)



#Alternate:
def stringbalance(s1 , s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
            break
    return flag
