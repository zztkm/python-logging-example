import logging

from hoge import huga

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def main():
    logger.debug("レベルをDEBUGに設定しているのに表示されへん")
    huga("Hello!")
    logger.info("INFOは表示される")


if __name__ == "__main__":
    main()
