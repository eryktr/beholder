from beholder.analyzer.state_checker import StateChecker
# from beholder.analyzer.site import Site
from unittest.mock import Mock
from typing import NamedTuple, List
from argparse import Namespace

import pytest


class TestCase(NamedTuple):
    sites: List[str]
    sites_first_content: List[str]
    sites_second_content: List[str]
    with_diffs: bool


def safezip(*args):
    if any(len(arg) != len(args[0]) for arg in args):
        raise ValueError("All iterables must be of the same length.")
    return zip(*args)


def testcases():
    sites = ([
         "https://site1.com",
         "https://site2.pl",
        ],
    )
    sites_first_content_list = ([
        "<p>Current number of DSJ4 players: 7</p><p>Current number of DSJ3 players: 5</p>",
        "<p>Current number of DSJ4 players: 5</p><p>Current number of DSJ3 players: 5</p>",
    ],
    )
    sites_second_content_list = ([
        "<p>Current number of DSJ4 players: 3</p><p>Current number of DSJ3 players: 6</p>",
        "<p>Current number of DSJ4 players: 5</p><p>Current number of DSJ3 players: 5</p>",
    ],
    )
    with_diffs_list = ([
        True,
    ],
    )

    return [
        TestCase(sites=sites, sites_first_content=first_content,
                 sites_second_content=second_content, with_diffs=with_diffs)
        for sites, first_content, second_content, with_diffs
        in safezip(sites, sites_first_content_list, sites_second_content_list, with_diffs_list)
    ]


@pytest.mark.parametrize("testcase", testcases())
def test_state_checker(monkeypatch, testcase):
    diffs = testcase.with_diffs[0]
    websites = testcase.sites
    opts = Namespace(config_path=Mock(),
                     output_path=None,
                     show_diffs=diffs,
                     time=5)
    checker = StateChecker(websites, opts, 1)
    assert [site[0] for site in checker.sites] == websites
