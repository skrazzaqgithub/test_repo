# Write a function to check if number is even
def even_number():
    number = int(input("Enter the Number: "))
    if number%2 == 0:
        print("The number entered is even:", number)
    return True
output = even_number()
print(output)