"""
=========================================================
DSA4050 COMPUTER VISION PROJECT

Module:
07 - Register Student

Description:
Registers a new student by capturing 50 face images.

=========================================================
"""

from common import *

import cv2
import pandas as pd

# -------------------------------------------------------
# Student Details
# -------------------------------------------------------

student_id = input("Enter Student ID: ").strip()
student_name = input("Enter Student Name: ").strip()

folder_name = f"{student_name}_{student_id}"

dataset_path = PROJECT_ROOT / "dataset" / "custom" / folder_name
dataset_path.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------
# Save Student Record
# -------------------------------------------------------

students_file = PROJECT_ROOT / "data" / "students.csv"
students_file.parent.mkdir(parents=True, exist_ok=True)

new_student = pd.DataFrame({
    "StudentID": [student_id],
    "StudentName": [student_name],
    "Folder": [folder_name]
})

if students_file.exists():
    students = pd.read_csv(students_file)
    students = pd.concat([students, new_student], ignore_index=True)
else:
    students = new_student

students.to_csv(students_file, index=False)

# -------------------------------------------------------
# Haar Cascade
# -------------------------------------------------------

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# -------------------------------------------------------
# Webcam
# -------------------------------------------------------

camera = cv2.VideoCapture(0)

count = 0

print("\nCapturing face images...")
print("Press 'q' to stop.\n")

while True:

    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=5,
        minSize=(80, 80)
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (128, 128))

        count += 1

        filename = dataset_path / f"img_{count:03}.jpg"

        cv2.imwrite(str(filename), face)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(
            frame,
            f"Captured: {count}/50",
            (20, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        if count >= 50:
            break

    cv2.imshow("Register Student", frame)

    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

    if count >= 50:
        break

camera.release()
cv2.destroyAllWindows()

print("\nRegistration completed successfully!")
print(f"Images Saved : {count}")
print(f"Location     : {dataset_path}")