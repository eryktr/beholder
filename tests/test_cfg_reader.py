from itertools import permutations
from beholder.cfg_reader import (
    protocol_correct, find_incorrect_websites
)


def test_protocol_correct_ok():
    rand_comb = [''.join(p) for p in permutations('eryktr')]
    for comb in rand_comb:
        assert protocol_correct(comb.join(["https://", ".pl"]))


def test_protocol_correct_fail():
    rand_comb = [''.join(p) for p in permutations('eryktr')]
    for comb in rand_comb:
        assert not(protocol_correct(comb.join(".pl")))


def test_find_incorrect_websites_bad():
    bad_website = "eryktrzeciakiewicz.pl"
    incorrect_list = [bad_website] * 2
    assert len(find_incorrect_websites(incorrect_list)) == 2


def test_find_incorect_websites_good():
    good_website = "https://eryktrzeciakiewicz.pl"
    correct_list = [good_website] * 2
    assert not(len(find_incorrect_websites(correct_list)))
