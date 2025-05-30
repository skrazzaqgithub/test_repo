"""S11Q03
Write a Python script that takes a file name as its first argument.
Create a copy of the contents of this file satisfying the following conditions :

   - If the file name is “file.txt”,
       then the name of the new file should be “file-new.txt”
   - Every even line of the first file, should be
       repeated in the new file.
   - The first line of the first line, should be
       repeated after the last line of the first file.
   - A sample input and output file is shown below"""
# import sys
# def process_file(file_name):
#     new_file_name = file_name.replace(".txt", "-new.txt")
#     try:
#         with open(file_name, 'r') as f:
#             lines = f.readlines()
#         with open(new_file_name, 'w') as nf:
#             for i, line in enumerate(lines):
#                 nf.write(line)
#                 if (i + 1) % 2 == 0:  # Even lines (1-based index)
#                     nf.write(line)  # Repeat even line
#             if lines:  # Append the first line at the end
#                 nf.write(lines[0])
#         print(f"New file '{new_file_name}' created successfully.")
#     except FileNotFoundError:
#         print("Error: File not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# # Run the script with command-line arguments
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python script.py <filename>")
#     else:
#         process_file(sys.argv[1])

import sys
import os

def process_file(filename):
    try:
        with open(filename, 'r') as infile:
            lines = infile.readlines()

        if not lines:
            print("The file is empty.")
            return

        base, ext = os.path.splitext(filename)
        new_filename = f"{base}-new{ext}"

        with open(new_filename, 'w') as outfile:
            for i, line in enumerate(lines):
                outfile.write(line)
                if (i + 1) % 2 == 0:  # even line (1-based index)
                    outfile.write(line)  # repeat even line

            # Append the first line again at the end
            outfile.write(lines[0])

        print(f"New file created: {new_filename}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: python script.py file.txt
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
    else:
        process_file(sys.argv[1])
