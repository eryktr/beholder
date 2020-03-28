from typing import List
from pathlib import Path


class PathNotFoundError(Exception):
    def __init__(self, arg: Path):
        if arg:
            self.path = arg

    def __str__(self):
        return f"{self.path} does not exist."


class NotAFileError(Exception):
    def __init__(self, arg: Path):
        if arg:
            self.path = arg

    def __str__(self):
        return f"{self.path} is not a file."


class IncorrectWebsitesError(Exception):
    def __init__(self, args: List[str]):
        if args:
            self.websites = args

    def __message__(self):
        return self.websites
