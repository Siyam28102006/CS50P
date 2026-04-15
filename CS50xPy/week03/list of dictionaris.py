students= [
    {"name":"Hermoine","House":"Gryffindor","Patronus":"Otter"},
    {"name":"Harry","House":"Gryffindor","Patronus":"Stag"},
    {"name":"Ron","House":"Gryffindor","Patronus":"Jack Russel Tarrier"},
    {"name":"Draco","House":"Slytherin" , "Patronus":None},
]

for i in students:
    print(f"The name of the student is : {i["name"]} and the House : {i["House"]} , Patronus : {i["Patronus"]}")

#stduents = []  --> is a list.in the list, {} is a dictionary and evabe onekgula dictionaries banano jae.
#name,House,Patronus etc holo dictionary er ek ekta key, jader moddhe value/string stored kora ache
#None --->> is a special keyword,which literally means nothing in python


print()
print('#'*4) #4bar hash
print('#\n'*4) #4bar hash but with newline