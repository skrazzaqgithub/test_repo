# """
Ask the user to enter a 3 digit number, till he enters 0.
Discard all numbers that are not 3 digit numbers.
From all the 3 digit numbers entered by the user,
     find and print the prime numbers in descending order.
# """
#
# inp = int(input("Enter 3 digit number: "))
# if inp <= 0 and inp <= 99:
#     print("Enter 3 digit numbers only")
#
# for i in range(10, inp):
#     if inp%i == 0:
#         print("Number is not prime", inp)
#         break
# else:
#     print("Number is prime", inp)

a = 1
b = 1
print(a)
print(b)
count = 0
while count>0:
    a = a+b
    b = a+b
    print(a)
    print(b)
    count += 1