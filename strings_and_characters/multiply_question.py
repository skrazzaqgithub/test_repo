# Create a "multiply()" function that takes "num1" and "num2" as parameters
# It should return the product of "num1" and "num2"
# Make sure the function behaves as mentioned below :
#
# >>> multiply()              # returns  1
# 1
# >>> multiply(10)         # returns  10
# 10
# >>> multiply(10, 2)     # returns  20
# # 20
# # >>>
def multiply():
    num1 = int(input("Enter the number: "))
    print(">>> multiply")
    print(num1)
def multiply(num1):
    num1 = int(input("Enter the number: "))
    print(">>> multiply")
    print(num1)
def multiply_1(num1,num2):
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))
    print(">>> multiply")
    print(num1*num2)
multiply(1)
multiply(10)
multiply_1(10,2)