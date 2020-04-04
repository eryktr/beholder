import pytest
import pathlib
import requests
import beholder.errors as errors

from beholder.fetcher import WebFetcher


def test_fetch_raises_for_invalid_statcode(mocker, monkeypatch):
    res_mock = mocker.Mock(status_code=999)
    monkeypatch.setattr(requests, 'get', lambda addr: res_mock)
    fetcher = WebFetcher()

    with pytest.raises(errors.IncorrectStatusError):
        fetcher.fetch('www.hello-world.com', pathlib.Path() / 'file.html')
