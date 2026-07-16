import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import json

from theme import *

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = PROJECT_ROOT / "config.json"


def settings_page(parent):

    frame = tk.Frame(parent, bg=BACKGROUND)

    tk.Label(
        frame,
        text="System Settings",
        font=TITLE_FONT,
        bg=BACKGROUND,
        fg=TEXT
    ).pack(pady=20)

    form = tk.Frame(frame, bg=BACKGROUND)
    form.pack(pady=20)

    # -----------------------------
    # Camera Index
    # -----------------------------

    tk.Label(
        form,
        text="Camera Index",
        bg=BACKGROUND,
        font=TEXT_FONT
    ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

    camera = tk.IntVar(value=0)

    ttk.Combobox(
        form,
        textvariable=camera,
        values=[0, 1, 2],
        width=25,
        state="readonly"
    ).grid(row=0, column=1, padx=10)

    # -----------------------------
    # Confidence Threshold
    # -----------------------------

    tk.Label(
        form,
        text="Recognition Confidence",
        bg=BACKGROUND,
        font=TEXT_FONT
    ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

    confidence = tk.DoubleVar(value=0.85)

    ttk.Scale(
        form,
        variable=confidence,
        from_=0.50,
        to=1.00,
        orient="horizontal",
        length=250
    ).grid(row=1, column=1, padx=10)

    confidence_label = tk.Label(
        form,
        text="0.85",
        bg=BACKGROUND,
        font=TEXT_FONT
    )

    confidence_label.grid(row=1, column=2)

    def update_confidence(value):
        confidence_label.config(text=f"{float(value):.2f}")

    confidence.trace_add(
        "write",
        lambda *args: update_confidence(confidence.get())
    )

    # -----------------------------
    # Theme
    # -----------------------------

    tk.Label(
        form,
        text="Theme",
        bg=BACKGROUND,
        font=TEXT_FONT
    ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

    theme = tk.StringVar(value="Light")

    ttk.Combobox(
        form,
        textvariable=theme,
        values=["Light", "Dark"],
        width=25,
        state="readonly"
    ).grid(row=2, column=1)

    # -----------------------------
    # Save Settings
    # -----------------------------

    def save_settings():

        settings = {

            "camera_index": camera.get(),
            "confidence": round(confidence.get(), 2),
            "theme": theme.get()

        }

        with open(CONFIG_FILE, "w") as f:
            json.dump(settings, f, indent=4)

        messagebox.showinfo(
            "Success",
            "Settings saved successfully."
        )

    # -----------------------------
    # Load Settings
    # -----------------------------

    if CONFIG_FILE.exists():

        with open(CONFIG_FILE) as f:

            settings = json.load(f)

            camera.set(settings.get("camera_index", 0))
            confidence.set(settings.get("confidence", 0.85))
            theme.set(settings.get("theme", "Light"))

    # -----------------------------
    # Reset
    # -----------------------------

    def reset():

        camera.set(0)
        confidence.set(0.85)
        theme.set("Light")

    buttons = tk.Frame(frame, bg=BACKGROUND)
    buttons.pack(pady=30)

    ttk.Button(
        buttons,
        text="Save Settings",
        width=20,
        command=save_settings
    ).grid(row=0, column=0, padx=10)

    ttk.Button(
        buttons,
        text="Reset",
        width=20,
        command=reset
    ).grid(row=0, column=1, padx=10)

    return frame