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

print("Press 'Q' to Quit")

while True:

    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=5,
        minSize=(80,80)
    )

    for (x, y, w, h) in faces:

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

        confidence = np.max(probability)

        folder = encoder.inverse_transform([prediction])[0]

        student = students[students["Folder"] == folder]

        if student.empty or confidence < 0.85:

            label = "Unknown"

        else:

            student_id = str(student.iloc[0]["StudentID"])
            student_name = student.iloc[0]["StudentName"]

            recorded = mark_attendance(student_id, student_name)

            if recorded:
                status = "Attendance Marked"
            else:
                status = "Already Marked"

            label = f"{student_name} ({confidence*100:.1f}%)"

            cv2.putText(
                frame,
                status,
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,255,0),
                2
            )

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.putText(
            frame,
            label,
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

    cv2.imshow("Face Recognition Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()