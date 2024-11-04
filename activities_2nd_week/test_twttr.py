
from twttr import shorten


def test_shorten():

    assert shorten("HELLO") == "HLL"
    assert shorten("123good") == "123gd"
    assert shorten("hi.hi") == "h.h"
    assert shorten("aB") == "B"
