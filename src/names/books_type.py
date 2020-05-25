from random import choice
from logging import getLogger

logger = getLogger(__name__)


class BooksType:
    """
    Class

    TODO: guess the book type based on the book name
    """

    def __init__(self):
        """
        Init the BooksType object
        """
        self.BOOS_TYPE = []  # pylint: disable=invalid-name
        self.load_books_type()

    def load_books_type(self) -> None:
        """
        Load the books type
        """
        with open("./data/french_book_types.txt") as file:
            self.BOOS_TYPE = [line.rstrip() for line in file]

    def get_random_books_type(self) -> str:
        """
        Get two random books type
        """
        return choice(self.BOOS_TYPE)
