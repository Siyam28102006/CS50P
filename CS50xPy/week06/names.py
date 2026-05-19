names=[]

for _ in range(3):
    x=input("What's your name ? : ")
    names.append(x)

for name in sorted(names):
    print(f"Hello,{name}")