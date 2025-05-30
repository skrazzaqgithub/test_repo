import re
ipv4_address_pattern = re.compile(r'''^(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)
                                                (\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)){3}$''', re.VERBOSE)
def valid_address(ip):
    if ipv4_address_pattern.match(ip):
        return f"{ip} is valid ip address"
    else:
        return f"{ip} is not valid ip address"
test_ips = ["192.168.1.1", "255.255.255.255", "256.100.100.100", "10.0.0.1", "192.168.1"]
for ip in test_ips:
    print(valid_address(ip))