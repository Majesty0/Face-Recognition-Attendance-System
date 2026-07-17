"""
=========================================================
DSA4050 COMPUTER VISION PROJECT

Module:
11 - Face Recognition Attendance System
=========================================================
"""

from common import *

import cv2
import joblib
import numpy as np
import pandas as pd
import time

from datetime import datetime
from skimage.feature import hog

from attendance.attendance_manager import mark_attendance

# -------------------------------------------------------
# Load Models
# -------------------------------------------------------

MODEL_PATH = PROJECT_ROOT / "models"

model = joblib.load(MODEL_PATH / "custom_svm_model.pkl")
scaler = joblib.load(MODEL_PATH / "custom_scaler.pkl")
encoder = joblib.load(MODEL_PATH / "custom_label_encoder.pkl")

students = pd.read_csv(PROJECT_ROOT / "data" / "students.csv")
print(students.head())
print(f"Total students: {len(students)}")

# Remove duplicate registrations if any
students = students.drop_duplicates(subset="Folder")

print("=" * 70)
print("FACE RECOGNITION ATTENDANCE SYSTEM")
print("=" * 70)
print("Registered Students :", len(students))
print("Known Classes       :", len(encoder.classes_))
print("=" * 70)

# -------------------------------------------------------
# Haar Cascade
# -------------------------------------------------------

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# -------------------------------------------------------
# Webcam
# -------------------------------------------------------

camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

if not camera.isOpened():
    print("Could not open webcam.")
    exit()

print("Press Q to Quit")

previous_time = time.time()

# -------------------------------------------------------
# Main Loop
# -------------------------------------------------------

while True:

    frame_start = time.time()

    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.10,
        minNeighbors=7,
        minSize=(120,120),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    attendance_status = ""

    for (x,y,w,h) in faces:

        face = gray[y:y+h, x:x+w]

        face = cv2.resize(face,(128,128))

        face = cv2.GaussianBlur(face,(3,3),0)

        face = cv2.equalizeHist(face)

        features = hog(
            face,
            orientations=12,
            pixels_per_cell=(8,8),
            cells_per_block=(2,2),
            block_norm="L2-Hys",
            transform_sqrt=True,
            visualize=False
        )

        features = features.reshape(1,-1)

        features = scaler.transform(features)

        prediction = model.predict(features)[0]

        probability = model.predict_proba(features)[0]

        confidence = float(np.max(probability))

        folder = encoder.inverse_transform([prediction])[0]

        student = students[
            students["Folder"] == folder
        ]

                # -------------------------------------------------------
        # Recognition Decision
        # -------------------------------------------------------

        if student.empty or confidence < 0.85:

            label = "UNKNOWN"

            color = (0,0,255)

        else:

            student_id = str(student.iloc[0]["StudentID"])
            student_name = student.iloc[0]["StudentName"]

            recorded = mark_attendance(
                student_id,
                student_name
            )

            if recorded:

                attendance_status = (
                    f"{student_name} - Attendance Marked"
                )

            else:

                attendance_status = (
                    f"{student_name} - Already Marked"
                )

            label = (
                f"{student_name} | "
                f"{confidence*100:.1f}%"
            )

            color = (0,255,0)

        # -------------------------------------------------------
        # Draw Bounding Box
        # -------------------------------------------------------

        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            color,
            2
        )

        cv2.putText(
            frame,
            label,
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

    # -------------------------------------------------------
    # Dashboard Information
    # -------------------------------------------------------

    current_time = time.time()

    fps = 1 / (current_time - previous_time)

    previous_time = current_time

    processing_time = (
        time.time() - frame_start
    ) * 1000

    now = datetime.now()

    cv2.putText(
        frame,
        now.strftime("%d-%m-%Y %H:%M:%S"),
        (20,35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        f"FPS : {fps:.1f}",
        (20,70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Processing : {processing_time:.1f} ms",
        (20,105),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Faces : {len(faces)}",
        (20,140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,255),
        2
    )

        # -------------------------------------------------------
    # Attendance Status
    # -------------------------------------------------------

    if attendance_status != "":

        cv2.rectangle(
            frame,
            (10, frame.shape[0]-55),
            (650, frame.shape[0]-10),
            (0,120,0),
            -1
        )

        cv2.putText(
            frame,
            attendance_status,
            (20, frame.shape[0]-25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (255,255,255),
            2
        )

    # -------------------------------------------------------
    # Footer
    # -------------------------------------------------------

    cv2.putText(
        frame,
        "Press Q to Exit",
        (frame.shape[1]-200, frame.shape[0]-20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        "DSA4050 Computer Vision Project",
        (frame.shape[1]-340,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (0,255,255),
        2
    )

    # -------------------------------------------------------
    # Display Window
    # -------------------------------------------------------

    cv2.imshow(
        "Face Recognition Attendance System",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# -------------------------------------------------------
# Release Resources
# -------------------------------------------------------

camera.release()

cv2.destroyAllWindows()

print("\nSystem Closed Successfully.")