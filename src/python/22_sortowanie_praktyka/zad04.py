"""
Tytul: Sortowanie napisow w liscie wzgledem dlugosci.
Tresc: Masz dana liste napisow. Posortuj napisy w liscie wzgledem dlugosci.
Dane wejsciowe: Lista napisow.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla listy ["abcd", "ab", "a", "abc"] powinno zostac zwrocone ["a", "ab", "abc", "abcd"].

"""


def posortuj_liste_wzgledem_dlugosci_napisow(lista_napisow):
    """
    Funkcja sortuje liste napisow wzgledem dlugosci napisow.
    """
    return sorted(lista_napisow, key=len)


def test_posortuj_liste_wzgledem_dlugosci_napisow():
    assert posortuj_liste_wzgledem_dlugosci_napisow(
        ["Ala", "ma", "kota", "a", "kot", "ma", "Ale"]
    ) == ["a", "ma", "ma", "Ala", "kot", "Ale", "kota"]


if __name__ == "__main__":
    test_posortuj_liste_wzgledem_dlugosci_napisow()
