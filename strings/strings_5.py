# QUESTION: Arrange string characters such that lowercase letters should come first.

def stringsort(str):
    lower=[]
    upper=[]
    for i in str:
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)

    print("".join(lower + upper))      
