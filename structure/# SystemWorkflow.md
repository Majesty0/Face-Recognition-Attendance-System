```text
Camera
    │
    ▼
Capture Image
    │
    ▼
Image Preprocessing
    │
    ├── Resize
    ├── Grayscale
    ├── Histogram Equalization
    └── Noise Removal
    │
    ▼
Face Detection
(Haar Cascade)
    │
    ▼
Feature Extraction
(HOG)
    │
    ▼
Classifier
(SVM)
    │
    ▼
Known Person?
   │        │
 Yes       No
 │           │
 ▼           ▼
Record      Unknown
Attendance
 │
 ▼
Attendance Report
```

## Process Description

1. **Camera** captures a live image.
2. **Capture Image** acquires the frame for processing.
3. **Image Preprocessing** improves image quality through:
   - Resize
   - Grayscale Conversion
   - Histogram Equalization
   - Noise Removal
4. **Face Detection** identifies faces using the **Haar Cascade** algorithm.
5. **Feature Extraction** extracts facial features using **Histogram of Oriented Gradients (HOG)**.
6. **Classifier (SVM)** compares extracted features against trained facial data.
7. **Known Person?**
   - **Yes:** Record attendance.
   - **No:** Mark as unknown.
8. Generate the **Attendance Report**
```