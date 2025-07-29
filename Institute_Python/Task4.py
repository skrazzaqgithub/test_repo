# def a1():
#     num1 = int(input("enter a number : "))
#     # print(*list(range(num1+1))[-3:])
#     for i in range(num1-2, num1+1):
#         print(i, end=" ")
# a1()

def maximum_of_three_numbers():
    num1 = int(input("Enter the number: "))
    print(*list(range(num1+1)[-3:]))
maximum_of_three_numbers()