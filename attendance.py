from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-mark-attendance-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'storageBucket': "face-mark-attendance.appspot.com"
})

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("FACE MARK ATTENDANCE - ATTENDANCE MANAGER")
        self.root.iconbitmap('Resources/logo.ico')

        # ===========varaibles===============
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_roll_presentees = StringVar()
        self.var_atten_roll_absentees = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_st_year = StringVar()
        self.var_atten_sem = StringVar()
        self.var_atten_sub = StringVar()
        self.var_atten_day = StringVar()
        self.var_atten_month = StringVar()
        self.var_atten_year = StringVar()
        self.var_atten_hour = StringVar()
        self.var_atten_attendance = StringVar()
        self.var_atten_total_presentees = StringVar()
        self.var_atten_total_absentees = StringVar()

        title_lbl = Label(text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white",
                          fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        main_frame = Frame(bd=2, bg="white")
        main_frame.place(x=0, y=45, width=1366, height=750)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="STUDENT ATTENDANCE DETAILS",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=273, height=640)

        # total presentees count
        totalPresenteesLabel = Label(Left_frame, text="TOTAL PRESENTEES: ", font=("times new roman", 12, "bold"), bg="white")
        totalPresenteesLabel.grid(row=0, column=0, padx=15, pady=2, sticky=W)

        atten_total_presentees = ttk.Entry(Left_frame, width=30, textvariable=self.var_atten_total_presentees,
                               font=("times new roman", 12, "bold"), state="readonly")
        atten_total_presentees.grid(row=1, column=0, padx=15, pady=2, sticky=W)

        # total absentees count
        totalAbsenteesLabel = Label(Left_frame, text="TOTAL ABSENTEES: ", font=("times new roman", 12, "bold"), bg="white")
        totalAbsenteesLabel.grid(row=2, column=0, padx=15, pady=2, sticky=W)

        atten_total_absentees = ttk.Entry(Left_frame, width=30, textvariable=self.var_atten_total_absentees,
                                           font=("times new roman", 12, "bold"), state="readonly")
        atten_total_absentees.grid(row=3, column=0, padx=15, pady=2, sticky=W)

        # roll number
        # rollLabel = Label(Left_frame, text="ROLL NUMBER: ", font=("times new roman", 12, "bold"), bg="white")
        # rollLabel.grid(row=2, column=0, padx=15, pady=2, sticky=W)
        #
        # atten_roll = ttk.Entry(Left_frame, width=30, textvariable=self.var_atten_roll,
        #                        font=("times new roman", 12, "bold"), state="readonly")
        # atten_roll.grid(row=3, column=0, padx=15, pady=2, sticky=W)
        #
        # # name
        # nameLabel = Label(Left_frame, text="NAME: ", font=("times new roman", 12, "bold"), bg="white")
        # nameLabel.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        #
        # atten_name = ttk.Entry(Left_frame, width=30, textvariable=self.var_atten_name,
        #                        font=("times new roman", 12, "bold"), state="readonly")
        # atten_name.grid(row=5, column=0, padx=15, pady=2, sticky=W)

        # present or not
        # present_label = Label(Left_frame, text="PRESENT/ABSENT: ", font=("times new roman", 12, "bold"), bg="white")
        # present_label.grid(row=4, column=0, padx=15, pady=2, sticky=W)
        #
        # atten_present = ttk.Entry(Left_frame, width=30, textvariable=self.var_atten_attendance,
        #                        font=("times new roman", 12, "bold"), state="readonly")
        # atten_present.grid(row=5, column=0, padx=15, pady=2, sticky=W)
        #

        # left inside frame
        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=27, y=125, width=210, height=470  )

        # DEPARTMENT

        dep_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold"),
                                 state="readonly")
        dep_combo["values"] = ("Select Department", "CSD")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=0, padx=12, pady=10)

        st_year_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_st_year, font=("times new roman", 12, "bold"),
                                 state="readonly")
        st_year_combo["values"] = ("Select Year", "2021-2025")
        st_year_combo.current(0)
        st_year_combo.grid(row=1, column=0, padx=12, pady=10)

        # Semester

        sem_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_sem, font=("times new roman", 12, "bold"),
                                 state="readonly")
        sem_combo["values"] = ("Select Semester", "Semester-3")
        sem_combo.current(0)
        sem_combo.grid(row=2, column=0, padx=12, pady=10)

        # subject label
        sub_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_sub, font=("times new roman", 12, "bold"),
                                 state="readonly")
        sub_combo["values"] = ("Select Subject", "SIP", "PYTHON LAB", "DBMS LAB", "OS LAB", "SFD", "DAA", "DBMS", "OS")
        sub_combo.current(0)
        sub_combo.grid(row=3, column=0, padx=12, pady=10)

        # hour label
        hour_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_hour,
                                 font=("times new roman", 12, "bold"),
                                 state="readonly")
        hour_combo["values"] = ("Select Hour/Period", "Hour 1", "Hour 2", "Hour 3", "Hour 4", "Hour 5", "Hour 6")
        hour_combo.current(0)
        hour_combo.grid(row=4, column=0, padx=12, pady=10)

        # Present/Absent
        # att_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance,
        #                          font=("times new roman", 12, "bold"),
        #                          state="readonly")
        # att_combo["values"] = ("Select Option", "Presentees", "Absentees")
        # att_combo.current(0)
        # att_combo.grid(row=5, column=0, padx=12, pady=10)

        # date label
        date_label = Label(left_inside_frame, text="SPECIFY DATE", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=6, column=0, padx=45, sticky=W)

        # date frame
        date_frame = Frame(left_inside_frame, bd=2, bg="white", relief=RIDGE)
        date_frame.place(x=12, y=250, width=177, height=90)

        # day label
        day_label = Label(date_frame, text="DAY: ", font=("times new roman", 12, "bold"), bg="white")
        day_label.grid(row=0, column=0, padx=2, sticky=W)

        atten_day = ttk.Entry(date_frame, width=10, textvariable=self.var_atten_day,
                              font=("times new roman", 12, "bold"))
        atten_day.grid(row=0, column=1, pady=2, sticky=W)

        # month label
        month_label = Label(date_frame, text="MONTH: ", font=("times new roman", 12, "bold"), bg="white")
        month_label.grid(row=1, column=0, padx=2, sticky=W)

        atten_month = ttk.Entry(date_frame, width=10, textvariable=self.var_atten_month,
                                font=("times new roman", 12, "bold"))
        atten_month.grid(row=1, column=1, pady=2,sticky=W)

        # date - year label
        year_label = Label(date_frame, text="YEAR: ", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=2, column=0, padx=2, sticky=W)

        atten_year = ttk.Entry(date_frame, width=10, textvariable=self.var_atten_year,
                               font=("times new roman", 12, "bold"))
        atten_year.grid(row=2, column=1, pady=2, sticky=W)

        # Buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=5, y=350, width=195, height=103)

        generate_atten_btn = Button(btn_frame, command=self.generate_data,text="GENERATE REPORT", width=20,
                          font=("times new roman", 12, "bold"), bg="green", fg="white")
        generate_atten_btn.grid(row=0, column=0, padx=1)

        delete_presentees_btn = Button(btn_frame, command=self.delete_presentees_data, text="DELETE - PRESENTEES", width=20,
                           font=("times new roman", 12, "bold"), bg="red", fg="white")
        delete_presentees_btn.grid(row=1, column=0, padx=1)

        delete_absentees_btn = Button(btn_frame, command=self.delete_absentees_data, text="DELETE - ABSENTEES", width=20,
                                       font=("times new roman", 12, "bold"), bg="red", fg="white")
        delete_absentees_btn.grid(row=2, column=0, padx=1)

        # presentees label frame
        presentees_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="PRESENTEES",
                                 font=("times new roman", 12, "bold"))
        presentees_frame.place(x=288, y=10, width=530, height=640)

        presentees_table_frame = Frame(presentees_frame, bd=2, relief=RIDGE, bg="white")
        presentees_table_frame.place(x=5, y=5, width=516, height=605)

        scroll_x = ttk.Scrollbar(presentees_table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(presentees_table_frame, orient=VERTICAL)

        self.PresenteesReportTable = ttk.Treeview(presentees_table_frame, column=(
        "roll", "name"), xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.PresenteesReportTable.xview)
        scroll_y.config(command=self.PresenteesReportTable.yview)

        self.PresenteesReportTable.heading("roll", text="Roll Number")
        self.PresenteesReportTable.heading("name", text="Name")
        # self.AttendanceReportTable.heading("present", text="Present/Absent")
        # self.AttendanceReportTable.heading("total_attendance", text="Subject Total Attendance")

        self.PresenteesReportTable["show"] = "headings"

        self.PresenteesReportTable.column("roll", width=100)
        self.PresenteesReportTable.column("name", width=100)
        # self.AttendanceReportTable.column("present", width=100)
        # self.AttendanceReportTable.column("total_attendance", width=100)

        self.PresenteesReportTable.pack(fill=BOTH, expand=1)

        self.PresenteesReportTable.bind("<ButtonRelease>", self.get_cursor_presentees)

        # Absentees label frame
        absentees_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="ABSENTEES",
                                      font=("times new roman", 12, "bold"))
        absentees_frame.place(x=822, y=10, width=530, height=640)

        absentees_table_frame = Frame(absentees_frame, bd=2, relief=RIDGE, bg="white")
        absentees_table_frame.place(x=5, y=5, width=516, height=605)

        scroll_x = ttk.Scrollbar(absentees_table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(absentees_table_frame, orient=VERTICAL)

        self.AbsenteesReportTable = ttk.Treeview(absentees_table_frame, column=(
            "roll", "name"), xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AbsenteesReportTable.xview)
        scroll_y.config(command=self.AbsenteesReportTable.yview)

        self.AbsenteesReportTable.heading("roll", text="Roll Number")
        self.AbsenteesReportTable.heading("name", text="Name")
        # self.AttendanceReportTable.heading("present", text="Present/Absent")
        # self.AttendanceReportTable.heading("total_attendance", text="Subject Total Attendance")

        self.AbsenteesReportTable["show"] = "headings"

        self.AbsenteesReportTable.column("roll", width=100)
        self.AbsenteesReportTable.column("name", width=100)
        # self.AttendanceReportTable.column("present", width=100)
        # self.AttendanceReportTable.column("total_attendance", width=100)

        self.AbsenteesReportTable.pack(fill=BOTH, expand=1)

        self.AbsenteesReportTable.bind("<ButtonRelease>", self.get_cursor_absentees)

    def proceed(self):
        if self.var_atten_dep.get() == "Select Department" or self.var_atten_st_year.get() == "Select Year" or self.var_atten_sem.get() == "Select Semester" or self.var_atten_sub.get() == "Select Subject" or self.var_atten_hour.get() == "Select Hour/Period" or self.var_atten_attendance == "Select Option" or self.var_atten_day.get() == "" or self.var_atten_month.get() == "" or self.var_atten_year.get() == "":
            return True
        else:
            return False

    def generate_data(self):
        if self.proceed():
            messagebox.showerror("ERROR", "Fill all the fields", parent=self.root)
        else:
            try:
                day = self.var_atten_day.get()
                month = self.var_atten_month.get()
                year = self.var_atten_year.get()
                date_conv = datetime.strptime(f"{day} {month} {year}", "%d %m %Y")
                date = date_conv.strftime("%d %B %Y")

                att_ref = db.reference(f"Attendance/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}/{self.var_atten_sem.get()}/{self.var_atten_sub.get()}/{date}/{self.var_atten_hour.get()}")
                atten_rolls = att_ref.get()

                present_stud = []

                for key, val in atten_rolls.items():
                    present_stud.append(key)

                stu_ref = db.reference(f"Students/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}").get()

                total_present = 0
                total_absent = 0

                for key, val in stu_ref.items():
                    # total_attendance = db.reference(f"Students/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}/{key}/total_attendance/{self.var_atten_sem.get()}/{self.var_atten_sub.get()}").get()
                    if atten_rolls.setdefault(key) == 1:
                        self.PresenteesReportTable.insert("", END, values=(key, val["Student Name"]))
                        total_present += 1
                    else:
                        self.AbsenteesReportTable.insert("", END, values=(key, val["Student Name"]))
                        total_absent += 1
                self.var_atten_total_presentees.set(str(total_present))
                self.var_atten_total_absentees.set(str(total_absent))
                # if self.var_atten_attendance == "Presentees":
                #     for key, val in stu_ref.items():
                #         # total_attendance = db.reference(f"Students/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}/{key}/total_attendance/{self.var_atten_sem.get()}/{self.var_atten_sub.get()}").get()
                #         if atten_rolls.setdefault(key) == 1:
                #             self.PresenteesReportTable.insert("", END, values=(key, val["Student Name"]))
                #             total_present += 1
                #     self.var_atten_total.set(str(total_present))
                # elif self.var_atten_attendance == "Absentees":
                #     for key, val in stu_ref.items():
                #         # total_attendance = db.reference(f"Students/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}/{key}/total_attendance/{self.var_atten_sem.get()}/{self.var_atten_sub.get()}").get()
                #         if atten_rolls.setdefault(key) != 1:
                #             self.AbsenteesReportTable.insert("", END, values=(key, val["Student Name"]))
                #             total_absent += 1
                #     self.var_atten_total.set(str(total_absent))

            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def get_cursor_presentees(self, event=""):
        cursor_presentees = self.PresenteesReportTable.focus()
        content_presentees = self.PresenteesReportTable.item(cursor_presentees)
        rows_presentees = content_presentees['values']
        self.var_atten_roll_presentees.set(rows_presentees[0])
        self.var_atten_name.set(rows_presentees[1])

    def get_cursor_absentees(self, event=""):
        cursor_absentees = self.AbsenteesReportTable.focus()
        content_absentees = self.AbsenteesReportTable.item(cursor_absentees)
        rows_absentees = content_absentees['values']
        self.var_atten_roll_absentees.set(rows_absentees[0])
        self.var_atten_name.set(rows_absentees[1])

    def reset_data(self):
        try:
            self.var_atten_dep.set("Select Department")
            self.var_atten_st_year.set("Select Year")
            self.var_atten_sem.set("Select Semester")
            self.var_atten_sub.set("Select Subject")
            self.var_atten_hour.set("Select Hour/Period")
            self.var_atten_day.set("")
            self.var_atten_month.set("")
            self.var_atten_year.set("")
            self.var_atten_name.set("")
            self.var_atten_roll.set("")
        except Exception as es:
            messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def delete_presentees_data(self):
        if self.var_atten_roll_presentees.get() == "":
            messagebox.showerror("Error", "Roll Number is required", parent=self.root)
        else:
            try:
                day = self.var_atten_day.get()
                month = self.var_atten_month.get()
                year = self.var_atten_year.get()
                date_conv = datetime.strptime(f"{day} {month} {year}", "%d %m %Y")
                date = date_conv.strftime("%d %B %Y")

                # total_attendance = db.reference(
                #     f"Students/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}/{self.var_atten_roll.get()}/total_attendance/{self.var_atten_sem.get()}/{self.var_atten_sub.get()}").get()
                # db.reference(
                    # f"Students/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}/{self.var_atten_roll.get()}/total_attendance/{self.var_atten_sem.get()}/{self.var_atten_sub.get()}").set(total_attendance-1)

                att_ref = db.reference(
                    f"Attendance/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}/{self.var_atten_sem.get()}/{self.var_atten_sub.get()}/{date}/{self.var_atten_hour.get()}")
                atten_rolls = att_ref.get()

                present_stud = []

                for key, val in atten_rolls.items():
                    present_stud.append(key)

                stu_ref = db.reference(f"Students/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}").get()

                delete = messagebox.askyesno("Confirmation", "Do you want to delete this student's attendance?",
                                             parent=self.root)

                if delete > 0:
                    att_ref.child(self.var_atten_roll_presentees.get()).delete()
                    for key, val in stu_ref.items():
                        # total_attendance = db.reference(f"Students/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}/{key}/total_attendance/{self.var_atten_sem.get()}/{self.var_atten_sub.get()}").get()
                        if key == self.var_atten_roll_presentees.get():
                            self.AbsenteesReportTable.insert("", END, values=(key, val["Student Name"]))
                            self.var_atten_total_presentees.set((int(self.var_atten_total_presentees.get()) - 1))
                            self.PresenteesReportTable.delete(self.PresenteesReportTable.selection()[0])
                            self.var_atten_total_absentees.set((int(self.var_atten_total_absentees.get()) + 1))
                else:
                    if not delete:
                        return

                messagebox.showinfo("Delete", "Successfully deleted student attendance", parent=self.root)
                # self.var_atten_attendance.set("Absent")
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def delete_absentees_data(self):
        if self.var_atten_roll_absentees.get() == "":
            messagebox.showerror("Error", "Roll Number is required", parent=self.root)
        else:
            try:
                day = self.var_atten_day.get()
                month = self.var_atten_month.get()
                year = self.var_atten_year.get()
                date_conv = datetime.strptime(f"{day} {month} {year}", "%d %m %Y")
                date = date_conv.strftime("%d %B %Y")

                att_ref = db.reference(f"Attendance/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}/{self.var_atten_sem.get()}/{self.var_atten_sub.get()}/{date}/{self.var_atten_hour.get()}")
                atten_rolls = att_ref.get()

                present_stud = []

                for key, val in atten_rolls.items():
                    present_stud.append(key)

                stu_ref = db.reference(f"Students/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}").get()

                delete = messagebox.askyesno("Confirmation", "Do you want to delete this student's attendance?",
                                             parent=self.root)
                if delete > 0:
                    for key, val in stu_ref.items():
                        # total_attendance = db.reference(f"Students/{self.var_atten_dep.get()}/{self.var_atten_st_year.get()}/{key}/total_attendance/{self.var_atten_sem.get()}/{self.var_atten_sub.get()}").get()
                        if key == self.var_atten_roll_absentees.get():
                            attend = db.reference("/")
                            stud_att = attend.child('Attendance').child(self.var_atten_dep.get()).child(
                                self.var_atten_st_year.get()).child(
                                self.var_atten_sem.get()).child(self.var_atten_sub.get()).child(date).child(
                                self.var_atten_hour.get()).child(self.var_atten_roll_absentees.get()).set(1)
                            self.PresenteesReportTable.insert("", END, values=(key, val["Student Name"]))
                            self.var_atten_total_absentees.set(int(self.var_atten_total_absentees.get()) - 1)
                            self.var_atten_total_presentees.set(int(self.var_atten_total_presentees.get()) + 1)
                    self.AbsenteesReportTable.delete(self.AbsenteesReportTable.selection()[0])

                else:
                    if not delete:
                        return

                messagebox.showinfo("Delete", "Successfully deleted student attendance", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()

