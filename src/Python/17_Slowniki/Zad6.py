"""
Otrzymujesz napis. Znajdz czestosc wystepowania znakow w otrzymanym 
napisie. Inaczej, zwroc histogram znakow w otrzymanym napisie.
"""


def histogram(napis):
    """
    Funkcja zwraca slownik zawierajacy wszystkie litery w napisie oraz czestosc ich wystepowania.
    """
    histogram = {}
    for znak in napis:
        if znak in histogram:
            histogram[znak] += 1
        else:
            histogram[znak] = 1
    return histogram


def test_histogram():
    assert histogram("") == {}
    assert histogram("ala") == {"a": 2, "l": 1}
    assert histogram("ala ma kota") == {
        "a": 4,
        " ": 2,
        "k": 1,
        "l": 1,
        "m": 1,
        "o": 1,
        "t": 1,
    }


if __name__ == "__main__":
    test_histogram()