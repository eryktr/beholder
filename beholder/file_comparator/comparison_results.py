import abc
from typing import List
from dataclasses import dataclass


@dataclass(frozen=True)
class ComparisonResult(abc.ABC):
    equal: bool

    def __str__(self, website: str) -> str:
        return "Found changes on website: " + website + "\n"


@dataclass(frozen=True)
class SimpleComparisonResult(ComparisonResult):
    pass


@dataclass(frozen=True)
class WithDiffsComparisonResult(ComparisonResult):
    diffs: List[str]

    def __str__(self, addr: str) -> str:
        msg = "Found changes on website: " + addr + "\n"
        for diff in self.diffs:
            msg += diff + "\n"
        return msg
