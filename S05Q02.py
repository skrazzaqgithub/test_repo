"""
    Ask the user to enter a number till he enters 0.
          Print the maximum and minimum values among all entered numbers.
          Print the number of single, two and three digit numbers entered.
"""
l1 = []
for i in range(0,6):
    n=int(input("Enter your number:"))
    l1.append(n)
    if n > 0 and n < 10:
        print("single digit")
    elif n >= 10 and n < 100:
        print("double digit")
    elif n >= 100 and n < 1000:
        print("three digit")
    elif n == 0:
        break
print(l1)
print("Your Maximum number from the list is :",max(l1))
print("Your Minimum number from the list is :",min(l1))
# Number = int(input("Enter your number:"))
# while Number>=0:
#     if Number == 0:
#         print("Enter max number or min number")
#     elif((Number >= 10)&(Number <=100)):
#         print("max(Number)")
#         Number += 1
##num = 1
##while num <= 10:
##    multiplication = (multipy * num)
##    print(multipy, "x", num, "=", multiplication)
##    num += 1

##for num in [1,2,3,4,5,6,7,8,9,10]:
##    if num * 9
##    item *= 1
##    print(item)

# for num in range(0, Number, 1):
#     if Number > 0:
#         print(num)
#     elif Number > num:
#         print("Entered Number is max number:", num)

##multipy     num     multiplication
##10          1       10
##10          2       20
##10          3       30
##...
##10          10      100
