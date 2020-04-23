from pathlib import Path

import requests
from lxml.html.clean import Cleaner

import beholder.const as const
from beholder.errors import IncorrectStatusError
import beholder.processor as processor


class WebFetcher:
    cleaner: Cleaner = Cleaner()

    def fetch(self, addr: str, path: Path) -> None:
        res = requests.get(addr)
        if res.status_code not in const.ALLOWED_STATCODES:
            raise IncorrectStatusError(addr, res.status_code)
        cleaned_text = processor.process(self.cleaner, res.text)
        path.write_text(cleaned_text, encoding='utf-8')
