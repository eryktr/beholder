import pytest
from pathlib import Path


@pytest.fixture
def paths(tmp_path):
    cfg_file = tmp_path / 'config.cfg'
    cfg_file.touch()
    out_file = tmp_path / 'output.out'
    return cfg_file, out_file


@pytest.fixture
def correct_cfgfile_paths():
    correct = Path("tests") / "correct.txt"
    correct_2 = Path("tests") / "correct2.txt"
    return correct, correct_2


@pytest.fixture
def incorrect_cfgfile_path():
    incorrect = Path("tests") / "incorrect.txt"
    return incorrect
