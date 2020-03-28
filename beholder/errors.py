from typing import List
from pathlib import Path


class PathNotFoundError(Exception):
    path: Path

    def __init__(self, path: Path):
        self.path = path
        msg = f"{path} not found"
        self.msg = msg
        super().__init__(self.msg)


class IncorrectWebsitesError(Exception):
    sites: List[str]
    msg = "Some of the websites you provided are invalid"

    def __init__(self, sites: List[str]):
        self.sites = sites
        super().__init__(self.msg)
