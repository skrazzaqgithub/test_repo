import requests
headerdata={'T1':'FirstHeader', 'T2':'SecondHeader'}
response = requests.get('https://httpbin.org/get', headers=headerdata)
print(response.text)