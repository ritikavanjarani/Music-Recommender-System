from tkinter import *
root=Tk()
root.geometry('500x500')
root.title("Emotional Songs")
frame_Break=Frame(root,height=500,width=500,bg='gray')
frame_Break.pack(padx=140,pady=160,fill=BOTH,expand=1)
picture_break = PhotoImage(file="")
label=Label(frame_Break,image=picture_break)
label.place(x=0,y=0)

tere_mere=Radiobutton(label,text="Tere Mere",font=('calibre',15))
tere_mere.grid(row=1,column=0)
ik_vaari_aa=Radiobutton(label,text="Ik Vaari Aa",font=('calibre',15))
ik_vaari_aa.grid(row=2,column=0)
mai_agar=Radiobutton(label,text="Mai Agar",font=('calibre',15))
mai_agar.grid(row=3,column=0)
thodi_dher=Radiobutton(label,text="Thodi Dher",font=('calibre',15))
thodi_dher.grid(row=4,column=0)
label_heading=Label(label,text="Emotional Songs",font=('calibre',20, 'bold',"underline"))
label_heading.grid(row=0,column=0)


root.mainloop()