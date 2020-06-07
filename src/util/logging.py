import logging
import logging.config
import sys


class _ExcludeErrorsFilter(logging.Filter):
    def filter(self, record):
        """Filters out log messages with log level ERROR (numeric value: 40) or higher."""
        return record.levelno < 40


def setting_logging():
    """
    Logging configuration
    """
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {"exclude_errors": {"()": _ExcludeErrorsFilter}},
        "formatters": {
            "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"}
        },
        "handlers": {
            "console_stderr": {
                # Sends log messages with log level ERROR or higher to stderr
                "class": "logging.StreamHandler",
                "level": "ERROR",
                "formatter": "standard",
                "stream": sys.stderr,
            },
            "console_stdout": {
                # Sends log messages with log level lower than ERROR to stdout
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "filters": ["exclude_errors"],
                "stream": sys.stdout,
            },
            "default_handler": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "filename": "./application.log",
                "encoding": "utf8",
            },
        },
        "loggers": {
            "": {
                "handlers": ["default_handler", "console_stdout", "console_stderr"],
                "level": "DEBUG",
                "propagate": False,
            }
        },
    }

    logging.config.dictConfig(logging_config)
