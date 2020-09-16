# QUESTION: print a file in all uppercase letters

fh = open("mbox-short.txt", "r")
for line in fh:
    print(line.strip().upper())
