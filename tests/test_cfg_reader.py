import pathlib

import pytest

from beholder.cfg_reader import parse_file
from beholder.cfg_validator import _protocol_correct, validate_websites
from beholder.errors import IncorrectWebsitesError


def test_protocol_is_correct_ok():
    assert _protocol_correct("http://website.loc")


def test_protocol_is_correct_fail():
    assert not _protocol_correct("addr")


def test_find_incorrect_websites_bad(monkeypatch):
    txt = "https://eryktr.pl\neryktr.pl\n"
    monkeypatch.setattr(pathlib.Path, 'read_text', lambda path: txt)
    monkeypatch.setattr(pathlib.Path, 'is_file', lambda path: True)
    lst = parse_file(pathlib.Path())
    with pytest.raises(IncorrectWebsitesError):
        validate_websites(lst)


def test_validate_websites_very_bad(monkeypatch):
    txt = "http://address.dom\nhttp://ad.do\n\nnotaddr\n\n"
    monkeypatch.setattr(pathlib.Path, 'read_text', lambda path: txt)
    monkeypatch.setattr(pathlib.Path, 'is_file', lambda path: True)
    lst = parse_file(pathlib.Path())
    with pytest.raises(IncorrectWebsitesError):
        validate_websites(lst)
