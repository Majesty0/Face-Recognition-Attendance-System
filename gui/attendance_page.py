import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import subprocess
import threading

from theme import *

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def attendance_page(parent):

    frame = tk.Frame(parent, bg=BACKGROUND)

    tk.Label(
        frame,
        text="Live Face Recognition Attendance",
        font=TITLE_FONT,
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    status = tk.Label(
        frame,
        text="System Ready",
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

    def start_attendance():

        progress.start(10)
        status.config(text="Opening camera...")

        try:
            script = PROJECT_ROOT / "src" / "11_face_recognition_attendance.py"

            print("PROJECT_ROOT =", PROJECT_ROOT)
            print("SCRIPT =", script)
            print("EXISTS =", script.exists())
            subprocess.run(
                [
                    "python",
                    str(PROJECT_ROOT / "src" / "11_face_recognition_attendance.py")
                ],
                cwd=PROJECT_ROOT,
                check=True
            )

            status.config(text="Attendance completed.")

        except Exception as e:

            messagebox.showerror(
                "Attendance Error",
                str(e)
            )

            status.config(text="Attendance failed.")

        progress.stop()

    ttk.Button(
        frame,
        text="Start Attendance",
        width=30,
        command=lambda: threading.Thread(
            target=start_attendance,
            daemon=True
        ).start()
    ).pack(pady=20)

    return frame