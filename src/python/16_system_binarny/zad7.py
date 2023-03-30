"""
Tytul: Zamien A na B.
Tresc: Otrzymujesz dwie liczby naturalne. Oblicz, ile bitow nalezy odwrocic, aby zamienic liczbe A na liczbe B.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanych liczb 34 i 73, powinna zostac zwrocona liczba 5.

"""


def zamien_sasiadow(liczba):
    """
    Funkcja zamienia sasiadujace bity w binarnym zapisie liczby.
    """
    parzyste = liczba & 0xAAAAAAAA
    nieparzyste = liczba & 0x55555555

    parzyste >>= 1
    nieparzyste <<= 1

    return parzyste | nieparzyste


def test_zamien_sasiadow():
    assert zamien_sasiadow(9131) == 4951


if __name__ == "__main__":
    test_zamien_sasiadow()

