# QUESTION: Initialize dictionary with default values
#Given: employees = ['Kelly', 'Emma', 'John']
#defaults = {"designation": 'Application Developer', "salary": 8000}

def dictintialize(x , y ):
    dictionary = dict.fromkeys(x , y)
    return dictionary

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
dictintialize(employees , defaults)        
