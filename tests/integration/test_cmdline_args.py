import pytest

import beholder.argparser as argparser
import beholder.opts_validator as validator


@pytest.mark.integration
def test_args_are_parsed_and_validated(paths):
    cfg_file, out_file = paths
    args = ["-t", "70", "-o", str(out_file), "-d", str(cfg_file)]

    opts = argparser.parse(args)

    assert opts.time == 70
    assert opts.output_path == out_file
    assert opts.config_path == cfg_file
    assert opts.show_diffs

    validator.validate_opts(opts)
