from itertools import permutations
from pathlib import Path
from beholder.cfg_reader import protocol_is_correct, arguments_are_valid
from beholder.cfg_reader import find_incorrect_websites
# from beholder.cfg_reader import file_is_valid


def test_protocol_is_correct():
    rand_comb = [''.join(p) for p in permutations('eryktr')]
    for comb in rand_comb:
        assert protocol_is_correct(comb.join(["https://", ".pl"]))
        assert not(protocol_is_correct(comb.join(".pl")))


def test_arguments_are_valid():
    cwd = Path.cwd()
    arguments = ["cfg_reader.py", "-t", "5050"]
    arguments.append(Path.joinpath(cwd, "tests", "correct.txt"))
    other_arguments = ["cfg_reader.py", "-t", "05050"]
    assert arguments_are_valid(arguments)
    assert not(arguments_are_valid(other_arguments))


def test_find_incorrect_websites():
    correct_list = []
    incorrect_list = []
    for i in range(0, 12):
        correct_list.append("https://eryktrzeciakiewicz.pl")
        incorrect_list.append("eryktrzeciakiewicz.pl")
    assert not(len(find_incorrect_websites(correct_list)))
    assert len(find_incorrect_websites(incorrect_list)) == 12


""" def test_file_is_valid():
    cwd = Path.cwd()
    assert file_is_valid(Path.joinpath(cwd, "tests", "correct.txt")) """
