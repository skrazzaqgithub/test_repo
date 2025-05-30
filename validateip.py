import re
ip=input("Enter valid IPaddress:")
pattern="^((25[0-5]|2[0-4][0-9]|1[0-9[0-9]|[1-9]?[0-9]\.){3}(25[0-5]|2[0-4][0-9]|1[0-9[0-9]|[1-9]?[0-9]))$"
def check_ip(ip):
    if (re.search(pattern,ip)):
           print("{IP} address is valid")
    else:
           print ("{IP} address is invalid")
check_ip(ip)

