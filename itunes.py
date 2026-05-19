import sys
from xml.etree.ElementTree import indent

import requests
import json


#base_url="https://itunes.apple.com/search?entity=song&limit=1&term="
name=input("name = ? ")
limit_or_total_songs = int(input("highest amount of songs : "))
response=requests.get(f"https://itunes.apple.com/search?entity=song&limit={limit_or_total_songs}&term={name}")

# print(json.dumps(response.json(),indent=2))

o=response.json()
for i in o["results"]:
    print(i["trackName"])