class Bank:
    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",self.cname, ", Your Account Number ",self.acno,", Is opened with ,",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
        else:
            self.needs=amount-self.blance
            print("Sorry You Need Another ",self.needs,"Rs. To Withdraw")
    def checkBalance(self):
        print("Current Balance : ",self.balance)
        
b1=Bank()
acno=int(input("Enter Account Number : "))
cname=input("Enter Customer Name : ")
balance=int(input("Enter Initial Balance : "))

b1.openAccount(acno,cname,balance)
while True:
    print("*"*50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice: "))
    print("*"*50)
    
    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*"*50)
    elif choice==2:
        amount=int(input("Enter Withdrawl Amount : "))
        b1.withdraw(amount)
    elif choice==3:
        b1.checkBalance()
        print("*"*50)
    elif choice==4:
        print("Thank You for using our Services.")
        print("*"*50)
        break
    else:
        print("Invalid Choice.Try Again")
