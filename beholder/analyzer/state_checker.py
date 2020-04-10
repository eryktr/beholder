from typing import List
import time
from beholder.fetcher import WebFetcher
from beholder.analyzer.file_manager import FileManager
from beholder.file_comparator.comparators import FileComparator
from argparse import Namespace


class StateChecker:
    comparator: FileComparator

    def __init__(self, comparator: FileComparator):
        self.comparator = comparator

    def run(self, opts: Namespace, sites: List[str]) -> None:
        fetcher = WebFetcher()
        manager = FileManager(sites)
        while True:
            for addr in sites:
                latest_path = manager.latest_path(addr)
                fetcher.fetch(addr, latest_path)
            time.sleep(opts.time)
            for addr in sites:
                latest_path = manager.latest_path(addr)
                chall_path = manager.chall_path(addr)
                fetcher.fetch(addr, chall_path)
                cmp_res = self.comparator.compare(latest_path, chall_path)
                eq = cmp_res.equal
                info = ""
                if not(eq):
                    info = cmp_res.__str__(addr)
                if opts.output_path and info:
                    with open(str(opts.output_path), mode='a') as f:
                        f.write(info)
                elif not(opts.output_path):
                    print(info)
