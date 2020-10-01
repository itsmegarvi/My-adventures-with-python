# QUESTION: Find all occurrences of “USA” in given string ignoring the case
#Given: str1 = "Welcome to USA. usa awesome, isn't it?"

 def occurrence(s1 , s2):
     count =  s2.lower().count(s1.lower())
     print(f"The {s1} count is: {count}" )
