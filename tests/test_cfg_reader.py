import pathlib

import beholder.cfg_reader as cfg_reader
from beholder.cfg_reader import find_incorrect_websites
from beholder.cfg_reader import protocol_correct, file_valid


def test_protocol_is_correct_ok():
    assert protocol_correct("http://website.loc")


def test_protocol_is_correct_fail():
    assert not protocol_correct("addr")


def test_find_incorrect_websites_bad():
    bad_website = "eryktrzeciakiewicz.pl"
    incorrect_list = [bad_website] * 2
    assert len(find_incorrect_websites(incorrect_list)) == 2


def test_find_incorect_websites_good():
    good_website = "https://eryktrzeciakiewicz.pl"
    correct_list = [good_website] * 2
    assert not (len(find_incorrect_websites(correct_list)))


def test_file_valid_invalid_file(monkeypatch):
    txt = "http://address.dom\nhttp://ad.do\n\nnotaddr\n\n"
    monkeypatch.setattr(cfg_reader.Path, 'read_text', lambda path: txt)
    monkeypatch.setattr(cfg_reader.Path, 'is_file', lambda path: True)
    assert not file_valid(pathlib.Path())


def test_file_valid_valid_file(monkeypatch):
    txt = "http://address.dom\nhttp://ad.do\n\n\n"
    monkeypatch.setattr(cfg_reader.Path, 'is_file', lambda path: True)
    monkeypatch.setattr(cfg_reader.Path, 'read_text', lambda path: txt)
    assert file_valid(pathlib.Path())


def test_file_valid_not_a_file(monkeypatch):
    monkeypatch.setattr(cfg_reader.Path, 'is_file', lambda path: False)
    assert not file_valid(pathlib.Path())
