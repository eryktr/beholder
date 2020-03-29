from typing import List


class IncorrectWebsitesError(Exception):
    sites: List[str]
    msg: str = "Some of the websites you provided are invalid"

    def __init__(self, sites: List[str]):
        self.sites = sites
        super().__init__(self.msg)
