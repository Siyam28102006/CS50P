import csv
import sys

with open("Students2.csv", "a") as file:
    writer = csv.writer(file)
    while True:
        name=input("what's your name? ")
        home=input("Where's your home? ")
        writer.writerow([name, home])
        uwu=input("do you want to continue [y/n] ? ")
        if uwu=="n":
            sys.exit()