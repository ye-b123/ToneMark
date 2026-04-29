# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from Data.twiWords import googleTranslate

def build_tab(tab):
    tk.Label(
        tab,
        text="Google Translate Failures",
        font=("Baskerville Old Face", 14, "bold"),
        pady=10
    ).pack()

    tk.Label(
        tab,
        text="Real examples where missing tone marks cause mistranslation",
        font=("Baskerville Old Face", 10),
        fg="gray"
    ).pack()

    outer_frame = tk.Frame(tab)
    outer_frame.pack(fill="both", expand=True, padx=20, pady=10)

    canvas = tk.Canvas(outer_frame)
    scrollbar = tk.Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    inner_frame = tk.Frame(canvas)
    canvas_window = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    def update_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(canvas_window, width=canvas.winfo_width())

    inner_frame.bind("<Configure>", update_scroll)
    canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas_window, width=e.width))

    for example in googleTranslate:
        card = tk.Frame(inner_frame, relief="groove", bd=2, padx=15, pady=15, bg="white")
        card.pack(fill="x", pady=10, padx=10)

        tk.Label(
            card,
            text=f"Twi input (no tone marks):  {example['input']}",
            font=("Baskerville Old Face", 12, "bold"),
            anchor="w",
            bg="white"
        ).pack(fill="x")

        tk.Label(
            card,
            text=f"❌  GoogleTranslateOutput:  {example['googleTranslateOutput']}",
            font=("Baskerville Old Face", 11),
            fg="red",
            anchor="w",
            bg="white"
        ).pack(fill="x", pady=3)

        tk.Label(
            card,
            text="✓  Correct translations with tone marks:",
            font=("Baskerville Old Face", 11),
            fg="green",
            anchor="w",
            bg="white"
        ).pack(fill="x")

        for correct in example["correctTranslations"]:
            tk.Label(
                card,
                text=f"      • {correct}",
                font=("Baskerville Old Face", 10),
                fg="green",
                anchor="w",
                bg="white"
            ).pack(fill="x")

        tk.Label(
            card,
            text=f"\n{example['explanation']}",
            font=("Arial", 10),
            fg="#555555",
            wraplength=600,
            justify="left",
            anchor="w",
            bg="white"
        ).pack(fill="x", pady=5)