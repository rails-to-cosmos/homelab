import logging
import sys


class Logger(logging.Logger):
    def __init__(self, name: str, level: str, fmt: str) -> None:
        super().__init__(name)

        self.setLevel(level)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)
        self.addHandler(handler)
