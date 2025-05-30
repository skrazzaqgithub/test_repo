"""
Modify program in S01Q02 to print the multiplication table
           of any number desired by the user

           You can use following code template to create your solution : https://git.io/vgov6
           [ Click on "RAW" button if you find it difficult to download the code ]
"""

def get_number():
    """
        This function should fetch a number from user
        Input : None
        Return : an integer
    """
    number = int(input("Enter the number: "))
    # Check out your code behaviour by commenting the line below
    number = int(number) # What happens if you dont perform this operation ?
    return number


def print_mtable(num):
    """
        This function prints the multiplication table of num
        Input : an integer
        Output : Display multiplication table of input integer
        Return : None
    """
    # Your solution code goes in here
    for i in range(1, 11):
        multipy = num*i
        print(num,"x",i,"=", multipy)

def main():
    '''
        Main program
    '''
    inp = get_number()
    print_mtable(inp)

# Main starts from here
main()

# n = int(input("Enter the number: "))
#     for i in range(1,11):
#         multipy = n*i
#         print(n,"x",i,"=", multipy)