import logging

logger = logging.getLogger(__name__)


def bar(msg: str):
    logger.debug(f"msg length: {len(msg)}")
    return msg
