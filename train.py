from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from PIL import Image, ImageTk


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(
            self.root,
            text="TRAIN DATA SET",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"D:\Final Project\Project_img\facialrecognition.png")
        img_top = img_top.resize((1530, 335), Image.ANTIALIAS)
        self.photo_img_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photo_img_top)
        f_lbl.place(x=0, y=45, width=1530, height=335)

        # botton
        b1_1 = Button(
            self.root,
            text="TRAIN DATA",
            command=self.train_data,
            cursor="hand2",
            font=("times new roman", 30, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=0, y=380, width=1530, height=60)

        img_bottom = Image.open(r"D:\Final Project\Project_img\images.jpg")
        img_bottom = img_bottom.resize((1530, 350), Image.ANTIALIAS)
        self.photo_img_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photo_img_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=350)

    # ============Train data=========================
    def train_data(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            # ==Convert Gray Scale Image==
            img = Image.open(image).convert("L")

            # Numpy Array
            imageNp = np.array(img, "uint8")
            # uint8 data type

            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # ==================== Train the classifier and save ================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
