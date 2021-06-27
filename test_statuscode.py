from parse import get_coinmarket


def test():
    q = get_coinmarket()
    assert q.status_code == 200
