# QUESTION: Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it.
# And also it must return both addition and subtraction in a single return call.

def calculation(num1 , num2):
    sum = num1 + num2
    subtraction = num1 - num2 
    return (sum , subtraction)
