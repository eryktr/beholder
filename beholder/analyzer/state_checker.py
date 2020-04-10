from typing import List
import time
from beholder.__doc__fetcher import WebFetcher
from beholder.analyzer.file_manager import FileManager
from beholder.file_comparator.comparators import FileComparator


class StateChecker:
    comparator: FileComparator

    def __init__(self, comparator: FileComparator):
        self.comparator = comparator

    def run(self, path: str, t: int, sites: List[str]) -> None:
        fetcher = WebFetcher()
        manager = FileManager(sites)
        if path:
            output = path
        while True:
            for addr in sites:
                l_path = manager.latest_path(addr)
                fetcher.fetch(addr, l_path)
            time.sleep(t)
            for addr in sites:
                l_path = manager.latest_path(addr)
                c_path = manager.chall_path(addr)
                fetcher.fetch(addr, c_path)
                cmp = self.comparator.compare(c_path, l_path)
                eq = cmp.equal
                info = ""
                if not(eq):
                    info = "Found changes on website:" + addr
                    if 'diffs' in vars(cmp):
                        differences = self.comparator.compare(c_path, l_path).diffs
                        for diff in differences:
                            info += diff
                if path and info:
                    with open(output, mode='a') as f:
                        print(info, file=f)
                elif not(path):
                    print(info)
                    
