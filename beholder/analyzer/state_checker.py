import time
from argparse import Namespace
from typing import List, Optional

from beholder.analyzer.file_manager import FileManager
from beholder.fetcher import WebFetcher
from beholder.file_comparator.comparator_factory import ComparatorFactory
from beholder.file_comparator.comparators import FileComparator
from beholder.file_comparator.reporter_factory import ReporterFactory
from beholder.file_comparator.reporters import Reporter


class StateChecker:
    __slots__ = ('comparator', 'fetcher', 'sites', 'time', 'reporter', 'file_manager')

    comparator: FileComparator
    fetcher: WebFetcher
    sites: List[str]
    time: int
    reporter: Reporter
    file_manager: FileManager
    output_path: Optional[str] = None

    def __init__(self, sites: List[str], opts: Namespace):
        self.sites = sites
        self.time = opts.time
        self.comparator = ComparatorFactory.create(opts.show_diffs)
        self.reporter = ReporterFactory.create(opts.output_path)
        self.file_manager = FileManager(sites)
        self.fetcher = WebFetcher()

    def run(self) -> None:
        self._download_websites()
        while 1:
            for site in self.sites:
                latest_path = self.file_manager.latest_path(site)
                chall_path = self.file_manager.chall_path(site)
                self.fetcher.fetch(site, chall_path)
                res = self.comparator.compare(latest_path, chall_path)
                if not res.equal:
                    self.reporter.report(site, res)
                    latest_path.write_text(chall_path.read_text())
            time.sleep(self.time)

    def _download_websites(self) -> None:
        for site in self.sites:
            path = self.file_manager.latest_path(site)
            self.fetcher.fetch(site, path)
