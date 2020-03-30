from beholder.file_comparator.comparison_types import ComparisonType
from beholder.file_comparator.comparison_results import ComparisonResult
from pathlib import Path


class FileComparator:
    comparison_type: ComparisonType

    def __init__(self, comparison_type: ComparisonType):
        self.comparison_type = comparison_type

    def compare(self, file1: Path, file2: Path) -> ComparisonResult:
        return self.comparison_type.compare(file1, file2)
