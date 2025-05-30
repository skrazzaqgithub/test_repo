"""
Write a Python script that takes a file name as its argument.
Write the contents of this file to another file such that,
   each sentence is stored on a new line.
"""

def write_content_to_file():
    with open("CPLD_Info.txt", 'a') as file:
        data = file.write("\n Appending new line to existing file12399241289")
        print(data)

write_content_to_file()
