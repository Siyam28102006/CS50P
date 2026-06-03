import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.(.+)/(.+)$", url, re.IGNORECASE):
    if matches.group(1) == "com":
        print(f"Username:", matches.group(1))