# def fibonacci_of_first_12_nums(count):
#     fib1, fib2 = 1, 1
#     even_fibs = []
#     while len(even_fibs) < count:
#         next_fib = fib1 + fib2
#         if next_fib%2 == 0:
#             even_fibs.append(next_fib)
#         fib1, fib2 = fib2, next_fib
#     print("first", count, "even numbers fibonacci numbers:")
#     for num in even_fibs:
#         print(num, end=' ')
# fibonacci_of_first_12_nums(5)
def fibonacci_even_odd_only(count):
    fib1, fib2 = 1, 1
    even_fibs = []
    odd_fibs = []
    while len(even_fibs) < count:
        next_fib = fib1+fib2
        if next_fib%2==0:
            even_fibs.append(next_fib)
        # fib1, fib2 = fib2, next_fib
            # print("first", count, "even numbers in fibonacci numbers")
        else:
            odd_fibs.append(next_fib)
            # print("first", count, "even numbers in fibonacci numbers")
        fib1, fib2 = fib2, next_fib
    # print(count)
    for num in even_fibs:
        print(num, "is even fibonacci number", end="\n")
    print("------------------------")
    for num in odd_fibs:
        print(num, "is odd fibonacci number", end="\n")
fibonacci_even_odd_only(5)

# def fibonacci_even_odd_only(count):
#     fib1, fib2 = 1, 1
#     even_fibs = []
#     odd_fibs = []
#     while len(even_fibs) < count or len(odd_fibs) < count:
#         next_fib = fib1+fib2
#         if next_fib%2==0 and len(even_fibs) < count:
#             even_fibs.append(next_fib)
#         elif next_fib%2!=0 and len(odd_fibs) < count:
#             odd_fibs.append(next_fib)
#         fib1, fib2 = fib2, next_fib
#     for num in even_fibs:
#         print(num, "is evn fibonacci number", end="\n")
#     print("------------------------")
#     for num in odd_fibs:
#         print(num, "is odd fibonacci number", end="\n")
# fibonacci_even_odd_only(9)