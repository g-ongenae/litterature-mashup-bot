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

FONT_AUTHOR = ImageFont.truetype(FONT_NAME, 16)
FONT_TITLE = ImageFont.truetype(FONT_NAME, 28)
FONT_TYPE = ImageFont.truetype(FONT_NAME, 12)
FONT_EDITOR = ImageFont.truetype(FONT_NAME, 14)

MAX_WIDTH = 300


def center_text(
    draw: ImageDraw, height: int, text: str, color: COLOR, font: ImageFont
) -> None:
    """
    Add text in the middle of the image
    """
    wrapped = wrap(text, width=15)

    current_h, padding = height, 10
    for line in wrapped:
        width, text_height = draw.textsize(line, font=font)
        draw.text(((MAX_WIDTH - width) / 2, current_h), line, color, font=font)
        current_h += text_height + padding


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
    center_text(draw, 65, author.upper(), BLACK, font=FONT_AUTHOR)
    center_text(draw, 150, title.upper(), LIGHT_RED, font=FONT_TITLE)
    center_text(draw, 250, book_type.lower(), BLACK, font=FONT_TYPE)
    center_text(draw, 430, "Gallimart".upper(), BLACK, font=FONT_EDITOR)

    return image
