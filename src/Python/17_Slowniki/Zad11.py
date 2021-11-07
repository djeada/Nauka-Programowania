"""
Otrzymujesz slownik skladajacy sie z par napisow i liczb calkowitych. 
a) Wypisz pary posortowane wzgledem napisow.
b) Wypisz pary posortowane wzgledem liczb.
"""


def sortuj_wzgledem_kluczy(slownik):
    """
    Funkcja sortuje slownik wzgledem kluczy.
    """
    return sorted(slownik.items(), key=lambda x: x[0])


def sortuj_wzgledem_wartosci(slownik):
    """	
    Funkcja sortuje slownik wzgledem wartosci.
    """
    return sorted(slownik.items(), key=lambda x: x[1])


def test_sortuj_wzgledem_kluczy():
    assert sortuj_wzgledem_kluczy({"a": 2, "c": 1, "b": 3}) == [
        ("a", 2),
        ("b", 3),
        ("c", 1),
    ]


def test_sortuj_wzgledem_wartosci():
    assert sortuj_wzgledem_wartosci({"a": 2, "c": 1, "b": 3}) == [
        ("c", 1),
        ("a", 2),
        ("b", 3),
    ]


if __name__ == "__main__":

    test_sortuj_wzgledem_kluczy()
    test_sortuj_wzgledem_wartosci()
