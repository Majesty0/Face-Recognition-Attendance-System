# 🎓 Face Recognition Attendance System using Traditional Computer Vision and Machine Learning

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📖 Overview

The **Face Recognition Attendance System** is a desktop-based computer vision application developed as part of the **DSA4050 – Computer Vision** course at the **United States International University – Africa (USIU-Africa)**.

The system automates student attendance using **traditional computer vision techniques** and **machine learning** without relying on deep learning models. It detects faces using **Haar Cascade Classifiers**, extracts facial features using the **Histogram of Oriented Gradients (HOG)** descriptor, and recognizes individuals using a **Support Vector Machine (SVM)** classifier.

The project demonstrates the complete computer vision workflow from image acquisition through preprocessing, feature extraction, classification, evaluation, and deployment into a functional desktop application.

---

## 🚀 Key Features

- Face registration from a live webcam
- Automatic image dataset creation
- Haar Cascade face detection
- Image preprocessing and enhancement
- HOG feature extraction
- SVM-based face recognition
- Automatic attendance recording
- Duplicate attendance prevention
- Desktop graphical user interface (Tkinter)
- Model evaluation and visualization
- Performance reporting
- Excel attendance management

---

# System Workflow

```text
Student Registration
        │
        ▼
Image Acquisition
        │
        ▼
Image Preprocessing
        │
        ▼
Face Detection (Haar Cascade)
        │
        ▼
Feature Extraction (HOG)
        │
        ▼
Model Training (SVM)
        │
        ▼
Real-Time Face Recognition
        │
        ▼
Attendance Recording
```

---

# Technologies Used

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Feature Extraction | Scikit-image (HOG) |
| Machine Learning | Scikit-Learn |
| GUI | Tkinter |
| Data Handling | Pandas, NumPy |
| Attendance Storage | OpenPyXL |
| Visualization | Matplotlib |
| Model Persistence | Joblib |

---

# Project Structure

```text
Face-Recognition-Attendance-System/

│
├── assets/
│      ├── logo.png
│      └── usiu_logo.png
│
├── attendance/
│      ├── Attendance.xlsx
│      └── attendance_manager.py
│
├── data/
│      ├── students.csv
│      └── custom_features/
│             ├── X.npy
│             └── y.npy
│
├── dataset/
│      └── custom/
│             ├── Student_1/
│             ├── Student_2/
│             └── ...
│
├── models/
│      ├── custom_svm_model.pkl
│      ├── custom_scaler.pkl
│      └── custom_label_encoder.pkl
│
├── reports/
│      └── figures/
│
├── src/
│      ├── register_page.py
│      ├── train_page.py
│      ├── attendance_page.py
│      ├── dashboard.py
│      ├── records_page.py
│      ├── settings_page.py
│      ├── 09_feature_extraction.py
│      ├── 10_train_custom_model.py
│      ├── 11_face_recognition_attendance.py
│      └── 12_model_evaluation.py
│
└── README.md
```
```text
# Project Structure

```text
Face-Recognition-Attendance-System/
│
├── assets/                     # Logos, icons, and GUI resources
├── attendance/                 # Attendance records and attendance manager
├── controller/                 # Application controllers and backend logic
├── data/                       # Student records, extracted features, and datasets
├── dataset/                    # Face image datasets used for training
├── gui/                        # Desktop graphical user interface components
├── haarcascade/                # Haar Cascade XML classifier files
├── models/                     # Trained machine learning models
├── reports/                    # Evaluation results, figures, and project report
├── src/                        # Main source code modules
├── structure/                  # Project architecture and design resources
│
├── README.md                   # Project documentation
├── config.json                 # System configuration settings
├── developmentStructure.md     # Development workflow documentation
└── requirements.txt            # Python project dependencies
```
---

# Computer Vision Pipeline
> <img width="975" height="650" alt="image" src="https://github.com/user-attachments/assets/733b88ac-b9e9-45e4-bc3e-3d058e5c3200" />


## 1. Image Acquisition

- Live webcam image capture
- Automatic face dataset generation
- Approximately 50 facial images captured per student

---

## 2. Image Preprocessing

Each detected face undergoes:

- Grayscale conversion
- Image resizing (128 × 128)
- Gaussian Blur
- Histogram Equalization

These preprocessing techniques improve image consistency and enhance recognition performance under varying lighting conditions.

---

## 3. Face Detection

The system detects faces using the OpenCV implementation of the **Haar Cascade Classifier**, enabling fast and reliable frontal face detection suitable for real-time applications.

---

## 4. Feature Extraction

Instead of using deep learning embeddings, facial characteristics are represented using the **Histogram of Oriented Gradients (HOG)** descriptor.

Benefits include:

- Computational efficiency
- Illumination robustness
- Edge orientation representation
- Excellent compatibility with SVM classifiers

---

## 5. Face Recognition

Extracted HOG features are classified using a **Support Vector Machine (SVM)**.

The trained model predicts:

- Student identity
- Recognition confidence

Unknown individuals are rejected using a confidence threshold.

---

## 6. Attendance Management

Recognized students are automatically recorded into an Excel workbook containing:

- Student ID
- Student Name
- Date
- Time
- Attendance Status

Duplicate attendance entries are prevented.

---

# Desktop Application

The system includes a fully functional desktop GUI featuring:

- Dashboard
- Student Registration
- Model Training
- Face Recognition
- Attendance Records
- System Settings

---

# Model Evaluation

Performance is evaluated using standard machine learning metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- False Positive Rate
- Processing Time
- Confusion Matrix

---

# Sample Output

```
CUSTOM MODEL PERFORMANCE

Training Samples : 360
Testing Samples  : 90

Accuracy  : 96.67%
Precision : 97.44%
Recall    : 96.67%
F1 Score  : 96.73%
```

---

# Screenshots

## Dashboard

> *<img width="975" height="506" alt="image" src="https://github.com/user-attachments/assets/cc15153d-24c4-44cb-87a6-05f7feda516c" />*

---

## Student Registration
> <img width="975" height="760" alt="image" src="https://github.com/user-attachments/assets/0ef1d973-d77f-41d8-b7f8-7c6e4d6cb45c" />
---
## Image Capture
> <img width="829" height="652" alt="image" src="https://github.com/user-attachments/assets/3612ced5-a64c-4537-8b70-d6f3bcc5f764" />

---

## Model Training

> <img width="1139" height="639" alt="image" src="https://github.com/user-attachments/assets/faa713ed-87a8-4834-aaec-d6d4b964f6c3" />


---

## Face Recognition

> <img width="975" height="773" alt="image" src="https://github.com/user-attachments/assets/c58be538-dd10-4376-8767-59d0d2c6e9bb" />


---

## Attendance Records

> <img width="975" height="475" alt="image" src="https://github.com/user-attachments/assets/dd00b232-3cf4-4a3b-b24e-11b9cd43d2aa" />


---

## Model Evaluation

> <img width="1041" height="764" alt="image" src="https://github.com/user-attachments/assets/6db81f08-b985-4bba-8080-f313d620fd62" />
> <img width="975" height="609" alt="image" src="https://github.com/user-attachments/assets/9cd9b419-b4fb-4977-85d0-bc517c33ebee" />


---



## Getting Started...

### Clone the repository

```bash
git clone https://github.com/Majesty0/Face-Recognition-Attendance-System.git
```
Navigate into the project.

```bash
cd Face-Recognition-Attendance-System
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the desktop application.

```bash
python dashboard.py
```
If you plan to contribute to the project and do not have write access, first fork the repository on GitHub, then clone your fork and submit a pull request with your changes.
---

# Future Improvements

- Multi-face tracking
- Face anti-spoofing
- Student database integration
- Cloud attendance synchronization
- Mobile application support
- RFID and face recognition hybrid authentication
- Improved feature extraction methods
- Face recognition under extreme illumination
- Multiple camera support

---

# Academic Context

This project was developed for:

**DSA4050 – Computer Vision**

School of Science and Technology

United States International University – Africa (USIU-Africa)

Supervisor:

**Dr. Dennis Kitari**

---

# Author

**Kyeremateng Martin**

Data Science and Analytics Student

United States International University – Africa

GitHub: *Add your GitHub profile*

LinkedIn: *Add your LinkedIn profile*

---

# Acknowledgements

Special appreciation to:

- Dr. Dennis Kitari
- United States International University – Africa
- OpenCV Community
- Scikit-Learn Developers
- NumPy Developers
- Pandas Developers
- The Python Software Foundation

for providing the tools and knowledge that made this project possible.

---

# License

This project is intended for educational and research purposes.

© 2026 Kyeremateng Martin. All Rights Reserved.
