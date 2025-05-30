# // Input strings : ['ABC', 'D', 'EF']
# // output should be displayed as : A D E B F C

def interleave_strings(strings):
    max_length = max(len(s) for s in strings)
    result = []
    for i in range(max_length):
        for s in strings:
            if i < len(s):
                result.append(s[i])
    return ' '.join(result)
input_string = ['ABC', 'D', 'EF']
output = interleave_strings(input_string)
print(output)