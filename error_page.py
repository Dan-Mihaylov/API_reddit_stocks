from tkinter import *


def show_error(root: Tk, get_code: str):
    error_label = Label(root, text=get_code)
    return error_label

