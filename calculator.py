def add(num1, num2):
    res = num1 + num2
    return res

def sub(num1, num2):
    res = num1 - num2
    return res

# Main starts from here
alpha = 10
beta = 20
total = add(alpha, beta)
print("sum", total)
diff = sub(alpha, beta)
print("diff", diff)

eng1 = 250
ind1 = 220
eng2 = 180
engtotal = add(eng1, eng2)
ind2 = sub(engtotal, ind1)
target = add(ind2, 1)
print("2nd innings for india target is:", target)

vegetables = 120
fruits = 45
cash = 200
total_cost = add(vegetables, fruits)
balance_amount = sub(cash, total_cost)
print("your balance amount is:", balance_amount)
