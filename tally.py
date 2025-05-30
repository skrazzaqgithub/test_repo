import calci

def main():
    vegetables = 120
    fruits = 45
    cash = 200
    total_cost = calci.add(vegetables, fruits)
    balance_amount = calci.sub(cash, total_cost)
    print("your balance amount is:", balance_amount)

if __name__ == "__main__":
    main()
