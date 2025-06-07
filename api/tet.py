import json

import requests

appid = "4a1f8a61b74546825af1e0be106e797b"
city = input("Enter city name\n")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units=metric"
print("Url = ", url)
response = requests.get(url)
code = response.status_code
if code != 200:
    print("Error", code)
else:
    print("Ok")
    print(response.text)