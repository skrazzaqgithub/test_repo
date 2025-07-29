###################################
#decorator is a function
#
###################################
def deco(fun):
    def wrapper(*args, **kwargs):
        print("Calling the function")
        return fun(*args, **kwargs)
    print("deco function")
    return wrapper
@deco
def sum(a,b):
    total = a + b
    return total
tot = sum(10,20)
print(tot)
