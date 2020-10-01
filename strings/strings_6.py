# QUESTION: count all lower case, upper case, digits, and special symbols from a given string

def charcounter(str):
    char = 0
    digits = 0
    symbols = 0
    for i in str:
        if i.islower() or i.isupper():
            char += 1
        elif i.isnumeric():
            digits += 1
        else:
            symbols += 1
    print("Characters = ", char )
    print("Digits = ", digits)
    print("Special symbols = " , symbols)
