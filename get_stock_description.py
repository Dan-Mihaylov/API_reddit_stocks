from PIL import ImageTk, Image
import requests
from io import BytesIO


def get_company_image(ticker: str):
    # Fetch the image from the URL
    url = f"https://financialmodelingprep.com/image-stock/{ticker}.png"
    response = requests.get(url)
    image_data = response.content

    # Convert the image data to a Tkinter-compatible format
    image = Image.open(BytesIO(image_data))
    resize_image = Image.Image.resize(image, (128, 128))
    tk_image = ImageTk.PhotoImage(resize_image)

    return tk_image


# Bellow is testing code only.

from tkinter import Tk, Label


# Getting the image object and displaying it here works, but not in display_results line 46, 55, 83
# I get, just the black background and the dimensions without the actual image.

# def the_gui():
#     # 128 128 width height
#
#     root = Tk()
#     img = get_company_image("NVDA")
#     a, b = img.width(), img.height()
#     print(a, b)
#     label = Label(root, image=img, bg="black")
#     label.pack()
#
#     root.mainloop()
#
#
# the_gui()

