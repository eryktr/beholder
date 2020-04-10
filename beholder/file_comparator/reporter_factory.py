from pathlib import Path
from typing import Optional

from beholder.file_comparator.reporters import BaseReporter, StdoutReporter, FileReporter


class ReporterFactory:
    @staticmethod
    def create(output_path: Optional[Path] = None):
        reporter = StdoutReporter(BaseReporter())
        if output_path:
            reporter = FileReporter(reporter, output_path)
        return reporter
