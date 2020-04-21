from bs4 import BeautifulSoup
from lxml.html.clean import Cleaner


def process(res_content: str) -> str:
    cleaner = Cleaner()
    cleaner.javascript = True
    cleaner.style = True
    y = cleaner.clean_html(res_content)
    return BeautifulSoup(y, "lxml").text
