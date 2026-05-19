import random

x=random.randint(1,10)
print(f"X is {x}")

card=["gawk","Hiya","Ron"]
random.shuffle(card)
for i in card:
    print(i)