import json
import os
import time

import requests

API_KEY = os.environ.get("WEATHER_API_KEY")

cities = [
    "Lahore",
    "Narowal",
    "Faisalabad",
    "Rawalpindi",
    "Multan",
    "Gujranwala",
    "Hyderabad",
    "Sialkot",
    "Peshawar",
    "Sargodha",
    "Sukkur",
    "Bahawalpur",
    "Sambrial",
    "Kasur",
    "Jhang",
    "Khanewal",
    "Dera Ghazi Khan",
    "Jhelum",
    "Khanpur",
    "Kohat",
    "Larkana",
    "Mandi Bahauddin",
    "Mianwali",
    "Mirpur Khas",
    "Okara",
    "Rahim Yar Khan",
    "Sheikhupura",
    "Sialkot",
    "Tando Adam",
    "Tando Allahyar",
    "Tando Muhammad Khan",
    "Thatta",
    "Vehari",
    "Wah Cantonment",
    "Wazirabad",
    "Zafarwal",
]
data = []

start = time.time()
for city in cities:
    r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}")
    data.append(r.json())

end = time.time()
print(f"Total time taken: {end - start}")
# make json file and store data
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
