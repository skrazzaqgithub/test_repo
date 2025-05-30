import requests
# import json
header = {'Content-Type': 'Application/json',
          'Authorization': 'Bearer 4f9ebab65999f9defba723f126e0b8598517765889c79963803ac7aa1308e846'}
request_put_payload = {
  "id": 999927,
  "title": "string",
  "dueDate": "2024-12-04T14:52:24.586Z",
  "completed": True
}
print("After Update")
response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/2", headers=header, json=request_put_payload)
print(response.status_code)
print(response.json())
assert response.status_code == 200