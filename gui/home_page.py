from pathlib import Path
from datetime import datetime
import tkinter as tk
from tkinter import ttk

import pandas as pd
from PIL import Image, ImageTk


# ==========================================================
# COLORS
# (Delete these if you already import them from theme.py)
# ==========================================================

BACKGROUND = "#F4F6F9"
PRIMARY = "#1565C0"
TEXT = "#1E1E1E"
TEXT_LIGHT = "#757575"

HEADER_FONT = ("Segoe UI", 13, "bold")


# ==========================================================
# HOME PAGE
# ==========================================================

def home_page(parent):

    frame = tk.Frame(parent, bg=BACKGROUND)

    project = Path(__file__).resolve().parent.parent

    assets = project / "assets"
    data_folder = project / "data"
    dataset_folder = project / "dataset" / "custom"
    models_folder = project / "models"

    # =====================================================
    # TOP BAR
    # =====================================================

    top = tk.Frame(frame, bg=BACKGROUND)
    top.pack(fill="x", padx=20, pady=20)

    # -----------------------------------------------------

    try:
        logo = Image.open(assets / "logo.png")
        logo = logo.resize((90, 90))
        logo = ImageTk.PhotoImage(logo)

        lbl = tk.Label(top, image=logo, bg=BACKGROUND)
        lbl.image = logo
        lbl.pack(side="left")

    except Exception:
        tk.Label(
            top,
            text="LOGO",
            bg=BACKGROUND,
            fg=PRIMARY,
            font=("Segoe UI", 14, "bold")
        ).pack(side="left")

    # -----------------------------------------------------

    try:
        usiu = Image.open(assets / "usiu_logo.png")
        usiu = usiu.resize((120, 100))
        usiu = ImageTk.PhotoImage(usiu)

        lbl = tk.Label(top, image=usiu, bg=BACKGROUND)
        lbl.image = usiu
        lbl.pack(side="right")

    except Exception:
        tk.Label(
            top,
            text="USIU",
            bg=BACKGROUND,
            fg=PRIMARY,
            font=("Segoe UI", 14, "bold")
        ).pack(side="right")

    # =====================================================
    # TITLE
    # =====================================================

    tk.Label(
        frame,
        text="Face Recognition Attendance System",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Segoe UI", 24, "bold")
    ).pack()

    # =====================================================
    # CLOCK
    # =====================================================

    clock = tk.Label(
        frame,
        bg=BACKGROUND,
        fg=PRIMARY,
        font=("Segoe UI", 12, "bold")
    )

    clock.pack(pady=10)

    def update_clock():
        clock.config(
            text=datetime.now().strftime(
                "%A | %d %B %Y | %H:%M:%S"
            )
        )

        frame.after(1000, update_clock)

    update_clock()

    # =====================================================
    # STUDENTS
    # =====================================================

    student_file = data_folder / "students.csv"

    if student_file.exists():

        try:
            students = len(pd.read_csv(student_file))
        except Exception:
            students = 0

    else:
        students = 0

    # =====================================================
    # ATTENDANCE
    # =====================================================

    attendance_file = data_folder / "attendance.xlsx"

    attendance = 0

    if attendance_file.exists():

        try:

            df = pd.read_excel(attendance_file)

            if "Date" in df.columns:

                today = datetime.now().strftime("%Y-%m-%d")

                attendance = len(
                    df[df["Date"].astype(str) == today]
                )

            else:
                attendance = len(df)

        except Exception:
            attendance = 0

    # =====================================================
    # DATASET IMAGES
    # =====================================================

    if dataset_folder.exists():

        images = len(list(dataset_folder.rglob("*.jpg")))

    else:

        images = 0

    # =====================================================
    # MODEL STATUS
    # =====================================================

    model_file = models_folder / "custom_svm_model.pkl"

    if model_file.exists():
        model_status = "Available"
    else:
        model_status = "Not Trained"

    # =====================================================
    # DASHBOARD CARDS
    # =====================================================

    cards = tk.Frame(frame, bg=BACKGROUND)
    cards.pack(pady=30)

    dashboard = [

        ("Students", students),

        ("Today's Attendance", attendance),

        ("Dataset Images", images),

        ("Model", model_status)

    ]

    for column, (title, value) in enumerate(dashboard):

        card = tk.Frame(
            cards,
            bg="white",
            width=230,
            height=150,
            relief="raised",
            bd=2
        )

        card.grid(row=0, column=column, padx=15)

        card.pack_propagate(False)

        tk.Label(
            card,
            text=title,
            bg="white",
            fg=TEXT_LIGHT,
            font=HEADER_FONT
        ).pack(pady=(18, 5))

        tk.Label(
            card,
            text=str(value),
            bg="white",
            fg=PRIMARY,
            font=("Segoe UI", 24, "bold")
        ).pack()

    # =====================================================
    # REFRESH
    # =====================================================

    def refresh():

        frame.destroy()

        new_page = home_page(parent)

        new_page.pack(fill="both", expand=True)

    ttk.Button(
        frame,
        text="Refresh Dashboard",
        command=refresh,
        width=25
    ).pack(pady=20)

    # =====================================================
    # FOOTER
    # =====================================================

    tk.Label(
        frame,
        text="Developed for DSA4050 Computer Vision Project",
        bg=BACKGROUND,
        fg=TEXT_LIGHT,
        font=("Segoe UI", 10, "italic")
    ).pack(side="bottom", pady=15)

    return frame