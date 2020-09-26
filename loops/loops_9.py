# QUESTION: Reverse a given number and return true if it is the same as the original number.
def reversecheck(num):
    print("Original number",num)
    originalnum = num
    reversenum = 0
    while num != 0:
        remainder = num % 10
        reversenum = (reversenum * 10) + remainder
        num //= 10
    if originalnum == reversenum:
        print("The original and reverse  number are same")
    else:
        print("The original and reverse number ae not the same")
