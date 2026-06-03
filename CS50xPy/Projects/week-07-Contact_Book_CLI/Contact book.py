import re
import sys

contacts = []
def menu():
    print("\n----- MENU -----")
    print("1. Add New Contact\n2. Search\n3. Delete Contact\n4. Edit Existing Contact\n5. View Contact List\n6. View Menu\n7.Saving contact list as a file\n8. Exit the Contact Book")


def Add_new_contact():
    while True:
        enter_name = input("\nWhat's the name? ")
        if re.search(r"^([a-zA-Z '-])+$", enter_name):
            valid_name = enter_name
        else:
            print("Invalid name! Please use only letters and spaces.")
            continue

        enter_phone_number = input("Enter Phone Number: ")
        if re.search(r"^\d+$", enter_phone_number) and len(enter_phone_number) == 11:
            valid_phone_number = enter_phone_number
        else:
            print("Invalid number! Please enter exactly 11 digits.\n")
            continue

        enter_email = input("What's your email? ").strip()
        if re.search(r"^(\w|[.])+@(\w+[.])*(\w|[.])+[.](\w)+$", enter_email, re.IGNORECASE):
            valid_email = enter_email
        else:
            print("Invalid email format!")
            continue

        contact_data = {"name": valid_name, "email": valid_email, "Phone Number": valid_phone_number}
        contacts.append(contact_data)
        print(f"Successfully added {valid_name}!\n")

        choice = input("Do you want to add another contact? (y/n): ").strip().lower()
        if choice == 'n':
            print("Returning to main menu.")
            break
        elif choice == 'y':
            print("Enter the info for another contact!!")
            continue
        else:
            print("Invalid option. Returning to menu.")
            break


def view_contact_list():
    if not contacts:
        print("\nYour contact list is empty!")
    else:
        for i in contacts:
            print(f"\nThe info of Name: {i['name']}\n    Email: {i['email']}\n    Phone Number: {i['Phone Number']}")


def edit_contacts():
    if not contacts:  # empty list
        print("\nNothing to Edit here. It's Empty!")
        return
    else:
        found = False
        name_search = input("\nEnter The Name you want to edit info on?: ")
        for i in contacts:
            if name_search == i['name']:
                found = True
                while True:
                    uu = input("Found! What do you want to change? [name / number / email]? ").strip().lower()
                    if uu == 'name':
                        while True:
                            new_name = input("Enter new name: ").strip()
                            if re.search(r"^([a-zA-Z '-])+$", new_name):
                                i['name'] = new_name
                                break
                            else:
                                print("Invalid name! Please use only letters and spaces and try again.")
                                continue
                        break  # for the while just before uu=input(....)
                    elif uu == 'number':
                        while True:
                            new_number = input("Enter the new Number: ")
                            if re.search(r"^\d+$", new_number) and len(new_number) == 11:
                                i['Phone Number'] = new_number
                                break
                            else:
                                print("Invalid number! Please enter exactly 11 digits.\n")
                                continue
                        break  # for the while just before uu=input(....)
                    elif uu == 'email':
                        while True:
                            new_email = input("Enter the new Email: ")
                            if re.search(r"^(\w|[.])+@(\w+[.])*(\w|[.])+[.](\w)+$", new_email, re.IGNORECASE):
                                i['email'] = new_email
                                break
                            else:
                                print("Invalid email format! Please enter again!!!")
                                continue
                        break  # for the while just before uu=input(....)
                    else:
                        print("Please enter one of the following! name / email / number")
                        continue
                break  # for the 'for loop'
        if not found:
            print(f"The entered name: {name_search}, is not in the list.\n")


def search_contacts():
    if not contacts:
        print("\nNothing here. It's Empty!")
        return
    else:
        name_search = input("\nEnter The Name you want to search?: ")
        found = False
        for i in contacts:
            if name_search == i['name']:
                found = True
                print(f"\nThe info of Name: {i['name']}\n    Email: {i['email']}\n    Phone Number: {i['Phone Number']}")
                break
        if found == False:
            print(f"The contact '{name_search}' doesn't exist!\n")


def delete_contacts():
    if not contacts:
        print("\nThe List is Empty!!\n")
        return
    else:
        dlt_name = input("\nEnter the name of the contact you want to delete: ")
        found = False
        for i in contacts:
            if dlt_name == i['name']:
                contacts.remove(i)
                print(f"'{dlt_name}' has been deleted successfully!")
                found = True
                break
        if not found:
            print(f"The contact '{dlt_name}' doesn't exist!\n")

def save_the_contact_list():
    file_name=input("What do you want to save it as ? : ")
    with open(f"{file_name}.txt", "w") as file:
        for i in contacts:
            file.write(f"Info for {i['name']} :\n")
            file.write(f"          Email : {i['email']}\n")
            file.write(f"          Phone Number : {i['Phone Number']}\n\n")
        print(f"Successfully saved to {file_name}.txt!\n")
def main():
    print("----------- Welcome to Contact Book CLI -----------")
    while True:
        menu()
        select = int(input("\nSelect an option (1 - 8): "))
        if select == 1:
            Add_new_contact()
        elif select == 2:
            search_contacts()
        elif select == 3:
            delete_contacts()
        elif select == 4:
            edit_contacts()
        elif select == 5:
            view_contact_list()
        elif select == 6:
            menu()
        elif select == 7:
            inn=input("Do you want to save the contact list ? [y/n] :-> ").strip().lower()
            if inn=='y':
                save_the_contact_list()
            else:
                print("Alright , going back to the menu!! \n")
        elif select == 8:
            if (w := input("Do you want to continue? [y/n]: ").strip().lower() == "y"):
                continue
            else:
                print("\nExiting the Contact Book........ !!")
                sys.exit()


if __name__ == "__main__":
    main()