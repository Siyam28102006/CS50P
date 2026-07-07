class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name !!!")
        self.name = name

    # Every Wizard, Student, and Professor will use this to introduce themselves!
    def __str__(self):
        return f"My name is {self.name}."


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)  # Fixed: added () to super
        self.house = house

    # You can override the parent __str__ if the student needs a special format:
    def __str__(self):
        return f"{self.name} is a student from {self.house}."


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)  # Fixed: added () to super
        self.subject = subject

    # You can override the parent __str__ if the professor needs a special format:
    def __str__(self):
        return f"Professor {self.name} teaches {self.subject}."


def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense against Dark Arts")

    # Now printing is incredibly clean!
    print(wizard)     # Output: My name is Albus.
    print(student)    # Output: Harry is a student from Gryffindor.
    print(professor)  # Output: Professor Severus teaches Defense against Dark Arts.


if __name__ == "__main__":
    main()