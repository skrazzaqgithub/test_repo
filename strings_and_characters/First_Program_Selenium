import requests

head = {
    'Content-Type' : 'application/json',
    'Authorization' : 'Bearer 4f9ebab65999f9defba723f126e0b8598517765889c79963803ac7aa1308e846'
}
url = 'https://gorest.co.in/public/v2/users'
response = requests.get(url, headers=head)
print("Before Creating an account")
body = {
    "name": "Razzaq",
    "email": "razzaq1@krajcik.test",
    "gender": "male",
    "status": "active"
  }

responsePost = requests.post(url, headers=head, json=body)
print("After Creating an account")

print(responsePost.status_code)
print(responsePost.json())
assert responsePost.status_code == 201
getResponse = requests.get(url+'/'+str(responsePost.json()['id']),headers=head)