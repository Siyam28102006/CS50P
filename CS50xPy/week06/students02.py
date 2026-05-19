students=[]

with open("students.csv","r") as file:
    for line in file :
        name,house,year=line.rstrip().split(",")
        student={"name":name,"house":house,"year":year}
        #student['name']=name
        #student['house']=house
        students.append(student)

#def get_name(student):
    #return student["name"] ; instead of get_name , we may use lambda function
#the lambda is weird syntax wise

uwu = lambda student:student["name"]
for student in sorted(students,key=uwu): # to sort on the name of the student of the dictionary
    print(f"{student['name']} from {student['house']} and s/he is in {student['year']}")