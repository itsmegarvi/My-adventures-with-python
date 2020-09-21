# QUESTION: Python program to display all the prime numbers within a range.
start = int(input('start number: '))
end = int(input('end number: '))
for i in range (start , end ):
   for n in range (2 , i):
       if i % n == 0:
          break
#keep indentation of else in mind.
   else:
      print (i)
