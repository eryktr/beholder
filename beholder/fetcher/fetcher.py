from pathlib import Path

import requests
from lxml.html.clean import Cleaner

import beholder.const as const
from beholder.errors import IncorrectStatusError
import beholder.processor as processor


class WebFetcher:
    cleaner: Cleaner = Cleaner()

    def fetch(self, site: str, dst: Path) -> None:
        res = requests.get(site)
        if res.status_code not in const.ALLOWED_STATCODES:
            raise IncorrectStatusError(site, res.status_code)
        cleaned_text = processor.process(self.cleaner, res.text)
        dst.write_text(cleaned_text, encoding='utf-8')
