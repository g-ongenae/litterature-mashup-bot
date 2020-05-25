class Books:
    """
	Class Books
	"""

    def __init__(self):
        pass

    def get_author_books(self, author: str) -> List[str]:
        return

    def mashup_names(self, authors: (str, str)) -> str:
        # Get books by author name
        books_authors0 = self.get_author_books(name[0])
        books_authors1 = self.get_author_books(name[1])
        # Equalize the number of books
        books_to_mashup = _equalize_size(books_authors0, books_authors1)

        return


def _equalize_size(lst_1: List[str], lst_2: List[str]) -> List[str]:
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
