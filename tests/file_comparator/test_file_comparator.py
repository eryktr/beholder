import pytest

from beholder.file_comparator.comparators import FileComparator
from beholder.file_comparator.comparison_results import (
    SimpleComparisonResult, WithDiffsComparisonResult,
)
from beholder.file_comparator.comparison_types import SimpleComparison, WithDiffsComparison


@pytest.fixture
def equal_files_pair(tmp_path):
    content = '''
    <html>
        <head>
            <title>Hello world</title>
        </head>
        <body>
            <p>
                Once upon a time, there lived a young Python developer. One day,
                he got bored of having to dig through vague duck-typing studded
                endless chunks of poor quality code and the poor brave developer
                became
                a
                sailor.
            </p>
        </body>
    </html>
    '''
    f1 = tmp_path / 'f1.html'
    f2 = tmp_path / 'f2.html'
    f1.write_text(content)
    f2.write_text(content)
    return f1, f2


@pytest.fixture
def nonequal_files_pair(tmp_path):
    content1 = '''
    <html>
        <head>
        </head>
        <body>
        </body>
    </html>
    '''
    content2 = '''
    <html>
        <head>
            <title>Java1.7 + AWT -> Graphics Designer Starter Kit </title>
        </head>
        <body>
        </body>
    </html>
    '''
    f1 = tmp_path / 'f1.html'
    f2 = tmp_path / 'f2.html'
    f1.write_text(content1)
    f2.write_text(content2)
    return f1, f2


def test_simple_comparator_equal_files(equal_files_pair):
    f1, f2 = equal_files_pair
    comparator = FileComparator(comparison_type=SimpleComparison())

    result = comparator.compare(f1, f2)

    assert isinstance(result, SimpleComparisonResult)
    assert result.equal is True


def test_simple_comparator_nonequal_files(nonequal_files_pair):
    f1, f2 = nonequal_files_pair
    comparator = FileComparator(comparison_type=SimpleComparison())

    result = comparator.compare(f1, f2)

    assert isinstance(result, SimpleComparisonResult)
    assert result.equal is False


def test_with_diffs_comparator_equal_files(equal_files_pair):
    f1, f2 = equal_files_pair
    comparator = FileComparator(comparison_type=WithDiffsComparison())

    result = comparator.compare(f1, f2)

    assert isinstance(result, WithDiffsComparisonResult)
    assert result.equal is True
    assert result.diffs == []


def test_with_diffs_comparator_nonequal_files(nonequal_files_pair):
    f1, f2 = nonequal_files_pair
    comparator = FileComparator(comparison_type=WithDiffsComparison())

    result = comparator.compare(f1, f2)

    assert isinstance(result, WithDiffsComparisonResult)
    assert result.equal is False
    assert result.diffs == [
        '--- \n',
        '+++ \n',
        '@@ -1,6 +1,7 @@\n',
        ' ',
        '     <html>',
        '         <head>',
        '+            <title>Java1.7 + AWT -> Graphics Designer Starter Kit </title>',
        '         </head>', '         <body>', '         </body>',
    ]
