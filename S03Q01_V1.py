"""S03Q01
     - Take 2 numbers from the user. 
            Print which number is a 2 digit number, 
            and which number is a 3 digit number. 
            If it is neither, then print the number as it is


            You can use following code template to create your solution : https://git.io/vgoVG
            [ Click on "RAW" button if you find it difficult to download the code ] """

# Implement the helper functions here
def check_if_2digit(inp):
    if(inp >= 10 and inp < 100):
        print("Entered number is 2 digit:", inp)

def check_if_3digit(inp):
    if(inp >= 100 and inp < 1000):
        print("Entered number is 3 digit:", inp)
        
def check_any_digit(inp):
    if(inp < 10 or inp > 999):
        print("Entered any number digit:", inp)

def perform_check(number):  
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    check_if_2digit(number)
    check_if_3digit(number)
    check_any_digit(number)

def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    inp = int(input("Enter your number:"))
    return inp
    
# Main starts from here
num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)
