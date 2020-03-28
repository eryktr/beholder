import pathlib
import pytest
from beholder.cfg_reader import protocol_correct, file_valid
import beholder.errors as err


def test_protocol_is_correct_ok():
    assert protocol_correct("http://website.loc")


def test_protocol_is_correct_fail():
    assert not protocol_correct("addr")


def test_find_incorrect_websites_bad(monkeypatch):
    txt = "https://eryktr.pl\neryktr.pl\n"
    monkeypatch.setattr(pathlib.Path, 'read_text', lambda path: txt)
    monkeypatch.setattr(pathlib.Path, 'is_file', lambda path: True)
    with pytest.raises(err.IncorrectWebsitesError):
        file_valid(pathlib.Path())


def test_find_incorrect_websites_good(monkeypatch):
    txt = "https://eryktr.pl\nhttps://eryktr.pl\n"
    monkeypatch.setattr(pathlib.Path, 'read_text', lambda path: txt)
    monkeypatch.setattr(pathlib.Path, 'is_file', lambda path: True)
    assert file_valid(pathlib.Path())


def test_file_valid_invalid_file(monkeypatch):
    txt = "http://address.dom\nhttp://ad.do\n\nnotaddr\n\n"
    monkeypatch.setattr(pathlib.Path, 'read_text', lambda path: txt)
    monkeypatch.setattr(pathlib.Path, 'is_file', lambda path: True)
    with pytest.raises(err.IncorrectWebsitesError):
        file_valid(pathlib.Path())


def test_file_valid_valid_file(monkeypatch):
    txt = "http://address.dom\nhttp://ad.do\n\n\n"
    monkeypatch.setattr(pathlib.Path, 'is_file', lambda path: True)
    monkeypatch.setattr(pathlib.Path, 'read_text', lambda path: txt)
    assert file_valid(pathlib.Path())


def test_file_valid_not_a_file(monkeypatch):
    monkeypatch.setattr(pathlib.Path, 'is_file', lambda path: False)
    with pytest.raises(FileNotFoundError):
        file_valid(pathlib.Path())


def test_file_valid_path_not_exists(monkeypatch):
    monkeypatch.setattr(pathlib.Path, 'exists', lambda path: False)
    with pytest.raises(err.PathNotFoundError):
        file_valid(pathlib.Path())
