# a = 1
# b = 1
# print(a)
# print(b)
#
# count = 0
# while count < 4:
#     if count == 4:
#         pass
#     a = a+b
#     b = a+b
#     print(a)
#     print(b)
#     count += 1

def fibonacci(n):
    fib = [0,1]
    while n>=1:
        next_fib = fib[-1] + fib[-2]
        if next_fib>n:
            if next_fib%2==0:
                print("Not Prime")
            else:
                fib.append(next_fib)
    return fib
n = 90
print(fibonacci(n))

# # Initialize the first two Fibonacci numbers
# a, b = 0, 1
#
# # Continue generating Fibonacci numbers until they exceed 3 digits
# while a < 2000:
#     # Check if the Fibonacci number is even and has 3 digits
#     if a >= 100 and a % 2 == 0:
#         print(a)
#     # Update a and b to the next Fibonacci numbers
#     a, b = b, a + b


# import turtle
# vs = turtle.Screen()
# alex = turtle.Turtle()
#
# for color in ["yellow", "Red", "blue", "orange"]:
#     alex.color(color)
#     alex.forward(50)
#     alex.left(90)

# import turtle
# vs = turtle.Screen()
# alex = turtle.Turtle()
#
# for i in range(3):
#     alex.forward(50)
#     alex.left(90)
