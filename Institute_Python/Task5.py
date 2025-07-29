# Write a function that returns the factorial of a number
def factorial(n):
    prod = 1
    while n>1:
        prod = prod*n
        n-=1
    return prod
print(factorial(5))

