import pathlib
import pytest
from beholder.cfg_reader import protocol_correct, validate_websites, parse_file
import beholder.errors as err


def test_protocol_is_correct_ok():
    assert protocol_correct("http://website.loc")


def test_protocol_is_correct_fail():
    assert not protocol_correct("addr")


def test_find_incorrect_websites_bad(monkeypatch):
    txt = "https://eryktr.pl\neryktr.pl\n"
    monkeypatch.setattr(pathlib.Path, 'read_text', lambda path: txt)
    monkeypatch.setattr(pathlib.Path, 'is_file', lambda path: True)
    lst = parse_file(pathlib.Path())
    with pytest.raises(err.IncorrectWebsitesError):
        validate_websites(lst)


def test_validate_websites_very_bad(monkeypatch):
    txt = "http://address.dom\nhttp://ad.do\n\nnotaddr\n\n"
    monkeypatch.setattr(pathlib.Path, 'read_text', lambda path: txt)
    monkeypatch.setattr(pathlib.Path, 'is_file', lambda path: True)
    lst = parse_file(pathlib.Path())
    with pytest.raises(err.IncorrectWebsitesError):
        validate_websites(lst)
