from get_reddit_stocks import GetInfo
from tkinter import *
from click_and_drag import Drag
from diplay_results import Display



root = Tk()
root.geometry("400x600+200+200")
root.overrideredirect(True)

windows_buttons_frame = LabelFrame(
    root,
    borderwidth= 0,
)

windows_buttons_frame.columnconfigure(0, weight=3)
windows_buttons_frame.columnconfigure(1, weight=3)
windows_buttons_frame.columnconfigure(2, weight=3)

windows_buttons_frame.pack(fill="x")

title_label = Label(windows_buttons_frame, text="Trending Tickers API", anchor="w")
title_label.grid(row=0, column=0, sticky="w")


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

exit_button.grid(row=0, column=2, sticky="e")


app_frame = LabelFrame(root, borderwidth=0)
app_frame.pack(expand=True, fill="both")

# Connect to the API and store the info in a JSON dict.

reddit_stocks = GetInfo("https://tradestie.com/api/v1/apps/reddit")
reddit_stocks.retrieve_info()
print(reddit_stocks.get_info())

# Create a dragging option when click and drag on the top frame

set_drag = Drag(root, windows_buttons_frame)

# Display the result into the app_frame

displayer = Display(app_frame, reddit_stocks.information)
displayer.get_next_result()


root.mainloop()

