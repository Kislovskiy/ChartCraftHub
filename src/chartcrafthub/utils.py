import logging

from rich.logging import RichHandler


def setup_logger(
    level=logging.INFO, fmt="%(message)s", datefmt="[%X]", handlers=None
) -> None:
    if handlers is None:
        handlers = [RichHandler()]
    logging.basicConfig(level=level, format=fmt, datefmt=datefmt, handlers=handlers)


if __name__ == "__main__":
    setup_logger()
    logger = logging.getLogger(__name__)
    logger.info("This is a test log message")
