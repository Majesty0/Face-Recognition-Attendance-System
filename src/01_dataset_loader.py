"""
=========================================================
DSA4050 COMPUTER VISION PROJECT

Module:
01 - Dataset Loader

Author:
<Kyeremateng Martin>

Description:
Loads the ORL Face Dataset and performs dataset validation.

=========================================================
"""

import os
import cv2
import matplotlib.pyplot as plt

# -------------------------------------------------------
# Dataset Path
# -------------------------------------------------------
from common import *
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "dataset" / "ORL"

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

images = []
labels = []
persons = []

for person in sorted(os.listdir(DATASET_PATH)):

    person_path = os.path.join(DATASET_PATH, person)

    if not os.path.isdir(person_path):
        continue

    persons.append(person)

    for image_name in sorted(os.listdir(person_path)):

        image_path = os.path.join(person_path, image_name)

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            print(f"Could not read {image_path}")
            continue

        images.append(image)
        labels.append(person)

print("=" * 50)
print("DATASET SUMMARY")
print("=" * 50)

print(f"Total Persons : {len(persons)}")
print(f"Total Images  : {len(images)}")

print("=" * 50)

# -------------------------------------------------------
# Images Per Person
# -------------------------------------------------------

for person in persons:

    count = len(os.listdir(os.path.join(DATASET_PATH, person)))

    print(f"{person:5} --> {count} images")

print("=" * 50)

# -------------------------------------------------------
# Display Sample Images
# -------------------------------------------------------

plt.figure(figsize=(12,8))

for i in range(12):

    plt.subplot(3,4,i+1)

    plt.imshow(images[i], cmap="gray")

    plt.title(labels[i])

    plt.axis("off")

plt.tight_layout()

plt.show()