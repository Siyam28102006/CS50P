import re

url=input("URL : ")

#matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)

#if matches := re.search(r"^https?://(?:www\.)?twitter\.(?:com|org)/(.+)$",url,re.IGNORECASE):
if matches := re.search(r"^https?://(?:www\.)?twitter\.(?:com|org)/([a-zA-Z0-9_]+)$",url,re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
    #group(1) -> (www\.) and then matches.group(2)->(.+) without(?:.....)
    #with ?: = (www\.) ke capture kora hocche na . so matches.group(1) is the username!!!
else: print("Invalid")