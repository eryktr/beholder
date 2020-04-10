from typing import List


class IncorrectWebsitesError(Exception):
    sites: List[str]
    msg: str = "Some of the websites you provided are invalid"

    def __init__(self, sites: List[str]):
        self.sites = sites
        super().__init__(self.msg)


class IncorrectStatusError(Exception):
    addr: str
    status_code: int
    msg: str

    def __init__(self, addr: str, status_code: int):
        self.addr = addr
        self.status_code = status_code
        self.msg = f"Status code of {addr} is invalid. Status code: {status_code}"
        super().__init__(self.msg)
