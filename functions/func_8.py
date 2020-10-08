# QUESTION: 1's complement
#Given an integer N as input, find 1's complement of N.
#Input:5
#where: First line represents the value of N.
#Output: 2
#Assumption: Value of N can be in the range 0 to 10000.

def flip(c):
    print("1" if c == 0 else "0")
def complement(N):
    print ("N is : ",N)
    n = len(N)
    ones = ""
    for i in range(n):
        ones += flip(bin[i])
