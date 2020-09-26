# QUESTION: Print the following pattern
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

def numrally(num):
    for i in range(num + 1):
        n = 0
        while n < i :
            print (i , end = " ")
            n += 1
        print("\n")

numrally(5)
