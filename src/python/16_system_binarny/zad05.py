"""
Tytul: Wybieranie minimum i maksimum.
Tresc: Otrzymujesz dwie liczby naturalne.
a) Zwroc mniejsza z nich. Zabronione jest uzycie instrukcji warunkowej oraz zewnetrznych bibliotek.
b) Zwroc wieksza z nich. Zabronione jest uzycie instrukcji warunkowej oraz zewnetrznych bibliotek.
Dane wejsciowe: Dwie liczby naturalne w obu podpunktach.
Dane wyjsciowe: Liczba naturalna w obu podpunktach.
Przyklad:
a) Dla otrzymanych liczb: 3 i 2, powinna zostac zwrocona liczba: 2.
b) Dla otrzymanych liczb: 3 i 2, powinna zostac zwrocona liczba: 3.

"""


def znak(n):
    """
    Funkcja zwraca znak liczby n.
    """
    return (n >> 31) & 0x01


def maksimum(a, b):
    """
    Funkcja zwraca maksimum dwoch liczb.
    dla a >= b: znak_a = 1, znak_b = 0;
    dla a < b: znak_a = 0, znak_b = 1;
    """
    znak_b = znak(a - b)
    znak_a = znak_b ^ 1
    return znak_a * a + znak_b * b


def minimum(a, b):
    """
    Funkcja zwraca minimum dwoch liczb.
    dla a >= b: znak_a = 0, znak_b = 1;
    dla a < b: znak_a = 1, znak_b = 0;
    """
    znak_b = znak(a - b)
    znak_a = znak_b ^ 1
    return znak_b * a + znak_a * b


def test_maksimum():
    assert maksimum(2, 3) == 3
    assert maksimum(3, 2) == 3
    assert maksimum(3, 3) == 3
    assert maksimum(0, 0) == 0
    assert maksimum(-2, -3) == -2
    assert maksimum(-3, -2) == -2
    assert maksimum(-3, -3) == -3


def test_minimum():
    assert minimum(2, 3) == 2
    assert minimum(3, 2) == 2
    assert minimum(3, 3) == 3
    assert minimum(0, 0) == 0
    assert minimum(-2, -3) == -3
    assert minimum(-3, -2) == -3
    assert minimum(-3, -3) == -3


if __name__ == "__main__":

    test_minimum()
    test_maksimum()
