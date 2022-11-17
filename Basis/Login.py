from tkinter import *
root=Tk()
root.geometry('450x450')
root.title("Login Page")
f=Frame(root,height=450,width=450,bg='gray')
f.pack()
picture = PhotoImage(file="img_1.png")
label =Label(f,image=picture)
label.place(x=0,y=0,relheight=1,relwidth=1)
user_name=Label(label,text="Username").place(x=35,y=60)

user_password = Label(label,text="Password").place(x=35,y=100)

submit_button = Button(label, text="Submit").place(x=90,y=150)

user_name_input_area = Entry(label, width=30).place(x=110,y=60,width=120)

user_password_entry_area = Entry(label,width=30, show='*').place(x=110,y=100,width=120)

root.mainloop()