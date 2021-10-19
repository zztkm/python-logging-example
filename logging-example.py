import logging

from foo import bar

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def main():
    logger.info("start")
    bar("Hello!")
    logger.info("finished")

if __name__ == "__main__":
    main()
