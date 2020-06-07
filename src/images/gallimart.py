from logging import getLogger
from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont

logger = getLogger(__name__)


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
    logger.debug("Get biggest word length of sentence: {}".format(sentence))
    maximum = 0
    for word in sentence.split(" "):
        maximum = max(len(word), maximum)
    return maximum


class Cover:
    """
    Create a cover for "Gallimart"
    """

    def __init__(self):
        """
        Initialize
        """
        self.last_height = 0
        # Image
        self.image = Image.new("RGB", BOOK_SIZE, BG_COLOR)
        self.image_drawer = ImageDraw.Draw(self.image)

    def center_text(
        self, height: int, text: str, color: COLOR, fonts: [ImageFont]
    ) -> None:
        """
        Add text in the middle of the image
        """
        logger.debug("Adding text to image: %s", text)
        biggest_len = _get_biggest_words_len(text)
        if biggest_len > 12 or len(text) > 40:
            font = fonts[1]
            wrapped = wrap(text, width=max(biggest_len, 15))
        else:
            font = fonts[0]
            wrapped = wrap(text, width=12)

        current_h, padding = max(self.last_height, height), 10
        for line in wrapped:
            width, text_height = self.image_drawer.textsize(line, font=font)
            self.image_drawer.text(
                ((MAX_WIDTH - width) / 2, current_h), line, color, font=font
            )
            current_h += text_height + padding
        self.last_height = current_h

    def draw_borders(self) -> None:
        """
        Borders
        """
        self.image_drawer.rectangle(RECT_1, outline=BLACK)
        self.image_drawer.rectangle(RECT_2, outline=LIGHT_RED)
        self.image_drawer.rectangle(RECT_3, outline=LIGHT_RED)

    def make_image(self, author: str, title: str, book_type: str) -> Image:
        """
        Make the image
        """
        logger.info("Creating Gallimart image cover")
        self.draw_borders()

        # Add texts
        self.center_text(height=65, text=author.upper(), color=BLACK, fonts=FONT_AUTHOR)
        self.center_text(
            height=150, text=title.upper(), color=LIGHT_RED, fonts=FONT_TITLE
        )
        self.center_text(
            height=250, text=book_type.lower(), color=BLACK, fonts=FONT_TYPE
        )
        self.center_text(
            height=430, text="Gallimart".upper(), color=BLACK, fonts=FONT_EDITOR
        )

        return self.image


def make_image(author: str, title: str, book_type: str) -> Image:
    """
    Make the image
    """
    message = "Creating Gallimart image cover for author {} and title {} and type {}"
    logger.info(message.format(author, title, book_type))
    cover = Cover()
    return cover.make_image(author, title, book_type)
