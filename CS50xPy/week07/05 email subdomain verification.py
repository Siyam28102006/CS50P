import re

#re.search(pattern,string,flags=0)

email=input("What's your email?").strip()
if re.search(r"^(\w|[.])+@(\w+[.])*(\w|[.])+[.](\w)+$",email,re.IGNORECASE):#re.IGNORECASE instead of .lower()
    print(f"Valid")
else :
    print(f"Invalid")
