from tkinter import *
import os


def show_error(frame: LabelFrame, get_code: str):
    error_label = Label(frame, text=get_code)
    return error_label


def clear_temp_close_program(folder: str, root: Tk):
    for file_name in os.listdir(folder):
        file = os.path.join(folder, file_name)
        os.remove(file)

    root.destroy()
