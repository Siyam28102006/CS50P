import re

url=input("URL : ").strip()

username=re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url) #? -> 0 or 1(for s)
# www. is optional ! . er age escape char(\) jaate .-ta char na hoye www. hishabe treat hoy
print(f"Username : {username}")

#re.sub(pattern, replacement, string)