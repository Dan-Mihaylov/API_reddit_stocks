from PIL import ImageTk, Image
import requests
from io import BytesIO
from helpers import MY_KEY


def get_company_image(ticker: str):

    # Fetch the image from the URL

    url = f"https://financialmodelingprep.com/image-stock/{ticker}.png"
    response = requests.get(url)
    image_data = response.content

    # Display the company logo, if it doesn't exist create it from the response.

    try:
        saved_img = Image.open(f"temp/{ticker}.png")
        saved_img_open = ImageTk.PhotoImage(saved_img)

    except FileNotFoundError:

        image = Image.open(BytesIO(image_data))

        resize_image = Image.Image.resize(image, (128, 128))
        resize_image.save(f"temp/{ticker}.png")

        saved_img = Image.open(f"temp/{ticker}.png")
        saved_img_open = ImageTk.PhotoImage(saved_img)

    # keep a reference of the image object

    saved_img_open.image = saved_img_open

    return saved_img_open


def get_company_profile(ticker: str, key=MY_KEY):

    url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={key}"
    response = requests.get(url)
    return response.json()
