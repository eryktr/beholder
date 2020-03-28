from pathlib import Path
from typing import List
import beholder.errors as err


def protocol_correct(addr: str) -> bool:
    return addr.startswith("https://") or addr.startswith("http://")


def find_incorrect_websites(sites: List[str]) -> List[str]:
    inc_websites = [site for site in sites if not protocol_correct(site)]
    return inc_websites


def file_valid(path: Path) -> bool:
    if not path.exists():
        raise err.PathNotFoundError(path)
    elif not path.is_file():
        raise FileNotFoundError(path)
    sites = _parse_file(path)
    bad_websites = find_incorrect_websites(sites)
    if len(bad_websites):
        raise err.IncorrectWebsitesError(bad_websites)
    return True


def _parse_file(path: Path) -> List[str]:
    return [line for line in path.read_text().split('\n') if line]
