# QUESTION: Given a string, display only those characters which are present at an even index number.
N = input()
print ("Original string is ",N)
print ("Printing only even number characters.")
for i in range(len(N)):
    if i % 2 == 0:
      print(N[i])
    else:
      continue
