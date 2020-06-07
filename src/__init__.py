from os import getenv, remove
import time
from logging import getLogger
import tweepy
import schedule
from .images.gallimart import make_image
from .names.author import Author, mashup_names
from .names.books_type import BooksType
from .names.books import Books

# Global variables
AUTHOR = None
BOOK_TYPES = None
BOOKS = None
TWITTER = None

logger = getLogger(__name__)


def init_twitter(
    consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str
):
    """
    Log on Twitter API with tweepy
    """
    logger.info("Logging in with Twitter")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def tweet() -> None:
    """
    Tweet the mashup
    """
    logger.info("Preparing to tweet")
    filepath = "./image_test.jpg"
    # Get the author to mashup
    author_names = AUTHOR.get_random_names()
    # Mashup info
    new_author_name = mashup_names(author_names)
    new_book_title = BOOKS.mashup_names(author_names)
    new_book_type = BOOK_TYPES.get_random_books_type()
    # Create the mashup image and save it
    image = make_image(new_author_name, new_book_title, new_book_type)
    image.save(filepath)
    # Tweet the image with the info
    message = "{authors[0]} + {authors[1]} = {new_author}".format(
        authors=author_names, new_author=new_author_name
    )
    logger.info("Tweeting: {}".format(message))
    TWITTER.update_with_media(filepath, status=message)
    remove(filepath)


def main():
    """
    Main
    """
    logger.info("Starting the application")

    # Declare the global variables
    global AUTHOR
    global BOOK_TYPES
    global BOOKS
    global TWITTER

    # Init the global variables
    AUTHOR = Author()
    BOOK_TYPES = BooksType()
    BOOKS = Books(api_key=getenv("GBOOKS_API_KEY"))
    TWITTER = init_twitter(
        consumer_key=getenv("TWITTER_CONSUMER_KEY"),
        consumer_secret=getenv("TWITTER_CONSUMER_SECRET"),
        access_token=getenv("TWITTER_ACCESS_TOKEN"),
        access_token_secret=getenv("TWITTER_ACCESS_TOKEN_SECRET"),
    )

    # Create cron to tweet once every hour
    schedule.every().hour.do(tweet)

    logger.info("The application started correctly!")

    # Run
    while 1:
        logger.debug("Still up")
        schedule.run_pending()
        time.sleep(1)
