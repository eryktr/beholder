from beholder.file_comparator.comparators import FileComparator
from beholder.file_comparator.comparison_types import SimpleComparison, WithDiffsComparison


class ComparatorFactory:
    @staticmethod
    def create(diffs: bool) -> FileComparator:
        comparison_type = WithDiffsComparison() if diffs else SimpleComparison()
        return FileComparator(comparison_type)
