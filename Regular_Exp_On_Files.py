"""
A Python program to create a regular expression that reads email-ids from a text file
"""
# with open("API_Testing_Skills.txt", 'r') as file:
#     data = file.read()
#     print(data)
#     for line in file:
#         result = re.findall(r'\S+@\S+', line)
#         if len(result)>0:
#             print(res)
import re
f = open("API_Testing_Skills.txt", 'r')
for line in f:
    result = re.findall(r'\S+@\S+', line)
    if len(result)>0:
        print(result)
f.close()

# import re
# f1 = open("salaries.txt", 'r')
# f2 = open("salaries1.txt", 'w')
# for line in f1:
#     result1 = re.search(r'\d{4}', line)
#     result2 = re.search(r'\d{5,}.\d{2}', line)
#     print(result1.group(), result2.group())
#     f2.write(result1.group()+"\t")
#     f2.write(result2.group()+"\n")
# f1.close()
# f2.close()