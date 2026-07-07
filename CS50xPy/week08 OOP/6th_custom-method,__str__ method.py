class  Student:
    def __init__(self,name,house,patronus):
        if not name: #if name=="" ,empty arki
            raise ValueError(f"Missing Name!!")
        if house not in["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid House")
        self.name=name # to store the passed name argument.
        self.house=house
        self.patronus=patronus


    def __str__(self):
        #return "a student"
        return f"{self.name} is from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:  # this handles everything else (onekta default in C++ er moto)
                return "🪄"

  #When you pass an object to print(), it automatically looks for the __str__ method inside that object's class to know how to convert it into text.
def main():
        student = get_student()
        print("Get Patronum!!!")
        print(student.charm())

def get_student():
        name=input("Name : ").capitalize()
        house=input("House : ").strip().capitalize()
        patronus=input("Patronus : ").title()
        #student=Student(name,house) #constructor call
        return Student(name,house,patronus)
if __name__ == "__main__":
        main()


# ====================================================================================
# WHY WE USE THE LOWERCASE VARIABLE 'student' INSTEAD OF THE CAPITAL CLASS 'Student'
# ====================================================================================
#
# 1. THE BLUEPRINT VS. THE INSTANCE (Class vs. Object)
# ---------------------------------------------------
# Think of the capital 'Student' as a factory blueprint or a architectural map.
# It defines what a student *should* have (name, house, patronus) and what they
# can *do* (like the charm() method). However, the blueprint itself isn't a real person.
#
# When you write:
# student = get_student()
#
# You are using the blueprint to manufacture a REAL, unique student object and
# saving it inside a lowercase variable named 'student'.
#
# * If you try to run: print(Student)
#   You are telling Python to print the literal blueprint. Python will just output
#   something unhelpful like: <class '__main__.Student'>
#
# * If you run: print(student)
#   You are telling Python to print the actual data of the specific person you just
#   created (e.g., Harry from Gryffindor).
#
#
# 2. HOW THE LOWERCASE VARIABLE INTERACTS WITH THE __str__ METHOD
# ---------------------------------------------------------------
# When you pass the lowercase 'student' variable into a print() function, Python
# triggers a specific chain reaction behind the scenes:
#
#   Step A: print(student) looks at the object and asks, "What class created you?"
#   Step B: It sees it was created by the 'Student' class blueprint.
#   Step C: It automatically searches inside that class for the __str__(self) method.
#   Step D: The 'self' parameter inside __str__(self) automatically represents your
#           lowercase 'student' instance.
#   Step E: It safely extracts self.name ("Harry") and self.house ("Gryffindor")
#           to construct and print a readable sentence.
#
# If you attempted to do print(Student), Python would completely skip this process
# because a bare blueprint doesn't possess individual 'self' data to pull from!
#
#
# SUMMARY CHEAT SHEET:
# -------------------
# * Use 'Student' (Capitalized) when you want to CREATE or define a new person.
# * Use 'student' (Lowercase variable) when you want to TALK TO, print, or use the
#   data of the specific person you just built.
#
# ====================================================================================