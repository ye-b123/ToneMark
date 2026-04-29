# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from Data.twiWords import nlpComparison

def build_tab(tab):
    tk.Label(
        tab,
        text="NLP Model Comparison",
        font=("Baskerville Old Face", 14, "bold"),
        pady=10
    ).pack()

    tk.Label(
        tab,
        text="See how tone marks affect NLP model predictions",
        font=("Baskerville Old Face", 10),
        fg="gray"
    ).pack()
    
    tk.Label(
        tab,
        text="Note: Confidence scores are illustrative estimates based on known NLP model behavior on low-resource tonal languages.",
        font=("Baskerville Old Face", 9, "italic"),
        fg="#888888",
        wraplength=700
    ).pack()

    # Button frame at top
    button_frame = tk.Frame(tab)
    button_frame.pack(pady=10)

    tk.Label(
        button_frame,
        text="Choose a word:",
        font=("Baskerville Old Face", 11, "bold")
    ).pack(side="left", padx=10)

    # Results area
    results_frame = tk.Frame(tab)
    results_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Left panel — with tone marks
    left_panel = tk.Frame(results_frame, relief="groove", bd=2, bg="#e8f5e9", padx=15, pady=15)
    left_panel.pack(side="left", fill="both", expand=True, padx=5)

    tk.Label(
        left_panel,
        text="✅  With Tone Marks",
        font=("Baskerville Old Face", 12, "bold"),
        fg="green",
        bg="#e8f5e9"
    ).pack(pady=5)

    left_input = tk.Label(left_panel, text="", font=("Arial", 24, "bold"), bg="#e8f5e9", fg="#2e7d32")
    left_input.pack(pady=5)

    left_prediction = tk.Label(left_panel, text="", font=("Arial", 12), bg="#e8f5e9")
    left_prediction.pack(pady=3)

    left_confidence = tk.Label(left_panel, text="", font=("Arial", 11), bg="#e8f5e9", fg="#2e7d32")
    left_confidence.pack(pady=3)

    left_bar = tk.Canvas(left_panel, height=20, bg="#e8f5e9", highlightthickness=0)
    left_bar.pack(fill="x", pady=5)

    left_explanation = tk.Label(
        left_panel, text="", font=("Arial", 10),
        bg="#e8f5e9", fg="#555555",
        wraplength=250, justify="left"
    )
    left_explanation.pack(pady=5)

    # Right panel  without tone marks
    right_panel = tk.Frame(results_frame, relief="groove", bd=2, bg="#ffebee", padx=15, pady=15)
    right_panel.pack(side="left", fill="both", expand=True, padx=5)

    tk.Label(
        right_panel,
        text="❌  Without Tone Marks",
        font=("Baskerville Old Face", 12, "bold"),
        fg="red",
        bg="#ffebee"
    ).pack(pady=5)

    right_input = tk.Label(right_panel, text="", font=("Arial", 24, "bold"), bg="#ffebee", fg="#c62828")
    right_input.pack(pady=5)

    right_prediction = tk.Label(right_panel, text="", font=("Arial", 12), bg="#ffebee")
    right_prediction.pack(pady=3)

    right_confidence = tk.Label(right_panel, text="", font=("Arial", 11), bg="#ffebee", fg="#c62828")
    right_confidence.pack(pady=3)

    right_bar = tk.Canvas(right_panel, height=20, bg="#ffebee", highlightthickness=0)
    right_bar.pack(fill="x", pady=5)

    right_explanation = tk.Label(
        right_panel, text="", font=("Arial", 10),
        bg="#ffebee", fg="#555555",
        wraplength=250, justify="left"
    )
    right_explanation.pack(pady=5)

    def draw_bar(canvas, percentage, color):
        canvas.delete("all")
        canvas.update()
        width = canvas.winfo_width()
        filled = int(width * percentage / 100)
        canvas.create_rectangle(0, 0, width, 20, fill="#dddddd", outline="")
        canvas.create_rectangle(0, 0, filled, 20, fill=color, outline="")
        canvas.create_text(width // 2, 10, text=f"{percentage}%", font=("Arial", 9, "bold"), fill="white")

    def show_comparison(example):
        w = example["with_tone"]
        wo = example["without_tone"]

        left_input.config(text=w["input"])
        left_prediction.config(text=f"Prediction: {w['prediction']}")
        left_confidence.config(text=f"Confidence: {w['confidence']}%")
        left_explanation.config(text=w["explanation"])
        tab.after(100, lambda: draw_bar(left_bar, w["confidence"], "#43a047"))

        right_input.config(text=wo["input"])
        right_prediction.config(text=f"Prediction: {wo['prediction']}")
        right_confidence.config(text=f"Confidence: {wo['confidence']}%")
        right_explanation.config(text=wo["explanation"])
        tab.after(100, lambda: draw_bar(right_bar, wo["confidence"], "#e53935"))

    # Create buttons
    for example in nlpComparison:
        tk.Button(
            button_frame,
            text=example["word"],
            font=("Baskerville Old Face", 11),
            width=8,
            command=lambda e=example: show_comparison(e)
        ).pack(side="left", padx=5)
        
    if nlpComparison:
        show_comparison(nlpComparison[0])