"""
    Calculating the ZAKAT 2023
"""
savings = input("Enter your savings: ")
#savings = int(savings)
excess = int(savings) - 500000
if excess > 0:
    zakat = 2.5 * excess / 100
    print("Zakat Amount is :", zakat)
else:
    print("No Zakat")

