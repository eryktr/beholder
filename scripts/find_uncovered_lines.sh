#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )";
PYTHONPATH=$(pwd);
pytest --cov="$PYTHONPATH/beholder" --cov-config="$PYTHONPATH/.coveragerc" \
  --cov-report=term-missing --rootdir="$PYTHONPATH";