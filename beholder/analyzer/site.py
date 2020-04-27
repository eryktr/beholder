from pathlib import Path
from typing import NamedTuple


class Site(NamedTuple):
    addr: str
    reference_path: Path
    update_path: Path
