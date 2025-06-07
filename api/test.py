
import json

import requests


appid = "4a1f8a61b74546825af1e0be106e797b"    
city = input("enter the city name\n")
 
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units=metric"
print("url =" , url)
response = requests.get(url)
code = response.status_code

if code !=200:
    print("error",code)
else:
    print("ok")
print(response.text)