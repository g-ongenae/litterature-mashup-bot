import requests
from random import choice, choices, randint
from logging import getLogger

logger = getLogger(__name__)

# Constants
CONJUNCTIONS = ["mais", "ou", "et", "donc", "or", "ni", "car"]


class Books:
    """
	Class Books
	"""

    def __init__(self, api_key):
        """
        Init the Books class
        """
        logger.info("Creating book object")
        self.api_key = api_key

    def get_author_books(self, author: str) -> [str]:
        """
        Get the list of books written by an author
        """
        logger.info("Getting author books for author {}".format(author))
        r = requests.get(
            "https://www.googleapis.com/books/v1/volumes",
            params={
                "q": "inauthor:{}".format(author),
                "langRestrict": "fr",
                "key": self.api_key,
            },
            headers={"Accept": "application/json"},
        )
        res = r.json()
        book_list = []
        for i in res["items"]:
            title = i["volumeInfo"]["title"]
            if not author in title:
                book_list.append(title)
        logger.debug("Got book list for author {}: {}".format(author, book_list))
        return book_list

    def mashup_names(self, authors: (str, str)) -> str:
        """
        Mashup books from two different authors
        """
        logger.debug("Mashup book names for authors: {}".format(authors))
        # Get books by author name
        books_authors0 = self.get_author_books(authors[0])
        books_authors1 = self.get_author_books(authors[1])
        # Equalize the number of books
        books_to_mashup = _equalize_size(books_authors0, books_authors1)
        logger.debug("Books to mashup: {}".format(books_to_mashup))

        return _mashup_titles(books_to_mashup)


def _mashup_titles(titles: [str]) -> str:
    """
    Mashup titles
    """
    mashup_id = randint(0, 1)
    logger.info("Mashup book type: {}".format(mashup_id))
    if mashup_id == 0:
        return choose_one(titles)
    if mashup_id == 1:
        return join_two_titles(titles)

    logger.error(f"Invalid book mashup choice: {i}")
    raise ValueError("Invalid book mashup choice")


def choose_one(titles: [str]) -> str:
    """
    Choose one
    """
    logger.debug("Choose one random book title")
    return choice(titles)


def join_two_titles(titles: [str]) -> str:
    """
    Join two titles
    """
    chosen_conjunction = choice(CONJUNCTIONS)
    logger.debug(
        "Joining the two titles with a conjunction: {}".format(chosen_conjunction)
    )
    try:
        chosen_titles = choices(titles, k=2)
        return chosen_titles[0] + " " + chosen_conjunction + " " + chosen_titles[1]
    except ValueError:
        logger.info("Not enough titles: {}".format(titles))
        if len(titles) == 1:
            return titles[0]
        return "Œuvres"  # TODO call a generator


def _equalize_size(lst_1: [str], lst_2: [str]) -> [str]:
    """
	Equalize "logarythmically" size of two list
	"""
    logger.debug("Equalizing book lists")
    BASE = 3
    # Handle empty lists
    if not lst_1:
        return lst_2
    if not lst_2:
        return lst_1
    # Handle case list widely different size
    if BASE < len(list(lst_1)) / len(list(lst_2)):
        return lst_1[: len(list(lst_2))] + lst_2
    if BASE < len(list(lst_2)) / len(list(lst_1)):
        return lst_2[: len(list(lst_1))] + lst_1
    # Handle case of about same length (same BASE)
    return lst_1 + lst_2
