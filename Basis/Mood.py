from tkinter import *
class MoodPage:
    def __init__(self, root):


        #super().__init__(root)
        self.root = root
        self.root.geometry('700x700')
        self.root.title('Mood')

        #self.f.pack()

        self.mood_frame = Frame(root, height=700, width=700, bg='white')
        self.mood_frame.pack()

        self.radioVal = StringVar(value=2)
        relaxed_frame=Frame(self.mood_frame, height=250, width=250, bg='black')
        relaxed_frame.grid(row=0, column=1)
        self.relaxed_picture = PhotoImage(file="img_6.png")
        self.relaxed_label = Label(relaxed_frame, image=self.relaxed_picture, padx=30, pady=30)
        self.relaxed_label.image = self.relaxed_picture
        self.relaxed_label.place(x=0, y=0, relheight=1, relwidth=1)
        self.relaxed_button = Radiobutton(relaxed_frame, variable=self.radioVal, value="REL", text="Relaxed", font=('calibre', 15, 'bold'))
        self.relaxed_button.place(x=50, y=220,)

        romantic_frame = Frame(self.mood_frame, height=250, width=250, bg='white')
        romantic_frame.grid(row=0, column=2)
        self.romantic_picture = PhotoImage(file="img_5.png")
        self.romantic_label = Label(romantic_frame, image=self.romantic_picture, padx=30, pady=30)
        self.romantic_label.image = self.romantic_picture
        self.romantic_label.place(x=0, y=0, relheight=1, relwidth=1)
        self.romantic_button = Radiobutton(romantic_frame, variable=self.radioVal, value="ROM", text="Romantic", font=('calibre', 15, 'bold'))
        self.romantic_button.place(x=50, y=220)

        sad_frame = Frame(self.mood_frame, height=250, width=250, bg='white')
        sad_frame.grid(row=1, column=1)
        self.sad_picture = PhotoImage(file="img_7.png")
        self.sad_label = Label(sad_frame, image=self.sad_picture, padx=30, pady=30)
        self.sad_label.image = self.sad_picture
        self.sad_label.place(x=0, y=0, relheight=1, relwidth=1)
        self.sad_button = Radiobutton(sad_frame, variable=self.radioVal, value="SAD", text="Sad", font=('calibre', 15, 'bold'))
        self.sad_button.place(x=50, y=220)


        dance_frame=Frame(self.mood_frame,height=250,width=250,bg='yellow')
        dance_frame.grid(row=1, column=2)
        self.dance_picture = PhotoImage(file="img_8.png")
        self.dance_label = Label(dance_frame, image=self.dance_picture, padx=30, pady=30,)
        self.dance_label.image = self.dance_picture
        self.dance_label.place(x=0, y=0, relheight=1, relwidth=1)
        self.dance_button = Radiobutton(dance_frame, variable=self.radioVal, value="DAN", text="Dance", font=('calibre', 15, 'bold'))
        self.dance_button.place(x=50, y=220)



if(__name__=="__main__"):
    root = Tk()
    m = MoodPage(root)
    root.mainloop()

