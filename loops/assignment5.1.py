# QUESTION: Write a program which repeatedly reads numbers untill user enters 'done'.once  user enters done print total, count and average.
N = input()
x = 0
count = 0
while N != 'done':
     try:
         N = int(N)
         print('Enter a number: ' + str(N))
         count += 1
         x += N
     except:
         print('Enter a number: bad data')
         print('Invalid input')
     if N == 'done':
         break
     N = input()
print('Enter a number: done')
print (x , count , x / count )
