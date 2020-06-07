from random import choices, choice, randint
from logging import getLogger

logger = getLogger(__name__)


class Author:
    """
    Class
    """

    def __init__(self):
        """
        Init the author object, load_author_names
        """
        logger.info("Creating author object")
        self.AUTHOR_NAMES = []  # pylint: disable=invalid-name
        self.AUTHOR_NAMES_RANGE = []  # pylint: disable=invalid-name
        self.load_author_names()

    def load_author_names(self) -> None:
        """
        Load the author names

        Updated on the 18 May 2020
        from https://fr.wikipedia.org/wiki/ \
            Liste_d'écrivains_de_langue_française_par_ordre_chronologique
        """
        logger.info("Loading author names")
        with open("./data/french_authors.txt") as file:
            self.AUTHOR_NAMES = [line.rstrip() for line in file]
            self.AUTHOR_NAMES_RANGE = range(len(self.AUTHOR_NAMES))
        logger.debug("Loaded author names: {}".format(len(self.AUTHOR_NAMES)))

    def get_random_names(self) -> (str, str):
        """
        Get two random author names
        """
        logger.debug("Getting two author names")
        i, j = choices(self.AUTHOR_NAMES_RANGE, k=2)
        logger.debug("Got author name ids: {}, {}".format(i, j))
        return self.AUTHOR_NAMES[i], self.AUTHOR_NAMES[j]


def mashup_names(names: (str, str)) -> str:
    """
    Mashup names of the authors
    """
    i = randint(0, 4)
    logger.info("Mashup author type: {}".format(i))
    if i == 0:
        return get_simple_new_name(names)
    if i == 1:
        return get_joined_firstname(names)
    if i == 2:
        return get_joined_lastname(names)
    if i == 3:
        return get_duo_name(names)
    if i == 4:
        return get_cut_paste_name(names)

    logger.error(f"Invalid author mashup choice: {i}")
    raise ValueError("Invalid author mashup choice")


def get_simple_new_name(name: (str, str)) -> str:
    """
    Return a new name from the two authors names

    Type: Simple [firstname 1] [lastname 2]
    """
    logger.debug("Mashup simple type")
    (firstname, _) = _spliter(name[0])
    (_, lastname) = _spliter(name[1])
    return f"{firstname} {lastname}"


def get_joined_firstname(name: (str, str)) -> str:
    """
    Return a new author name based on the two provided

    Type: joined first names
    """
    logger.debug("Mashup firstname type")
    (firstname1, lastname1) = _spliter(name[0])
    (firstname2, lastname2) = _spliter(name[1])
    lastname = choice([lastname1, lastname2])

    join_type = choice(["DASH", "INIT"])
    if join_type == "DASH":
        return f"{firstname1}-{firstname2} {lastname}"
    if join_type == "INIT":
        init = firstname2[0].upper()
        return f"{firstname1} {init}. {lastname}"

    logger.error(f"Invalid firstname join type: {join_type}")
    raise ValueError("Invalid")


def get_joined_lastname(name: (str, str)) -> str:
    """
    Return a new author name based on the two provided

    Type: joined last names
    """
    logger.debug("Mashup lastname type")
    (firstname1, lastname1) = _spliter(name[0])
    (_, lastname2) = _spliter(name[1])

    join_type = choice(["DASH", "INIT", "LINK", "WORD"])
    if join_type == "DASH":
        return f"{firstname1} {lastname1}-{lastname2}"
    if join_type == "INIT":
        init1 = lastname1[0].upper()
        init2 = lastname1[0].upper()
        return f"{firstname1} {init1}.-{init2}."
    if join_type == "LINK":
        return f"{firstname1} {lastname1}{lastname2}"
    if join_type == "WORD":
        # from https://fr.wikipedia.org/wiki/Particule_(onomastique)
        with open("./data/name_particles.txt", "r") as particle_file:
            particles = [line.rstrip() for line in particle_file]
        particle = choice(particles)
        if "'" in particle and particle != "'t":
            return f"{firstname1} {lastname1} {particle}{lastname2}"

        return f"{firstname1} {lastname1} {particle} {lastname2}"

    logger.error(f"Invalid lastname join type: {join_type}")
    raise ValueError("Invalid")


def get_duo_name(name: (str, str)) -> str:
    """
    Return the names of the two authors (duo)

    Type: duo
    """
    logger.debug("Mashup duo type")
    (_, lastname1) = _spliter(name[0])
    (_, lastname2) = _spliter(name[1])

    return f"{lastname1} et {lastname2}"


def get_cut_paste_name(name: (str, str)) -> str:
    """
    Return a complete new name from the 2 (cutted)

    Type: cut
    """
    logger.debug("Mashup cut type")
    (firstname1, lastname1) = _spliter(name[0])
    (_, lastname2) = _spliter(name[1])

    lastname = f"{lastname1} {lastname2}"  # TODO # pylint: disable=fixme

    return f"{firstname1} {lastname}"


def _spliter(name: str) -> (str, str):
    """
    Split a name in its two part
    """
    logger.debug("Splitting name: %s" % name)
    if " " in name:
        return name.split(" ", 1)
    return (name, "")
