from pathlib import Path
from typing import List, Set


def parse_file(path: Path) -> List[str]:
    return _uniq([site for line in path.read_text().split('\n') if (site := line.strip())])


def _uniq(lst: List[str]) -> List[str]:
    seen: Set[str] = set()
    seen_add = seen.add
    return [seen_add(elem) or elem for elem in lst if elem not in seen]
