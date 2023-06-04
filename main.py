import helpers
from get_reddit_stocks import GetInfo
from tkinter import *
from click_and_drag import Drag
from diplay_results import Display
from clear_screen import remove_items
import json


root = Tk()
root.geometry("600x800+200+200")
root.overrideredirect(True)

# a frame with the X exit button

windows_buttons_frame = LabelFrame(
    root,
    borderwidth= 0,
)
windows_buttons_frame.pack(fill="x")


exit_button = Button(
    windows_buttons_frame,
    text="X",
    fg="grey",
    activebackground="red",
    borderwidth=0,
    command=lambda: helpers.clear_temp_close_program(f"temp", root),    # Clears the temp folder and closes the window
    width=4,
    height=2,
)

exit_button.pack(anchor="e", pady=5, padx=10)

# This is going to be the main app frame

app_frame = LabelFrame(root, borderwidth=0)
app_frame.pack(expand=True, fill="both")

# Create a dragging option when click and drag on the top frame

set_drag = Drag(root, windows_buttons_frame)

# Connect to the API and store the info in a JSON dict.

reddit_stocks = GetInfo( 'https://tradestie.com/api/v1/apps/reddit?date=2023-04-03')


def start_button():

    remove_items(app_frame)

    try:
        reddit_stocks.retrieve_info_as_json()

        # Display the result into the app_frame
        displayer = Display(app_frame, reddit_stocks.information)
        displayer.get_next_result()

        helpers.update_json(reddit_stocks.information)

    except json.JSONDecodeError:
        error_label = helpers.show_error(app_frame, reddit_stocks.info_as_text())
        error_label.pack()
        the_data = helpers.load_json()
        displayer = Display(app_frame, the_data)
        displayer.get_next_result()


start_button = Button(app_frame, text="Start", command=start_button)
start_button.pack()

root.mainloop()

