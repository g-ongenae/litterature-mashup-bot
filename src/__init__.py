from .images.gallimart import make_image
from .names.author import Author, mashup_names


def main() -> None:
    """
    Main
    """
    author = Author()
    author_names = author.get_random_names()
    author_name = mashup_names(author_names)
    # book_title = author.get_book_title(author_names)
    image = make_image(author_name, "Le Désespoir des jours heureux", "Roman")
    image.save("./image_test.jpg")
