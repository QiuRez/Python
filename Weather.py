import requests
from tokenw import token


city_name = input("Город")
respone = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + tokenw.token)
kelvin = respone.json()['main']['temp']
celsiya = int(kelvin) - int(273)
celsiya = str(celsiya)
print(celsiya)
