```text

Face_Recognition_Attendance_System/
│
├── dataset/
│   ├── ORL/
│   ├── processed/
│   ├── cropped/
│   └── custom/
│
├── data/
│   └── features/
│       ├── X.npy
│       └── y.npy
│
├── models/
│   ├── svm_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── attendance/
│   └── attendance.csv
│
├── reports/
│   ├── figures/
│   ├── tables/
│   └── screenshots/
│
├── src/
│   ├── common.py
│   ├── config.py
│   ├── utils.py
│   ├── evaluation.py
│   ├── recognizer.py
│   ├── attendance.py
│   ├── camera.py
│   ├── 01_dataset_loader.py
│   ├── 02_preprocessing.py
│   ├── 03_face_detection.py
│   ├── 04_feature_extraction.py
│   ├── 05_train_model.py
│   └── 06_model_evaluation.py
│
├── gui/
│   └── app.py
│
├── requirements.txt
├── README.md
└── main.py
```
