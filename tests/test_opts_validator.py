import pytest

import beholder.opts_validator as validator


def test_validate_opts_passes(mocker, paths):
    cfg_file, out_file = paths
    opts = mocker.Mock(config_path=cfg_file, output_path=out_file, time=30, show_diffs=False)

    validator.validate_opts(opts)


def test_validate_opts_fails_invalid_time(mocker, paths):
    cfg_file, out_file = paths
    opts = mocker.Mock(config_path=cfg_file, output_path=out_file, time=0, show_diffs=False)

    with pytest.raises(ValueError):
        validator.validate_opts(opts)


def test_validate_opts_fails_cfg_file_doesnt_exist(mocker, tmp_path):
    cfg_file = tmp_path / 'config.cfg'
    opts = mocker.Mock(config_path=cfg_file, output_path=None, time=10, show_diffs=True)

    with pytest.raises(FileNotFoundError):
        validator.validate_opts(opts)


def test_validate_opts_faild_out_file_exists(mocker, paths):
    cfg_file, out_file = paths
    out_file.touch()
    opts = mocker.Mock(config_path=cfg_file, output_path=out_file, time=10, show_diffs=True)

    with pytest.raises(FileExistsError):
        validator.validate_opts(opts)
