from beholder.analyzer.site import Site
from beholder.analyzer.state_checker import StateChecker
from pathlib import Path

import requests
import beholder.processor as processor
import beholder.reports.report_builder as report_builder


def test_check_site(mocker, paths, state_paths, monkeypatch):
    cfg_file, out_file = paths
    old_file, new_file = state_paths
    site = Site("dummy", old_file, new_file)
    opts = mocker.Mock(config_path=cfg_file, output_path=out_file, time=30, show_diffs=False)
    checker = StateChecker([site], opts, 1)

    res_mock = mocker.Mock(status_code=200)
    monkeypatch.setattr(requests, 'get', lambda addr: res_mock)
    monkeypatch.setattr(Path, 'write_text', mocker.Mock())
    monkeypatch.setattr(processor, 'process', mocker.Mock())

    checker._check_site(site)
    compare = checker.comparator.compare(site.reference_path, site.update_path)

    assert "Website has not changed" in report_builder.build(site.addr,
                                                             compare,
                                                             with_diffs=False)
