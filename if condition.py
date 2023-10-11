rno=int(input("Enter Roll NO :"))
sname=input("Enter Student Name :")
s1=int(input("Enter Marks of Maths :"))
s2=int(input("Enter Mars of Physics :"))
s3=int(input("Enter Marks of Chemistry :"))

Total=s1+s2+s3
per=Total/3

print("Roll.No :",rno)
print("Student Name :",sname)
print(Total)
print("percentage: ",per)

if s1>=40:
    if s2>=40:
        if s3>=40:
            if per>=70:
                print("Distinction")
            elif per>=60:
                print("First Class")
            elif per>=50:
                print("Second Class")
            elif per>=40:
                print("Pass Class")
            else:
                print("Fail")
        else:
            print("You are Fail in Maths")
    else:
        print("You are Fail in Physics")
else:
    print("You are Fail in Chemistry")
                                           

