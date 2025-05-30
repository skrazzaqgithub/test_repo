import requests
# import json
header = {'Content-Type': 'Application/json',
          'Authorization': 'Bearer 4f9ebab65999f9defba723f126e0b8598517765889c79963803ac7aa1308e846'}
url = "https://gorest.co.in/public/v2/users"
request_payload = {'id': 22599, "name": "abdulrazzaq", "email": "abc@9abctestp.co.in", "gender": 'male', "status": "active"}
response = requests.post(url, headers=header, json=request_payload)
print(response.status_code)
print(response.json())
assert response.status_code == 201

getResponse = requests.get(url+'/'+ str(response.json()['id']), headers=header)
print(getResponse.json())
assert getResponse.status_code == 200