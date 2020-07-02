import beholder.reports.report_builder as report_builder
from beholder.analyzer.site import Site
from beholder.analyzer.state_checker import StateChecker
from beholder.file_comparator.comparators import FileComparator
from beholder.file_comparator.comparators import ComparisonResult

from pathlib import Path


def my_check_site(site, with_diffs):
    latest_path = site.reference_path
    chall_path = site.update_path
    comparator = FileComparator()
    res = comparator.compare(latest_path, chall_path)
    report = report_builder.build(site.addr, res, with_diffs)
    return res, report


def test_check_site(mocker, paths):
    site = Site(mocker.Mock(),
                Path("tests") / "test_files" / "1o.html",
                Path("tests") / "test_files" / "1n.html")
    cfg_file, out_file = paths
    sh_diffs = False
    opts = mocker.Mock(config_path=cfg_file, output_path=out_file, time=30, show_diffs=sh_diffs)
    checker = StateChecker([site], opts, 1)
    checker._check_site = my_check_site
    site_check = my_check_site(site, sh_diffs)
    assert site_check[0] == ComparisonResult(diffs=[
                                                    '--- \n', '+++ \n',
                                                    '@@ -1 +1 @@\n',
                                                    '-<h1>Hello world!</h1>',
                                                    '+'])
    assert "Website has changed." in site_check[1]
