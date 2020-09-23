# QUESTION: Print the following pattern
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

def numrally(num):
    for i in range(num + 1):
        n = 0
        while n < i - 1 :
            print (i , end = " ")
            n += 1
        if n == i - 1 :
            print (i)
            continue

numrally(5)

            
