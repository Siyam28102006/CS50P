""" comment """
name=input("what's your name?" )
"""
#rmove whitespace
name=name.strip()
#capitialize 1st character
name=name.capitalize()

#capitalize the first letter or every word
name=name.title()
"""
name=name.strip().title() #whitespace rmv & proti word er capitalization of 1st letter eksathe
print(f"My name is {name}")
first,last=name.split() # name ke duita part e bhag, first =David & last = Malan
print(f"Hello,{first}")
#usually input string e ashe and + diye string concat kore
x=float(input("what's x ? "))
y=float(input("what's y ? "))

z=x/y
print(f"{z:.2f}")