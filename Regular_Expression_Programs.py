"""
A Python program to create a regular expression to search for strings
starting with m and having total 3 characters using the search() method
"""

import re
str = 'man sun mop run'
result = re.search(r'm\w\w', str)
if result:
    print(result.group())

"""
A Python program to create a regular expression to search for strings
starting with m and having total 3 characters using the findall() method
"""
import re
str = 'man sun mop run'
result = re.findall(r'm\w\w', str)
print(result)

"""
A Python program to create a regular expression using the match() method to 
search for strings starting with m and having total 3 characters
"""
import re
str = 'map sun mop run'
result = re.match(r'm\w\w', str)
print(result.group())

"""
A Python program to create a regular expression using the match() method to 
search for strings starting with m and having total 3 characters
"""
import re
str = 'sun mop run nor'
result = re.match(r'm\w\w', str)
print(result)

"""
A Python program to create a regular expression to split a 
string into pieces where one or more alpha numeric characters are found.
"""
import re
str = '234 This; is the: "Core" python\'s book'
result = re.split(r'\W+', str)
print(result)

"""
A Python program to create a regular expression to replace a 
string with a new string.
"""
import re
str = 'Khumbamela will be conducted at ahmedabad in india'
result = re.sub(r'ahmedabad','allahabad', str)
print(result)

"""
A Python program to create a regular expression to retrieve all words
starting with 'a' in a given string
"""

import re
str = "my name is abdul razzaq and i live in bengaluru"
result = re.findall(r'a[\w]*', str)
for i in result:
    print(i)

"""
A Python program to create a regular expression to retrieve all words
starting with numeric digit
"""
import re
str = "my name is abdul razzaq and i live in bengaluru since 1st of 5mar"
result = re.findall(r'\d[\w]*', str)
for i in result:
    print(i)

"""
A Python program to create a regular expression to retrieve all words
having 5 characters length
"""
import re
str = "my name is abdul razzaq and i live in bengaluru since 1st of 5mar"
result = re.findall(r'\b\w{5}\b', str)
for i in result:
    print(i)

"""
A Python program to create a regular expression to retrieve all words
having 5 characters length using search()
"""
import re
str = "my name is abdul razzaq and i live in bengaluru since 1st of 5mar"
result = re.search(r'\b\w{5}\b', str)
print(result.group())

"""
A Python program to create a regular expression to retrieve all words
having the length of atleast 4 characters
"""
import re
str = "my name is abdul razzaq and i live in bengaluru since 1st of 5mar"
result = re.findall(r'\b\w{4,}\b', str)
print(result)

"""
A Python program to create a regular expression to retrieve all words
with 3 or 4 or 5 characters length
"""
import re
str = "my name is abdul razzaq and i live in bengaluru since 1st of 5mar"
result = re.findall(r'\b\w{3,5}\b', str)
print(result)

"""
A Python program to create a regular expression to retrieve only
single digits from a strings.
"""
import re
str = "my name is abdul razzaq and i live in bengaluru since 1st of 5mar 8 9 10"
result = re.findall(r'\b\d\b', str)
print(result)

"""
A Python program to create a regular expression to 
retrieve the last word of a string if it starts with t
"""
import re
str = "my name is abdul razzaq and i live in bengaluru since 15th of march"
result = re.findall(r'm[\w]*\Z', str)
print(result)

"""
A Python program to create a regular expression to 
retrieve the mobile number of a person.
"""
import re
str = 'Nageswar Roa: 7348858348'
result = re.search(r'\d+', str)
print(result.group())

"""
A Python program to create a regular expression to 
retrieve only name but not the mobile number of a person.
"""
import re
str = 'Nageswar Roa: 7348858348'
result = re.search(r'\D+', str)
print(result.group())

"""
A Python program to create a regular expression to 
find all words starting with 'an' and 'ab'
retrieve only name but not the mobile number of a person.
"""
import re
str = "my name is abdul razzaq and i live in bengaluru since 15th of march"
result = re.findall(r'a[nb][\w]*', str)
print(result)

"""
A Python program to create a regular expression to retrieve
date of births from a string.
"""
import re
str = 'Razzaq 24-12-1989 Shabbu 17-02-1991 Zahra 22-11-2022 and Ammi 1-01-1973'
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result)