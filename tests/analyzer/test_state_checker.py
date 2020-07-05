from beholder.analyzer.site import Site
from beholder.analyzer.state_checker import StateChecker
from beholder.const import HTTPStatus
from pathlib import Path

import pytest
import requests
import beholder.processor as processor
import beholder.reports.report_builder as report_builder


@pytest.fixture
def state_paths(tmp_path):
    old_file = tmp_path / '1o.html'
    old_file.touch()
    new_file = tmp_path / '1n.html'
    new_file.touch()
    return old_file, new_file


def test_check_site(mocker, paths, state_paths, monkeypatch):
    cfg_file, out_file = paths
    old_file, new_file = state_paths
    opts = mocker.Mock(config_path=cfg_file, output_path=out_file, time=30, show_diffs=False)
    sites = [Site("dummy", old_file, new_file)]
    checker = StateChecker(sites, opts)

    res_mock = mocker.Mock(status_code=HTTPStatus.OK)
    simple_mock = mocker.Mock()

    monkeypatch.setattr(requests, "get", lambda addr: res_mock)
    monkeypatch.setattr(Path, "write_text", simple_mock)
    monkeypatch.setattr(processor, "process", simple_mock)

    checker._check_site(sites[0])
    res = checker.comparator.compare(sites[0].reference_path, sites[0].update_path)

    assert "Website has not changed" in report_builder.build(sites[0].addr, res, with_diffs=False)
