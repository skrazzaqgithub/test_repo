"""
Re-write the earlier question of S01Q01 using functions as mentioned below :

           You can use following code template to create your solution : https://git.io/vgrjP
           [ Click on "RAW" button if you find it difficult to download the code ]

  - Modify the first “Hello World” program to prompt for user’s name
           and then wish the user by saying Hello followed by his name

           Example :
           If user's name is Sam, then expected output is :
           Hello Sam !!!
"""


def get_username():
    """
    Prompt the user to enter his name
    Input : None
    Output : Return the user input as a string
    """
    # Your solution code should go in here


def say_hello(user):
    '''
    Greet the user by saying Hello followed by his name
    Input : user name
    Output : Greeting statement on the screen. No return value
    Example : If input string is Sam
        Then the expected output is
        Hello Sam !!!
    '''
    print("Hello", "Razzaq !!!")


def main():
    '''
    Main function of the program
    '''
    name = get_username()
    say_hello(name)


# Main starts from below
main()