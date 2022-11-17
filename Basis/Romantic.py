from tkinter import *

root = Tk()
root.geometry('700x700')
root.title('Romantic')

rom_label = Label(root, text="Romantic", font=('calibre', 10, 'bold'))
rom_label.place(x=0, y=0)

rom_frame = Frame(root, height=700, width=700, bg='white')
rom_frame.grid(padx=100, pady=60)

decade_frame = Frame(rom_frame, height=250, width=250, bg='white')
decade_frame.grid(row=0, column=1)
decade_picture = PhotoImage(file="img_decade.png")
decade_label = Label(decade_frame, image=decade_picture, padx=30, pady=30)
decade_label.place(x=0, y=0, relheight=1, relwidth=1)
decade_button = Checkbutton(decade_frame, text="Decade in Romance", font=('calibre', 15, 'bold'))
decade_button.place(x=50, y=220)

jukebox_frame = Frame(rom_frame, height=250, width=250, bg='white')
jukebox_frame.grid(row=0, column=2)
jukebox_picture = PhotoImage(file="img_jukebox.png")
jukebox_label = Label(jukebox_frame, image=jukebox_picture, padx=30, pady=30)
jukebox_label.place(x=0, y=0, relheight=1, relwidth=1)
jukebox_button = Checkbutton(jukebox_frame, text="Romantic Jukebox", font=('calibre', 15, 'bold'))
jukebox_button.place(x=50, y=220)

love_frame = Frame(rom_frame, height=250, width=250, bg='white')
love_frame.grid(row=1, column=1)
love_picture = PhotoImage(file="img_love.png")
love_label = Label(love_frame, image=love_picture, padx=30, pady=30)
love_label.place(x=0, y=0, relheight=1, relwidth=1)
love_button = Checkbutton(love_frame, text="Love Aaj Kal", font=('calibre', 15, 'bold'))
love_button.place(x=50, y=220)


pyaar_frame = Frame(rom_frame, height=250, width=250, bg='yellow')
pyaar_frame.grid(row=1, column=2)
pyaar_picture = PhotoImage(file="img_pyaar.png")
pyaar_label = Label(pyaar_frame, image=pyaar_picture, padx=30, pady=30)
pyaar_label.place(x=0, y=0, relheight=1, relwidth=1)
pyaar_button = Checkbutton(pyaar_frame, text="90's Waala Pyaar", font=('calibre', 15, 'bold'))
pyaar_button.place(x=50, y=220)


root.mainloop()