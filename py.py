import requests

a = None
for a in range(1, 201):
    respone = requests.get("https://api.thedogapi.com/v1/breeds/" + str(a))
    print(respone.json()["name"])
