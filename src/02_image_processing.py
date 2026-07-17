"""
=========================================================
DSA4050 COMPUTER VISION PROJECT

Module:
02 - Image Preprocessing

Description:
Preprocesses the ORL dataset and saves processed images.

=========================================================
"""

from common import *
import os
import cv2

# -------------------------------------------------------
# Paths
# -------------------------------------------------------

PROCESSED_PATH = PROJECT_ROOT / "dataset" / "cropped"

PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------
# Processing Statistics
# -------------------------------------------------------

processed_count = 0

# -------------------------------------------------------
# Process Dataset
# -------------------------------------------------------

for person in sorted(os.listdir(DATASET_PATH)):

    person_folder = DATASET_PATH / person

    if not person_folder.is_dir():
        continue

    output_folder = PROCESSED_PATH / person
    output_folder.mkdir(exist_ok=True)

    for image_name in sorted(os.listdir(person_folder)):

        image_path = person_folder / image_name

        image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

        if image is None:
            continue

        # Resize
        image = cv2.resize(image, (128, 128))

        # Histogram Equalization
        image = cv2.equalizeHist(image)

        # Gaussian Blur
        image = cv2.GaussianBlur(image, (3, 3), 0)

        output_path = output_folder / image_name

        cv2.imwrite(str(output_path), image)

        processed_count += 1

print("=" * 50)
print("PREPROCESSING COMPLETE")
print("=" * 50)
print(f"Processed Images : {processed_count}")
print(f"Saved To         : {PROCESSED_PATH}")
print("=" * 50)