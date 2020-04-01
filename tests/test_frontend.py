import pytest
import beholder.argparser as argparser
import beholder.cfg_reader as cfg_reader
import beholder.opts_validator as validator
import beholder.errors as err
from pathlib import Path
from . import utils as u


@pytest.mark.parametrize("argv", [
    u.mkargv(["-t", "100", "-o", "out.txt", "-d", str(Path("tests") / "correct.txt")]),
    u.mkargv([str(Path("tests") / "correct.txt")]),
    u.mkargv(["-t", "100", "-o", "out.txt", "-d", str(Path("tests") / "correct2.txt")]),
    u.mkargv([str(Path("tests") / "correct2.txt")]),
])
def test_frontend_correct(argv, correct_cfgfile_paths):
    correct, correct_2 = correct_cfgfile_paths
    opts = argparser.parse(argv[1:])
    validator.validate_opts(opts)
    cfg_reader.validate_websites(correct)
    cfg_reader.validate_websites(correct_2)


@pytest.mark.parametrize("argv", [
    u.mkargv(["-t", "100", "-o", "out.txt", "-d", str(Path("tests") / "incorrect.txt")]),
    u.mkargv([str(Path("tests") / "incorrect.txt")]),
])
def test_frontend_incorrect(argv, incorrect_cfgfile_path):
    incorrect = incorrect_cfgfile_path
    opts = argparser.parse(argv[1:])
    validator.validate_opts(opts)
    with pytest.raises(err.IncorrectWebsitesError):
        cfg_reader.validate_websites(incorrect)
