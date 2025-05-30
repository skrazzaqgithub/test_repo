"""
S08Q02
Ask the user to enter a number.
- If the number is a single digit number, add 7 to it,
     and print the number in its unit’s place
- If the number is a two digit number, raise the number to the power of 5,
     and print the last 2 digits
- If the number is a three digit number, ask user to enter another number.
     Add the 2 numbers and print the last 3 digits """

number = int(input("Enter the Number:"))
if (number < 10):
    print("Adding 7 to the number:", number + 7)
elif (number < 100):
    print("Raising the number to the power of 5:", number ** 5)
elif (number < 1000):
    Another_Number = int(input("Enter another Number:"))
    print("Adding the 2 numbers with another number entered:", number + Another_Number)