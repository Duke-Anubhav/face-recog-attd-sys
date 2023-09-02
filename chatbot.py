import time
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import pyttsx3
from datetime import datetime
import pytz

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
class chatbot:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x830")
        self.root.title("ChatBot")
        self.root.config(bg="white")
        speak("starting chatbot created by curious coders")
        main_frame=Frame(self.root,bd=4,bg="powder blue",width=820)
        main_frame.pack()


        img_chat=Image.open(r'C:\Users\91895\OneDrive\Desktop\PBL\images\chat.jpg')
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=1530,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg="green",bg="white")
        Title_label.pack(side=TOP)

        # Main Frame
        second_frame = Frame(self.root, bd=2, bg="white")
        second_frame.place(x=0, y=90, width=1600, height=760)
        # Left Label Frame
        left_label_frame = LabelFrame(second_frame, bd=2, bg="white", relief=RIDGE, text="STUDENT QUERY",font=("times new roman", 12, "bold"))
        left_label_frame.place(x=10, y=10, width=750, height=750)
        # Right Label Frame
        right_label_frame = LabelFrame(second_frame, bd=2, bg="white", relief=RIDGE, text="BOT RESPONSE:",font=("times new roman", 12, "bold"))
        right_label_frame.place(x=740, y=10, width=750, height=750)

#self scrollbar right side
        self.scroll_y=ttk.Scrollbar(right_label_frame,orient=VERTICAL)
        self.text=Text(right_label_frame,width=65,height=80,bd=2,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

# QUERIES

        self.send = Button(left_label_frame, text="how does facial recognition work step by step",command = self.query, cursor="hand2", font=("times new roman", 15, " bold"),bg="lightblue", fg="black")
        self.send.grid(row=0,column=0,padx=5,sticky=W,pady=10)
        self.send = Button(left_label_frame, text="how does facial recognition work step by step", command=self.query,cursor="hand2", font=("times new roman", 15, " bold"), bg="lightblue", fg="black")
        self.send.grid(row=1, column=0, padx=5, sticky=W,pady=10)
        self.send = Button(left_label_frame, text="how does facial recognition work step by step", command=self.query,cursor="hand2", font=("times new roman", 15, " bold"), bg="lightblue", fg="black")
        self.send.grid(row=2, column=0, padx=5, sticky=W,pady=10)
        self.send = Button(left_label_frame, text="how does facial recognition work step by step", command=self.query,cursor="hand2", font=("times new roman", 15, " bold"), bg="lightblue", fg="black")
        self.send.grid(row=3, column=0, padx=5, sticky=W,pady=10)
        self.send = Button(left_label_frame, text="how does facial recognition work step by step", command=self.query,cursor="hand2", font=("times new roman", 15, " bold"), bg="lightblue", fg="black")
        self.send.grid(row=4, column=0, padx=5, sticky=W,pady=10)
        self.send = Button(left_label_frame, text="how does facial recognition work step by step", command=self.query,cursor="hand2", font=("times new roman", 15, " bold"), bg="lightblue", fg="black")
        self.send.grid(row=5, column=0, padx=5, sticky=W,pady=10)



# =====================================================================Functions Declaration=======================================================================================

    def generating(self):
        speak("generating response")
        self.text.insert(END, '\n' + "GENERATING RESPONSE\n")
        # time.sleep(1)
        self.text.insert(END, "...")
        # time.sleep(1)



    def query(self):
        IST = pytz.timezone('Asia/Kolkata')
        datetime_ist = datetime.now(IST)
        send="YOU>>>"+"how does facial recognition work step by step.\n"+ datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z')+"\n-------------------------------------------------------------------------------------------------------------------"
        self.text.insert(END,'\n'+send)
        self.generating()
        self.text.insert(END, '\n' + "Bot>>> Facial recognition is a technology that identifies and verifies individuals by \n analyzing their facial features. \nIt typically involves several steps in the process of recognizing a face. \nBelow is a step-by-step explanation of how facial recognition works:\n"+"1. **Face Detection**\n"+"2. **Face Alignment**\n"+"3. **Feature Extraction**\n"+"4. **Face Representation and Encoding**\n"+"5. **Database Search (Recognition)**\n"+"6. **Decision and Identification**\n"+"7. **Verification vs. Identification**\n")






if __name__ == "__main__":
    root=Tk()
    obj=chatbot(root)
    # speak("starting chatbot created by curious coders")
    root.mainloop()








