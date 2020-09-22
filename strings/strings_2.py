# QUESTION: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string.
def removechar(str , n):
    return str[n : ]
string = input("Enter string plz: ")
N = int(input('Enter number plz: '))
print ("removing ", N ," characters of ",string )
removechar(string , N)


    
