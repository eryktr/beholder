from datetime import datetime
from typing import NamedTuple, List

import pytest

from beholder.file_comparator.comparators import ComparisonResult
import beholder.reports.report_builder as report_builder


class TestCase(NamedTuple):
    site: str
    diffs: List[str]
    with_diffs: bool
    expected_report: str


def safezip(*args):
    if any(len(arg) != len(args[0]) for arg in args):
        raise ValueError("All iterables must be of the same length.")
    return zip(*args)


def testcases():
    sites = (
        "https://site1.com",
        "https://site2.pl",
        "https://site3.us",
        "https://site4.uk",
    )
    diffs_list = (
        [],
        ["diff1"],
        ["diff2", "diff3"],
        ["diff4", "diff5", "diff6"],
    )
    with_diffs_list = (
        True,
        True,
        True,
        False,
    )
    reports = (
        "NOW - https://site1.com - Website has not changed.",
        "NOW - https://site2.pl - Website has changed.diff1",
        "NOW - https://site3.us - Website has changed.diff2\ndiff3",
        "NOW - https://site4.uk - Website has changed.",
    )

    return [
        TestCase(site=site, diffs=diffs, with_diffs=with_diffs, expected_report=report)
        for site, diffs, with_diffs, report
        in safezip(sites, diffs_list, with_diffs_list, reports)
    ]


class DatetimeMock(datetime):
    @classmethod
    def now(cls, tz=None):
        return "NOW"


@pytest.mark.parametrize("testcase", testcases())
def test_reports_are_build_correctly(monkeypatch, testcase):
    monkeypatch.setattr(report_builder, "datetime", DatetimeMock)
    site = testcase.site
    comparison_result = ComparisonResult(testcase.diffs)
    with_diffs = testcase.with_diffs
    expected_report = testcase.expected_report

    assert report_builder.build(site, comparison_result, with_diffs) == expected_report
