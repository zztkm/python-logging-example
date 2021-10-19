import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

from .bar import bar

__all__ = ["bar"]
