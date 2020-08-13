from tkinter import *
import sqlite3

root=Tk()
root.title("Db creater")


def conn():
    con=sqlite3.connect('addr.db')
    c=con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS address (firsrname text,lastname text,address text,mobilenumber integer)")    
    c.execute("INSERT INTO address VALUES (:fname,:lname,:addr,:mob)",
                {
                    'fname':fname.get(),
                    'lname':lname.get(),
                    'addr':addr.get(),
                    'mob':mob.get()
                    }

              )

    fname.delete(0,END)
    lname.delete(0,END)
    addr.delete(0,END)
    mob.delete(0,END)
    con.commit()
    con.close()
def retrive():
    con=sqlite3.connect('tasks.db')
    c=con.cursor()
    c.execute("SELECT *FROM tasks")
    t=c.fetchall()
    print_records=''
    for i in t:
        print_records+=str(i[0])+"\t"+str(i[1])+"\t"+str(i[2])+"\t"+str(i[3])+"\n"
        ql=Label(root,text=print_records)
        ql.grid(row=11,column=0,columnspan=2)
    con.commit()
    con.close()
def delete():
    conn=sqlite3.connect('addr.db')
    c=conn.cursor()
    c.execute("DELETE from address WHERE lastname ='%s'"%delet.get())
    delet.delete(0,END)
    conn.commit()
    conn.close()
    
fname= Entry(root,width=30)
fname.grid(row=0,column=1,padx=20)
lname= Entry(root,width=30)
lname.grid(row=1,column=1,padx=20)
addr= Entry(root,width=30)
addr.grid(row=2,column=1,padx=20)
mob= Entry(root,width=30)
mob.grid(row=3,column=1,padx=20)
delet= Entry(root,width=30)
delet.grid(row=6,column=1,padx=20)

fl=Label(root,text="Enter First name")
fl.grid(row=0,column=0)
ll=Label(root,text="Enter Last name")
ll.grid(row=1,column=0)
al=Label(root,text="Enter address")
al.grid(row=2,column=0)
ml=Label(root,text="Enter Mobile number")
ml.grid(row=3,column=0)
deleta=Label(root,text="Enter Firstname to delete")
deleta.grid(row=6,column=0)

button=Button(root,text="Insert into table",command=conn,bg="black",fg="white")
button.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
butt=Button(root,text="get attrebutes in table",command=retrive,bg="blue",fg="white")
butt.grid(row=9,column=0,columnspan=3,pady=10,padx=10,ipadx=100)

delb=Button(root,text="DELETE in table",command=delete,bg="red",fg="white")
delb.grid(row=7,column=0,columnspan=3,pady=10,padx=10,ipadx=100)
root.mainloop()
