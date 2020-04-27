import time
from argparse import Namespace
from multiprocessing.dummy import Pool as ThreadPool
from typing import List

import beholder.reports.report_builder as report_builder
from beholder.analyzer.downloader import Downloader
from beholder.analyzer.file_manager import FileManager
from beholder.analyzer.site import Site
from beholder.fetcher.fetcher import WebFetcher
from beholder.file_comparator.comparators import FileComparator
from beholder.reports.reporters import Reporter


class StateChecker:
    comparator: FileComparator
    fetcher: WebFetcher
    sites: List[Site]
    time: int
    reporter: Reporter
    file_manager: FileManager
    show_diffs: bool = False
    thread_pool: ThreadPool

    def __init__(self, sites: List[str], opts: Namespace, num_threads: int = 1):
        file_manager = FileManager(sites)
        self.sites = [Site(site, file_manager.latest_path(site), file_manager.chall_path(site))
                      for site in sites]
        self.time = opts.time
        self.show_diffs = opts.show_diffs
        self.comparator = FileComparator()
        self.reporter = Reporter.get(getattr(opts, 'output_path', None))
        self.downloader = Downloader(WebFetcher())
        self.thread_pool = ThreadPool(num_threads)

    def run(self) -> None:
        self.thread_pool.map(self.downloader.download_reference, self.sites)
        while 1:
            self.thread_pool.map(self._check_site, self.sites)
            time.sleep(self.time)

    def _check_site(self, site: Site) -> None:
        self.downloader.download_updated(site)
        latest_path = site.reference_path
        chall_path = site.update_path
        res = self.comparator.compare(latest_path, chall_path)
        report = report_builder.build(site.addr, res, with_diffs=self.show_diffs)
        self.reporter.report(report)
        if res.diffs:
            latest_path.write_text(chall_path.read_text('utf8'), encoding='utf8')
