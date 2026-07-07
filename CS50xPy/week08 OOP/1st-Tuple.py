def main():
    #house,name = get_stduent() #same sequence as return !!
    student=get_stduent()
    print(f"{student[1]} from {student[0]}")


def get_stduent():
    name=input("Name : ")
    house = input("House : ")
    return (house,name)

if __name__== "__main__":
    main()