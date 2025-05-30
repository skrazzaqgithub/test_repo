import sys

def usage():
    print(f"Usage: python {sys.argv[0]} num1 num2")
    
#print(f'{sys.argv = }')
if len(sys.argv) < 3:
    usage()
    exit()
    
##x = input("Enter the number:")
x = int(sys.argv[1])
##y = input("Enter the number:")
y = int(sys.argv[2])
print(x+y)
