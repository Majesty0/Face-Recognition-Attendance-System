import os
from pathlib import Path
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import joblib

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "dataset" / "ORL"
MODELS_PATH = PROJECT_ROOT / "models"

HAAR_PATH = PROJECT_ROOT / "haarcascade" / "haarcascade_frontalface_default.xml"