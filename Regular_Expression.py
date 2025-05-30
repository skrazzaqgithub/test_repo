import re
str = 'Myself abdul and im in bengaluru'
x = re.findall('u', str)
print(x)

import re
str = 'Myself abdul and im in bengaluru'
x = re.search('ab', str)
print(x.start())

import re
str = 'Myself abdul and im in bengaluru'
x = re.search('ab', str)
print(x.span())

import re
str = 'Myself abdul and im in bengaluru'
x = re.search('im', str)
print(x.string)

import re
str = 'Myself abdul and im in bengaluru'
x = re.split(" ", str, 2)
print(x)

import re
str = 'Myself abdul and im in bengaluru im'
x = re.sub("im", "live", str, 1)
print(x)

import re
prog = re.compile(r'm\w\w')
str = 'cat mat bat rat'
result = prog.search(str)
print(result.group())
prog = re.compile(r'c\w\w')
str1 = 'sophisticate'
result = prog.search(str1)
print(result.group())