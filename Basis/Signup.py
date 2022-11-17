from tkinter import *

root=Tk()
root.title("SignUp Page")
root.geometry('650x650')

signup_frame=Frame(root,height=650,width=650,bg='gray')
signup_frame.pack()

firstname_label=Label(signup_frame,text='FirstName',font=('calibre',10, 'bold'))
firstname_label.place(x=35,y=55)
firstname=Entry(signup_frame)
firstname.place(x=125,y=55)

lastname_label=Label(signup_frame,text='LastName',font=('calibre',10, 'bold'))
lastname_label.place(x=35,y=105)
lastname=Entry(signup_frame)
lastname.place(x=125,y=105)

username_label=Label(signup_frame,text='UserName',font=('calibre',10, 'bold'))
username_label.place(x=35,y=155)
username=Entry(signup_frame)
username.place(x=125,y=155)


age_label=Label(signup_frame,text='Age',font=('calibre',10, 'bold'))
age_label.place(x=35,y=205)
age=Entry(signup_frame)
age.place(x=125,y=205)


gender_label=Label(signup_frame,text='Gender',font=('calibre',10, 'bold'))
#gender_label=Label(signup_frame,text='Gender',font=('calibre',10, 'bold'))
gender_label.place(x=35,y=255)
gender=Entry(signup_frame)
gender.place(x=125,y=255)

mobile_label=Label(signup_frame,text='Mobile No',font=('calibre',10, 'bold'))
mobile_label.place(x=35,y=305)
mobile=Entry(signup_frame)
mobile.place(x=125,y=305)

emailid_label=Label(signup_frame,text='Email ID',font=('calibre',10, 'bold'))
emailid_label.place(x=35,y=355)
emailid=Entry(signup_frame)
emailid.place(x=125,y=355)

signup=Button(signup_frame,text="SignUp",font=('calibre',10, 'bold'))
signup.place(x=100,y=425)

prev=Button(signup_frame,text="Previous",font=('calibre',10, 'bold'))
prev.place(x=100,y=475)


root.mainloop()