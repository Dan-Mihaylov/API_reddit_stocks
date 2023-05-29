import error_page
from get_reddit_stocks import GetInfo
from tkinter import *
from click_and_drag import Drag
from diplay_results import Display
from clear_screen import remove_items



root = Tk()
root.geometry("400x600+200+200")
root.overrideredirect(True)

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
    command=root.destroy,
    width=4,
    height=2,
)

exit_button.pack(anchor="e", pady=5, padx=10)


app_frame = LabelFrame(root)
app_frame.pack(expand=True, fill="both")

# Create a dragging option when click and drag on the top frame

set_drag = Drag(root, windows_buttons_frame)

# Connect to the API and store the info in a JSON dict.

reddit_stocks = GetInfo("https://tradestie.com/api/v1/apps/reddit")


def start_button():
    remove_items(app_frame)

    try:
        reddit_stocks.retrieve_info_as_json()
        print(reddit_stocks.get_info())

        # Display the result into the app_frame

        displayer = Display(app_frame, reddit_stocks.information)
        displayer.get_next_result()
    except Exception:
        error_label = error_page.show_error(root, reddit_stocks.info_as_text())
        error_label.pack()


start_button = Button(app_frame, text="Start", command=start_button)
start_button.pack()

root.mainloop()

