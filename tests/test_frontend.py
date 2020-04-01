import pytest
import beholder.argparser as argparser
import beholder.cfg_reader as cfg_reader
import beholder.opts_validator as validator
import beholder.errors as err
from pathlib import Path


@pytest.mark.parametrize("args", [
    ["-t", "100", "-o", "out.txt", "-d", str(Path("tests") / "correct.txt")],
    [str(Path("tests") / "correct.txt")],
    ["-t", "100", "-o", "out.txt", "-d", str(Path("tests") / "correct2.txt")],
    [str(Path("tests") / "correct2.txt")]
])
def test_frontend_correct(args, correct_cfgfile_paths):
    correct, correct_2 = correct_cfgfile_paths
    opts = argparser.parse(args)
    validator.validate_opts(opts)
    cfg_reader.validate_websites(correct)
    cfg_reader.validate_websites(correct_2)


@pytest.mark.parametrize("args", [
    ["-t", "100", "-o", "out.txt", "-d", str(Path("tests") / "incorrect.txt")],
    [str(Path("tests") / "incorrect.txt")],
])
def test_frontend_incorrect(args, incorrect_cfgfile_paths):
    incorrect = incorrect_cfgfile_paths
    opts = argparser.parse(args)
    validator.validate_opts(opts)
    with pytest.raises(err.IncorrectWebsitesError):
        cfg_reader.validate_websites(incorrect)
