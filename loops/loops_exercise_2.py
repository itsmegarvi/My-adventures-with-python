# QUESTION: Given numbers N, find all factors of it.Assumption - N can be in range of 1-100000.

N = input("Enter number please: ")
try:
    0 < int(N) < 100001
except:
    print ("Number should be b\w 1 to 100000 ")
    quit()
print ("The factors of N are - ")
n = 1
while n <= int(N):
     if int(N) % n == 0:
         print (n)
     n = n + 1



# QUESTION: Given an integer N, print the sequence of integers from N to 0 using do-while statement.
N = input('Enter number please: ')

while int(N) != 0:
     if int(N) > 0:
         print (N )
         N = int(N) - 1
     else:
         print(N )
         N = int(N) + 1
print(0)

# QUESTION: Given an integer N, print the number of digits in N.
#attempt 2
N = int(input('Enter number please: '))

count = 0
while N != 0:
      N //= 10
      count += 1
print(count)


# QUESTION: Given an integer N, print the sum of the digits in the number.
N = int(input('Enter number please: '))
sum = 0
while N != 0:
      a = N % 10
      N //= 10
      # we need to use integer division not float division
      sum += a
print (sum)


# QUESTION: Given an integer N, print the digits of number N in reverse order.

N = int(input('Enter number please: '))
