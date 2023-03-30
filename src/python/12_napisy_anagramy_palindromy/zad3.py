"""
Tytul: Sprawdzenie, czy dwa slowa sa anagramami.
Tresc: Napisz program, ktory dla podanych dwoch napisow sprawdzi, czy sa anagramami. Dwa napisy sa anagramami, jesli jeden z nich mozna zbudowac poprzez przestawienie znakow w drugim.
Dane wejsciowe: Napis.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla otrzymanego napisu: “ula” oraz “lua”, powinna zostac zwrocona wartosc logiczna: Prawda.

"""


def anagramy(napis_a, napis_b):
    """
    Funkcja sprawdza czy dane napisy sa anagramami.
    """
    if len(napis_a) != len(napis_b):
        return False

    for znak in napis_a:
        if napis_a.count(znak) != napis_b.count(znak):
            return False

    return True


def test_anagramy():
    assert anagramy("kajak", "kajak")
    assert not anagramy("kajak", "kjakk")
    assert anagramy("adam", "mada")


if __name__ == "__main__":
    test_anagramy()

