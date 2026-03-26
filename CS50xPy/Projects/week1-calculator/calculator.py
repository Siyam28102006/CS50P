def add(a,b):
    return a+b

def subt(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


def main():
    print(f"Available operations are: +,-,x,/,exit ")
    z = float(0)

    while 1:
        s = input("Enter operation : ")

        if s == "exit":
            return

        elif s != "exit":
            if z == 0:
                x = float(input("Enter x: "))
                y = float(input("Enter y: "))
            elif z != 0:
                x = float(input("Enter x : "))

            if s == '+':
                if z == 0:
                    z=add(x, y)
                    print(z)
                else:
                    z=add(z, x)
                    print(z)

            elif s == '-':
                if z == 0:
                    z=subt(x, y)
                    print(z)
                else:
                    z=subt(z, x)
                    print(z)

            elif s == 'x':
                if z == 0:
                    z=mul(x, y)
                    print(z)
                else:
                   z=mul(z, x)
                   print(z)

            elif s == '/':
                if y==0:
                    print("Error")
                elif z == 0 and y!=0 :
                    z=div(x, y)
                    print(z)
                elif z!=0 and y!=0 :
                    z=div(z,x)
                    print(z)



main()