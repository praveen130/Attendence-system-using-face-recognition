from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import glob, os


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ============Variable==================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.va_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # first image
        img = Image.open(r"D:\Final Project\Project_img\student.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photo_img = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photo_img)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(r"D:\Final Project\Project_img\clg.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photo_img1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # ================== Third image ====================
        img2 = Image.open(r"D:\Final Project\Project_img\smart-attendance.jpg")
        img2 = img2.resize((550, 130), Image.ANTIALIAS)
        self.photo_img2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photo_img2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # ====================== Background Image ====================
        img3 = Image.open(r"D:\Final Project\Project_img\di.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photo_img3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photo_img3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_img,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1500, height=600)

        # ================== Left side label frame ====================

        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold "),
        )
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"D:\Final Project\Project_img\girl.jpeg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photo_img_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photo_img_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # ================= Current Course Information =====================
        Current_Course_frame = LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current Course Information",
            font=("times new roman", 12, "bold "),
        )
        Current_Course_frame.place(x=5, y=133, width=720, height=115)

        # Department
        dep_label = Label(
            Current_Course_frame,
            text="Department",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_dep,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=20,
        )
        dep_combo["values"] = (
            "Select Department",
            "E&TC",
            "Computer",
            "Civil",
            "Electrical",
            "Mechanical",
        )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        Course_label = Label(
            Current_Course_frame,
            text="Course",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Course_label.grid(row=0, column=2, padx=10, sticky=W)

        Course_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_course,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=20,
        )
        Course_combo["values"] = ("Select Course", "FE", "SE", "TE", "B.Tech")
        Course_combo.current(0)
        Course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        Year_label = Label(
            Current_Course_frame,
            text="Year",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Year_label.grid(row=1, column=0, padx=10, sticky=W)

        Year_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_year,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=20,
        )
        Year_combo["values"] = (
            "Select Year",
            "2017-18",
            "2018-19",
            "2019-20",
            "2020-21",
        )
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        Semester_label = Label(
            Current_Course_frame,
            text="Semester",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Semester_label.grid(row=1, column=2, padx=10, sticky=W)

        Semester_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_semester,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=20,
        )
        Semester_combo["values"] = ("Select Semester", "Semester - 1", "Semester - 2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        Class_Student_frame = LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Class Student Information",
            font=("times new roman", 12, "bold "),
        )
        Class_Student_frame.place(x=5, y=248, width=720, height=307)

        # Student ID
        StudentId_label = Label(
            Class_Student_frame,
            text="Student ID:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        StudentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.va_std_id,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        StudentName_label = Label(
            Class_Student_frame,
            text="Student Name:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        StudentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        StudentName_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_std_name,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        StudentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class division
        class_div_label = Label(
            Class_Student_frame,
            text="Class Division:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # class_div_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_div, width=20, font=("times new roman", 13, "bold"))
        # class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        class_div_combo = ttk.Combobox(
            Class_Student_frame,
            textvariable=self.var_div,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=18,
        )
        class_div_combo["values"] = ("Select Division", "A", "B", "C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        Roll_No_label = Label(
            Class_Student_frame,
            text="Roll No:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Roll_No_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Roll_No_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_roll,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        Roll_No_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        Gender_label = Label(
            Class_Student_frame,
            text="Gender:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        # Gender_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_gender, width=20, font=("times new roman", 13, "bold"))
        # Gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Gender_combo = ttk.Combobox(
            Class_Student_frame,
            textvariable=self.var_gender,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=18,
        )
        Gender_combo["values"] = ("Male", "Female", "other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date Of Birth
        dob_label = Label(
            Class_Student_frame,
            text="DOB:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_dob,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        Email_label = Label(
            Class_Student_frame,
            text="Email ID:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Email_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_email,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        Phone_label = Label(
            Class_Student_frame,
            text="Phone Number:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        Phone_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_phone,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        Phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        Address_label = Label(
            Class_Student_frame,
            text="Address:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        Address_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_address,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        Address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        Teacher_label = Label(
            Class_Student_frame,
            text="Teacher Name:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        Teacher_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_teacher,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        Teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # ======================== Radio Button ============================
        self.var_radio1 = StringVar()
        Radiobutton1 = ttk.Radiobutton(
            Class_Student_frame,
            variable=self.var_radio1,
            text="Take Photo Samples",
            value="Yes",
        )
        Radiobutton1.grid(row=6, column=0)

        Radiobutton2 = ttk.Radiobutton(
            Class_Student_frame,
            variable=self.var_radio1,
            text="No Photo Samples",
            value="No",
        )
        Radiobutton2.grid(row=6, column=1)

        # button frame
        btn_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=210, width=715, height=36)

        # Save button
        save_btn = Button(
            btn_frame,
            command=self.add_data,
            text="Save",
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        save_btn.grid(row=0, column=0)

        # Update
        Update_btn = Button(
            btn_frame,
            command=self.update_data,
            text="Update",
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        Update_btn.grid(row=0, column=1)

        # Delete
        Delete_btn = Button(
            btn_frame,
            command=self.delete_data,
            text="Delete",
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        Delete_btn.grid(row=0, column=2)

        # Reset
        Reset_btn = Button(
            btn_frame,
            command=self.reset_data,
            text="Reset",
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        Reset_btn.grid(row=0, column=3)

        # ================ Button Frame ==============================
        btn_frame1 = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=247, width=715, height=34)

        # ==================== Take Photo Sample ======================
        Take_Photo_btn = Button(
            btn_frame1,
            command=self.generate_dataset,
            text="Take Photo Sample",
            width=35,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        Take_Photo_btn.grid(row=0, column=0)

        # ======================== Update Photo Sample ==================
        Update_Photo_btn = Button(
            btn_frame1,
            command=self.update_data_set,
            text="Update Photo Sample",
            width=35,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        Update_Photo_btn.grid(row=0, column=1)

        # ======================== Right Side Label Frame ===============

        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold "),
        )
        Right_frame.place(x=750, y=10, width=730, height=580)

        img_right = Image.open(r"D:\Final Project\Project_img\students.jpg")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photo_img_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photo_img_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # ================ Search Frame ==================================

        Search_frame = LabelFrame(
            Right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 12, "bold "),
        )
        Search_frame.place(x=5, y=135, width=710, height=70)

        # ================ Search Combob ==================================

        search_label = Label(
            Search_frame,
            text="Search By:",
            font=("times new roman", 15, "bold"),
            bg="red",
            fg="white",
        )
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # ================ Search Combob ==================================
        self.var_combobox_search = StringVar()

        search_combo = ttk.Combobox(
            Search_frame,
            textvariable=self.var_combobox_search,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=15,
        )
        search_combo["values"] = ("Select", "Student_Id", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # ================= Entry Field ==================
        self.var_search = StringVar()
        search_entry = ttk.Entry(
            Search_frame,
            textvariable=self.var_search,
            width=15,
            font=("times new roman", 13, "bold"),
        )
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # ======================= Search button ==================
        search_btn = Button(
            Search_frame,
            command=self.search_data,
            text="Search",
            width=13,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        search_btn.grid(row=0, column=3, padx=4)

        # ================== Show All Button ==================
        showAll_btn = Button(
            Search_frame,
            command=self.fetch_data,
            text="Show All",
            width=13,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        showAll_btn.grid(row=0, column=4)

        # =================Table Frame======================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "teacher",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Headers
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ===================Function Declaration=============

    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.va_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Field are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="7028898230",
                    database="my_data",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.va_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student details has been added Successfully",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # =======================fetch data==========================

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="7028898230", database="my_data"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, value=i)
            conn.commit()
        conn.close()

    # ====================get function===========================

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ========Update function================

    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.va_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Field are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update",
                    "Do you want to update this student details",
                    parent=self.root,
                )
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="7028898230",
                        database="my_data",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_Id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.va_std_id.get(),
                        ),
                    )
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success",
                    "Student details successfully completed",
                    parent=self.root,
                )
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ======================Delete Function====================

    def delete_data(self):
        if self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student Id must be required", parent=self.root
            )
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page",
                    "Do you want to delete this student",
                    parent=self.root,
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="7028898230",
                        database="my_data",
                    )
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_Id=%s"
                    val = (self.va_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted student details", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ==================Rest Function=======================

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        self.va_std_id.set("")

    # ============= Take photo Sample OR Genrate data set =================

    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.va_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Field are required", parent=self.root)
        else:
            try:
                #print(self.va_std_id.get())
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="7028898230",
                    database="my_data",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                my_result = my_cursor.fetchall()
                # id = 0
                # for x in my_result:
                # id += 1
                my_cursor.execute(
                    "update student set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_Id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.va_std_id.get(),
                        # == id + 1,
                    ),
                )
                conn.commit()
                self.fetch_data()
                # self.reset_data()
                conn.close()

                # ========= Load predefined data on frontal face from open_cv =========
                face_classifier = cv2.CascadeClassifier(
                    "D:/haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    # Scaling factor = 1.3
                    #  Minimum Neighbor = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y : y + h, x : x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        #print(str(self.va_std_id.get()))
                        file_name_path = (
                            "data/student."
                            + str(self.va_std_id.get())
                            + "."
                            + str(img_id)
                            + ".jpg"
                        )
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(
                            face,
                            str(img_id),
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            2,
                            (0, 255, 0),
                            2,
                        )
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ======================== Search Function ==================
    def search_data(self):
        if self.var_combobox_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please Select Option")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="7028898230",
                    database="my_data",
                )
                my_cursor = conn.cursor()

                # =========== queries ============

                my_cursor.execute(
                    "select * from student where "
                    + str(self.var_combobox_search.get())
                    + " LIKE '%"
                    + str(self.var_search.get())
                    + "%'"
                )
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ======================= Update Photo Sample =================================
    def update_data_set(self):

        for f in glob.glob("data/student." + str(self.va_std_id.get()) + ".*.jpg"):
            os.remove(f)
        
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.va_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Field are required", parent=self.root)
        else:
            try:
                #print(self.va_std_id.get())
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="7028898230",
                    database="my_data",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                my_result = my_cursor.fetchall()
                # id = 0
                # for x in my_result:
                # id += 1
                my_cursor.execute(
                    "update student set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_Id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.va_std_id.get(),
                        # == id + 1,
                    ),
                )
                conn.commit()
                self.fetch_data()
                # self.reset_data()
                conn.close()

                # ========= Load predefined data on frontal face from open_cv =========
                face_classifier = cv2.CascadeClassifier(
                    "D:/haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    # Scaling factor = 1.3
                    #  Minimum Neighbor = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y : y + h, x : x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        #print(str(self.va_std_id.get()))
                        file_name_path = (
                            "data/student."
                            + str(self.va_std_id.get())
                            + "."
                            + str(img_id)
                            + ".jpg"
                        )
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(
                            face,
                            str(img_id),
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            2,
                            (0, 255, 0),
                            2,
                        )
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
