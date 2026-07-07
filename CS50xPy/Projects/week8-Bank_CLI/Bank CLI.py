import re
import sys

customer_data=[]
transaction_history=[]
class Bank_Account_Creation:
    def __init__(self,Name,Address,Cash_Remaining,Phone_Number):
        self.Name=Name
        self.Address=Address
        self.Phone_Number=Phone_Number
        self.Cash_Remaining = Cash_Remaining
    def __str__(self):
        return (f"\n--- Account Information ---\n"
                f"Name: {self.Name}\n"
                f"Phone Number: {self.Phone_Number}\n"
                f"City: {self.Address}\n"
                f"Balance: {self.Cash_Remaining} BDT\n"
                f"---------------------------")

    def deposit_cash(self,amount):
        print(f"The previous amount was {self.Cash_Remaining} for the account {self.Name} \n")
        self.Cash_Remaining += amount
        print(f"The new amount was {self.Cash_Remaining} for the account {self.Name} \n")

    def withdraw_cash(self,amount):
        print(f"The previous amount before withdrawal was {self.Cash_Remaining} for the account {self.Name} \n")
        self.Cash_Remaining -= amount
        print(f"The new amount was {self.Cash_Remaining} for the account {self.Name} \n")

    def Change_Info(self,Name,Address,Phone_Number):
        self.Name=Name
        self.Address=Address
        self.Phone_Number=Phone_Number


def main():
    print(f"Welcome to Bank CLI.What do u wanna do today ? .....\n" )
    while True:
        options()
        print(f"Select a number to proceed!! ")
        try:
            uwu = int(input("Option no : "))
            if uwu>8 or uwu<=0:
                print(f"Enter from 1 to 8 only !!")
                continue
        except ValueError:
            print("Enter a number only from the options")
            continue #crucial! Skips down to loop restart, preventing NameError

        if uwu==1:
            newAccount = newaccountinfo()
        elif uwu == 2:
            deposit()  # Runs the deposit system!
        elif uwu == 3:
            withdrawal() #runs withdrawal system
        elif uwu == 4:
            change_acc_info()
        elif uwu == 5:
            view_account_info()
        elif uwu == 6:
            history_of_transaction()
        elif uwu==7:
            show_balance()
        elif uwu==8 :
            print("Thank you for using Bank CLI. Goodbye!")
            sys.exit()


def newaccountinfo():
    while 1:
        nname=input("Enter your bank account name(Must be in block letters !) : ")
        if re.search(r"^[A-Z_. ]+$",nname) : #+ means 1 or more
            Name=nname
            break
        else:
            print(f"Please enter your name in BLOCK letters only i.e A,B,C,.....,Z\n")
    while 1:
        Address=input("Enter your city : ")
        if len(Address)>2:
            break
        else:
            print(f"Please enter the correct city name\n")

    while 1:
        number=input("Enter your phone number : ")
        if re.search(r"^[0-9]+$",number) and len(number)==11:
            Phone_Number=number
            break
        else:
            print(f"Please enter the phone number\n")

    Cash_Remaining=int(0)

#without obj arki
    # new_customer_data={"name":Name,"Phone_Number":Phone_Number,"Cash remaining":Cash_Remaining,"Address":Address}

    #store data with obj#new customer_data is an obj of Bank_account_creation Class.sei full obj tai list of dict e store hocche!!
    new_customer_data = Bank_Account_Creation(Name, Address, Cash_Remaining, Phone_Number)
    customer_data.append(new_customer_data)
    print(f"\n Account successfully created for {Name}! \n")
    return new_customer_data

def options():
    print(f"1.Create new Account\n2.Deposit\n3.Withdrawal\n4.Change Information of Existing Account\n5.View Account Information\n6.Transaction History\n7.Show balance\n8.Exit")

def deposit():
    search_acc=input("Enter account no. : ")
    found_acc = None # Tracks the object itself, start it as None.found-acc is an object jeta None diye initialize kora lage!.eta diye object tai track hoy
    for i in customer_data: #i is an actual object jeta ke found_acc grab korbe and ei i e account er shob info thakbe but in the cond. we are using the phone number to match
        if i.Phone_Number==search_acc:
            found_acc=i
            break
    if found_acc:# If it found something, found_acc will hold the object (which is True)
        while 1:
            try:
                amnt=int(input("Enter the amount u want to deposit : "))
            except ValueError:
                print("Enter a valid integer.")
                continue
            if amnt>0:
                found_acc.deposit_cash(amnt)
                transaction = f"{found_acc.Phone_Number} deposited {amnt} BDT of cash"
                transaction_history.append({"Phone_Number":found_acc.Phone_Number,"Transaction":transaction})
                break
            else:
                print("Deposit amount must be greater than 0.")
                continue
    else:
        print(f"Account doesn't exist in the system!!\n")

        # 🔄 MEMORY FLOW ARCHITECTURE: HOW DEPOSIT TALKS TO THE OBJECT
        # ==================================================================================
        #
        # [1. deposit() Function]
        #       │
        #       ├─► Asks user for phone number string ("01711223344")
        #       ├─► Loops through customer_data list
        #       ├─► Matches i.Phone_Number
        #       │       │
        #       │       ▼
        #       │   Assigns found_acc = i (found_acc now holds a pointer to the target object)
        #       │
        #       ├─► Asks user for deposit amount integer (e.g., 500)
        #       └─► Calls found_acc.deposit_cash(500)
        #                │
        #                ▼
        # [2. Bank_account_creation Class Method]
        #       │
        #       └─► def deposit_cash(self, amount):
        #               │
        #               └─► self.Cash_Remaining += amount
        #                   (Modifies the balance directly inside the live object!)

def withdrawal():
    search_acc=input("Enter account no. : ")
    found_acc=None
    for i in customer_data:
        if i.Phone_Number==search_acc:
            found_acc=i
            break
    if not found_acc:
        print(f"Account doesn't exist in the system!!\n")
    else:
        while 1:
            try:
                amnt=int(input("Enter the amount u want to withdraw : "))
                if amnt>0 and amnt<=found_acc.Cash_Remaining:
                    found_acc.withdraw_cash(amnt)
                    transaction = f"{found_acc.Phone_Number} withdrew {amnt} BDT of cash"
                    transaction_history.append({"Phone_Number": found_acc.Phone_Number, "Transaction": transaction})
                    break
                else:
                    print(f"Insufficient funds! You cannot withdraw {amnt} BDT. Please try a lower amount.\n")
            except ValueError:
                print(f"Enter a valid integer value greater than 0")
                continue

def view_account_info():
    search_acc = input("Enter account no. : ")
    found_acc = None
    for i in customer_data:
        if i.Phone_Number == search_acc:
            found_acc = i
            break
    if not found_acc:
        print(f"Account doesn't exist in the system!!\n")
    else:
        print(found_acc)

def show_balance():
    acc=input("Enter the account number : ")
    found_acc=None
    for i in customer_data:
        if i.Phone_Number==acc:
            found_acc=i
            break
    if (found_acc):
        print(f"The balance for {found_acc.Phone_Number} is {found_acc.Cash_Remaining} BDT\n")
    else :
        print(f"{acc} doesn't exist in the Bank System !! ")



def change_acc_info():
    search_acc=input("Enter Your Account Number : ")
    found_acc = None
    for i in customer_data:
        if i.Phone_Number == search_acc:
            found_acc = i
            break
    if not found_acc:
        print(f"Account doesn't exist in the system!!\n")
    else:
        n=input("Do you want to change your account info ?[y/n] : ")
        if n=='y':
            while 1:
                print(f"What do u want to change ? \n   1.Phone Number\n   2.Address\n")
                new_number=int(input("Enter an option Number : "))
                if new_number==1:
                    new_number=input("Enter your new phone number : ")
                    new_name=found_acc.Name
                    new_address=found_acc.Address
                    found_acc.Change_Info(new_name,new_address,new_number)
                    break
                elif new_number==2:
                   # new_number = search_acc.Phone_Number ❌ Crash 1: search_acc is a string, not the object! so not correct,use the object found_acc!!
                    new_number = found_acc.Phone_Number
                    new_name = found_acc.Name
                    new_address = input("Enter your new address : ")
                    found_acc.Change_Info(new_name,new_address,new_number)
                    break
                else:
                    print(f"Invalid option number,try againnnnnn!!!!")
                    continue
        elif n=='n':
            print(f"Going back to the main menu.....................")
            options()


def history_of_transaction():
    cnt=int(0)
    found=False
    uwu=input("What's ur account phone number : ")
    if re.search(r"^[0-9]+$", uwu) and len(uwu) == 11:
        for i in transaction_history:
            if i['Phone_Number']==uwu:
                found=True
                break
        if found:
            for j in transaction_history:
                if j['Phone_Number']==uwu:
                    cnt += 1
                    print(f"{cnt}.{j['Transaction']}")
        else:
            print("No Transaction history Available!!")
    else:
        print("Enter Again with the correct phone Number")





if __name__=="__main__":
    main()