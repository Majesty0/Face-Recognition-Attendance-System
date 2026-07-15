"""
=========================================================
DSA4050 COMPUTER VISION PROJECT

Module:
06 - Model Evaluation & Visualization
=========================================================
"""

from common import *

import joblib
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# -------------------------------------------------------
# Paths
# -------------------------------------------------------

FEATURE_PATH = PROJECT_ROOT / "data" / "features"
MODEL_PATH = PROJECT_ROOT / "models"
FIGURE_PATH = PROJECT_ROOT / "reports" / "figures"

FIGURE_PATH.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------

X = np.load(FEATURE_PATH / "X.npy")
y = np.load(FEATURE_PATH / "y.npy")

encoder = joblib.load(MODEL_PATH / "label_encoder.pkl")
scaler = joblib.load(MODEL_PATH / "scaler.pkl")
model = joblib.load(MODEL_PATH / "svm_model.pkl")

y = encoder.transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

X_test = scaler.transform(X_test)

y_pred = model.predict(X_test)

# -------------------------------------------------------
# Metrics
# -------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")

# -------------------------------------------------------
# Bar Chart
# -------------------------------------------------------

metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
values = [accuracy, precision, recall, f1]

plt.figure(figsize=(8,5))
plt.bar(metrics, values)

plt.ylim(0,1.05)

for i,v in enumerate(values):
    plt.text(i, v+0.02, f"{v:.2f}", ha="center")

plt.title("Model Performance")

plt.savefig(FIGURE_PATH/"model_performance.png",
            dpi=300,
            bbox_inches="tight")

plt.close()

# -------------------------------------------------------
# Confusion Matrix
# -------------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(cm)

fig, ax = plt.subplots(figsize=(12,12))

disp.plot(
    ax=ax,
    colorbar=False,
    xticks_rotation=90
)

plt.title("Confusion Matrix")

plt.savefig(FIGURE_PATH/"confusion_matrix.png",
            dpi=300,
            bbox_inches="tight")

plt.close()

print("="*50)
print("VISUALIZATION COMPLETE")
print("="*50)
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print()
print("Figures saved to:")
print(FIGURE_PATH)
print("="*50)