#Write a function that checks if a number is positive, negative or zero
def positive_negative():
    num1 = int(input("Enter the number: "))
    if num1 < 0:
        print("Entered Number is negative: ", num1)
    else:
        print("Entered Number is positive: ", num1)
    # return "Entered number is: ", num1
positive_negative()