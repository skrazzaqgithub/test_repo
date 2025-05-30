# lst = ['A2','B3','C10']
# o/p = ['AA','BBB'.'CCCCCCCCCC']
lst = ['A2','B3','C10']
output = []
for i in lst:
    char = i[0]
    num = i[1:]
    output.append(char*int(num))
print(output)

# list1 = [1,2,3,4]
# list2 = [1,3]
# output = [2,4]
list1 = [1,2,3,4]
list2 = [1,3]
output = []
for i in list1:
    if i not in list2:
        output.append(i)
print(output)