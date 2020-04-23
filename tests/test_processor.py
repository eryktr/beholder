from beholder.processor import process
from lxml.html.clean import Cleaner
import re


def test_processor_correct():
    content = '''
<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Gall Anonim</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <div id="container">
    <header>
      <h1>Witaj na mojej stronie!</h1>
    </header>
    <div id="content">
      <nav>
        <div class="MenuWrap">
          <a href="./index.html" class="FirstItem">Główna</a>
          <a href="./about.html" class="ListItem">O mnie</a>
          <a href="./contact.html" class="SelectedLastItem">Kontakt</a>
        </div>
      </nav>
      <main>
        <h2>Dane kontaktowe</h2>
        <h3>Telefon komórkowy:</h3>
        <p>124912481248</p>
        <h3>Adres e-mail: example@example.com</h3>
        <script src="./email.js"></script>
      </main>
    </div>
  </div>
</body>
</html>
'''
    result = "".join([
      " Gall Anonim Witaj na mojej stronie! Główna ",
      "O mnie Kontakt Dane kontaktowe Telefon komórkowy: 124912481248 ",
      "Adres e-mail: example@example.com "
      ])
    cleaner = Cleaner()
    processed_html = process(cleaner, content)
    compact_html = re.sub("[\n' ']+", ' ', processed_html)
    assert compact_html == result
