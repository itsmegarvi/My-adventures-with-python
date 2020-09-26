# QUESTION: Display Fibonacci series up to 10 terms

def fibonacci(num1 , num2 , int):
    count = 0
    while count < int:
        print (num1 , end = " ")
        sum = num1 + num2
        num1 = num2
        num2 = sum
        count += 1
    print()
