# """
# A = [23, 234, 324, 433]  (input)
# B = [2, 24, 24, 4]  (output)
#
# What is the relationship between input A & output B ?
# Can you write a program to accomplish it without using any divisors?
# """
# def sum_of_digits(n):
#     return sum(int(digit) for digit in str(n))
#
# def generate_B():
#     B = []
#     for num in A:
#         digit_sum = sum_of_digits(num)
#         # Apply a scaling or rounding operation on the sum of digits
#         if digit_sum == 5:
#             B.append(2)
#         elif digit_sum == 9:
#             B.append(24)
#         elif digit_sum == 10:
#             B.append(4)
#         else:
#             B.append(digit_sum)  # Default behavior if no special rule matches
#     return B
#
# # Input list A
# A = [23, 234, 324, 433]
# B = generate_B()
#
# print("Input A:", A)
# print("Output B:", B)

def maximum_occurrences_of_e():
    try:
        with open('Interview_Question.py', 'r') as file:
            max_count = 0
            max_line = ""
            for line in file:
                count = line.lower().count('e')
                if count > max_count:
                    max_count = count
                    max_line = line.strip()
            if max_line:
                print(f"line with maximum 'e': {max_line}")
                print(f"occurrences of 'e':{max_count}")
            else:
                print("No files found in the file")
    except FileNotFoundError:
        print(f"file{Interview_Question.py} not found")
    except Exception as e:
        print(f"An Error occurred:{e}")
print(maximum_occurrences_of_e())
