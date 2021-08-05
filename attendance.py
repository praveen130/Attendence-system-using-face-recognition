from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import csv


mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # =========== Variables =========================

        self.var_Attendance_id = StringVar()
        self.var_Attendance_roll = StringVar()
        self.var_Attendance_name = StringVar()
        self.var_Attendance_dep = StringVar()
        self.var_Attendance_time = StringVar()
        self.var_Attendance_date = StringVar()
        self.var_Attendance_attendance = StringVar()

        # ============ first image =================
        img = Image.open(r"D:\Final Project\Project_img\student.jpg")
        img = img.resize((800, 200), Image.ANTIALIAS)
        self.photo_img = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photo_img)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # second image
        img1 = Image.open(r"D:\Final Project\Project_img\clg.jpg")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photo_img1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # Background Image
        img3 = Image.open(r"D:\Final Project\Project_img\di.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photo_img3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photo_img3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        # =========== Attendance ====================
        title_lbl = Label(
            bg_img,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # =========== Main Frame =======================
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1500, height=600)

        # Left side label frame

        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Attendance Details",
            font=("times new roman", 12, "bold "),
        )
        Left_frame.place(x=10, y=10, width=730, height=580)

        # ============== Image ==================
        img_left = Image.open(r"D:\Final Project\Project_img\girl.jpeg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photo_img_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photo_img_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # =========== Left Inside Frame =======================
        left_inside_frame = Frame(Left_frame, relief=RIDGE, bd=2, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=370)

        # ========== Label And Entry============================

        # Attendance ID
        AttendanceId_label = Label(
            left_inside_frame,
            text="Attendance ID:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        AttendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        AttendanceId_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_Attendance_id,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        AttendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # =================== Roll ===================================
        Roll_label = Label(
            left_inside_frame,
            text="Roll:",
            bg="white",
            font="comicsansns 11 bold",
        )
        Roll_label.grid(row=0, column=2, padx=4, pady=8)

        Roll_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_Attendance_roll,
            width=22,
            font="comicsansns 11 bold",
        )
        Roll_entry.grid(row=0, column=3, pady=8)

        # =================== Name ===================================
        Name_label = Label(
            left_inside_frame,
            text="Name:",
            bg="white",
            font="comicsansns 11 bold",
        )
        Name_label.grid(row=1, column=0)

        Name_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_Attendance_name,
            width=22,
            font="comicsansns 11 bold",
        )
        Name_entry.grid(row=1, column=1, pady=8)

        # =================== Department ===================================
        dep_label = Label(
            left_inside_frame,
            text="Department:",
            bg="white",
            font="comicsansns 11 bold",
        )
        dep_label.grid(row=1, column=2)

        dep_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_Attendance_dep,
            width=22,
            font="comicsansns 11 bold",
        )
        dep_entry.grid(row=1, column=3, pady=8)

        # =================== Time ===================================
        Time_label = Label(
            left_inside_frame,
            text="Time:",
            bg="white",
            font="comicsansns 11 bold",
        )
        Time_label.grid(row=2, column=0)

        Time_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_Attendance_time,
            width=22,
            font="comicsansns 11 bold",
        )
        Time_entry.grid(row=2, column=1, pady=8)

        # =================== Date ===================================
        Date_label = Label(
            left_inside_frame,
            text="Date:",
            font="comicsansns 11 bold",
            bg="white",
        )
        Date_label.grid(row=2, column=2)

        Date_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_Attendance_date,
            width=20,
            font="comicsansns 11 bold",
        )
        Date_entry.grid(row=2, column=3, pady=8)

        # =================== Attendance ===================================
        Attendance_label = Label(
            left_inside_frame,
            text="Attendance Status",
            bg="white",
            font="comicsansns 11 bold",
        )
        Attendance_label.grid(row=3, column=0)

        self.Attendance_combo = ttk.Combobox(
            left_inside_frame,
            textvariable=self.var_Attendance_attendance,
            width=20,
            font="comicsansns 11 bold",
            state="readonly",
        )
        self.Attendance_combo["values"] = ("Status", "Present", "Absent")
        self.Attendance_combo.grid(row=3, column=1, pady=8)
        self.Attendance_combo.current(0)

        # ================= button frame ======================
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=36)

        # =========================== Import csv button ========================
        Importcsv_btn = Button(
            btn_frame,
            text="Import csv",
            command=self.importCsv,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        Importcsv_btn.grid(row=0, column=0)

        # Export csv
        Exportcsv_btn = Button(
            btn_frame,
            text="Export csv",
            command=self.exportCsv,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        Exportcsv_btn.grid(row=0, column=1)

        # Update
        Update_btn = Button(
            btn_frame,
            text="Update",
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        Update_btn.grid(row=0, column=2)

        # Reset
        Reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.rest_data,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        Reset_btn.grid(row=0, column=3)

        # ========================== Right side label frame ================================

        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Attendance Details",
            font=("times new roman", 12, "bold "),
        )
        Right_frame.place(x=750, y=10, width=730, height=580)

        # ================= button frame ======================
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=705, height=455)

        # ========== scroll bar ===================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            columns=("id", "roll", "name", "department", "time", "date", "attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ======================== Fetch Data =========================

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # =============== Import csv ==============================
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open csv",
            filetypes=(("csv File", "*csv"), ("All File", "*.*")),
            parent=self.root,
        )
        with open(fln) as my_file:
            csvread = csv.reader(my_file, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # =============== Export csv ==============================
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "No Data found to export", parent=self.root
                )
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Open csv",
                filetypes=(("csv File", "*csv"), ("All File", "*.*")),
                parent=self.root,
            )
            with open(fln, mode="w", newline="") as my_file:
                exp_write = csv.writer(my_file, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Export",
                    "Your Data Exported To" + os.path.basename(fln) + "Successfully",
                )
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ===================== Student Attendance Detail Button ===================
    def get_cursor(self, even=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_Attendance_id.set(rows[0])
        self.var_Attendance_roll.set(rows[1])
        self.var_Attendance_name.set(rows[2])
        self.var_Attendance_dep.set(rows[3])
        self.var_Attendance_time.set(rows[4])
        self.var_Attendance_date.set(rows[5])
        self.var_Attendance_attendance.set(rows[6])

    # ========Update function================

    """def update_data(self):
        if(self.var_Attendance_id.get("") or self.var_Attendance_roll.get("") or self.var_Attendance_name.get("") or self.var_Attendance_dep.get("")):
            messagebox.showerror("Error", "All Field are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update",
                    "Do you want to update this student details",
                    parent=self.root,
                )
"""

    # ============ Rest Button ===================
    def rest_data(self):
        self.var_Attendance_id.set("")
        self.var_Attendance_roll.set("")
        self.var_Attendance_name.set("")
        self.var_Attendance_dep.set("")
        self.var_Attendance_time.set("")
        self.var_Attendance_date.set("")
        self.var_Attendance_attendance.set("Status")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
