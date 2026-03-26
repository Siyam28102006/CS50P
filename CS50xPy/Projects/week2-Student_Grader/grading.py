def grade(total_sub_number,total_mark):
    percentage=(total_mark/(total_sub_number*100))*100
    if percentage>=90 :
        return 'A*'
    elif percentage>=80 :
        return 'A'
    elif percentage>=75:
        return 'A-'
    elif percentage>=70:
        return 'B'
    elif percentage>=65:
        return 'B-'
    elif percentage>=60:
        return 'C'
    elif percentage>=55:
        return 'C-'
    elif percentage>=40:
        return 'D'
    else :
        return "Fail"




def main():
    z=0;total_mark=0;exam_mark=0;
    print("NB : If you entered here by mistake,just give \"input subject = end\" to end the progress. ")
    while 1:
        sub_name=input("Input Subject : ")
        if sub_name == "end":
            break
        else :
            sub_mark=int(input(f"Input marks of {sub_name} : "))
            if sub_mark>100 or sub_mark<0:
                print("error.Please input the correct marks again.")
                continue
            z+=1
            total_mark+=sub_mark
            uwu=input("Do you want to keep going? [y/n] : ")
            if(uwu!="y"):break

    #grade(z,total_mark)
    if z!=0:
        print(f"Your percentage is {(total_mark/(z*100))*100:.2f} %")
        print(f"Your grade is : {grade(z,total_mark)}" )
    else:
        print("No subjects were given as input")
main()