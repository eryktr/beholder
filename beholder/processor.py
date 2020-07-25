from bs4 import BeautifulSoup
from lxml.html.clean import Cleaner


def process(cleaner: Cleaner, res_content: str) -> str:
    cleaner.javascript = True
    cleaner.style = True
    clean_text = cleaner.clean_html(res_content.encode('utf8'))
    return BeautifulSoup(clean_text, "lxml").text
