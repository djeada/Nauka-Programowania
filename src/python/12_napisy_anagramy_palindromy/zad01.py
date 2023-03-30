"""
Tytul: Sprawdzenie, czy slowo jest palindromem.
Tresc: Napisz program, ktory sprawdzi, czy slowo jest palindromem. Palindromem jest slowo, ktore brzmi tak samo czytane od lewej do prawej i od prawej do lewej.
Dane wejsciowe: Napis.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla otrzymanego napisu: “kajak”, powinna zostac zwrocona wartosc logiczna: Prawda.

"""

def czy_palindrom(napis):
    """
    Funkcja sprawdza czy podany napis jest palindromem.
    """
    return napis == napis[::-1]

def test_czy_palindrom():
    assert czy_palindrom("kajak")
    assert not czy_palindrom("Pan")

if __name__ == "__main__":
    test_czy_palindrom()

