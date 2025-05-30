"""
Get the name of the text file from the user.
Check if all the sentences in that text file begin with a capital letter.
"""
def check_capitalization(CPLD_Info):
    try:
        with open("CPLD_Info.txt", 'r') as file:
            if file == "CPLD_Info.txt":
                text = file.read()
            # Split text into sentences (you can adjust the splitting logic as needed)
                sentences = text.split('. ')
                for sentence in sentences:
                # Strip any leading/trailing whitespace and check the first character
                    if sentence and not sentence[0].isupper():
                        return False
                return True
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
        return False
# Get the file name from the user
CPLD_Info = input("Enter the name of the text file: ")
if check_capitalization(CPLD_Info):
    print("All sentences begin with a capital letter.")
else:
    print("Not all sentences begin with a capital letter.")
