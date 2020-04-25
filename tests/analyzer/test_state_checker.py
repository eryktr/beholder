import pytest
import time

from unittest.mock import Mock
from beholder.analyzer.state_checker import StateChecker
from beholder.fetcher import WebFetcher
from beholder.file_comparator.comparators import FileComparator, ComparisonResult
from beholder.reports import report_builder

name1 = 'site_a'
name2 = 'site_b'


def fetch(self, site, path):
    path.write_text({
        name1: 'content_1',
        name2: 'content_2',
    }[site])


def run(self):
    self._download_websites()
    start = time.time()
    while time.time() - start < 3 * self.time:
        for site in self.sites:
            self._check_site(site)
        time.sleep(self.time)


def create_state_checker(time, output_path, show_diffs, config_path):
    sites = [name1, name2]
    opts = Mock(
        time=time,
        output_path=output_path,
        show_diffs=show_diffs,
        config_path=config_path,
    )
    state_checker = StateChecker(sites, opts)
    return state_checker


@pytest.fixture
def monkeypatched_state_checker(monkeypatch):
    monkeypatch.setattr(WebFetcher, 'fetch', lambda self, site, path: fetch(self, site, path))
    monkeypatch.setattr(StateChecker, 'run', lambda self: run(self))


def test_state_checker_no_diffs(monkeypatched_state_checker):
    state_checker = create_state_checker(0.2, None, False, Mock())
    state_checker.run()


def test_state_checker_diffs_found(monkeypatch, monkeypatched_state_checker):
    state_checker = create_state_checker(0.2, None, False, Mock())
    monkeypatch.setattr(
        FileComparator,
        'compare',
        lambda self, path1, path2: ComparisonResult(diffs=['diff']),
    )
    monkeypatch.setattr(report_builder, 'build', lambda site, res, with_diffs: Mock())
    state_checker.run()
