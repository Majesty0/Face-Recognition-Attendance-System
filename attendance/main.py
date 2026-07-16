import tkinter as tk
from tkinter import ttk
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
SRC = PROJECT_ROOT / "src"


def run_script(script_name):
    subprocess.Popen(
        ["python", str(SRC / script_name)],
        cwd=PROJECT_ROOT
    )


root = tk.Tk()

root.title("Face Recognition Attendance System")
root.geometry("650x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="FACE RECOGNITION ATTENDANCE SYSTEM",
    font=("Arial", 18, "bold")
)

title.pack(pady=20)

ttk.Button(
    root,
    text="Register Student",
    command=lambda: run_script("07_register_student.py"),
    width=35
).pack(pady=10)

ttk.Button(
    root,
    text="Train Custom Model",
    command=lambda: run_script("10_train_custom_model.py"),
    width=35
).pack(pady=10)

ttk.Button(
    root,
    text="Start Attendance",
    command=lambda: run_script("11_face_recognition_attendance.py"),
    width=35
).pack(pady=10)

ttk.Button(
    root,
    text="Exit",
    command=root.destroy,
    width=35
).pack(pady=20)

root.mainloop()