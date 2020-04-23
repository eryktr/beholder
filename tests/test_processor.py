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
      <h1>Welcome to my webpage!</h1>
    </header>
    <div id="content">
      <nav>
        <div class="MenuWrap">
          <a href="./index.html" class="FirstItem">Main site</a>
          <a href="./about.html" class="ListItem">About</a>
          <a href="./contact.html" class="SelectedLastItem">Contact</a>
        </div>
      </nav>
      <main>
        <h2>Contact details</h2>
        <h3>Phone number:</h3>
        <p>124912481248</p>
        <h3>E-mail: example@example.com</h3>
        <script src="./email.js"></script>
      </main>
    </div>
  </div>
</body>
</html>
'''
    result = "".join([
      " Gall Anonim Welcome to my webpage! Main site ",
      "About Contact Contact details Phone number: 124912481248 ",
      "E-mail: example@example.com ",
      ])
    cleaner = Cleaner()
    processed_html = process(cleaner, content)
    compact_html = re.sub("[\n' ']+", ' ', processed_html)
    assert compact_html == result
