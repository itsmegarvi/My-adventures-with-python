# QUESTION: You are given a string .
#Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

def stringvalidator(s):
    for method in [str.isalnum , str.isalpha , str.isnumeric , str.islower , str.isupper]:
        print any(method(char) for char in s)
