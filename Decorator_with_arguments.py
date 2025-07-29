# decorators with basic arguments
def decorator_with_args(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator arguments: {arg}")
            result = func(*args, **kwargs)
            print(result)
            print("Function executed with arguments", args, "and keyword arguments", kwargs)
        return wrapper
    return decorator

@decorator_with_args("Hello")
def my_function(x, y):
    return x + y
result = my_function(8, 1)
print(result)

#Decorator concept

# def my_decorator(func):
#     def wrapper():
#         print("Executing before")
#         func()
#         print("Executing after")
#     return wrapper()
# @my_decorator
# def do_this():
#     print("Doing this")
# def do_that():
#     print("Doing that")
# do_this()
# do_that()
#
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Some extra code before executing this step")
#         result = func(*args, **kwargs)
#         print("Some extra code after executing this step")
#         return result
#     return wrapper
# @my_decorator
# def new_decorator(a,b):
#     return a+b
# print(new_decorator(2,7))


