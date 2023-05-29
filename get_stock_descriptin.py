from PIL import ImageTk, Image
import requests
from io import BytesIO


# This will be changed to taking a parameter, The parameter will be the ticker, and then
# the ticker will be added at the end of the string to retrieve the company's logo.

def get_company_image():
    url = "https://financialmodelingprep.com/image-stock/IBM.png"
    response = requests.get(url)
    image_data = response.content

    # Convert the image data to a Tkinter-compatible format
    image = Image.open(BytesIO(image_data))
    tk_image = ImageTk.PhotoImage(image)

    return tk_image
