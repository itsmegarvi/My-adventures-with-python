# QUESTION: Download a copy of the file www.py4e.com/code3/romeo.txt.
#Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function.
#For each word, check to see if the word is already in a list. If the wordis not in the list, add it to the list. When the program completes, sortand print the resulting words in alphabetical order.
fname = ('Enter file name:')
fhand = open('fname', 'r')
list = []
for line in fhand:
    y = line.split()
    for word in y:
        if word not in list:
            list.append(word)
print (sorted(list))
