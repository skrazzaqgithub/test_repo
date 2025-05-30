""" What does this program do ?
"""

# Implement the helper functions here

def do_1digit_oper(inp):
    print("inside 1d")
    if(inp < 10):
        inp = inp + 7
        print("Entered single digit number is added with 7:", inp)

def do_2digit_oper(inp):
    print("inside 2d")
    if(inp > 10 and inp < 100):
        print("Entered number is 2 digit then raised to the power of 5:", inp ** 5)

def do_3digit_oper(inp):
    print("inside 3d")
    if(inp > 100 and inp < 1000):
        print("Entered number is 3 digit:", inp)
    inp1 = int(input("Enter your number:"))
    print("Number is added with inp:", inp + inp1)

def perform_check(number):  
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    print("inside main")
    do_1digit_oper(number)
    do_2digit_oper(number)
    do_3digit_oper(number)

def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    inp = int(input("Enter your number:"))
    return inp
    
# Main starts from here
num0 = get_number()
num1 = get_number()
num2 = get_number()
perform_check(num0)
perform_check(num1)
perform_check(num2)
