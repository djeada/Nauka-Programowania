"""
Otrzymujesz napis. Zamień wszystkie małe litery na wielkie.
"""


def na_male(napis):
    return napis.lower()


def test_na_male():
    assert na_male("test") == "test"
    assert na_male("Test") == "test"
    assert na_male("TEST") == "test"


if __name__ == "__main__":
    test_na_male()
