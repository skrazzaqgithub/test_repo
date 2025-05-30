name=str(input("Enter your name:"))
surname=str(input("Enter your surname:"))
print("Name:", name, "Surname:", surname)
surname=surname[-5]
name=name[0:6]
print(name, surname)

# n1=name.upper()
# n2=surname.upper()
# print(n1, n2)
# print("-------", "-----")
# n3 = n1.capitalize()
# n4 = n2.capitalize()
# print(n4, ",", n3)
# n4 = n4[2:4]
# print(n4)