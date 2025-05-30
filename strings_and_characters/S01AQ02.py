"""
Re-write the earlier question of S01Q02 using functions as mentioned below :

           You can use following code template to create your solution : https://git.io/vgoeT
           [ Click on "RAW" button if you find it difficult to download the code ]

   - Print the multiplication table of 17

"""

""" 
Describe what this program does
"""

def print_mtable():
    """
        Describe what this function does
    """
    # Your solution code goes in here
    multipy = input("Enter your table number for multiplication :")
    multipy = int(multipy)
    if (multipy == 17):
            multiplication = (multipy * 1)
            print("multiplication of 17 x 1 : ", multiplication)
            multiplication = (multipy * 2)
            print("multiplication of 17 x 2: ", multiplication)
            multiplication = (multipy * 3)
            print("multiplication of 17 x 3: ", multiplication)
            multiplication = (multipy * 4)
            print("multiplication of 17 x 4: ", multiplication)
            multiplication = (multipy * 5)
            print("multiplication of 17 x 5: ", multiplication)
            multiplication = (multipy * 6)
            print("multiplication of 17 x 6: ", multiplication)
            multiplication = (multipy * 7)
            print("multiplication of 17 x 7: ", multiplication)
            multiplication = (multipy * 8)
            print("multiplication of 17 x 8: ", multiplication)
            multiplication = (multipy * 9)
            print("multiplication of 17 x 9: ", multiplication)
            multiplication = (multipy * 10)
            print("multiplication of 17 x 10: ", multiplication)
    else:
            print("Entered table number is wrong")

# Main starts from here
print_mtable()

# multipy = input("Enter your table number for multiplication :")
# multipy = int(multipy)
# if (multipy == 17):
#         multiplication = (multipy * 1)
#         print("multiplication of 17 x 1 : ", multiplication)
#         multiplication = (multipy * 2)
#         print("multiplication of 17 x 2: ", multiplication)
#         multiplication = (multipy * 3)
#         print("multiplication of 17 x 3: ", multiplication)
#         multiplication = (multipy * 4)
#         print("multiplication of 17 x 4: ", multiplication)
#         multiplication = (multipy * 5)
#         print("multiplication of 17 x 5: ", multiplication)
#         multiplication = (multipy * 6)
#         print("multiplication of 17 x 6: ", multiplication)
#         multiplication = (multipy * 7)
#         print("multiplication of 17 x 7: ", multiplication)
#         multiplication = (multipy * 8)
#         print("multiplication of 17 x 8: ", multiplication)
#         multiplication = (multipy * 9)
#         print("multiplication of 17 x 9: ", multiplication)
#         multiplication = (multipy * 10)
#         print("multiplication of 17 x 10: ", multiplication)
# else:
#         print("Entered table number is wrong")
