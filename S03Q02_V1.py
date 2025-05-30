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

def main(number):  
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    print("inside main")
    do_1digit_oper(number)
    do_2digit_oper(number)
    do_3digit_oper(number)

print("program starts")
number = int(input("Enter your number:"))
main(number)
