from pathlib import Path
from typing import Optional, Protocol, List


class Handler(Protocol):
    def handle(self, report: str) -> None:
        pass


class StdoutHandler:
    def handle(self, report: str) -> None:
        print(report)


class FileHandler:
    fpath: Path

    def __init__(self, fpath: Path):
        self.fpath = fpath

    def handle(self, report: str) -> None:
        with self.fpath.open(mode="a") as fd:
            fd.write("".join([report, "\n"]))


class Reporter:
    handlers: List[Handler]

    def __init__(self, handlers: list):
        self.handlers = handlers

    def report(self, report: str) -> None:
        for handler in self.handlers:
            handler.handle(report)

    @classmethod
    def get(cls, output_path: Optional[Path] = None):
        handlers: List[Handler] = [StdoutHandler()]
        if output_path:
            handlers.append(FileHandler(output_path))
        return cls(handlers)
