from pathlib import Path

import pytest

import beholder.argparser as argparser
import beholder.cfg_reader as cfg_reader
import beholder.cfg_validator as cfg_validator
import beholder.opts_validator as opts_validator
from beholder.errors import IncorrectWebsitesError
from tests.utils import mkargv


@pytest.fixture
def correct_cfgfile_paths():
    correct = Path("tests") / "correct.txt"
    correct_2 = Path("tests") / "correct2.txt"
    return correct, correct_2


@pytest.fixture
def incorrect_cfgfile_path():
    incorrect = Path("tests") / "incorrect.txt"
    return incorrect


@pytest.mark.parametrize("argv", [
    mkargv(["-t", "100", "-o", "out.txt", "-d", str(Path("tests") / "correct.txt")]),
    mkargv([str(Path("tests") / "correct.txt")]),
    mkargv(["-t", "100", "-o", "out.txt", "-d", str(Path("tests") / "correct2.txt")]),
    mkargv([str(Path("tests") / "correct2.txt")]),
])
def test_frontend_correct(argv, correct_cfgfile_paths):
    correct, correct_2 = correct_cfgfile_paths
    opts = argparser.parse(argv[1:])
    opts_validator.validate_opts(opts)
    sites1 = cfg_reader.parse_file(correct)
    sites2 = cfg_reader.parse_file(correct_2)
    cfg_validator.validate_websites(sites1)
    cfg_validator.validate_websites(sites2)


@pytest.mark.parametrize("argv", [
    mkargv(["-t", "100", "-o", "out.txt", "-d", str(Path("tests") / "incorrect.txt")]),
    mkargv([str(Path("tests") / "incorrect.txt")]),
])
def test_frontend_incorrect(argv, incorrect_cfgfile_path):
    incorrect = incorrect_cfgfile_path
    opts = argparser.parse(argv[1:])
    opts_validator.validate_opts(opts)
    sites = cfg_reader.parse_file(incorrect)
    with pytest.raises(IncorrectWebsitesError):
        cfg_validator.validate_websites(sites)
