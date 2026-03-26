name = input("Enter your name : ")
age= input("Enter your age : ")
mark = input("Enter your mark : ")

koyta_golfen=int(input("Enter you golfen songkha : "))
print(type(koyta_golfen))
# input always string format e hoy.so kono operations korar somoy eta kheyal rekhe typecast kora lagte pare
print(type(age))
print(f"My name is {name}")
print(f"my mark is {mark}")
print(f"My age is {age} years old")

age= int(age)+1
mark= int(mark)
mark+=3020
print(f"My new age is {age} && my new mark is {mark} wahoooo")
print(f"My golfen songkha is {koyta_golfen}")