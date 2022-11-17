from tkinter import *

root=Tk()
root.geometry('700x700')
root.title('Mood')

mood_label=Label(root,text="Mood",font=('calibre',10, 'bold'))
mood_label.place(x=0,y=0)

mood_frame=Frame(root,height=700,width=700,bg='white')
mood_frame.grid(padx=100, pady=60)

relaxed_frame=Frame(mood_frame,height=250,width=250,bg='white')
relaxed_frame.grid(row=0,column=1)
relaxed_picture=PhotoImage(file="img_6.png")
relaxed_label=Label(relaxed_frame,image=relaxed_picture,padx=30,pady=30)
relaxed_label.place(x=0,y=0,relheight=1,relwidth=1)
relaxed_button=Checkbutton(relaxed_frame,text="Relaxed",font=('calibre',15, 'bold'))
relaxed_button.place(x=50,y=220,)

romantic_frame=Frame(mood_frame,height=250,width=250,bg='white')
romantic_frame.grid(row=0,column=2)
romantic_picture=PhotoImage(file="img_5.png")
romantic_label=Label(romantic_frame,image=romantic_picture,padx=30,pady=30)
romantic_label.place(x=0,y=0,relheight=1,relwidth=1)
romantic_button=Checkbutton(romantic_frame,text="Romantic",font=('calibre',15, 'bold'))
romantic_button.place(x=50,y=220)

sad_frame=Frame(mood_frame,height=250,width=250,bg='white')
sad_frame.grid(row=1, column=1)
sad_picture=PhotoImage(file="img_7.png")
sad_label=Label(sad_frame, image=sad_picture, padx=30,pady=30,)
sad_label.place(x=0, y=0, relheight=1, relwidth=1)
sad_button=Checkbutton(sad_frame, text="Sad", font=('calibre', 15, 'bold'))
sad_button.place(x=50, y=220)


dance_frame = Frame(mood_frame, height=250, width=250, bg='yellow')
dance_frame.grid(row=1, column=2)
dance_picture = PhotoImage(file="img_8.png")
dance_label = Label(dance_frame, image=dance_picture, padx=30, pady=30)
dance_label.place(x=0, y=0, relheight=1, relwidth=1)
dance_button = Checkbutton(dance_frame, text="Dance", font=('calibre', 15, 'bold'))
dance_button.place(x=50, y=220)


root.mainloop()