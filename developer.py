from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(
            self.root,
            text="DEVELOPER",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="blue",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"D:\Final Project\Project_img\dev.jpg")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photo_img_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photo_img_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # =========== Main Frame =======================
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        # ============ Image1 ===================
        img_top1 = Image.open(r"D:\Final Project\Project_img\praveen.jpeg")
        img_top1 = img_top1.resize((200, 200), Image.ANTIALIAS)
        self.photo_img_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photo_img_top1)
        f_lbl.place(x=0, y=0, width=200, height=200)

        # ============ Image2 ===================
        img_top2 = Image.open(r"D:\Final Project\Project_img\amol.jpg")
        img_top2 = img_top2.resize((200, 200), Image.ANTIALIAS)
        self.photo_img_top2 = ImageTk.PhotoImage(img_top2)

        f_lbl = Label(main_frame, image=self.photo_img_top2)
        f_lbl.place(x=220, y=0, width=200, height=200)

        # ==================== Developer Label ==================
        dep_label = Label(
            main_frame,
            text="Hello My Name, Praveen",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        dep_label.place(x=0, y=200)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
