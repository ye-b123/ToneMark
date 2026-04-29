# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import tkinter as tk
from Data.twiWords import tonePairs

def build_tab(tab):
    tk.Label(
        tab,
        text="Twi Tonal Minimal Pairs",
        font=("Baskerville Old Face", 14, "bold"),
        pady=10
    ).pack()

    tk.Label(
        tab,
        text="Select a word to see how tone changes its meaning",
        font=("Baskerville Old Face", 10),
        fg="gray"
    ).pack()

    main_frame = tk.Frame(tab)
    main_frame.pack(fill="both", expand=True, padx=20, pady=10)

    button_frame = tk.Frame(main_frame)
    button_frame.pack(side="left", fill="y", padx=10)

    tk.Label(
        button_frame,
        text="Choose a word:",
        font=("Baskerville Old Face", 11, "bold")
    ).pack(pady=5)

    result_frame = tk.Frame(main_frame, relief="groove", bd=2)
    result_frame.pack(side="left", fill="both", expand=True, padx=10)

    result_text = tk.Text(
        result_frame,
        font=("Baskerville Old Face", 11),
        wrap="word",
        state="disabled",
        bg="#ceddec",
        padx=15,
        pady=15
    )
    result_text.pack(fill="both", expand=True)

    def show_word(word):
        entry = tonePairs[word]
        result_text.config(state="normal")
        result_text.delete("1.0", "end")

        result_text.insert("end", f"Word (no tone marks): {word.upper()}\n\n")
        result_text.insert("end", f"{entry['description']}\n")
        result_text.insert("end", f"Category: {entry['category']}\n\n")
        result_text.insert("end", "─" * 40 + "\n\n")
        result_text.insert("end", "Tonal Variants:\n\n")

        for variant in entry["variants"]:
            result_text.insert("end", f"  {variant['form']}")
            result_text.insert("end", f"  ({variant['tone_pattern']} tone)\n")
            result_text.insert("end", f"  Meaning: {variant['meaning']}\n\n")

        result_text.insert("end", "─" * 40 + "\n\n")
        result_text.insert("end", "⚠ Without tone marks, an NLP model sees only:\n")
        result_text.insert("end", f'  "{word}" — and cannot determine which meaning is intended.\n')

        result_text.config(state="disabled")

    for word in tonePairs:
        tk.Button(
            button_frame,
            text=word,
            font=("Baskerville Old Face", 11),
            width=10,
            command=lambda w=word: show_word(w)
        ).pack(pady=4)