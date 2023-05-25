file=open("tops1.txt","w")
file.write("This is file management demo using python.")
file.close()
print("File Written Successfully")

file=open("tops1.txt","r")
print(file.read())
file.close()

file=open("tops1.txt","a")
file.write("\nNow this file is appended")
file.close()

file=open("tops1.txt","r")
print(file.read())
file.close()

file=open("tops2.txt","w+")
file.write("This is w+ mode using python.")
print("Current File Position : ",file.tell())
file.seek(0)
print("File Data : ",file.read())
file.close()
