import pytest


@pytest.fixture
def paths(tmp_path):
    cfg_file = tmp_path / 'config.cfg'
    cfg_file.touch()
    out_file = tmp_path / 'output.out'
    return cfg_file, out_file


@pytest.fixture
def state_paths(tmp_path):
    old_file = tmp_path / '1o.html'
    old_file.touch()
    new_file = tmp_path / '1n.html'
    new_file.touch()
    return old_file, new_file
