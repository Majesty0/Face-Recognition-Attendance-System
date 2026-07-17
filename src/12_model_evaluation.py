"""
=========================================================
DSA4050 COMPUTER VISION PROJECT
Module 06 - Model Evaluation & Visualization (Enhanced)
=========================================================
"""
from common import *
import time
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, ConfusionMatrixDisplay,
    classification_report
)

FEATURE_PATH = PROJECT_ROOT / "data" / "custom_features"
MODEL_PATH = PROJECT_ROOT / "models"
REPORT_PATH = PROJECT_ROOT / "reports"
FIGURE_PATH = REPORT_PATH / "figures"

REPORT_PATH.mkdir(parents=True, exist_ok=True)
FIGURE_PATH.mkdir(parents=True, exist_ok=True)

X = np.load(FEATURE_PATH / "X.npy")
y = np.load(FEATURE_PATH / "y.npy")

encoder = joblib.load(MODEL_PATH / "custom_label_encoder.pkl")
scaler = joblib.load(MODEL_PATH / "custom_scaler.pkl")
model = joblib.load(MODEL_PATH / "custom_svm_model.pkl")

y = encoder.transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

X_test = scaler.transform(X_test)

start = time.perf_counter()
y_pred = model.predict(X_test)
elapsed = time.perf_counter() - start

probs = None
avg_conf = None
if hasattr(model, "predict_proba"):
    probs = model.predict_proba(X_test)
    avg_conf = float(np.mean(np.max(probs, axis=1)))

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted", zero_division=0)
recall = recall_score(y_test, y_pred, average="weighted", zero_division=0)
f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)

cm = confusion_matrix(y_test, y_pred)

FP = (cm.sum(axis=0) - np.diag(cm)).astype(float)
FN = (cm.sum(axis=1) - np.diag(cm)).astype(float)
TP = np.diag(cm).astype(float)
TN = cm.sum() - (FP + FN + TP)

fpr = np.mean(np.divide(FP, FP + TN, out=np.zeros_like(FP), where=(FP+TN)!=0))
fnr = np.mean(np.divide(FN, FN + TP, out=np.zeros_like(FN), where=(FN+TP)!=0))
specificity = np.mean(np.divide(TN, TN + FP, out=np.zeros_like(TN), where=(TN+FP)!=0))

avg_time = elapsed / len(X_test)

plt.figure(figsize=(8,5))
metrics=["Accuracy","Precision","Recall","F1","Specificity"]
values=[accuracy,precision,recall,f1,specificity]
plt.bar(metrics,values)
plt.ylim(0,1.05)
for i,v in enumerate(values):
    plt.text(i,v+0.02,f"{v:.3f}",ha="center")
plt.tight_layout()
plt.savefig(FIGURE_PATH/"model_performance.png",dpi=300)
plt.close()

fig,ax=plt.subplots(figsize=(10,10))
ConfusionMatrixDisplay(cm).plot(ax=ax,colorbar=False,xticks_rotation=90)
plt.tight_layout()
plt.savefig(FIGURE_PATH/"confusion_matrix.png",dpi=300)
plt.close()

report = classification_report(y_test,y_pred)

with open(REPORT_PATH/"evaluation_report.txt","w") as f:
    f.write("MODEL EVALUATION REPORT\n")
    f.write("="*50+"\n")
    f.write(f"Accuracy            : {accuracy:.4f}\n")
    f.write(f"Precision           : {precision:.4f}\n")
    f.write(f"Recall              : {recall:.4f}\n")
    f.write(f"F1 Score            : {f1:.4f}\n")
    f.write(f"False Positive Rate : {fpr:.4f}\n")
    f.write(f"False Negative Rate : {fnr:.4f}\n")
    f.write(f"Specificity         : {specificity:.4f}\n")
    if avg_conf is not None:
        f.write(f"Avg Confidence      : {avg_conf:.4f}\n")
    f.write(f"Total Eval Time (s) : {elapsed:.6f}\n")
    f.write(f"Avg Time/Image (s)  : {avg_time:.6f}\n\n")
    f.write(report)

print("="*60)
print("MODEL EVALUATION COMPLETE")
print("="*60)
print(f"Accuracy            : {accuracy:.4f}")
print(f"Precision           : {precision:.4f}")
print(f"Recall              : {recall:.4f}")
print(f"F1 Score            : {f1:.4f}")
print(f"False Positive Rate : {fpr:.4f}")
print(f"False Negative Rate : {fnr:.4f}")
print(f"Specificity         : {specificity:.4f}")
if avg_conf is not None:
    print(f"Avg Confidence      : {avg_conf:.4f}")
print(f"Total Eval Time (s) : {elapsed:.6f}")
print(f"Avg Time/Image (s)  : {avg_time:.6f}")
print("="*60)
