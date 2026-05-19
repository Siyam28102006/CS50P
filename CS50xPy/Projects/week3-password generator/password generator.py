import random
def main():
    character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(){}[]/+-=/"
    character_without_num = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(){}[]/+-=/"
    character_without_symbol = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    character_without_symbol_and_number ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        number=int(input("How many random passwords : "))
        if number <= 0 :
            print("Invalid input for the number of passwords.Must be at least 2 ! give input again ")
            continue
        length=int(input("Length of password : "))
        if length<6:
            print("Invalid input for password length.Must be at least 6 words")
            continue
        num=input("Do you want numbers in your password [y/n] ? :")
        sym=input("Do you want symbols in your password [y/n] ? :")
        for i in range(number):
            password=""
            j=1
            while j<=length:
                if num=='n' and sym=='n' :
                    password+=random.choice(character_without_symbol_and_number)
                elif num=='n':
                    password += random.choice(character_without_num)
                elif sym=='n':
                    password += random.choice(character_without_symbol)
                else :
                    password += random.choice(character)
                j+=1
            if (i+1)==1:
                 print(f"{i+1}st password is : {password}")
            elif (i+1)==2:
                print(f"{i+1}nd password is : {password}")
            elif (i+1)==3:
                print(f"{i+1}rd password is : {password}")
            else :
                print(f"{i+1}th password is : {password}")
        break

if __name__ == "__main__":
    main()



