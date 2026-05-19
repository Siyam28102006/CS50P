with open("newname02.txt","r") as file:
    lines=file.readlines()

for line in lines:
    print(f"Hello,{line.rstrip()}") #.rstrip() cuts out the newlines or end=""diyeo same kaaj hbe.it's a design decision at the end of the day

with open("newname.txt","r") as file:
    for i in sorted(file,reverse=True): #to reverse sort
        print(i,end="")
