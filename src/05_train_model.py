"""
=========================================================
DSA4050 COMPUTER VISION PROJECT

Module:
05 - Train Face Recognition Model

Description:
Train an SVM classifier using HOG features and evaluate
its performance.

=========================================================
"""

from common import *

import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

# -------------------------------------------------------
# Paths
# -------------------------------------------------------

FEATURE_PATH = PROJECT_ROOT / "data" / "features"
MODEL_PATH = PROJECT_ROOT / "models"

MODEL_PATH.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------
# Load Features
# -------------------------------------------------------

X = np.load(FEATURE_PATH / "X.npy")
y = np.load(FEATURE_PATH / "y.npy")

# -------------------------------------------------------
# Encode Labels
# -------------------------------------------------------

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# -------------------------------------------------------
# Split Dataset
# -------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

# -------------------------------------------------------
# Standardize Features
# -------------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -------------------------------------------------------
# Train SVM
# -------------------------------------------------------

model = SVC(
    kernel="rbf",
    C=10,
    gamma="scale",
    probability=True
)

model.fit(X_train, y_train)

# -------------------------------------------------------
# Prediction
# -------------------------------------------------------

y_pred = model.predict(X_test)

# -------------------------------------------------------
# Evaluation
# -------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")

print("=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")
print()

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

print("=" * 60)

print("\nClassification Report\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, y_pred))

# -------------------------------------------------------
# Save Models
# -------------------------------------------------------

joblib.dump(model, MODEL_PATH / "svm_model.pkl")
joblib.dump(scaler, MODEL_PATH / "scaler.pkl")
joblib.dump(label_encoder, MODEL_PATH / "label_encoder.pkl")

print("\nModels saved successfully!")