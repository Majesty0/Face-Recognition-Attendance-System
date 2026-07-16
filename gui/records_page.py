import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import pandas as pd

from theme import *

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def records_page(parent):

    frame = tk.Frame(parent, bg=BACKGROUND)

    tk.Label(
        frame,
        text="Attendance Records",
        font=TITLE_FONT,
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    attendance_file = PROJECT_ROOT / "attendance" / "Attendance.xlsx"

    # -------------------------
    # Search Bar
    # -------------------------

    search_frame = tk.Frame(frame, bg=BACKGROUND)
    search_frame.pack(fill="x", padx=20)

    tk.Label(
        search_frame,
        text="Search:",
        bg=BACKGROUND,
        font=TEXT_FONT
    ).pack(side="left")

    search_var = tk.StringVar()

    search_entry = ttk.Entry(
        search_frame,
        textvariable=search_var,
        width=40
    )

    search_entry.pack(side="left", padx=10)

    # -------------------------
    # Table
    # -------------------------

    columns = ("Student ID", "Student Name", "Date", "Time")

    tree = ttk.Treeview(
        frame,
        columns=columns,
        show="headings",
        height=18
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=180)

    scrollbar = ttk.Scrollbar(
        frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side="left", padx=(20, 0), pady=20, fill="both", expand=True)
    scrollbar.pack(side="right", pady=20, fill="y")

    # -------------------------
    # Load Records
    # -------------------------

    def load_records():

        tree.delete(*tree.get_children())

        if not attendance_file.exists():
            return

        df = pd.read_excel(attendance_file)

        keyword = search_var.get().strip().lower()

        if keyword != "":
            df = df[
                df.astype(str)
                  .apply(lambda x: x.str.lower())
                  .apply(lambda x: x.str.contains(keyword))
                  .any(axis=1)
            ]

        for _, row in df.iterrows():
            tree.insert("", "end", values=list(row))

        total.config(text=f"Total Records : {len(df)}")

    # -------------------------
    # Buttons
    # -------------------------

    btn_frame = tk.Frame(frame, bg=BACKGROUND)
    btn_frame.pack(pady=10)

    ttk.Button(
        btn_frame,
        text="Search",
        width=15,
        command=load_records
    ).grid(row=0, column=0, padx=5)

    ttk.Button(
        btn_frame,
        text="Refresh",
        width=15,
        command=lambda: [search_var.set(""), load_records()]
    ).grid(row=0, column=1, padx=5)

    def export_excel():

        if attendance_file.exists():
            messagebox.showinfo(
                "Export",
                f"Records already stored in:\n\n{attendance_file}"
            )
        else:
            messagebox.showwarning(
                "No Records",
                "Attendance file not found."
            )

    ttk.Button(
        btn_frame,
        text="Export",
        width=15,
        command=export_excel
    ).grid(row=0, column=2, padx=5)

    total = tk.Label(
        frame,
        text="Total Records : 0",
        bg=BACKGROUND,
        fg=PRIMARY,
        font=("Segoe UI", 11, "bold")
    )

    total.pack(pady=10)

    load_records()

    return frame