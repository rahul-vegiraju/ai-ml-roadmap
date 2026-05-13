from bank import value

def test_hello():

    assert value("Hello, Newman") == 0


def test_h():
    assert value("hey") == 20



def test_other():
    assert value("good morning") == 100
