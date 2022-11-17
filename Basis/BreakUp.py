from tkinter import *
root = Tk()
root.geometry('500x500')
root.title("Break Up Songs")
frame_Break = Frame(root, bg='light blue', height=500, width=500, )
frame_Break.pack(padx=140, pady=160, fill=BOTH, expand=1)
picture_break = PhotoImage(file="")
label=Label(frame_Break,image=picture_break)
label.place(x=0,y=0)

love_yourself=Radiobutton(label,text="Love Yourself",font=('calibre',15))
love_yourself.grid(row=1,column=0)
Tujhe_Bula_Diya=Radiobutton(label,text="Tujhe Bula Diya",font=('calibre',15))
Tujhe_Bula_Diya.grid(row=2,column=0)
Stitches=Radiobutton(label,text="Stitches",font=('calibre',15))
Stitches.grid(row=3,column=0)
Ae_Dil_Hai_Mushkil=Radiobutton(label,text="Ae Dil Hai Mushkil",font=('calibre',15))
Ae_Dil_Hai_Mushkil.grid(row=4,column=0)
label_heading=Label(label,text="Break Up Songs",font=('calibre',20, 'bold',"underline"))
label_heading.grid(row=0,column=0)


root.mainloop()