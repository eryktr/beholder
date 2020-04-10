from pathlib import Path
from typing import List, Set
import beholder.errors as err


def protocol_correct(addr: str) -> bool:
    return addr.startswith("https://") or addr.startswith("http://")


def find_incorrect_websites(sites: List[str]) -> List[str]:
    return [site for site in sites if not protocol_correct(site)]


def validate_websites(sites: List[str]) -> None:
    inc_sites = find_incorrect_websites(sites)
    if inc_sites:
        raise err.IncorrectWebsitesError(inc_sites)


def parse_file(path: Path) -> List[str]:
    return _uniq([line for line in path.read_text().split('\n') if line])


def _uniq(lst: List[str]) -> List[str]:
    seen: Set[str] = set()
    seen_add = seen.add
    return [seen_add(elem) or elem for elem in lst if elem not in seen]
