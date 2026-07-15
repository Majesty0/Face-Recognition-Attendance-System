```text
FaceRecognitionAttendance/

│
├── dataset/
│   ├── raw/
│   ├── processed/
│   └── labels.csv
│
├── haarcascade/
│   └── haarcascade_frontalface_default.xml
│
├── models/
│   ├── svm_model.pkl
│   ├── label_encoder.pkl
│   └── scaler.pkl
│
├── attendance/
│   ├── attendance.csv
│   └── logs/
│
├── src/
│   │
│   ├── capture_faces.py
│   ├── preprocess.py
│   ├── detect_faces.py
│   ├── feature_extraction.py
│   ├── train_classifier.py
│   ├── recognize.py
│   ├── attendance.py
│   ├── evaluation.py
│   └── utils.py
│
├── gui/
│   └── app.py
│
├── reports/
│   ├── figures/
│   ├── tables/
│   └── screenshots/
│
├── presentation/
│
├── requirements.txt
│
└── README.md
```