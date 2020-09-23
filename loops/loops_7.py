# QUESTION: Print multiplication table form 1 to 10.

def numtable(num):
    for i in range(1 , num + 1):
        for j in range(1 , 11):
            print(i * j , end= " ")
        print("\n")

numtable(10)
