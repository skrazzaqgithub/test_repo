def add(num1, num2):
    res = num1 + num2
    return res

def sub(num1, num2):
    res = num1 - num2
    return res

def div(num1, num2):
    res = num1 % num2
    return res

# Main starts from here
if __name__ == "__main__":
    alpha = 10
    beta = 20
    total = add(alpha, beta)
    print("sum", total)
    diff = sub(alpha, beta)
    print("diff", diff)
    division = div(alpha, beta)
    print("div", division)
