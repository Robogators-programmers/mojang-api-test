import requests

username =input("What is your username?")
url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
response = requests.get(url)
uuid = response.json()['id']
print(uuid)
