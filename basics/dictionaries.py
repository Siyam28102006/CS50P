# Mapping Name (Key) to House (Value)
hogwarts_students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# Accessing a value using a key
print(hogwarts_students["Draco"])  # Output: Slytherin

for i in hogwarts_students:
    print(f"key is -> {i} and the value is -> {hogwarts_students[i]}")