# QUESTION: Find avg. in a loop.
print('Before')
sanji = 0
luffy = 0
for thing in [9 , 41, 12 , 3 , 74 , 15]:
     sanji += 1
     luffy = luffy + thing
     print (sanji , luffy)
avg = luffy / sanji
print ('After', avg)


# QUESTION: Print smallest number
#smallest number
#smallest number
smallest_number = None
for chopper in [9 , 41 , 12 , 3 , 74 , 15]:
     if smallest_number is None:
          smallest_number = chopper
     elif chopper < smallest_number:
          smallest_number = chopper

print (smallest_number  )


# QUESTION: print all prime numbers till N
N = int(input('Enter number please: '))
n = 2
count = 0
for i in range (2, N):
       if i % n == 0:
       count += 1
