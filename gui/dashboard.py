import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path
from theme import *

from home_page import home_page
from register_page import register_page
from train_page import train_page
from attendance_page import attendance_page
from records_page import records_page
from settings_page import settings_page

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

root = tk.Tk()

PROJECT_ROOT = Path(__file__).resolve().parent.parent

icon = PROJECT_ROOT / "assets" / "icon.ico"

if icon.exists():
    root.iconbitmap(icon)

root.title("Face Recognition Attendance System - DSA4050")
root.geometry("1400x800")
root.configure(bg=BACKGROUND)


# ======================================================
# SIDEBAR
# ======================================================

sidebar = tk.Frame(root, bg=PRIMARY, width=SIDEBAR_WIDTH)
sidebar.pack(side="left", fill="y")


# ======================================================
# MAIN CONTENT
# ======================================================

content = tk.Frame(root, bg=BACKGROUND)
content.pack(side="right", fill="both", expand=True)


def clear_content():

    for widget in content.winfo_children():
        widget.destroy()


def show(page):

    clear_content()

    frame = page(content)
    frame.pack(fill="both", expand=True)


# ======================================================
# TITLE
# ======================================================

tk.Label(
    sidebar,
    text="Face Recognition\nAttendance System",
    bg=PRIMARY,
    fg="white",
    font=("Segoe UI", 24, "bold")
).pack(pady=30)

def exit_app():

    if messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit?"
    ):
        root.destroy()
# ======================================================
# BUTTONS
# ======================================================

buttons = [

    ("🏠 Dashboard", home_page),

    ("👤 Register Student", register_page),

    ("🎓 Train Model", train_page),

    ("📷 Attendance", attendance_page),

    ("📄 Records", records_page),

    ("⚙ Settings", settings_page)

]

for text, page in buttons:

    ttk.Button(

        sidebar,

        text=text,

        width=25,

        command=lambda p=page: show(p)

    ).pack(pady=8)


ttk.Button(

    sidebar,

    text="🚪 Exit",

    width=25,

    command=exit_app

).pack(side="bottom", pady=20)


tk.Label(
    sidebar,
    text="Version 1.0\nUSIU-Africa",
    bg=PRIMARY,
    fg="white",
    font=("Segoe UI",9)
).pack(side="bottom", pady=60)
# Load Dashboard first
show(home_page)

root.mainloop()