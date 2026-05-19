names=[]

for _ in range(4):
    name=input("What's ur name? ")
    names.append(name)

with open("newname02.txt","a") as file:
    for i in names:
        file.write(f"{i}\n")


for i in sorted(names,reverse=True):
    print(i)

