# QUESTION: Given a string of odd length greater 7, return a string made of the middle three chars of a given String.
def midstring(str):
    length = len(str)
    print(str[length//2 - 1 :(length//2) + 2])

midstring("JasonAy")    
