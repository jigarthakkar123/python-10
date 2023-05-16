#0 1 1 2 3 5 8 13 21 34 55 89

a,b=0,1
n=int(input("Enter N : "))

while b<n:
    print(b,end=" ")
    a,b=b,a+b
