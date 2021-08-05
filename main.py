import tkinter
from help import Help
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ================= First image ===============================
        img = Image.open(r"D:\Final Project\Project_img\student.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photo_img = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photo_img)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # ====================== Second image ==========================
        img1 = Image.open(r"D:\Final Project\Project_img\facialrecognition.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photo_img1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # ====================== Third image ===============================
        img2 = Image.open(r"D:\Final Project\Project_img\university.jpg")
        img2 = img2.resize((550, 130), Image.ANTIALIAS)
        self.photo_img2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photo_img2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # ==================== Background Image ============================
        img3 = Image.open(r"D:\Final Project\Project_img\di.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photo_img3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photo_img3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)


        # ===================== STUDENT BUTTON =======================
        img4 = Image.open(r"D:\Final Project\Project_img\student.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photo_img4 = ImageTk.PhotoImage(img4)

        b1 = Button(
            bg_img, image=self.photo_img4, command=self.student_details, cursor="hand2"
        )
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Student Details",
            command=self.student_details,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=200, y=300, width=220, height=40)

        #  Detect Face Button
        img5 = Image.open(r"D:\Final Project\Project_img\face_detector1.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photo_img5 = ImageTk.PhotoImage(img5)

        b1 = Button(
            bg_img, image=self.photo_img5, cursor="hand2", command=self.face_data
        )
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Face Detector",
            cursor="hand2",
            command=self.face_data,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=500, y=300, width=220, height=40)

        #  Attendance Face Button
        img6 = Image.open(r"D:\Final Project\Project_img\images.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photo_img6 = ImageTk.PhotoImage(img6)

        b1 = Button(
            bg_img, image=self.photo_img6, cursor="hand2", command=self.attendance_data
        )
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Attendance",
            cursor="hand2",
            command=self.attendance_data,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=800, y=300, width=220, height=40)

        #  Help Button
        img7 = Image.open(r"D:\Final Project\Project_img\help.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photo_img7 = ImageTk.PhotoImage(img7)

        b1 = Button(
            bg_img, image=self.photo_img7, cursor="hand2", command=self.help_data
        )
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Help Desk",
            cursor="hand2",
            command=self.help_data,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train Data Button
        img8 = Image.open(
            r"D:\Final Project\Project_img\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg"
        )
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photo_img8 = ImageTk.PhotoImage(img8)

        b1 = Button(
            bg_img, image=self.photo_img8, cursor="hand2", command=self.train_data
        )
        b1.place(x=200, y=375, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Train Data",
            cursor="hand2",
            command=self.train_data,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=200, y=575, width=220, height=40)

        #  Photos Button
        img9 = Image.open(r"D:\Final Project\Project_img\photo.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photo_img9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photo_img9, cursor="hand2", command=self.open_img)
        b1.place(x=500, y=375, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Photos",
            cursor="hand2",
            command=self.open_img,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=500, y=575, width=220, height=40)

        #  Developers Face Button
        img10 = Image.open(r"D:\Final Project\Project_img\dev.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photo_img10 = ImageTk.PhotoImage(img10)

        b1 = Button(
            bg_img, image=self.photo_img10, cursor="hand2", command=self.developer_data
        )
        b1.place(x=800, y=375, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Developers",
            cursor="hand2",
            command=self.developer_data,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=800, y=575, width=220, height=40)

        #  Exit Button
        img11 = Image.open(r"D:\Final Project\Project_img\exit.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photo_img11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photo_img11, cursor="hand2", command=self.iExit)
        b1.place(x=1100, y=375, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Exit",
            cursor="hand2",
            command=self.iExit,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=1100, y=575, width=220, height=40)

    # ===============photo Button===============================
    def open_img(self):
        os.startfile("data")

    # ==========================Functions button================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    # ========= Train Button ====================================
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    # ========= Face Detect Button ====================================
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    # ==================== Attendance Button ============================
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    # ==================== Developer Button ============================
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    # ==================== Help Button ============================
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    # ================ Exit ======================
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are You Sure Exit This Project", parent=self.root
        )
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
