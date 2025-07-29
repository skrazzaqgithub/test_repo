# input_file = "logs.txt"
# output_file = "errors_captured.txt"
# error_keyword = ["error","critical","fail","warning"]
# with open(input_file, "r") as infile, open(output_file, "w") as outfile:
#     for line in infile:
#         print(infile)
#         if any(keyword.lower() in line.lower() for keyword in error_keyword):
#             outfile.write(line)
# print("Finished filtering error-related lines.")
# Define the input and output filenames
input_file = 'logs.txt'       # Replace with your source log file name
output_file = 'error_logs.txt'   # Output file for error-related lines

# Keyword(s) to search for in each line
error_keywords = ['error']

# Open the input file for reading and output file for writing
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        print(line, end='')
        # Check if the line contains any error keyword (case-insensitive)
        if any(keyword.lower() in line.lower() for keyword in error_keywords):
            outfile.write(line)

print("Finished filtering error-related lines.")
