from tkinter import *
from collections import deque
import webbrowser
from clear_screen import remove_items


class Display:

    def __init__(self, frame: LabelFrame, results: list):
        self.frame = frame
        self.results = results
        self.first_item = self.results[0]
        self.results = deque(self.results)
        self.curr_result = {}
        self.was_next = True

    def get_next_result(self):

        if not self.was_next:   # Did that for when changing from prev to next
            self.results.append(self.results.popleft())
            self.was_next = True

        self.curr_result = self.results.popleft()
        self.results.append(self.curr_result)
        self.display_result()

    def get_previous_result(self):

        if self.was_next:   # To get the right value when changing from next to prev
            self.was_next = False
            self.results.appendleft(self.results.pop())

        self.curr_result = self.results.pop()
        self.results.appendleft(self.curr_result)
        self.display_result()

    def display_result(self):

        remove_items(self.frame)    # Clear everything that is in the frame, so you can build all over

        curr_ticker = self.curr_result["ticker"]
        curr_sentiment = self.curr_result["sentiment"]
        curr_no_of_comments = self.curr_result["no_of_comments"]

        header_label = Label(
            self.frame,
            text="WSB Daily Most Popular Tickers",
            font="Helvetica, 18",
            fg="black"
        )

        ticker_label = Label(
            self.frame,
            text=f"{curr_ticker}",
            font=("Helvetica, 20"),
            fg="Green"
        )

        sentiment_label = Label(
            self.frame,
            text=f"Sentiment: \n{curr_sentiment}",
            font=("Helvetica, 16"),
            fg="grey"
        )

        comments = Label(
            self.frame,
            text=f"Total Comments:\n{curr_no_of_comments}",
            font=("Helvetica, 16"),
            fg="grey"
        )

        header_label.pack(pady=10)
        ticker_label.pack(pady=10)
        sentiment_label.pack(pady=10)
        comments.pack(pady=10)

        self.navigation_buttons()

    def navigation_buttons(self):

        button_frame = LabelFrame(self.frame, borderwidth=0)
        button_frame.columnconfigure(0, weight=3)
        button_frame.columnconfigure(1, weight=3)
        button_frame.columnconfigure(2, weight=3)

        next_button = Button(
            button_frame,
            text="Next",
            command=self.get_next_result,
            width=20,
            borderwidth=0
        )

        if self.first_item != self.curr_result:

            previous_button = Button(
                button_frame,
                text="Previous",
                command=self.get_previous_result,
                width=20,
                borderwidth=1,
                relief="flat",
            )

            next_button.grid(column=2, row=0, sticky="e", padx=10)
            previous_button.grid(column=0, row=0, sticky="w", padx=10)

        else:
            next_button.grid(column=1, row=0, sticky="NSWE", padx=10)

        button_frame.pack(fill="both", pady=20)

        company_info_btn = Button(
            self.frame,
            text="Check Company",
            command=self.go_to_webpage,
        )


    def go_to_webpage(self):
        ticker = self.curr_result["ticker"]
        url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch"
        webbrowser.open(url)






