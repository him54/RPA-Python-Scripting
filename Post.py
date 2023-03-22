import requests
url = "https://reqres.in/api/users?page=2"

data = {
    "name": "morpheu",
    "job": "leade"
}
response = requests.post(url, json = data)

if response.status_code == 201:
   data = response.json()
   print(data)
else:
    print("Not found")
