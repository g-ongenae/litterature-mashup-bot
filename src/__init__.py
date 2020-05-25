from .images.gallimart import make_image
from .names.author import Author, mashup_names
from .names.books_type import BooksType


def main() -> None:
    """
    Main
    """
    author = Author()
    books_type = BooksType()

    author_names = author.get_random_names()
    author_name = mashup_names(author_names)
    # book_title = author.get_book_title(author_names)
    book_type = books_type.get_random_books_type()
    image = make_image(author_name, "Le Désespoir des jours heureux", book_type)
    image.save("./image_test.jpg")
