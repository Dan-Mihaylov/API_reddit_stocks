from tkinter import *
import os
import json


def show_error(frame: LabelFrame, get_code: str):
    error_label = Label(frame, text=get_code)
    return error_label


def clear_temp_close_program(folder: str, root: Tk):
    for file_name in os.listdir(folder):
        file = os.path.join(folder, file_name)
        os.remove(file)

    root.destroy()


def update_json(some_json: list):

    dump_data = json.dumps(some_json)

    with open("log/data.json", "w") as file:
        file.write(dump_data)


def load_json():

    with open("log/data.json", "r") as file:
        file_data = file.read()
        
    the_json_data = json.loads(file_data)

    return the_json_data


MY_KEY = "f8914e2e95915c184becb76c2ead4546"
bg_color = "#1d2129"
fg_color = "#cccccc"
