import requests

url = "https://api.withmono.com/account/auth"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)

print(response.text)