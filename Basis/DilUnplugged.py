from tkinter import *
root=Tk()
root.geometry('500x500')
root.title("Dil Unplugged")
frame_Break=Frame(root,height=500,width=500,bg='gray')
frame_Break.pack(padx=140,pady=160,fill=BOTH,expand=1)
picture_break = PhotoImage(file="")
label=Label(frame_Break,image=picture_break)
label.place(x=0,y=0)

inn_dino=Radiobutton(label,text="Inn Dino",font=('calibre',15))
inn_dino.grid(row=1,column=0)
kabira=Radiobutton(label,text="Kabira",font=('calibre',15))
kabira.grid(row=2,column=0)
dil_diyan_gallan=Radiobutton(label,text="Dil Diyan Gallan",font=('calibre',15))
dil_diyan_gallan.grid(row=3,column=0)
woh_baarishein=Radiobutton(label,text="Woh Baarishein",font=('calibre',15))
woh_baarishein.grid(row=4,column=0)
label_heading=Label(label,text="Dil Unplugged",font=('calibre',20, 'bold',"underline"))
label_heading.grid(row=0,column=0)


root.mainloop()