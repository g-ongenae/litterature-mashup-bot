from os import getenv
from .images.gallimart import make_image
from .names.author import Author, mashup_names
from .names.books_type import BooksType
from .names.books import Books

API_KEY = getenv("API_KEY")


def main() -> None:
    """
    Main
    """
    author = Author()
    books_type = BooksType()
    books = Books(api_key=API_KEY)

    author_names = author.get_random_names()
    new_author_name = mashup_names(author_names)
    new_book_title = books.mashup_names(author_names)
    new_book_type = books_type.get_random_books_type()
    image = make_image(new_author_name, new_book_title, new_book_type)
    image.save("./image_test.jpg")
