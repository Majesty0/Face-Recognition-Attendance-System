"""
=========================================================
DSA4050 COMPUTER VISION PROJECT

Module:
03 - Face Detection

Description:
Detect faces using OpenCV Haar Cascade and
save cropped faces.

=========================================================
"""

from common import *

import os
import cv2

# -------------------------------------------------------
# Paths
# -------------------------------------------------------

CASCADE_PATH = PROJECT_ROOT / "haarcascade" / "haarcascade_frontalface_default.xml"

INPUT_PATH = PROJECT_ROOT / "dataset" / "processed"

OUTPUT_PATH = PROJECT_ROOT / "dataset" / "cropped"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------
# Load Haar Cascade
# -------------------------------------------------------

face_detector = cv2.CascadeClassifier(str(CASCADE_PATH))

if face_detector.empty():
    raise FileNotFoundError(
        f"Could not load Haar Cascade.\nExpected at:\n{CASCADE_PATH}"
    )

# -------------------------------------------------------
# Statistics
# -------------------------------------------------------

total_images = 0
faces_detected = 0
faces_not_detected = 0

# -------------------------------------------------------
# Process Dataset
# -------------------------------------------------------

for person in sorted(os.listdir(INPUT_PATH)):

    person_folder = INPUT_PATH / person

    if not person_folder.is_dir():
        continue

    output_person = OUTPUT_PATH / person
    output_person.mkdir(exist_ok=True)

    for image_name in sorted(os.listdir(person_folder)):

        image_path = person_folder / image_name

        image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

        if image is None:
            continue

        total_images += 1

        faces = face_detector.detectMultiScale(
    image,
    scaleFactor=1.05,
    minNeighbors=3,
    minSize=(20, 20)
)
        image = cv2.equalizeHist(image)

        if len(faces) == 0:
            faces_not_detected += 1
            continue

        # Keep the largest detected face
        x, y, w, h = max(faces, key=lambda f: f[2] * f[3])

        face = image[y:y+h, x:x+w]

        face = cv2.resize(face, (128,128))

        save_path = output_person / image_name

        cv2.imwrite(str(save_path), face)

        faces_detected += 1

# -------------------------------------------------------
# Summary
# -------------------------------------------------------

print("="*50)
print("FACE DETECTION SUMMARY")
print("="*50)

print(f"Images Processed      : {total_images}")
print(f"Faces Detected        : {faces_detected}")
print(f"No Face Detected      : {faces_not_detected}")

print("="*50)
print("Cropped faces saved to:")
print(OUTPUT_PATH)
print("="*50)