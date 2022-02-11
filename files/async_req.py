import asyncio
import csv
import json
import os
import time

import aiohttp

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


async def get_weather():
    async with aiohttp.ClientSession() as session:
        for city in cities:
            async with session.get(
                f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
            ) as resp:
                data.append(await resp.json())


end = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(get_weather())
loop.close()
print(f"Total time taken: {end - start}")
# make json file and store data
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# make csv file and store data

with open("data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["city", "temp", "humidity", "wind_speed", "wind_dir"])
    for city in data:
        writer.writerow(
            [
                city["location"]["name"],
                city["current"]["temp_c"],
                city["current"]["humidity"],
                city["current"]["wind_kph"],
                city["current"]["wind_dir"],
            ]
        )
