from itertools import permutations
from pathlib import Path
from beholder.cfg_reader import correct_protocol, valid_arguments
from beholder.cfg_reader import correct_websites
from beholder.cfg_reader import valid_file


def test_corr_prot():
    rand_comb = [''.join(p) for p in permutations('eryktr')]
    for comb in rand_comb:
        assert correct_protocol(comb.join(["https://", ".pl"]))


def test_corr_prot_wrong():
    rand_comb = [''.join(p) for p in permutations('eryktr')]
    for comb in rand_comb:
        assert not(correct_protocol(comb.join(".pl")))


def test_val_arg_correct():
    cwd = Path.cwd()
    arguments = ["cfg_reader.py", "-t", "5050"]
    arguments.append(Path.joinpath(cwd, "tests", "correct.txt"))
    assert valid_arguments(arguments)


def test_val_arg_wrong():
    arguments = ["cfg_reader.py", "-t", "05050"]
    arguments.append("./nosuchfile.txt")
    assert not(valid_arguments(arguments))


def test_cor_websites():
    cwd = Path.cwd()
    assert correct_websites(Path.joinpath(cwd, "tests", "correct.txt"))


def test_wrong_websites():
    cwd = Path.cwd()
    assert not(correct_websites(Path.joinpath(cwd, "tests", "incorrect.txt")))


def test_valid_file():
    cwd = Path.cwd()
    assert valid_file(Path.joinpath(cwd, "tests", "correct.txt"))
