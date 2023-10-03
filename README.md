# Face-Mark-Attendance
<div>
  Face Mark Attendance is a Facial Recognition based attendance system for schools, universities and organizations.
</div>

## Installing and using the desktop application
<ul>
  <li>
    Download the zip files from the github repository and extract them into a folder
  </li>
  <li>
    Next, create a new firebase project and save the realtime database URL, storage bucket URL and the service account KEY for the next steps
  </li>
  <li>
    Now, open the database.py file in a code editor
  </li>
  <li>
    Copy the database URL, storage bucket URL and paste them in the approriate variables
  </li>
  <li>
    Rename the service account KEY to "serviceAccountKey.json" and store this file in the project destination
  </li>
  <li>
    Now, all you need are the required python libraries to install
  </li>
</ul>

## Required Python Libraries
<ul>
  <li>cv2</li>
  <li>dlib</li>
  <li>cvzone</li>
  <li>face_recognition</li>
  <li>pickle</li>
  <li>os</li>
  <li>firebase_admin</li>
  <li>numpy</li>
  <li>datetime</li>
  <li>tkinter</li>
  <li>PIL</li>
</ul>


## Addressing the problem installing dlib on a Windows machine 
Refer the link: https://github.com/ageitgey/face_recognition/issues/802#issuecomment-544232494
