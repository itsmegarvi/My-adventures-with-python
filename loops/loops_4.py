# QUESTION: Write a code to extract each digit from an integer, in the reverse order.

def reverseint(num):
    while num != 0:
        print (num % 10 , end = " ")
        num //= 10


reverseint(6457)
