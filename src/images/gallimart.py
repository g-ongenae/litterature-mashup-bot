from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont

# Sizes
BOOK_SIZE = (300, 500)
REAL_BOOK_SIZE = (107, 176)

BASE_X1 = 25
BASE_X2 = 275
BASE_Y1 = 25
BASE_Y2 = 475

PADDING_1 = 5
PADDING_2 = 3

RECT_1 = (BASE_X1, BASE_Y1, BASE_X2, BASE_Y2)
RECT_2 = (
    BASE_X1 + PADDING_1,
    BASE_Y1 + PADDING_1,
    BASE_X2 - PADDING_1,
    BASE_Y2 - PADDING_1,
)
RECT_3 = (
    BASE_X1 + PADDING_1 + PADDING_2,
    BASE_Y1 + PADDING_1 + PADDING_2,
    BASE_X2 - PADDING_1 - PADDING_2,
    BASE_Y2 - PADDING_1 - PADDING_2,
)

# Colors
COLOR = (int, int, int)
BG_COLOR = (253, 251, 239)
BLACK = (0, 0, 0)
LIGHT_RED = (230, 43, 28)

# Fonts
# See: https://github.com/python-pillow/Pillow/pull/1054/files
# https://www.dafont.com/fr/forum/read/249981/font-used-for-the-title-of-the-gallimard-blanche-books
# Font source: https://ufonts.com/download/8bauerbodoni09033-black.html
FONT_NAME = "./fonts/8bauerbodoni09033-black.ttf"

FONT_AUTHOR = [ImageFont.truetype(FONT_NAME, 16), ImageFont.truetype(FONT_NAME, 12)]
FONT_TITLE = [ImageFont.truetype(FONT_NAME, 28), ImageFont.truetype(FONT_NAME, 22)]
FONT_TYPE = [ImageFont.truetype(FONT_NAME, 12), ImageFont.truetype(FONT_NAME, 10)]
FONT_EDITOR = [ImageFont.truetype(FONT_NAME, 14), ImageFont.truetype(FONT_NAME, 12)]

MAX_WIDTH = 300


def _get_biggest_words_len(sentence: str) -> int:
    """
    Check word length in a string

    params:
    -------
    sentence: the string to check
    returns:
    --------
    the length of the biggest word of the sentence
    """
    maximum = 0
    for word in sentence.split(" "):
        maximum = max(len(word), maximum)
    return maximum


def center_text(
    image: ImageDraw,
    last_height: int,
    height: int,
    text: str,
    color: COLOR,
    fonts: [ImageFont],
) -> int:
    """
    Add text in the middle of the image
    """
    biggest_len = _get_biggest_words_len(text)
    if biggest_len > 12 or len(text) > 40:
        font = fonts[1]
        wrapped = wrap(text, width=max(biggest_len, 15))
    else:
        font = fonts[0]
        wrapped = wrap(text, width=12)

    current_h, padding = max(last_height, height), 10
    for line in wrapped:
        width, text_height = image.textsize(line, font=font)
        image.text(((MAX_WIDTH - width) / 2, current_h), line, color, font=font)
        current_h += text_height + padding
    return current_h


def make_image(author: str, title: str, book_type: str) -> Image:
    """
    Make the image
    """
    # Image
    image = Image.new("RGB", BOOK_SIZE, BG_COLOR)
    draw = ImageDraw.Draw(image)

    # Borders
    draw.rectangle(RECT_1, outline=BLACK)
    draw.rectangle(RECT_2, outline=LIGHT_RED)
    draw.rectangle(RECT_3, outline=LIGHT_RED)

    # Add texts
    l = 0
    l = center_text(
        image=draw,
        last_height=l,
        height=65,
        text=author.upper(),
        color=BLACK,
        fonts=FONT_AUTHOR,
    )
    l = center_text(
        image=draw,
        last_height=l,
        height=150,
        text=title.upper(),
        color=LIGHT_RED,
        fonts=FONT_TITLE,
    )
    l = center_text(
        image=draw,
        last_height=l,
        height=250,
        text=book_type.lower(),
        color=BLACK,
        fonts=FONT_TYPE,
    )
    l = center_text(
        image=draw,
        last_height=l,
        height=430,
        text="Gallimart".upper(),
        color=BLACK,
        fonts=FONT_EDITOR,
    )

    return image
