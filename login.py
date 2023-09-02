from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox


class Login_Windows:
    def __init__(self, root):  # root->window name

        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x830+0+0")

        bg1 = Image.open("images/login_background.jpg")
        bg1 = bg1.resize((1530, 830), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(bg1)
        lblbg1 = Label(image=self.photoimage, bg="black", borderwidth=0)
        lblbg1.place(x=0, y=0, width=1530, height=830)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open("images/LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # label
        username = lbl = Label(frame, text="Username", font=("times new roman", 20, "bold"), fg="white", bg="black")
        username.place(x=70, y=145)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 20, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = lbl = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
        password.place(x=70, y=220)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 20, "bold"))
        self.txtpass.place(x=40, y=255, width=270)

        # ..............icon images...........
        img2 = Image.open("images/profile.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open("images/lock-512.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=397, width=25, height=25)

        # LoginButton
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="white", bg="red",cursor="hand2")
        loginbtn.place(x=110, y=305, width=120, height=35)

        # register button
        registrbtn = Button(frame, text="New User Register",pady=1,cursor="hand2", font=("times new roman", 12, "bold"), borderwidth=0,fg="red", bg="black")
        registrbtn.place(x=20, y=380, width=160)

        # forget password button
        registrbtn = Button(frame, text="Forget Password    ",pady=1,cursor="hand2", font=("times new roman", 12, "bold"), borderwidth=0,fg="red", bg="black")
        registrbtn.place(x=20, y=410, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("error", "all field required")
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("success", "welcome")
        else:
            messagebox.showerror("invalid", "invalid  username or password")


# creating object and calling object
if  __name__ == "__main__":
    root = Tk()
    app = Login_Windows(root)
    root.mainloop()