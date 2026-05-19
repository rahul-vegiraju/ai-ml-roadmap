from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True



def test_invalid_range():
    assert validate("275.3.6.28") == False
   


def test_invalid_format():
    assert validate("1.2.3") == False
