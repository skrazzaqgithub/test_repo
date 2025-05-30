"""
    multiplication table of 17
"""
multipy = int(input("Enter your table number for multiplication :"))
num = 1
while num <= 10:
    multiplication = (multipy * num)
    print(multipy, "x", num, "=", multiplication)
    num += 1

##for num in [1,2,3,4,5,6,7,8,9,10]:
##    if num * 9
##    item *= 1
##    print(item)


##for num in range(1, 11):
##    multiplication = (multipy * num)
##    print(multipy, "x", num, "=", multiplication)

##multipy     num     multiplication
##10          1       10
##10          2       20
##10          3       30
##...
##10          10      100
