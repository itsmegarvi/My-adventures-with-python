# QUESTION: Swap value of two numbers
#Given two integers N1 and N2, interchange values of the variable and print it.
#Input:4, 10
#Output:10  4

def numswap(N1 , N2):
    a = N1
    b = N2
    N1 = b
    N2 = a
    print (N1,end= " ")
    print(N2)


numswap(4 , 10)
