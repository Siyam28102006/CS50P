names=[]

for _ in range(4):
    name=input("What's ur name? ")
    names.append(name)

file=open("newname.txt","a")
for i in names:
    file.write(f"{i}\n")

file.close()
