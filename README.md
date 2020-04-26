[![codecov](https://codecov.io/gh/eryktr/beholder/branch/master/graph/badge.svg?token=A0N7L9YHXS)](https://codecov.io/gh/eryktr/beholder)

# beholder
A tool to inform about latest updates on websites it tracks

# Usage
    usage: beholder [-h] [-t TIME] [-o OUTPUT_PATH] [-d] config_path

    positional arguments:
      config_path           Path to the config file containing website addresses.

    optional arguments:
      -h, --help            show this help message and exit
      -t TIME, --time TIME  Number of seconds between subsequent checks. (default: 5)
      -o OUTPUT_PATH, --output_path OUTPUT_PATH
                            File where the session should be dumped. (default: None)
      -d, --show_diffs      Display not only if something changes but also what changes. (default: False)

# Python requirement
Beholder requires Python >= 3.8.0.

# Installation (for developers)

    sudo apt install python3.8-venv
    python3.8 -m venv env
    source env/bin/activate
    pip3 install -e .[dev]
