from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import schedule
import time

class Face_Recongnition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x830+0+0")
        self.root.title("Face Recognition SYSTEM")

        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("times new roman", 35, " bold"),bg="white",fg="green",)
        title_lbl.place(x=0, y=0, width=1530, height=45)
#1st image
        img_top = Image.open(r"C:\Users\91895\OneDrive\Desktop\PBL\images\face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)
#2nd image
        img_bottom = Image.open(r"C:\Users\91895\OneDrive\Desktop\PBL\images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # BUTON
        b1_lbl = Button(f_lbl,text="Face Recongnition",cursor="hand2",command=self.face_recog,font=("times new roman", 18, " bold"),bg="darkgreen",fg="white")
        b1_lbl.place(x=365, y=620, width=200, height=40)

        # =============attendace===========

    def mark_attendance(self,i,r,n,d,e):
        with open("Student_daily_record.csv","r+",newline="\n") as f:
         myDataList=f.readlines()
         name_list=[]
         for line in myDataList:
             entry=line.split((","))
             name_list.append(entry[0])
         if((i not in name_list)and(r not in name_list)and( n not in name_list)and(d not in name_list)and(e not in name_list)):
             now=datetime.now()
             d1=now.strftime("%d/%m/%Y")
             dtString=now.strftime("%H:%M:%S")
             f.writelines(f"{n},{e},{i},{r},{d},{dtString},{d1},Present\n")



        # <============recognition===========>

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y: y + h, x: x + w])
                confidence = int((100 * (1 - predict / 300)))


                conn = mysql.connector.connect(host="localhost", user="root", password="hpndjain", database="face_recognizer_2")
                my_cursor = conn.cursor()

                my_cursor.execute("Select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"

                my_cursor.execute("Select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"

                my_cursor.execute("Select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"

                my_cursor.execute("Select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"

                my_cursor.execute("Select email from student where Student_id=" + str(id))
                e = my_cursor.fetchone()
                e = e[0] if e else "Unknown"

                if confidence > 72:
                    cv2.putText(img,f"Id:{i}",(x, y - 75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3,)
                    cv2.putText(img,f"Roll:{r}",(x, y - 55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3,)
                    cv2.putText(img,f"Name:{n}",(x, y - 30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3,)
                    cv2.putText(img,f"Deartment:{d}",(x, y - 5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3,)
                    self.mark_attendance(i,r,n,d,e)
                else:
                    cv2.rectangle(img, (x, y), (x + w,y + h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown face",(x, y - 5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3,)
                coord = [x, y, w, h]
            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1) == 13:  # Press Enter key to exit the loop
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recongnition(root)
    root.mainloop()
