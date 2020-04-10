import abc
from datetime import datetime
from pathlib import Path

from beholder.file_comparator.comparison_results import ComparisonResult


class Reporter(abc.ABC):
    @abc.abstractmethod
    def report(self, site: str, result: ComparisonResult) -> str:
        pass


class BaseReporter(Reporter):
    def report(self, site: str, result: ComparisonResult) -> str:
        now = datetime.now()
        return f"{now} - {site} - {result}"


class StdoutReporter(Reporter):
    reporter: Reporter

    def __init__(self, reporter: Reporter):
        self.reporter = reporter

    def report(self, site: str, result: ComparisonResult) -> str:
        report = self.reporter.report(site, result)
        print(report)
        return report


class FileReporter(Reporter):
    reporter: Reporter
    file: Path

    def __init__(self, reporter: Reporter, path: Path):
        self.reporter = reporter
        self.path = path

    def report(self, site: str, result: ComparisonResult) -> str:
        report = self.reporter.report(site, result)
        with self.path.open(mode='a') as fd:
            fd.write(report)
        return report
