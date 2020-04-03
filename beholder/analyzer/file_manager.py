from typing import List
from pathlib import Path
from tempfile import mkdtemp


class FileManager:
    sites: List[str]
    temp_dir: str
    _lut: dict

    def __init__(self, sites: List[str]):
        self.sites = sites
        self.temp_dir = mkdtemp()
        self._lut = {v: str(i) for i, v in enumerate(sites)}

    def latest_path(self, addr: str) -> Path:
        return Path(self.temp_dir) / (self._lut[addr] + "o.html")

    def chall_path(self, addr: str) -> Path:
        return Path(self.temp_dir) / (self._lut[addr] + "n.html")
