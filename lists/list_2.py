# QUESTION: Write a program to read through the mail box data andwhen you find line that starts with “From”, you will split the line intowords using the split function. We are interested in who sent the message, which is the second word on the From line.
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#From line, then you will also count the number of From (not From:) lines and print out a count at the end. This is a good sample output with a few lines removed:

fh = open("mbox-short.txt", "r")

count = 0
for line in fh:
    if not line.startswith('From'): continue
    x = line.split()
    print(x[1])
    count += 1

print ('There were ' + str(count) + ' lines in the file with From as the first word.')
