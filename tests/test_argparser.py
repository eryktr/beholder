import pathlib

import pytest

import beholder.argparser as argparser
import beholder.const as const


@pytest.mark.parametrize("args", [
    ["-t", "10", "-d"],
    ["-t", "config.cfg"],
    ["python3", "beholder.py", "-t", "-d", "config.cfg"],
    ["-t", "10", "-o", "7"],
    ["-t", "10", "o", "out.txt", "-q", "config.cfg"],
])
def test_argparser_fails(args):
    with pytest.raises(SystemExit):
        argparser.parse(args)


@pytest.mark.parametrize("args", [
    ["-t", "10", "-o", "output.txt", "-d", "config.cfg"],
    ["--output", "output.txt", "-d", "--time", "10", "config.cfg"],
    ["--output", "output.txt", "--show_diffs", "--time", "10", "config.cfg"],
])
def test_argparser_succeeds(args):
    opts = argparser.parse(args)

    assert opts.time == 10
    assert opts.output_path == pathlib.Path("output.txt")
    assert opts.show_diffs
    assert opts.config_path == pathlib.Path("config.cfg")


def test_argparser_default_values():
    args = ["--output", "output.txt", "config.cfg"]
    opts = argparser.parse(args)

    assert opts.time == const.DEFAULT_T
    assert opts.show_diffs == const.DEFAULT_D
