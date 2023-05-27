from tkinter import *


class Drag:

    # The only arguments you have to pass are the widget you want the drag on to apply to

    def __init__(self, root: Tk, widget):
        self.root = root
        self.widget = widget
        self.widget.bind("<ButtonPress-1>", self.start_drag)
        self.widget.bind("<B1-Motion>", self.drag)

    def start_drag(self, event):
        global last_x, last_y
        last_x = event.x_root
        last_y = event.y_root

    def drag(self, event):
        global last_x, last_y
        x = self.root.winfo_x() + (event.x_root - last_x)
        y = self.root.winfo_y() + (event.y_root - last_y)
        self.root.geometry(f"+{x}+{y}")
        last_x = event.x_root
        last_y = event.y_root
