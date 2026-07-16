import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import subprocess
import threading

from theme import *

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def train_page(parent):

    frame = tk.Frame(parent, bg=BACKGROUND)

    tk.Label(
        frame,
        text="Train Face Recognition Model",
        font=TITLE_FONT,
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    status = tk.Label(
        frame,
        text="Model not trained.",
        font=TEXT_FONT,
        bg=BACKGROUND,
        fg=TEXT_LIGHT
    )
    status.pack(pady=10)

    progress = ttk.Progressbar(
        frame,
        length=500,
        mode="indeterminate"
    )
    progress.pack(pady=20)

    def train_model():

        progress.start(10)
        status.config(text="Training model... Please wait.")

        try:

            subprocess.run(
                ["python", str(PROJECT_ROOT / "src" / "10_train_custom_model.py")],
                cwd=PROJECT_ROOT,
                check=True
            )

            status.config(text="Training completed successfully!")

            messagebox.showinfo(
                "Success",
                "Model trained successfully!"
            )

        except Exception as e:

            messagebox.showerror(
                "Training Error",
                str(e)
            )

            status.config(text="Training failed.")

        progress.stop()

    ttk.Button(
        frame,
        text="Train Model",
        width=25,
        command=lambda: threading.Thread(
            target=train_model,
            daemon=True
        ).start()
    ).pack(pady=20)

    return frame