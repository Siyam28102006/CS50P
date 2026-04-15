# The variable students is a dictionary (dict). In Python, dictionaries use curly braces {} and store data in key-value pairs.
# The Key: The student's name (e.g., "Hermione"). Keys must be unique.
# The Value: Their Hogwarts house (e.g., "Gryffindor").

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryndor",
    "Draco": "Slytherin",
}

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

for i in students:
    print(students[i],i,sep=" is in the index : ")