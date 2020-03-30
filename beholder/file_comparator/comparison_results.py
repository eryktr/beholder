import abc
from typing import List
from dataclasses import dataclass


@dataclass(frozen=True)
class ComparisonResult(abc.ABC):
    equal: bool


@dataclass(frozen=True)
class SimpleComparisonResult(ComparisonResult):
    pass


@dataclass(frozen=True)
class WithDiffsComparisonResult(ComparisonResult):
    diffs: List[str]
