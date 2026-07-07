class  Student:
    def __init__(self,name,house):
        if not name: #if name=="" ,empty arki
            raise ValueError(f"Missing Name!!")
        if house not in["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid House")
        self.name=name # to store the passed name argument.
        self.house=house



def main():
        student = get_student()
        print(f"{student.name} from {student.house}")

def get_student():
        name=input("Name : ").capitalize()
        house=input("House : ").strip().capitalize()
        #student=Student(name,house) #constructor call
        return Student(name,house)
if __name__ == "__main__":
        main()