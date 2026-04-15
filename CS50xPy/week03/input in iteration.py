n = int(input("How many items? "))
my_list = []


for i in range(n):
    item = input(f"Enter item {i+1}: ")
    my_list.append(item)


print(my_list)