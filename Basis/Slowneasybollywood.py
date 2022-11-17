from tkinter import *
root=Tk()
root.geometry('500x500')
root.title("Slow and Easy Bollywood")
frame_Break=Frame(root,height=500,width=500,bg='gray')
frame_Break.pack(padx=140,pady=160,fill=BOTH,expand=1)
picture_break = PhotoImage(file="")
label=Label(frame_Break,image=picture_break)
label.place(x=0,y=0)

tum_se_hi=Radiobutton(label,text="Tum Se Hi",font=('calibre',15))
tum_se_hi.grid(row=1,column=0)
kaise_hua=Radiobutton(label,text="Kaise Hua",font=('calibre',15))
kaise_hua.grid(row=2,column=0)
humraah=Radiobutton(label,text="Humraah",font=('calibre',15))
humraah.grid(row=3,column=0)
zara_zara=Radiobutton(label,text="Zara Zara",font=('calibre',15))
zara_zara.grid(row=4,column=0)
label_heading=Label(label,text="Slow and Easy Bollywood",font=('calibre',20, 'bold',"underline"))
label_heading.grid(row=0,column=0)


root.mainloop()