import pytest


@pytest.fixture
def paths(tmp_path):
    cfg_file = tmp_path / 'config.cfg'
    cfg_file.touch()
    out_file = tmp_path / 'output.out'
    return cfg_file, out_file
