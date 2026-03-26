# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# def is_even(n):
#     return True if n%2==0 else False

#easier way(pythonic) given below

def is_even(n):
    return n%2==0
# just return the question

def main():
    x=int(input("What's x? "))
    if is_even(x):
        print(f"Even")
    else :
        print(f"Odd")


main()