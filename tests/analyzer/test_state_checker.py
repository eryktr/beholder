import pytest
import time

from unittest.mock import Mock
from beholder.analyzer.state_checker import StateChecker
from beholder.fetcher import WebFetcher

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


@pytest.mark.integration
def test_state_checker(monkeypatch):
    state_checker = create_state_checker(1, None, False, Mock())
    monkeypatch.setattr(WebFetcher, 'fetch', lambda self, site, path: fetch(self, site, path))
    monkeypatch.setattr(StateChecker, 'run', lambda self: run(self))
    state_checker.run()
