from bank import value


def test_value():

    assert value("hi") == 20
    assert value("hello") == 0
    assert value("HELLO") == 0

