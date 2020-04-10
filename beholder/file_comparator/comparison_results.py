import abc
from typing import List
from dataclasses import dataclass


@dataclass(frozen=True)
class ComparisonResult(abc.ABC):
    equal: bool

    def __str__(self):
        pass


@dataclass(frozen=True)
class SimpleComparisonResult(ComparisonResult):
    pass

    def __str__(self):
        return "No change" if self.equal else "Changed"


@dataclass(frozen=True)
class WithDiffsComparisonResult(ComparisonResult):
    diffs: List[str]

    def __str__(self):
        return "Changed. Diffs: \n" + "".join(self.diffs)
