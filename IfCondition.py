'''
1. Simple If
    if condition:
        statement
2. If/else
    if condition:
        statement
    else:
        statement
3. Nested if
    if condition:
        if condition:
            statement
        else:
            statement
    else:
        statement
4. Ladder if
    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
        statement
'''
a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))

if a>b:
    if a>c:
        print("A Is Max Number")
    else:
        print("C Is Max Number")   
elif b>c:
    print("B Is Max Number")
else:
    print("C Is Max Number")
    
    
