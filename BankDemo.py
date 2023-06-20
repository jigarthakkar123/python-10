class Bank:

    def openAccount(self,cname,acno,balance):
        self.c=cname
        self.a=acno
        self.b=balance
        print("Hello ",self.c,", Your Account Number ",self.a," Is Opened With ",self.b," Rs.")
    def deposit(self,amount):
        self.b=self.b+amount
    def withdraw(self,amount):
        if amount<=self.b:
            self.b=self.b-amount
        else:
            print("Sorry You Need Another ",amount-self.b," Rs.")
    def checkBalance(self):
        print("Current Balance : ",self.b)


b1=Bank()
print("*"*75)
cname=input("Enter Customer Name : ")
print("*"*75)
acno=int(input("Enter Account Number : "))
print("*"*75)
balance=int(input("Enter Initial Balance : "))
print("*"*75)
b1.openAccount(cname,acno,balance)
print("*"*75)

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*75)
    choice=int(input("Enter Your Choice:"))

    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*"*75)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("*"*75)
    elif choice==3:
        b1.checkBalance()
        print("*"*75)
    else:
        print("Thank You For Using Our Services.Have Good Day")
        print("*"*75)
        break
    
        
