from tkinter import *


class Drag:

    # The only arguments you have to pass are the widget you want the drag on to apply to

    def __init__(self, root: Tk, widget):
        self.root = root
        self.widget = widget
        self.widget.bind("<ButtonPress-1>", self.start_drag)
        self.widget.bind("<B1-Motion>", self.drag)
        self.last_x = None
        self.last_y = None

    def start_drag(self, event):
        self.last_x = event.x_root
        self.last_y = event.y_root

    def drag(self, event):
        x = self.root.winfo_x() + (event.x_root - self.last_x)
        y = self.root.winfo_y() + (event.y_root - self.last_y)
        self.root.geometry(f"+{x}+{y}")
        self.last_x = event.x_root
        self.last_y = event.y_root
