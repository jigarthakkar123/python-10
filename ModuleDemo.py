import UDF

while True:
    print("*"*50)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Prime")
    print("5. Fibonacci")
    print("6. Exit") 
    print("*"*50)
    
    choice=int(input("Enter Your Choice : "))
    print("*"*50)
    
    if choice==1:
        n=int(input("Enter Value:"))
        UDF.oddeven(n)
        print("*"*50)
    elif choice==2:
        n=int(input("Enter Value:"))
        n1=int(input("Enter Value:"))
        UDF.maxoftwo(n,n1)
        print("*"*50)
    elif choice==3:
        n=int(input("Enter Value:"))
        n1=int(input("Enter Value:"))
        n2=int(input("Enter Value:"))
        UDF.maxofthree(n,n1,n2)
        print("*"*50)
    elif choice==4:
        n=int(input("Enter Value:"))
        UDF.prime(n)
        print("*"*50)
    elif choice==5:
        n=int(input("Enter Value:"))
        UDF.fibonacci(n)
        print("*"*50)
    else:
        print("Good Bye")
        break
