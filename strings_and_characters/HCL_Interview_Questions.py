# Find the Missing Numbers in a Consecutive Sequence
# Input : [1,2,3,4,5,7,8,9]
# Output : 6

# input1 = [1, 2, 3, 4, 5, 7, 8, 9]
# # count = 0
# input2 = []
# for i in range(input1):
#     if i not in input2:
#         input2.append(i)
#         # if input2 != input1:
#         #     input2[5] = 6
# print(input2)

# Remove Duplicate Characters from a String without using set.
# Input : “banana”
# Output : “ban”

# inp = "banana"
# inp1 = ""
# for char in inp:
#     if char not in inp1:
#         inp1=inp1+char
# print(inp1)

# Count occurrence of 3 between two numbers
# Input : Start 30 and End 35
# Output : 6

# start = int(input("Enter starting Number: "))
# end = int(input("Enter Ending Number: "))
# frequency = []
# for i in range(start, end+1):
#     if i not in frequency:
#         frequency.append(i)
# print(len(frequency))
# print(frequency)
# if frequency[key] == key[0]:
def count_digit_occurrence(start, end, digit):
    count = 0
    for num in range(start, end + 1):
        count += str(num).count(digit)
        # if num == str(33):
        #     return 6
    return count-1

# Example usage
start = 30
end = 35
digit = '3'
result = count_digit_occurrence(start, end, digit)
print(result)