from tkinter import *


def remove_items(widget: LabelFrame):
    for wid in widget.winfo_children():
        wid.destroy()

