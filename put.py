import requests
url = "https://reqres.in/api/users/2"   # Note that we need to specify the user ID here
data = {
    "name": "morpheus",
    "job": "zion resident"
}

response = requests.put(url, data=data)   # We need to pass the data parameter here
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Not found")
