"""
A Python program to create a regular expression to search whether a
given string is starting with 'He' or not
"""

import re
str = "He is in Bengaluru"
result = re.findall(r"^He", str)
print(result)
if result:
    print("String is starting with 'He'")
else:
    print("String is not starting with 'He'")

"""
A Python program to create a regular expression to search whether a
given string is ending with 'Bengaluru' or not
"""

import re
str = "He is in Bengaluru"
result = re.findall(r"Bengaluru$", str)
print(result)
if result:
    print("String is starting with 'Bengaluru'")
else:
    print("String is not starting with 'Bengaluru'")

"""
A Python program to create a regular expression to search 
at the ending of a string by ignoring the case.
"""

import re
str = "He is in Bengaluru"
result = re.findall(r"bengaluru$", str, re.IGNORECASE) # ignoring the case-sensitive string
print(result)
if result:
    print("String is starting with 'Bengaluru'")
else:
    print("String is not starting with 'Bengaluru'")

"""
A Python program to create a regular expression to search 
at the ending of a string by ignoring the case.
"""
import re
str = "Rajju got 59 marks, Shabbu got 81 marks, Zahra got 99 marks."
result = re.findall('\d{2}', str) # ignoring the case-sensitive string
print(result)
names = re.findall('[A-Z][a-z]*', str)
print(names)

"""
A Python program to create a regular expression to retrieve
the timings either 'am' or 'pm'.
"""
import re
str = "Rajju got 59 marks at 9pm, Shabbu got 81 marks at 7am, Zahra got 99 marks at 1pm."
result = re.findall('\dam|\dpm', str) # ignoring the case-sensitive string
print(result)
