from logging import getLogger
from random import choice

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
        logger.info("Creating book type object")
        self.BOOK_TYPES = []  # pylint: disable=invalid-name
        self.load_books_type()

    def load_books_type(self) -> None:
        """
        Load the books type
        """
        logger.info("Loading book types")
        with open("./data/french_book_types.txt") as file:
            self.BOOK_TYPES = [line.rstrip() for line in file]
        logger.debug("Loaded book types: {}".format(self.BOOK_TYPES))

    def get_random_books_type(self) -> str:
        """
        Get two random books type
        """
        logger.debug("Getting a book type")
        return choice(self.BOOK_TYPES)
