from tkinter import *

class Arijit:
    def __init__(self, root):

        #root=Tk()
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Arijit Sentimentals")
        self.Break_frame=Frame(root,height=500,width=500,bg='gray')
        self.Break_frame.pack()
        #picture_break = PhotoImage(file="")
        #label=Label(frame_Break,image=picture_break)
        #label.place(x=0,y=0)

        self.radioVal = StringVar(value=2)
        shayad=Radiobutton(self.Break_frame, variable=self.radioVal, value="shayad", text="Shayad",font=('calibre',15))
        shayad.place(x=130,y=50)
        Intezaar=Radiobutton(self.Break_frame, variable=self.radioVal, value="intezaar", text="Intezaar",font=('calibre',15))
        Intezaar.place(x=130,y=100)
        Channa_Mereya=Radiobutton(self.Break_frame, variable=self.radioVal, value="channa", text="Channa Mereya",font=('calibre',15))
        Channa_Mereya.place(x=130,y=150)
        Humari_Aadhuri_Kahani=Radiobutton(self.Break_frame, variable=self.radioVal, value="Hum", text="Humari Aadhuri Kahani",font=('calibre',15))
        Humari_Aadhuri_Kahani.place(x=130,y=200)
       # label_heading=Label(self.Break_frame,text="Arijit Sentimentals",font=('calibre',20, 'bold',"underline"))
        #label_heading.grid(row=0,column=0)


if(__name__=="__main__"):
    root = Tk()
    a = Arijit(root)
    root.mainloop()
