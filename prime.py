n=int(input("Enter the given number:"))
count=0
for i in range(2,n):
    if n%i==0:
        count=count+1
        break
if count==0:
    print("given number is prime")
else:
    print("given number is not prime")
    
