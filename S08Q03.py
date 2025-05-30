"""
S08Q03
    Ask the user to enter a number.
    - If the user enters a number as 5, then
    generate the following string :
    - 00001111222233334444

    - If the user enters the number as 3, then
    generate the following string :
    - 001122 """

number = int(input("Enter the Number:"))
if (number == 5):
    print("00001111222233334444")
elif (number == 3):
    print("001122")
else:
    print("Enter 5 or 3 numbers only")