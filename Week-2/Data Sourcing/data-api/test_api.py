# pylint: disable=missing-module-docstring

import requests

URL = "https://weather.lewagon.com/geo/1.0/direct?q=Barcelona"
response = requests.get(URL, timeout = 5).json()
city = response[0]

print(response)
print(type(city['lat']))
print(type(city['lon']))
print(f"{city['name']}: ({city['lat']}, {city['lon']})")
