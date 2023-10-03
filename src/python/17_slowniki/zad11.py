"""
Tytul: Sortowanie wzgledem kluczy/wartosci
Otrzymujesz slownik skladajacy sie z par napisow i liczb calkowitych. Twoim zadaniem jest wypisanie par posortowanych wzgledem napisow oraz wzgledem liczb.
Dane wejsciowe: Slownik par: napis, liczba calkowita.
Dane wyjsciowe: Lista par.
Przyklad:
Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("b", 4), ("c", 3), ("x", 5)].
Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("c", 3), ("b", 4), ("x", 5)].

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
