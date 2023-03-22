import requests
url = "https://reqres.in/api/users?page=2"

response=requests.get(url)

data = response.json()
#print(response.status_code)
if response.status_code == 201:
    print(data)
else:
    print("Not found")

for i in data:
    print(i)
