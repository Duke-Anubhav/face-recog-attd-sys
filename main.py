import tkinter.messagebox
from tkinter import*
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
from chatbot import chatbot
from train import Train
from attendance import Attendance
from face_recognition import Face_Recongnition
from student import Student
import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x830+0+0")
        self.root.title("Face Recognition System")

#1st image
        img=Image.open("images/Stanford.jpg")
        img=img.resize((510,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)
#2nd image
        img1=Image.open("images/facialrecognition.png")
        img1=img1.resize((520,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=520,height=130)
#3rd image
        img2=Image.open("images/u.jpg")
        img2=img2.resize((510,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1030,y=0,width=510,height=130)
#baground image
        img3=Image.open("images/bg1.jpg")
        img3=img3.resize((1540,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1540,height=710)

#Title Label
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman", 35," bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


#1st button student button
        img4=Image.open("images/gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details).place(x=170,y=100,width=220,height=220)
        b1_lbl=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman", 15," bold"),bg="darkblue",fg="red",command=self.student_details).place(x=170,y=320,width=220,height=40)

#2nd button student button
        img5=Image.open("images/face_detector1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.recognition).place(x=470,y=100,width=220,height=220)
        b2_lbl=Button(bg_img,text="Face Detector",command=self.recognition,cursor="hand2",font=("times new roman", 15," bold"),bg="darkblue",fg="red").place(x=470,y=320,width=220,height=40)

#3rd button student button
        img6=Image.open("images/report.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance).place(x=770,y=100,width=220,height=220)
        b3_lbl=Button(bg_img,text="Attendance",command=self.attendance,cursor="hand2",font=("times new roman", 15," bold"),bg="darkblue",fg="red").place(x=770,y=320,width=220,height=40)

#4th button student button
        img7=Image.open("images/help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chat_bot).place(x=1070,y=100,width=220,height=220)
        b4_lbl=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman", 15," bold"),bg="darkblue",fg="red",command=self.chat_bot).place(x=1070,y=320,width=220,height=40)


#5th button student button
        img8=Image.open("images/Train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data).place(x=170,y=380,width=220,height=220)
        b5_lbl=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman", 15," bold"),bg="darkblue",fg="red").place(x=170,y=600,width=220,height=40)

#6th button student button
        img9=Image.open("images/opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.oepn_img).place(x=470,y=380,width=220,height=220)
        b6_lbl=Button(bg_img,text="Photos",command=self.oepn_img,cursor="hand2",font=("times new roman", 15," bold"),bg="darkblue",fg="red").place(x=470,y=600,width=220,height=40)

#7th button student button
        img10=Image.open("images/developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.email).place(x=770,y=380,width=220,height=220)
        b7_lbl=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman", 15," bold"),bg="darkblue",fg="red",command=self.email).place(x=770,y=600,width=220,height=40)

#8th button student button
        img11=Image.open("images/exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit).place(x=1070,y=380,width=220,height=220)
        b8_lbl=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman", 15," bold"),bg="darkblue",fg="red",command=self.iExit).place(x=1070,y=600,width=220,height=40)

    def oepn_img(self):
        os.startfile("data")
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def chat_bot(self):
        self.new_window=Toplevel(self.root)
        self.app=chatbot(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recongnition(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure Exit This Project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
    def email(self):

        email_user = "g7@bmsit.in"
        email_password = "yxgcyxfzgdihxowa"
        subject = "Attendance alert"

        with open('Student_daily_record.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                text = "Hello " + line[0] + ", you were marked present today."
                send_email = line[1]
                print(send_email)
                msg = MIMEMultipart()
                msg['From'] = email_user
                msg['To'] = send_email
                msg['Subject'] = subject
                msg.attach(MIMEText(text, "plain"))

                text = msg.as_string()

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()  # Use STARTTLS encryption

                server.login(email_user, email_password)
                print("login successfull")
                server.sendmail(email_user, send_email, text)
                server.quit()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()