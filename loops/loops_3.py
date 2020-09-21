# QUESTION: Accept number from user and calculate the sum of all number between 1 and given number.
N = int(input('Enter number please: '))
sum = 0
for i in range(1 ,N + 1):
    sum += i
print (sum)     
