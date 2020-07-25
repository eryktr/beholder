from datetime import datetime

from beholder.file_comparator.comparators import ComparisonResult


def build(site: str, comparison_result: ComparisonResult, with_diffs: bool = False) -> str:
    now = datetime.now()
    diffs = comparison_result.diffs
    template = f"{now} - {site} - {{}}".format
    status = f"Website has {'not ' if not diffs else ''}changed."
    if with_diffs:
        status += "\n".join(diffs)
    return template(status)
