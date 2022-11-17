from tkinter import *
root=Tk()
root.geometry('500x500')
root.title("90's Waala Pyaar")
frame_Break=Frame(root,height=500,width=500,bg='gray')
frame_Break.pack(padx=140,pady=160,fill=BOTH,expand=1)
picture_break = PhotoImage(file="")
label=Label(frame_Break,image=picture_break)
label.place(x=0,y=0)

r1=Radiobutton(label,text="Tujhe Dekha To",font=('calibre',15))
r1.grid(row=1,column=0)
r2=Radiobutton(label,text="Ek Ladki ko Dekha",font=('calibre',15))
r2.grid(row=2,column=0)
r3=Radiobutton(label,text="Dil To Paagal Hai",font=('calibre',15))
r3.grid(row=3,column=0)
r4=Radiobutton(label,text="Mere Khwaboo",font=('calibre',15))
r4.grid(row=4,column=0)
label_heading=Label(label,text="90's Waala Pyaar",font=('calibre',20, 'bold',"underline"))
label_heading.grid(row=0,column=0)


root.mainloop()