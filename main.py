# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from Sections.tonePairs import build_tab as build_tonePairs
from Sections.googleTranslate import build_tab as build_googleTranslate
from Sections.nlpComparison import build_tab as build_nlpComparison

app = tk.Tk()
app.title("ToneMark")
app.geometry("800x600")

tk.Label(
    app,
    text="ToneMark: Visualizing Tonal Ambiguity in Twi NLP",
    font=("Baskerville Old Face", 16, "bold"),
    wraplength=700,
    pady=20
).pack()

tk.Label(
    app,
    text="A demonstration tool showing how missing tone marks affect NLP models",
    font=("Baskerville Old Face", 11),
    fg="gray"
).pack()

tabs = ttk.Notebook(app)
tabs.pack(expand=True, fill="both", padx=20, pady=10)

tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tab3 = ttk.Frame(tabs)

tabs.add(tab1, text="Tonal Pairs")
tabs.add(tab2, text="Google Translate Failures")
tabs.add(tab3, text="NLP Model Comparison")

build_tonePairs(tab1)

build_googleTranslate(tab2)

build_nlpComparison(tab3)


app.mainloop()




