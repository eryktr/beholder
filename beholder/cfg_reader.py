from pathlib import Path
from typing import List


def protocol_is_correct(addr: str) -> bool:
    return addr.startswith("https://") or addr.startswith("http://")


def arguments_are_valid(args: List[str]) -> bool:
    return len(args) in (2, 4)


def find_incorrect_websites(sites: List[str]) -> List[str]:
    return [site for site in sites if not protocol_is_correct(site)]


def file_is_valid(path: Path) -> bool:
    sites = [line for line in path.read_text().split('\n') if line]
    return path.is_file() and not(len(find_incorrect_websites(sites)))


def check(data: List[str]) -> bool:
    return (arguments_are_valid(data) and
            (file_is_valid(Path(data[3])) or file_is_valid(Path(data[1]))))
