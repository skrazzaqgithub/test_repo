"""
Write a Python script that takes a file name as its argument.
In that file, find the line that has the maximum number of
occurrences of the letter ‘e’
"""

# def find_line_with_max_e():
#     file_name = input("Please enter the file name: ")
#
#     try:
#         with open(file_name, 'r') as file:
#             max_count = 0
#             max_line = ""
#             for line in file:
#                 count = line.lower().count('e')  # Count occurrences of 'e'
#                 if count > max_count:
#                     max_count = count
#                     max_line = line.strip()  # Save the line without leading/trailing whitespace
#             if max_line:
#                 print(f"Line with maximum 'e': {max_line}")
#                 print(f"Occurrences of 'e': {max_count}")
#             else:
#                 print("No lines found in the file.")
#     except FileNotFoundError:
#         print(f"File '{file_name}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     find_line_with_max_e()

def maximum_occurences_with_e():
    with open("CPLD_Info.txt", 'r') as file:
        max_count = 0
        max_line = ""
        for line in file:
            count = line.lower().count('n')
            if count > max_count:
                max_count = count
                max_line = line.strip()
                if max_line:
                    print(f"line with maximum  'e': {max_line}")
                    print(f"Occurences of 'e': {max_count}")
                else:
                    print("No lines found in the file.")
maximum_occurences_with_e()
























