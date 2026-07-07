import random

class Hat:

    houses=["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
    @classmethod
    def sort(cls,name): #a function inside class
        print(name,"is in","house : " ,random.choice(cls.houses))
        #cls is for classmethod ,like self for objects in a same Class!!,When using a @classmethod, Python automatically passes the entire Class itself as cls.
        #When using a regular object method, Python automatically passes the individual object as self.

#hat=Hat() ; hat(name) . self ta python nijei diye daye! , for __init__ but now we are using classmethods
#now we dont need any "hat" objects like we did before the classmethod was used!!.
#classmethod use korar age, amra Class er under e init(self,...,...) use kortam ,and ekhane hat ekta obj jeta Class Hat er under e pore !!

Hat.sort("Harry") # because we are using classmethods,just Hat.sort() holei hbe
#eta class.classmethod() ; syntax arki
