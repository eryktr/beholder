from itertools import permutations
from beholder.cfg_reader import protocol_is_correct, file_is_valid
from beholder.cfg_reader import find_incorrect_websites
import pathlib
import beholder.cfg_reader as cfg_reader


def test_protocol_is_correct_ok():
    rand_comb = [''.join(p) for p in permutations('eryktr')]
    for comb in rand_comb:
        assert protocol_is_correct(comb.join(["https://", ".pl"]))


def test_protocol_is_correct_fail():
    rand_comb = [''.join(p) for p in permutations('eryktr')]
    for comb in rand_comb:
        assert not (protocol_is_correct(comb.join(".pl")))


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
    assert not file_is_valid(pathlib.Path())


def test_file_valid_valid_file(monkeypatch):
    txt = "http://address.dom\nhttp://ad.do\n\n\n"
    monkeypatch.setattr(cfg_reader.Path, 'is_file', lambda path: True)
    monkeypatch.setattr(cfg_reader.Path, 'read_text', lambda path: txt)
    assert file_is_valid(pathlib.Path())


def test_file_valid_not_a_file(monkeypatch):
    monkeypatch.setattr(cfg_reader.Path, 'is_file', lambda path: False)
    assert not file_is_valid(pathlib.Path())
