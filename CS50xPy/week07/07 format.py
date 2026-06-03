
name=input("What's ur name?")
if "," in name:
    last,first=name.split(",")
    name=f"{first}{last}"
print(f"Hello,{name}")

#cleaning up user input. io -> David,Malan but the output is Hello , David Malan