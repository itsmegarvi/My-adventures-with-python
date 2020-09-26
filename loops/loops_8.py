# QUESTION: Print the following pattern using for loop
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1

def pattern(num):
    k = num
    for i in range(num):
        for j in range (k - i , 0 , -1):
            print (j, end = " ")
            i -= 1
        print("\n")

pattern(5)
