# with open("file_handle_test.txt", "r") as file:
#     print file.readline(50)

# def print_lines(FH):
#     all_text = FH.read()
#     all_lines = all_text.split('\n')
#     for lines in all_lines:
#         print(lines)
# MYFH=open("file_handle_test.txt")
# print_lines(MYFH)
# MYFH.close()

# FH = open("file_handle_test.txt")
# with open("file_handle_test.txt") as FH:
#     text = FH.read()
#     lines = text.split('\n')
#     for line in lines:
#         print(line)

# try:
#     FH = open("file_handle_test.txt")
#     all_lines = FH.readline()
#     print(all_lines)
# except IOError:
#     print("could not open file")
# except:
#     print("Oops")


# FH = open("file_handle_test.txt")
# # all_lines = FH.read(10)
# all_lines = FH.read(100)
# FH.tell()
# FH.seek(0,1)
# FH.tell()

# def print_lines(FH):
#     while True:
#         line = FH.readline()
#         if line == "":
#             break
#         print(line)
# with open("file_handle_test.txt") as MYFH:
#     print_lines(MYFH)


# FH = input("Enter the file name:")
# first_char = FH.read()
# print("Sentence starts with capital letter", first_char)
# for char in FH:
#     if char[0].upper():
#         break
# print("Sentence starts with capital letter")

# with open('Razzaq_Passport_size_Photo.jpg', 'rb') as file:
#     image_data = file.read()

# with open('Screenshot_2024_10_16_214810.png', 'wb') as file:
#     image_data = file.write()

with open('D:\python\CPU_Info.txt', 'r') as file:
    for line in file:
        print(line)
lines = len(line)
print(lines)

# with open('CPU_Info.txt', 'w') as file:
#     for line in file:
#         if len(line) == 10:
#             new_line = file.write('adding new line')
#     print(line)
# lines = len(line)
# print(lines)

# import json
# with open('sample1.json', 'r') as file:
#     data = json.load(file)
#     print(data)

# import json
# data = {'name': 'John', 'age': 30}
# with open('new_data.json', 'w') as file:
#     json.dump(data, file)
#
# with open('new_data.json', 'r') as file:
#     data = json.load(file)
#     print(data)