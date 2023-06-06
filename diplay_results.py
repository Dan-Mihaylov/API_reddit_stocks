from tkinter import *
from collections import deque
import webbrowser
from clear_screen import remove_items
from get_stock_description import get_company_image, get_company_profile
import json
from helpers import bg_color, fg_color
from tkinter import ttk


class Display:

    def __init__(self, frame: LabelFrame, results: list):
        self.frame = frame
        self.results = results
        self.first_item = self.results[0]
        self.results = deque(self.results)
        self.curr_result = {}
        self.was_next = True

    def get_next_result(self):

        if not self.was_next:   # Did that for when changing from prev to next  / can do with rotate later.
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

        mid_frame = LabelFrame(self.frame, borderwidth=0, bg="#1d2129")
        mid_frame.columnconfigure(1, weight=2)
        mid_frame.columnconfigure(2, weight=2)
        mid_frame.columnconfigure(3, weight=2)

        curr_ticker = self.curr_result["ticker"]
        curr_sentiment = self.curr_result["sentiment"]
        curr_no_of_comments = self.curr_result["no_of_comments"]

        company_img = get_company_image(curr_ticker)   # Pass the ticker, and get the company logo with request

        header_label = Label(
            self.frame,
            text="WSB Daily Most Popular Tickers",
            font="Helvetica, 18",
            fg=fg_color,
            bg=bg_color,
        )

        company_image = Label(
            self.frame,
            image=company_img,
            bg=bg_color
        )

        ticker_label = Label(
            mid_frame,
            text=f"{curr_ticker}",
            font="Helvetica, 20",
            fg="Green",
            justify="center",
            bg=bg_color
        )

        sentiment_label = Label(
            mid_frame,
            text=f"Sentiment: {curr_sentiment}",
            font="Helvetica, 16",
            fg="grey",
            bg=bg_color
        )

        comments = Label(
            mid_frame,
            text=f"Total Comments: {curr_no_of_comments}",
            font="Helvetica, 16",
            fg="grey",
            bg=bg_color
        )

        # That is the left half of the grid filled with company info

        header_label.pack(pady=10)
        company_image.pack(pady=10)    # The image pack()
        mid_frame.pack(fill="x")
        ticker_label.grid(row=1, column=1, sticky="e")
        sentiment_label.grid(row=2, column=1, sticky="e")
        comments.grid(row=3, column=1, sticky="e")

        # Now will create the other labels and info for the right half, with another API and request

        # Get the company description and additional data, based on the ticker.
        try:
            more_stock_info = get_company_profile(curr_ticker).pop()

            company_price = more_stock_info["price"]
            company_market_cap = str(int(more_stock_info["mktCap"]) // 1000000000) + "B"
            company_range = more_stock_info["range"]
            description = more_stock_info["description"]

            price_label = Label(
                mid_frame,
                text=f"Price: {company_price}",
                font="Helvetica, 16",
                fg="grey",
                bg=bg_color
            )
            market_cap_label = Label(
                mid_frame,
                text=f"Market Cap: {company_market_cap}",
                font="Helvetica, 16",
                fg="grey",
                bg=bg_color
            )
            ranges_label = Label(
                mid_frame,
                text=f"52 Week Range: {company_range}",
                font="Helvetica, 16",
                fg="grey",
                bg=bg_color
            )

            price_label.grid(row=1, column=3, sticky="w")
            market_cap_label.grid(row=2, column=3, sticky="w")
            ranges_label.grid(row=3, column=3, sticky="w")

            company_description_frame = LabelFrame(
                self.frame,
                borderwidth=0,
                bg=bg_color
            )
            company_description_frame.pack(
                pady=50,
                expand=True,
                fill="both")

            info_canvas = Canvas(
                company_description_frame,
                borderwidth=0,
                bg=bg_color
            )

            info_canvas.pack(
                side="left",
                fill="both",
                expand=True
            )

            scrollbar = Scrollbar(
                company_description_frame,
                orient="vertical",
                command=info_canvas.yview,
                width=2,
                background=bg_color,
                troughcolor=bg_color
            )
            scrollbar.configure(relief="flat", troughcolor=bg_color, activebackground=bg_color)
            scrollbar.pack(
                side="right",
                fill="y",
                padx=5
            )
            info_canvas.configure(yscrollcommand=scrollbar.set, highlightthickness=0)

            content_frame = LabelFrame(
                info_canvas,
                borderwidth=0,
                bg=bg_color
            )

            info_canvas.create_window(
                (20, 0),
                window=content_frame,
                anchor="nw",
            )
            company_description_label = Label(
                content_frame,
                text=description,
                font="helvetica, 10",
                wraplength=550,
                justify="left",
                bg=bg_color,
                fg=fg_color
            )
            company_description_label.pack(fill="both", expand=True)

        except json.JSONDecodeError and IndexError and TypeError as e:

            error_label = Label(
                self.frame,
                text=f"Error Decoding Json\n{e}\nLimit Reached.More details at https://site.financialmodelingprep.com/",
                font="helvetica",
                bg=bg_color)

            error_label.pack()

        self.navigation_buttons()

    def navigation_buttons(self):

        button_frame = LabelFrame(self.frame, borderwidth=0, bg=bg_color)
        button_frame.columnconfigure(1, weight=3)
        button_frame.columnconfigure(2, weight=3)
        button_frame.columnconfigure(3, weight=3)

        next_button = Button(
            button_frame,
            text="Next",
            command=self.get_next_result,
            width=20,
            borderwidth=0,
            bg=bg_color,
            fg=fg_color,
            activebackground="#20242d",
            activeforeground=fg_color
        )
        previous_button = Button(
            button_frame,
            text="Previous",
            command=self.get_previous_result,
            width=20,
            borderwidth=0,
            bg=bg_color,
            fg=fg_color,
            activebackground="#20242d",
            activeforeground=fg_color
        )
        company_info_btn = Button(
            button_frame,
            text="Check Company",
            command=self.go_to_webpage,
            borderwidth=0,
            bg=bg_color,
            fg=fg_color,
            activebackground="#20242d",
            activeforeground=fg_color
        )

        next_button.grid(column=3, row=0, sticky="e", padx=10)
        previous_button.grid(column=1, row=0, sticky="w", padx=10)
        company_info_btn.grid(row=0, column=2)

        if self.first_item == self.curr_result:
            previous_button.configure(state="disabled")

        button_frame.pack(fill="both", pady=20)
        # TODO! Create a json dumps every time i see a company, and when clicking previous check the dumps first for
        # TODO! the info, so i save resources on requests. API KEY ==  200 PER DAY

    def go_to_webpage(self):
        ticker = self.curr_result["ticker"]
        url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch"
        webbrowser.open(url)
