from schema import *
from parse import *


def test_status():
    j = get_json("status")
    j = parse_json(j)
    assert valid(Status, j)


def test_data():
    j = get_json("data")
    j = j["1"]
    j = parse_json(j)
    assert valid(Data, j)


def test_quote():
    j = get_json("data")
    j = j["1"]['quote']['RUB']
    j = parse_json(j)
    assert valid(Quote, j)
