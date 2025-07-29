# def addition(a,b):
#     return a+b
# a = int(input("Enter the Number: "))
# b = int(input("Enter the Number: "))
# print("Sum of given numbers", addition(a,b))

# def sum(a,b):
#     total = a + b
#     return total
# tot = sum(10,20)
# print(tot)

# def fun1(*args): #args of tuple()
#     print(args)
# fun1()
# fun1(11,22,33)
# fun1('a','b','c')
# fun1(99,)

def fun2(**kwargs): #any number of keyword arguments
    print(kwargs)
fun2(a=10, b=20, c=30)
fun2(name="Rama", Addr = "Blr")