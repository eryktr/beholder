from pathlib import Path
import beholder.const as const
import beholder.errors as errors
import requests


class WebFetcher:

    def fetch(self, addr: str, path: Path):
        res = requests.get(path)
        if res.status_code not in const.ALLOWED_STATCODES:
            raise errors.IncorrectStatusError(addr, res.status_code)
        path.write_text(res.text)
