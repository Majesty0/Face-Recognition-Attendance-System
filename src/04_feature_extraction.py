"""
=========================================================
DSA4050 COMPUTER VISION PROJECT

Module:
04 - HOG Feature Extraction

Description:
Extract HOG features from cropped face images and save
them for machine learning.

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

INPUT_PATH = PROJECT_ROOT / "dataset" / "cropped"

FEATURE_PATH = PROJECT_ROOT / "data" / "features"

FEATURE_PATH.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------
# Containers
# -------------------------------------------------------

X = []
y = []

# -------------------------------------------------------
# Extract HOG Features
# -------------------------------------------------------

for person in sorted(os.listdir(INPUT_PATH)):

    person_folder = INPUT_PATH / person

    if not person_folder.is_dir():
        continue

    for image_name in sorted(os.listdir(person_folder)):

        image_path = person_folder / image_name

        image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

        if image is None:
            continue

        image = cv2.resize(image, (128,128))

        features = hog(
            image,
            orientations=9,
            pixels_per_cell=(8,8),
            cells_per_block=(2,2),
            block_norm="L2-Hys",
            visualize=False
        )

        X.append(features)
        y.append(person)

# -------------------------------------------------------
# Convert to NumPy
# -------------------------------------------------------

X = np.array(X)
y = np.array(y)

# -------------------------------------------------------
# Save Features
# -------------------------------------------------------

np.save(FEATURE_PATH / "X.npy", X)
np.save(FEATURE_PATH / "y.npy", y)

# -------------------------------------------------------
# Summary
# -------------------------------------------------------

print("="*50)
print("FEATURE EXTRACTION COMPLETE")
print("="*50)

print(f"Samples       : {len(X)}")
print(f"Classes       : {len(np.unique(y))}")
print(f"Feature Size  : {X.shape[1]}")

print("="*50)

print("Saved Files")

print(FEATURE_PATH / "X.npy")
print(FEATURE_PATH / "y.npy")

print("="*50)