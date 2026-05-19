import sys
import os
from PyPDF2 import PdfMerger

UwU=[]

sub=input("Enter The Name of the Subject : ")
print("Enter the file you want to append : ")
cnt=0
while True:
    name=input("What's the file name? ")+'.pdf'
    if os.path.exists(name):
        UwU.append(name)
        cnt += 1
        if (cnt > 0):
            e = input("Do you want to continue ? [y/n]").lower().strip()
            if e == "n":
                break

    else :
        print("Not found !!! Try Again with a proper name!")
        continue


merger=PdfMerger()
for pdf in UwU :
    print(f"Adding {pdf} ........ ")
    merger.append(pdf)

merger.write(f"{sub} all Merged.pdf")
merger.close()