def check_if_singledigit(inp):
    if(inp < 10):
        add = inp + 7
        print("Entered number is single digit:", add)

def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    inp = int(input("Enter your number:"))
    return inp
