import sys

def show_menu():
    print("-----MENU-----")
    print("01 : Add task")
    print("02 : Delete task")
    print("03 : View Tasks")
    print("04 : Tasks Left to do")
    print("05 : Clear List")
    print("06 : Exit")


def add_task(mylist,x): #1
    added=0
    for i in range(x):
        while True:
            task=input(f"Enter a task {i+1}: ").strip()
            #Users might accidentally enter spaces. .strip() prevents ghost tasks from being added or failing to delete:
            if len(task)!=0:
                mylist.append(task)
                added+=1
                break
            else : print("Please write something meaningful!!!")
    print(f"Total {added} tasks added newly!!")

def delete_task(mylist, task): #2
    if len(mylist) == 0:
        print("No tasks to delete!")
        return
    elif task not in mylist:
        print("Task not found.")
        return
    else:
        mylist.remove(task)
        print("Task deleted successfully.")


def view_tasks(mylist): #3
    print("Your tasks are : ")
    for i in range(len(mylist)):
        print(f"{i+1}.{mylist[i]}")

def task_count(mylist): #4
    print(f"Total tasks left to do : {len(mylist)}")

def clear_list(mylist): #5
    mylist.clear()




def main():
    mylist=[]
    while True:
        show_menu()
        try:
            n=int(input("Enter the Option : "))
            if n==1:
                x = int(input("Enter the amount of task: "))
                if x <= 0:
                    print("Please enter a positive number.")
                else:
                    add_task(mylist, x)
                print()
            elif n==2:
                if len(mylist)!=0:
                    view_tasks(mylist)
                    task=input("Enter the task you want to delete: ")
                    delete_task(mylist,task)
                elif len(mylist)==0:
                    print("No tasks to delete!!")
                print()
            elif n==3 :
                if len(mylist)!=0:
                    view_tasks(mylist)
                else :
                    print("The list is empty ! add something")
                print()
            elif n==4 :
                task_count(mylist)
                print()
            elif n==5:
                if len(mylist) == 0:
                    print("List is already empty")
                elif len(mylist)!=0:
                    confirm=input("Do you want to clear the entire list of tasks?[Y/N]").strip().upper()
                    if confirm== 'Y' and len(mylist)!=0:
                        clear_list(mylist)
                        print("List Cleared Successfully")
                    elif confirm=='N':
                        print("Operation Cancelled")
                    else:
                        print("Please enter Y or N.")
                    print()
            elif n==6:
                sys.exit()
            else :
                print("Please enter a valid number given on the menu")
        except ValueError:
            print("Please Enter an Integer !!")


main()