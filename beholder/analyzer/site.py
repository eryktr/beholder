from pathlib import Path
from typing import NamedTuple


class Site(NamedTuple):
    addr: str
    latest_path: Path
    chall_path: Path
