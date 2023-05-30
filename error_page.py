from tkinter import *


def show_error(frame: LabelFrame, get_code: str):
    error_label = Label(frame, text=get_code)
    return error_label

