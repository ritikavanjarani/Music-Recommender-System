from tkinter import *
class Dance:
    def __init__(self, root):

        #super().__init__(root)
        self.root = root
        self.root.geometry('700x700')
        self.root.title('Mood')

        #self.f.pack()

        self.dance_frame = Frame(root, height=700, width=700, bg='white')
        self.dance_frame.pack()
        #print("Mood Frame created")

        self.radioVal = StringVar(value=2)

        trip_frame = Frame(dance_frame, height=250, width=250, bg='white')
        trip_frame.grid(row=0, column=1)
        trip_picture = PhotoImage(file="img_trip.png")
        trip_label = Label(trip_frame, image=trip_picture, padx=30, pady=30)
        trip_label.place(x=0, y=0, relheight=1, relwidth=1)
        trip_button = Checkbutton(trip_frame, text="Bollywood Trippin", font=('calibre', 15, 'bold'))
        trip_button.place(x=50, y=220)

        twist_frame = Frame(dance_frame, height=250, width=250, bg='white')
        twist_frame.grid(row=0, column=2)
        twist_picture = PhotoImage(file="img_twist.png")
        twist_label = Label(twist_frame, image=twist_picture, padx=30, pady=30)
        twist_label.place(x=0, y=0, relheight=1, relwidth=1)
        twist_button = Checkbutton(twist_frame, text="Twist Karo", font=('calibre', 15, 'bold'))
        twist_button.place(x=50, y=220)

        cocktail_frame = Frame(dance_frame, height=250, width=250, bg='white')
        cocktail_frame.grid(row=1, column=1)
        cocktail_picture = PhotoImage(file="img_cocktail.png")
        cocktail_label = Label(cocktail_frame, image=cocktail_picture, padx=30, pady=30)
        cocktail_label.place(x=0, y=0, relheight=1, relwidth=1)
        cocktail_button = Checkbutton(cocktail_frame, text="Cocktail Party Mix", font=('calibre', 15, 'bold'))
        cocktail_button.place(x=50, y=220)


        latest_frame = Frame(dance_frame, height=250, width=250, bg='yellow')
        latest_frame.grid(row=1, column=2)
        latest_picture = PhotoImage(file="img_late.png")
        latest_label = Label(latest_frame, image=latest_picture, padx=30, pady=30)
        latest_label.place(x=0, y=0, relheight=1, relwidth=1)
        latest_button = Checkbutton(latest_frame, text="Latest Anthems", font=('calibre', 15, 'bold'))
        latest_button.place(x=50, y=220)


#root.mainloop()
if(__name__=="__main__"):
    root = Tk()
    m = MoodPage(root)
    root.mainloop()
