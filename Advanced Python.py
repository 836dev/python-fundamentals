class Student:
    def getData(self,fname,lname):
        self.f=fname
        self.l=lname
    def putData(self):
        print("First Name : ",self.f)
        print("Last Name : ",self.l)

s1=Student()
s1.getData("Dev ","Patel")
s1.putData()

print("*"*50, "\n")


class Cars:
    def getData(self,model,year):
        self.m=model
        self.y=year
    def putData(self):
        print("Model of Car : ",self.m)
        print("Year of Car : ",self.y)
s1=Cars()
s1.getData("Volvo",1988)
s1.putData()
print("*"*50, "\n")
