import requests
url = "https://reqres.in/api/users?page=2"
data = {
    "name": "morpheus",
    "job": "leader"
}
response = requests.delete(url)
if response.status_code == 204:
    print(data)
else:
    print("Not found")

