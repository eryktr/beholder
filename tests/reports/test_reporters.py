from beholder.reports.reporters import Reporter


class PathMock:
    captured = ""

    def __enter__(self):
        return self

    def __exit__(self, typ, val, tb):
        return self

    def open(self, mode=None):
        return self

    def write(self, txt):
        self.captured += txt


def test_reporter_with_file_handler_and_stdout_handler(capsys):
    report = "My report"
    output_path = PathMock()
    reporter = Reporter.get(output_path)

    reporter.report(report)

    assert capsys.readouterr().out == f"{report}\n"
    assert output_path.captured == report
