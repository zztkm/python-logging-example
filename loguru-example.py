import logging

from loguru import logger

from foo import bar


# logging の内容を Loguru で受け取る処理を記述した Handler
class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


logging.basicConfig(handlers=[InterceptHandler()], level=0)


def main():
    logger.info("start")
    bar("Hello!")
    logger.info("finished")

if __name__ == "__main__":
    main()
