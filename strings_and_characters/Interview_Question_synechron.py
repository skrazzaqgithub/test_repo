# X= {"glossary": {"title": "example glossary", "GlossDiv": {"title": "S","GlossList": {"GlossEntry": {"ID": "SGML", "SortAs": "SGML","GlossTerm": "Standard Generalized Markup Language", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"} } } } }
#
# output = X['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso']
# print(output)

# S = ['a', 'b', 'w', 'A', 'W', 'c']
# # print(S)
# S1 = []
# count = 0
# while S>len(S):
#     if str(S) == 'b' and str(S) == 'c':
#         S1.append(S)
#         count += 1
# print(S1)

# Create an empty list to store the unique elements
# unique_elements = []
def unique_elements(S):
    S1 = []
    for i in S:
        if str(i) == 'b':
            S1.append(str(i))
        elif str(i) == 'c':
            S1.append(str(i))
    return set(S1)
# S = ['a', 'b', 'w', 'A', 'W', 'c']
S = ['a', 'b', 'b', 'w', 'A', 'W', 'c', 'a', 'c']
output = unique_elements(S)
print(output)



# Loop through each element in the list
# for i in range(len(S)):
#     # Count occurrences of the current element in the list
#     count = 0
#     for j in range(len(S)):
#         if S[i] == S[j]:
#             count += 1
#
#     # If the element occurs only once, add it to the unique_elements list
#     if count == 1:
#         unique_elements.append(S[i])
#
# # Print the unique elements
# for element in unique_elements:
#     print(element)

# for i in range(len(S)):
#     if i not in S1:
#         S1.append(i)
# print(S1[0])