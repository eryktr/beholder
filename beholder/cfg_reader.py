from pathlib import Path
from typing import List


def protocol_correct(addr: str) -> bool:
    return addr.startswith("https://") or addr.startswith("http://")


def find_incorrect_websites(sites: List[str]) -> List[str]:
    return [site for site in sites if not protocol_correct(site)]


def parse_file(path: Path) -> List[str]:
    return [line for line in path.read_text().split('\n') if line]


def file_valid(path: Path) -> bool:
    if not path.is_file():
        return False
    sites = parse_file(path)
    return not any(find_incorrect_websites(sites))
