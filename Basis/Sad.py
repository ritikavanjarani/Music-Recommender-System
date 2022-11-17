from tkinter import *

class Sad:
    def __init__(self, root):
        # super().__init__(root)
        self.root = root
        self.root.geometry('700x700')
        self.root.title('SAD')

        # self.f.pack()

        self.sad_frame = Frame(root, height=700, width=700, bg='white')
        self.sad_frame.pack()

        self.radioVal = StringVar(value=2)

        breakup_frame = Frame(self.sad_frame, height=250, width=250, bg='white')
        breakup_frame.grid(row=0, column=1)
        self.breakup_picture = PhotoImage(file="img_breakup.png")
        self.breakup_label = Label(breakup_frame, image=self.breakup_picture, padx=30, pady=30)
        self.breakup_label.image = self.breakup_picture
        self.breakup_label.place(x=0, y=0, relheight=1, relwidth=1)
        self.breakup_button = Radiobutton(breakup_frame, variable=self.radioVal, value="Break", text="BreakUp", font=('calibre', 15, 'bold'))
        self.breakup_button.place(x=50, y=220)

        arijit_frame = Frame(self.sad_frame, height=250, width=250, bg='white')
        arijit_frame.grid(row=0, column=2)
        self.arijit_picture = PhotoImage(file="img_arijit.png")
        self.arijit_label = Label(arijit_frame, image=self.arijit_picture, padx=30, pady=30)
        self.arijit_label.image = self.arijit_picture
        self.arijit_label.place(x=0, y=0, relheight=1, relwidth=1)
        self.arijit_button = Radiobutton(arijit_frame, variable=self.radioVal, value="Ari",  text="Arijit Sentimentals", font=('calibre', 15, 'bold'))
        self.arijit_button.place(x=50, y=220)

        emo_frame = Frame(self.sad_frame, height=250, width=250, bg='white')
        emo_frame.grid(row=1, column=1)
        self.emo_picture = PhotoImage(file="img_emo.png")
        self.emo_label = Label(emo_frame, image=self.emo_picture, padx=30, pady=30)
        self.emo_label.image = self.emo_picture
        self.emo_label.place(x=0, y=0, relheight=1, relwidth=1)
        self.emo_button = Radiobutton(emo_frame, variable=self.radioVal, value="Emo", text="Emotional 2017", font=('calibre', 15, 'bold'))
        self.emo_button.place(x=50, y=220)


        bollywood_frame = Frame(self.sad_frame, height=250, width=250, bg='yellow')
        bollywood_frame.grid(row=1, column=2)
        self.bollywood_picture = PhotoImage(file="img_bolly.png")
        self.bollywood_label = Label(bollywood_frame, image=self.bollywood_picture, padx=30, pady=30)
        self.bollywood_label.image = self.bollywood_picture
        self.bollywood_label.place(x=0, y=0, relheight=1, relwidth=1)
        self.bollywood_button = Radiobutton(bollywood_frame, variable=self.radioVal, value="Boll", text="Bollywood 90", font=('calibre', 15, 'bold'))
        self.bollywood_button.place(x=50, y=220)


if(__name__=="__main__"):
    root = Tk()
    s = Sad(root)
    root.mainloop()

