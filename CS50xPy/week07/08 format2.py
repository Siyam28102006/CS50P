import re

name=input("What's Your Name?")

matches=re.search(r"^(.+), *(.+)$",name)
if matches:
    name=matches.group(2)+" "+matches.group(1) #in this context for re , we have 1-based counting according to documentation!
    print(f"hello , {name}")

d=input("Enter date : DD-MM-YYYY")
matchesss=re.search(r"^(\d{2})-(\d{2})-(\d{4})$",d)
#in this context for re , we have 1-based counting according to documentation!

if matchesss:
    date=matchesss.group(1) + "-" + matchesss.group(2) + "-" + matchesss.group(3)
    print(f"The date today is : {date}")
# (d{4})   -> Matches exactly the literal string "dddd"
# (\d{4})  -> Matches any 4-digit number like "2026"