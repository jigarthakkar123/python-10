from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

root=Tk()
root.title("My Tkinter Example")
root.geometry("420x480")
root.resizable(width=False,height=False)

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            database="python_tts_10_30",
            user="root",
            password=""
        )

def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")      

def search_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    if e_id.get()=="":
        msg.showinfo("Search Status","Id Is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
        else:
            msg.showinfo("Seartch Status","Id Not Found")
        conn.close()
            

def update_data():
    if e_id.get()=="" or e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Update Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update student set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Successfully")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","Id Is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Delete Status","Data Deleted Successfully")


l_id=Label(root,text="ID",font=("Arial",15))
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME",font=("Arial",15))
l_fname.place(x=50,y=120)

l_lname=Label(root,text="LAST NAME",font=("Arial",15))
l_lname.place(x=50,y=190)

l_email=Label(root,text="EMAIL",font=("Arial",15))
l_email.place(x=50,y=260)

l_mobile=Label(root,text="MOBILE",font=("Arial",15))
l_mobile.place(x=50,y=330)

e_id=Entry(root)
e_id.place(x=250,y=50)

e_fname=Entry(root)
e_fname.place(x=250,y=120)

e_lname=Entry(root)
e_lname.place(x=250,y=190)

e_email=Entry(root)
e_email.place(x=250,y=260)

e_mobile=Entry(root)
e_mobile.place(x=250,y=330)

insert=Button(root,text="INSERT",font=("Arial",15),fg="white",bg="black",command=insert_data)
insert.place(x=20,y=400)

search=Button(root,text="SEARCH",font=("Arial",15),fg="white",bg="black",command=search_data)
search.place(x=110,y=400)

update=Button(root,text="UPDATE",font=("Arial",15),fg="white",bg="black",command=update_data)
update.place(x=209,y=400)

delete=Button(root,text="DELETE",font=("Arial",15),fg="white",bg="black",command=delete_data)
delete.place(x=306,y=400)

root.mainloop()
