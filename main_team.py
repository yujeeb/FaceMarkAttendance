import os
import pickle
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-mark-attendance-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'storageBucket': "face-mark-attendance.appspot.com"
})

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("380x360+0+0")
        self.root.title("FACE MARK ATTENDANCE")
        self.root.iconbitmap('Resources/logo.ico')

        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_sub = StringVar()
        self.var_period = StringVar()

        main_frame = Frame(bd=2, bg="white")
        main_frame.place(x=0, y=0, width=380, height=1200)

        input_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="CURRENT COURSE INFORMATION",
                                          font=("times new roman", 12, "bold"))
        input_frame.place(x=5, y=0, width=365, height=300)

        date_label = Label(input_frame, text="TODAY : ", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        today_label = Label(input_frame, text=datetime.today().strftime("%d %B %Y"),
                            font=("times new roman", 12, "bold"), fg="white", bg="red")
        today_label.grid(row=0, column=1, padx=30, pady=10, sticky=W)

        dep_label = Label(input_frame, text="Department : ", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(input_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 state="readonly")
        dep_combo["values"] = ("Select Department", "CSD")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=1, padx=2, pady=10)

        year_label = Label(input_frame, text="Year : ", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=2, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(input_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"),
                                 state="readonly")
        year_combo["values"] = ("Select Year", "2021-2025")
        year_combo.current(0)
        year_combo.grid(row=2, column=1, padx=2, pady=10)

        sem_label = Label(input_frame, text="Semester : ", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=3, column=0, padx=10, sticky=W)

        sem_combo = ttk.Combobox(input_frame, textvariable=self.var_sem, font=("times new roman", 12, "bold"),
                                 state="readonly")
        sem_combo["values"] = ("Select Semester", "Semester-3")
        sem_combo.current(0)
        sem_combo.grid(row=3, column=1, padx=2, pady=10)

        sub_label = Label(input_frame, text="Subject : ", font=("times new roman", 12, "bold"), bg="white")
        sub_label.grid(row=4, column=0, padx=10, sticky=W)

        sub_combo = ttk.Combobox(input_frame, textvariable=self.var_sub, font=("times new roman", 12, "bold"),
                                 state="readonly")
        sub_combo["values"] = ("Select Subject", "SIP", "PYTHON LAB", "DBMS LAB", "OS LAB", "SFD", "DAA", "DBMS", "OS")
        sub_combo.current(0)
        sub_combo.grid(row=4, column=1, padx=2, pady=10)

        per_label = Label(input_frame, text="Period/Hour : ", font=("times new roman", 12, "bold"), bg="white")
        per_label.grid(row=5, column=0, padx=10, sticky=W)

        per_combo = ttk.Combobox(input_frame, textvariable=self.var_period, font=("times new roman", 12, "bold"),
                                 state="readonly")
        per_combo["values"] = ("Select Hour", "Hour 1", "Hour 2", "Hour 3", "Hour 4", "Hour 5", "Hour 6")
        per_combo.current(0)
        per_combo.grid(row=5, column=1, padx=2, pady=10)

        b1_1 = Button(self.root, text="MARK ATTENDANCE", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="green", fg="white")
        b1_1.place(x=5, y=310, width=370, height=40)

    def proceed(self):
        if self.var_dep.get() == "Select Department" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_sub.get() == "Select Subject" or self.var_period.get() == "Select Hour":
            return True
        else:
            return False

    def face_recog(self):
        if self.proceed():
            messagebox.showerror("ERROR", "Fill all the fields", parent=self.root)
        else:
            try:
                # Total attendance
                # try:
                #     ref_total_attendance = db.reference(f"Attendance/{self.var_dep.get()}/{self.var_year.get()}/{self.var_sem.get()}/{self.var_sub.get()}").get()
                #     tot = 0
                #     for key, val in ref_total_attendance.items():
                #         print(val)
                #         for hour, roll in val.items():
                #             print(hour)
                #             print(roll)
                #             for roll_n , one in roll.items():
                #                 studentIn = db.reference(f'Students/{self.var_dep.get()}/{self.var_year.get()}').get()
                #                 if roll_n in studentIn.keys():
                #                     tot += 1
                #                     db.reference(f'Students/{self.var_dep.get()}/{self.var_year.get()}/{roll_n}/total_attendance').child(self.var_sem.get()).child(self.var_sub.get()).set(tot)
                # except Exception as es:
                #     pass

                bucket = storage.bucket()

                students = []

                cap = cv2.VideoCapture(0)
                cap.set(3, 640)
                cap.set(4, 480)

                imgBackground = cv2.imread('Resources/background.png')

                # Importing the mode images into a list
                folderModePath = 'Resources/Modes'
                modePathList = os.listdir(folderModePath)
                imgModeList = []
                for path in modePathList:
                    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

                # Load the encoding file
                print("Loading Encode File ...")
                file = open('EncodeFile.p', 'rb')
                encodeListKnownWithIds = pickle.load(file)
                file.close()
                encodeListKnown, studentIds = encodeListKnownWithIds
                # print(studentIds)
                print("Encode File Loaded")

                modeType = 0
                counter = 0
                id = -1
                imgStudent = []


                while True:
                    success, img = cap.read()

                    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
                    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                    faceCurFrame = face_recognition.face_locations(imgS)
                    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

                    imgBackground[162:162 + 480, 55:55 + 640] = img
                    imgBackground[44:44 + 630, 808:808 + 414] = imgModeList[modeType]

                    if faceCurFrame:
                        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

                            matchIndex = np.argmin(faceDis)

                            if matches[matchIndex]:
                                y1, x2, y2, x1 = faceLoc
                                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                                id = studentIds[matchIndex]
                                if counter == 0:
                                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                                    cv2.imshow("FACE MARK ATTENDANCE", imgBackground)
                                    cv2.waitKey(1)
                                    counter = 1
                                    modeType = 1

                        if counter != 0:
                            if counter == 1:
                                # Get the Data
                                studentInfo = db.reference(f'Students/{self.var_dep.get()}/{self.var_year.get()}/{id}').get()
                                print(studentInfo)
                                if studentInfo is not None:
                                    # Get the Image from the storage
                                    blob = bucket.get_blob(f'Images/{id}.png')
                                    array = np.frombuffer(blob.download_as_string(), np.uint8)
                                    imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                                    attend = db.reference("/")
                                    stud_att = attend.child('Attendance').child(self.var_dep.get()).child(self.var_year.get()).child(
                                        self.var_sem.get()).child(self.var_sub.get()).child(datetime.today().strftime("%d %B %Y")).child(
                                        self.var_period.get()).child(id).set(1)

                            if modeType != 3:
                                # try:
                                #     ref_total_attendance = db.reference(
                                #         f"Attendance/{self.var_dep.get()}/{self.var_year.get()}/{self.var_sem.get()}/{self.var_sub.get()}").get()
                                #     tot = 0
                                #     for key, val in ref_total_attendance.items():
                                #         print(val)
                                #         for hour, roll in val.items():
                                #             print(hour)
                                #             print(roll)
                                #             for roll_n, one in roll.items():
                                #                 studentIn = db.reference(
                                #                     f'Students/{self.var_dep.get()}/{self.var_year.get()}').get()
                                #                 if roll_n in studentIn.keys():
                                #                     tot += 1
                                #                     db.reference(
                                #                         f'Students/{self.var_dep.get()}/{self.var_year.get()}/{roll_n}/total_attendance').child(
                                #                         self.var_sem.get()).child(self.var_sub.get()).set(tot)
                                # except Exception as es:
                                #     pass

                                studentInfo = db.reference(f'Students/{self.var_dep.get()}/{self.var_year.get()}/{id}').get()
                                print(studentInfo)
                                # total_att = db.reference(f'Students/{self.var_dep.get()}/{self.var_year.get()}/{id}/total_attendance').child(self.var_sem.get()).child(self.var_sub.get()).get()

                                if studentInfo is not None:

                                    imgBackground[44:44 + 630, 808:808 + 414] = imgModeList[modeType]
                                    # cv2.putText(imgBackground, str(total_att) if total_att is not None else "1", (861, 125),
                                    #             cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                                    cv2.putText(imgBackground, str(studentInfo['Department']), (1006, 550),
                                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                                    cv2.putText(imgBackground, str(id), (1006, 493),
                                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                                    # cv2.putText(imgBackground, str(studentInfo['Year']), (1006, 625),
                                    #             cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                                    (w, h), _ = cv2.getTextSize(studentInfo['Student Name'].split(" ")[0], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                                    offset = (414 - w) // 2
                                    cv2.putText(imgBackground, str(studentInfo['Student Name'].split(" ")[0]), (808 + offset, 445), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)

                                    imgBackground[175:175 + 216, 909:909 + 216] = imgStudent

                                    counter += 1
                    else:
                        modeType = 0
                        counter = 0
                    cv2.imshow("FACE MARK ATTENDANCE", imgBackground)
                    cv2.waitKey(1)

                    if cv2.waitKey(0) == 13:
                        break
                cap.release()
                cv2.destroyAllWindows()
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

if __name__ == "__main__":
    try:
        root = Tk()
        obj = Face_Recognition(root)
        root.mainloop()
    except Exception as es:
        print(es)
