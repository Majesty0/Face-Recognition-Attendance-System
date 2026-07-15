"""
=========================================================
DSA4050 COMPUTER VISION PROJECT

Module:
09 - Feature Extraction (Custom Dataset)
=========================================================
"""

from common import *

import os
import cv2
import numpy as np
from skimage.feature import hog

# -------------------------------------------------------
# Paths
# -------------------------------------------------------

INPUT_PATH = PROJECT_ROOT / "dataset" / "custom"

FEATURE_PATH = PROJECT_ROOT / "data" / "custom_features"
FEATURE_PATH.mkdir(parents=True, exist_ok=True)

X = []
y = []

# -------------------------------------------------------
# Extract Features
# -------------------------------------------------------

for student in sorted(os.listdir(INPUT_PATH)):

    student_folder = INPUT_PATH / student

    if not student_folder.is_dir():
        continue

    for image_name in sorted(os.listdir(student_folder)):

        image_path = student_folder / image_name

        image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

        if image is None:
            continue

        image = cv2.resize(image, (128, 128))
        image = cv2.equalizeHist(image)

        features = hog(
            image,
            orientations=9,
            pixels_per_cell=(8, 8),
            cells_per_block=(2, 2),
            block_norm="L2-Hys",
            visualize=False
        )

        X.append(features)
        y.append(student)

# -------------------------------------------------------
# Save Features
# -------------------------------------------------------

X = np.array(X)
y = np.array(y)

np.save(FEATURE_PATH / "X.npy", X)
np.save(FEATURE_PATH / "y.npy", y)

print("=" * 50)
print("CUSTOM FEATURE EXTRACTION COMPLETE")
print("=" * 50)
print(f"Samples      : {len(X)}")
print(f"Classes      : {len(np.unique(y))}")
print(f"Feature Size : {X.shape[1]}")
print("=" * 50)