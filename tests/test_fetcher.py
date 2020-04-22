import pathlib

import pytest
import requests

from beholder.errors import IncorrectStatusError
from beholder.fetcher import WebFetcher


def test_fetch_raises_for_invalid_statcode(mocker, monkeypatch):
    res_mock = mocker.Mock(status_code=999)
    monkeypatch.setattr(requests, 'get', lambda addr: res_mock)
    fetcher = WebFetcher()

    with pytest.raises(IncorrectStatusError):
        fetcher.fetch('www.hello-world.com', pathlib.Path() / 'file.html')


def test_fetch_correct(mocker, monkeypatch):
    res_mock = mocker.Mock(status_code=200)
    monkeypatch.setattr(requests, 'get', lambda addr: res_mock)
    monkeypatch.setattr(pathlib.Path, 'write_text', mocker.Mock())
    fetcher = mocker.Mock()
    fetcher.fetch('www.hello-world.com', pathlib.Path() / 'file.html')

