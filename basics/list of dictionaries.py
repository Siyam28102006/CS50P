# A list containing dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "year": 1},
    {"name": "Harry", "house": "Gryffindor", "year": 1},
    {"name": "Ron", "house": "Gryffindor", "year": 1},
    {"name": "Draco", "house": "Slytherin", "year": 1}
]

for i in students:
    print(f"{i['name']} is in {i['house']} and studies in year {i['year']}")