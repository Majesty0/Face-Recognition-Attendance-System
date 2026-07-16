import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

from theme import *

def register_page(parent):

    frame = tk.Frame(parent, bg=BACKGROUND)

    tk.Label(
        frame,
        text="Register New Student",
        font=TITLE_FONT,
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    form = tk.Frame(frame, bg=BACKGROUND)
    form.pack(pady=20)

    # -----------------------------
    # Student ID
    # -----------------------------
    tk.Label(
        form,
        text="Student ID",
        bg=BACKGROUND,
        font=TEXT_FONT
    ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

    student_id = tk.Entry(form, width=30)
    student_id.grid(row=0, column=1)

    # -----------------------------
    # Student Name
    # -----------------------------
    tk.Label(
        form,
        text="Student Name",
        bg=BACKGROUND,
        font=TEXT_FONT
    ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

    student_name = tk.Entry(form, width=30)
    student_name.grid(row=1, column=1)

    # -----------------------------
    # Progress Bar
    # -----------------------------
    progress = ttk.Progressbar(
        frame,
        length=400,
        mode="determinate"
    )

    progress.pack(pady=20)

    progress["value"] = 0

    status = tk.Label(
        frame,
        text="Ready to capture images.",
        bg=BACKGROUND,
        fg=TEXT_LIGHT,
        font=TEXT_FONT
    )

    status.pack()

    # -----------------------------
    # Capture Function
    # -----------------------------
    def capture():

        sid = student_id.get().strip()
        sname = student_name.get().strip()

        if sid == "" or sname == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter Student ID and Student Name."
            )
            return
        import subprocess
        from pathlib import Path
        PROJECT_ROOT = Path(__file__).resolve().parent.parent
        subprocess.run([
    "python",
    str(PROJECT_ROOT / "src" / "07_register_student.py"),
    sid,
    sname
])
    messagebox.showinfo(
    "Success",
    "Student registered successfully!"
)

    ttk.Button(
        frame,
        text="Capture Images",
        command=capture,
        width=30
    ).pack(pady=20)

    return frame