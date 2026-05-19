import sys

def show_menu():
        print("-----MENU-----\n")
        print("1 : Add task")
        print("2 : Delete task")
        print("3 : View Tasks")
        print("4 : Clear List")
        print("5 : Load")
        print("6 : Save file")
        print("7 : Exit\n")

def add(mylist):
    added=0
    try:
        n=int(input("Enter Amount of tasks to be added : "))
    except ValueError:
        print("Please Enter a Number!!")
        return
    if n>0:
        for i in range(n):
            task = input(f"Enter a task {i + 1}: ").strip()
            mylist.append(task)
            added += 1
        print(f"{added} Tasks were Added Successfully")

    else :
        print("No tasks were Added!!")
    print(" Don't forget to Save (Option 06) your tasks to review them again later !!")
def dlt(mylist):
    try:
        uwu=int(input("Enter the Task Serial You Want to Delete : "))
        if 0 < uwu <=len(mylist):
            mylist.pop(uwu-1)
            viewtasks(mylist)
        else :
            print("Enter a valid Task Serial!!")
            return
    except ValueError:
        print("Enter a Number !!")
        return
def viewtasks(mylist):
    if len(mylist)>0:
        print("Your tasks are : ")
        for i in range(len(mylist)):
            print(f"{i+1}.{mylist[i]}")
    else :
        print("No tasks Available")

def load(filename):
    try:
        with open(f"{filename}.txt","r") as file:
            readline=file.read().split("\n")
            return readline
    except FileNotFoundError:
        print(f"No File Found named {filename}.txt!!!")
        return []
def main():
    mylist=[]
    filename=input("Save Tasks as : ")
    while True:
        show_menu()
        try:
            num = int(input("Select A Task to Proceed With : "))
        except ValueError:
            print("Try Again!!")
            continue
        if num == 1:
            add(mylist)
        elif num==2:
            if len(mylist)!=0:
                dlt(mylist)
                viewtasks(mylist)
                with open(f"{filename}.txt", "w") as file:
                    file.write("\n".join(mylist))
            else :
                print("The list is already Empty!!")
        elif num==3:
            viewtasks(mylist)
        elif num==4:
            if len(mylist) == 0:
                print("List is already empty")
            elif len(mylist) != 0:
                confirm = input("Do you want to clear the entire list of tasks?[Y/N]").strip().upper()
                if confirm == 'Y' and len(mylist) != 0:
                    mylist.clear()
                    with open(f"{filename}.txt", "w") as file:
                        file.write("")  # overwrite with empty content
                    print("List Cleared Successfully")
                elif confirm == 'N':
                    print("Operation Cancelled")
                else:
                    print("Please enter Y or N.")
                continue
        elif num==5:
                mylist=load(filename) #returns the data of the filename to mylist
        elif num==6:
            with open(f"{filename}.txt","w") as file:
                file.write("\n".join(mylist))
        elif num==7:
            print("Good Bye!!")
            sys.exit()


if __name__=="__main__":
    main()