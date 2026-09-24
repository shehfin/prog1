from app import square, is_even

def test_square():
    assert square(5) == 25

def test_is_even():
    assert is_even(8) is True