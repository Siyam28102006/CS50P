class  Student:
    def __init__(self,name,house): #constructor
        if not name:
            raise ValueError(f"Missing Name!!")
        self.name=name #it can call the setter method
        if not house:
            raise ValueError(f"Missing Name!!")
        self.house=house #it can call the setter method

    def __str__(self):
        return f"{self.name} is from {self.house}"


#house
    @property #getter
    def house(self):
        return self._house

    @house.setter#setter
    def house(self,house):
        if house not in["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid House")
        self._house=house #ekhane pouchaile the data gets stored and it is correct
                          #self._house is a string not a func!!! tai () nai!

#name
    @property #this property decorayor turns this method into a getter
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if name not in ["Harry","Ron"]:
            raise ValueError(f"Invalid Name")
        self._name=name

#so property attribute is house but instance variable is _house!!

def main():
        student = get_student()
       # print(f"{student.name} is from {student.house}")
        print(student)

def get_student():
        name=input("Name : ").capitalize()
        house=input("House : ").strip().capitalize()
        #student=Student(name,house) #constructor call & creates a student object!
        return Student(name,house)
if __name__ == "__main__":
        main()