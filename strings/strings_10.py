# QUESTION: Split a given string on hyphens into several substrings and display each substring
# Given: str1 = Emma-is-a-data-scientist.

def stringsplit(str):
    string = str.split("-")
    for i in string:
        print (i)
