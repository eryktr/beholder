import abc
import difflib
import filecmp
from pathlib import Path
from beholder.file_comparator.comparison_results import (
    ComparisonResult, SimpleComparisonResult, WithDiffsComparisonResult,
)


class ComparisonType(abc.ABC):
    @abc.abstractmethod
    def compare(self, file1: Path, file2: Path) -> ComparisonResult:
        pass


class SimpleComparison(ComparisonType):
    def compare(self, file1: Path, file2: Path) -> ComparisonResult:
        return SimpleComparisonResult(filecmp.cmp(str(file1), str(file2)))


class WithDiffsComparison(ComparisonType):
    def compare(self, file1: Path, file2: Path) -> ComparisonResult:
        equal = filecmp.cmp(str(file1), str(file2))
        if equal:
            return WithDiffsComparisonResult(equal, [])
        content1 = file1.read_text().split("\n")
        content2 = file2.read_text().split("\n")
        diffs = difflib.unified_diff(content1, content2)
        return WithDiffsComparisonResult(False, [*diffs])
