# Face Mark Attendance

## Project Overview

**Face Mark Attendance** is an innovative facial recognition-based attendance system designed to address the prevalent issue of proxy attendance in educational institutions. By leveraging advanced AI technologies, this system ensures accurate and efficient attendance tracking, thereby enhancing institutional integrity.

## Objective

The primary objective of this project is to develop a robust prototype that mitigates unauthorized attendance marking by implementing a reliable facial recognition system.

## Technology Stack

- **Programming Language:** Python
- **User Interface:** Tkinter
- **Facial Recognition:** [face_recognition](https://pypi.org/project/face-recognition/) library built on dlib's state-of-the-art model
- **Additional Libraries:**
  - OpenCV
  - PIL (Python Imaging Library)
  - cmake
  - dlib
  - cvzone
- **Database:** Firebase Realtime Database (NoSQL Cloud Database)

## Key Features

The system comprises three independent yet interconnected modules:

1. **Student Management System**
   - **Data Entry:** Input and store student information in the database.
   - **Face Capture:** Capture and store students' facial images.
   - **Data Management:** Retrieve and update student records.
   - **Model Training:** Train the facial recognition model with a single click.

2. **Main Application**
   - **Attendance Recording:** Utilize facial recognition to mark attendance by selecting details such as Department and Subject.

3. **Attendance Management System**
   - **Attendance Verification:** Review attendance records, including roll numbers, student names, and total attendance for specific dates.

## Installation Instructions

To deploy and run the Face Mark Attendance system, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yujeeb/FaceMarkAttendance.git
   ```
   Alternatively, download the ZIP file from the repository and extract its contents.

2. **Set Up Firebase:**
   - Create a new project in Firebase.
   - Obtain the Realtime Database URL and Storage Bucket URL.
   - Generate the service account key JSON file.

3. **Configure the Application:**
   - Open the `database.py` file in a code editor.
   - Replace the placeholder variables with your Firebase project's Database URL and Storage Bucket URL.
   - Rename the service account key file to `serviceAccountKey.json` and place it in the project directory.

4. **Install Required Python Libraries:**
   Ensure you have Python installed on your system. Then, install the necessary libraries:
   ```bash
   pip install opencv-python dlib cvzone face_recognition pickle firebase_admin numpy pillow
   ```

   *Note:* Installing `dlib` on Windows can be challenging. Refer to the [face_recognition GitHub repository](https://github.com/ageitgey/face_recognition) for detailed installation instructions.

5. **Run the Application:**
   Execute the main application script:
   ```bash
   python main_team.py
   ```

## Usage Instructions

### 1. Student Management System

This module facilitates the management of student data and the training of the facial recognition model.

**Steps:**

- **Launch the Application:**
  - Run the `student.py` script to start the Student Management System interface.

- **Add New Student:**
  - Navigate to the "Add Student" section.
  - Enter the student's details, including:
    - **Name:** Full name of the student.
    - **Roll Number:** Unique identification number assigned to the student.
    - **Department:** Academic department or course the student is enrolled in.
  - Use the integrated webcam feature to capture image of the student's face. Ensure the following during capture:
    - The student's face is clearly visible with adequate lighting.
    - The student maintains a neutral expression and looks directly at the camera.

- **Update Student Information:**
  - In the "Manage Students" section, select a student from the list.
  - Modify the necessary details and save the changes.

- **Train Facial Recognition Model:**
  - After adding or updating student data, initiate the training process by clicking the "Train Model" button.
  - The system will process the captured images and update the facial recognition model accordingly.

### 2. Main Application

This module is responsible for conducting attendance sessions using the trained facial recognition model.

**Steps:**

- **Launch the Application:**
  - Run the `main_team.py` script to open the Main Application interface.

- **Configure Attendance Session:**
  - Select the relevant parameters for the session:
    - **Department:** Choose the department or course.
    - **Subject:** Specify the subject or class name.
    - **Date and Time:** Set the date and time for the attendance session.

- **Initiate Attendance:**
  - Position the camera to capture the students' faces as they enter the classroom.
  - The system will automatically recognize registered students and mark their attendance in real-time.

### 3. Attendance Management System

This module allows administrators and faculty to review and manage attendance records.

**Steps:**

- **Launch the Application:**
  - Run the `attendance.py` script to access the Attendance Management System interface.

- **View Attendance Records:**
  - Select the desired date, department, and subject to retrieve attendance logs.
  - The system will display a list of students with their attendance status and timestamps.

- **Generate Reports:**
  - Export attendance data to CSV or Excel formats for record-keeping and analysis.

## Contributors

- **Yujeeb Abbas Kashani** – Application Designer, Primary Developer and Team Lead
- **Team Members:**
  - Narendra Kumar Basimi – Application Development Support
  - Siddeshwara Chary – Documentation Specialist
  - Meena – Data Collection and Testing
  - Jaya Laxmi – Data Collection and Testing

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
