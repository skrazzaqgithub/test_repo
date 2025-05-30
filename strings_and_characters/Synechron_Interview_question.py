S = ['a', 'b', 'c', 'w', 'A', 'W']
# S = S[1:3:]
print(S)
S1 = []
for i in S:
    if i not in S1:
        S1.append(S[1:3:])
print(S1[0])