import requests
from random import choice, choices, randint


class Books:
    """
	Class Books
	"""

    def __init__(self, api_key):
        self.api_key = api_key

    def get_author_books(self, author: str) -> [str]:
        """
        Get the list of books written by an author
        """
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
        return book_list

    def mashup_names(self, authors: (str, str)) -> str:
        """
        Mashup books from two different authors
        """
        # Get books by author name
        books_authors0 = self.get_author_books(authors[0])
        books_authors1 = self.get_author_books(authors[1])
        # Equalize the number of books
        books_to_mashup = _equalize_size(books_authors0, books_authors1)

        return _mashup_titles(books_to_mashup)


def _mashup_titles(titles: [str]) -> str:
    """
    Mashup titles
    """
    mashup_id = randint(0, 1)
    if mashup_id == 0:
        return choose_one(titles)
    if mashup_id == 1:
        return join_two_titles(titles)


def choose_one(titles: [str]) -> str:
    """
    Choose one
    """
    return choice(titles)


conjunction = ["mais", "ou", "et", "donc", "or", "ni", "car"]


def join_two_titles(titles: [str]) -> str:
    """
    Join two titles
    """
    chosen_conjunction = choice(conjunction)
    try:
        chosen_titles = choices(titles, k=2)
        return chosen_titles[0] + " " + chosen_conjunction + " " + chosen_titles[1]
    except ValueError:
        return titles[0]


def _equalize_size(lst_1: [str], lst_2: [str]) -> [str]:
    """
	Equalize "logarythmically" size of two list
	"""
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
