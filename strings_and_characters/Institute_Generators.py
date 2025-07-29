# def numbers(num):
#     for i in range(1, num+1):
#         print(i)
#         yield
# new_gen = numbers(20)
# print(new_gen)
# next(new_gen)
# next(new_gen)
# next(new_gen)

# def numbers(num):
#     for i in range(1, num+1):
#         print(i*100)
#         yield
# new_gen = numbers(20)
# print(new_gen)
# next(new_gen)
# next(new_gen)
# next(new_gen)

def numbers(num):
    for i in range(1, num+1):
        print(i*100)
        yield
new_gen = numbers(20)
print(new_gen)
while True:  #conditional loop, It is always True
    next(new_gen)
print("generator function is successfully completed")

Unhandled exception : BSOD (Blue Screen on Death)
Windows Crash -> BSOD
Software operating systems hit any error or exception, It crashes.
Linux Crash -> Purple Screen of Death (PSOD)
