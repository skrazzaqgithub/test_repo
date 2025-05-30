"""S11Q01
From a file that contains a list of numbers.
Find the maximum number in that list.
Also find the sum of all the numbers in that list."""

def maximum_number():
    try:
        with open('list_numbers.txt', 'r') as file:
            for i in file:
                sum1 = sum(file)
                if i == max(file):
                    print("maximum number from the list is: ", i)
            print("sum of all numbers in the list: ", sum1)
    except FileNotFoundError:
        print(f"file{'list_numbers.txt'} not found")
    except Exception as file:
        print(f"An Error occurred:{file}")
print(maximum_number())

