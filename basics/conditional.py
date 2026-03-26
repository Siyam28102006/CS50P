age=int(input("What's your age? : "))
if age>=18:
    print("You are allowed")
elif age<18 :
    print("You are not allowed")
else:
    print("Invalid age")

#always start from absolute left(identation)

temp=int(input("What's the temperature today ? : "))
if temp>=35:
        print("Hot")
elif 20<=temp<=35 :
        print("Normal")
else :
        print("Cold")