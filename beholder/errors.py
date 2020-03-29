from typing import List
from pathlib import Path


class PathNotFoundError(Exception):
    path: Path
    msg: str

    def __init__(self, path: Path):
        self.msg = f"{path} not found"
        super().__init__(self.msg)


class IncorrectWebsitesError(Exception):
    sites: List[str]
    msg: str = "Some of the websites you provided are invalid"

    def __init__(self, sites: List[str]):
        self.sites = sites
        super().__init__(self.msg)
