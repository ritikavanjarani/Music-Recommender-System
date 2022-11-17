from tkinter import *

root = Tk()
root.geometry('700x700')
root.title('Relaxed')

relax_label = Label(root, text="Relaxed", font=('calibre', 10, 'bold'))
relax_label.place(x=0, y=0)

relax_frame = Frame(root, height=700, width=700, bg='white')
relax_frame.grid(padx=100, pady=60)

soul_frame = Frame(relax_frame, height=250, width=250, bg='white')
soul_frame.grid(row=0, column=1)
soul_picture = PhotoImage(file="img_soul.png")
soul_label = Label(soul_frame, image=soul_picture, padx=30, pady=30)
soul_label.place(x=0, y=0, relheight=1, relwidth=1)
soul_button = Checkbutton(soul_frame, text="Soul Southers", font=('calibre', 15, 'bold'))
soul_button.place(x=50, y=220)

vac_frame = Frame(relax_frame, height=250, width=250, bg='white')
vac_frame.grid(row=0, column=2)
vac_picture = PhotoImage(file="img_vac.png")
vac_label = Label(vac_frame, image=vac_picture, padx=30, pady=30)
vac_label.place(x=0, y=0, relheight=1, relwidth=1)
vac_button = Checkbutton(vac_frame, text="Vacation Plays", font=('calibre', 15, 'bold'))
vac_button.place(x=50, y=220)

dil_frame = Frame(relax_frame, height=250, width=250, bg='white')
dil_frame.grid(row=1, column=1)
dil_picture = PhotoImage(file="img_dil.png")
dil_label = Label(dil_frame, image=dil_picture, padx=30, pady=30)
dil_label.place(x=0, y=0, relheight=1, relwidth=1)
dil_button = Checkbutton(dil_frame, text="Dil Unplugged", font=('calibre', 15, 'bold'))
dil_button.place(x=50, y=220)


slow_frame = Frame(relax_frame, height=250, width=250, bg='white')
slow_frame.grid(row=1, column=2)
slow_picture = PhotoImage(file="img_slow.png")
slow_label = Label(slow_frame, image=slow_picture, padx=30, pady=30)
slow_label.place(x=0, y=0, relheight=1, relwidth=1)
slow_button = Checkbutton(slow_frame, text="Slow & Easy", font=('calibre', 15, 'bold'))
slow_button.place(x=50, y=220)


root.mainloop()