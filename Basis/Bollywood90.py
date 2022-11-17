from tkinter import *
root=Tk()
root.geometry('500x500')
root.title("Bollywood 90's")

frame_Break=Frame(root,height=500,width=500,bg='gray')
frame_Break.pack(padx=140,pady=160,fill=BOTH,expand=1)
picture_break = PhotoImage(file="")
label=Label(frame_Break,image=picture_break)
label.place(x=0,y=0)

hum_dil_se_haare=Radiobutton(label,text="Hum dil se Haare",font=('calibre',15))
hum_dil_se_haare.grid(row=1,column=0)
hum_dil_de_chuke_sanam=Radiobutton(label,text="Hum dil de chuke sanam",font=('calibre',15))
hum_dil_de_chuke_sanam.grid(row=2,column=0)
tu_hi_re=Radiobutton(label,text="Tu Hi Re",font=('calibre',15))
tu_hi_re.grid(row=3,column=0)
hum_yahan=Radiobutton(label,text="Hum Yahan",font=('calibre',15))
hum_yahan.grid(row=4,column=0)
label_heading=Label(label,text="Bollywood 90's",font=('calibre',20, 'bold',"underline"))
label_heading.grid(row=0,column=0)


root.mainloop()