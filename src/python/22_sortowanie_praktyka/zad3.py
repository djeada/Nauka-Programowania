"""
Tytul: Sortowanie listy par wzgledem jednej z kategorii.
Tresc: Masz dana liste par napisow i liczb. Posortuj pary w liscie wzgledem:
a) Liczb.
b) Dlugosci napisow.
Dane wejsciowe: Lista par napisow i liczb.
Dane wyjsciowe: Lista par napisow i liczb.
Przyklad:
Dla listy [(“ab”, 3), (“bca”, 1), (“c”, 2)] powinno zostac zwrocone:
a) [(“bca”, 1), (“c”, 2), (“ab”, 3)] lub
b) [(“c”, 2), (“ab”, 3), (“bca”, 1)].

"""

def posortuj_liste_wzgledem_liczb(lista):
    """
    Funkcja zwraca liste par napisow i liczb posortowanych wzgledem liczb.
    """
    return sorted(lista, key=lambda x: x[1])

def posortuj_liste_wzgledem_dlugosci_napisow(lista):
    """
    Funkcja zwraca liste par napisow i liczb posortowanych wzgledem dlugosci napisow.
    """
    return sorted(lista, key=lambda x: len(x[0]))

def test_posortuj_liste_wzgledem_liczb():
    assert posortuj_liste_wzgledem_liczb([("c", 3), ("b", 2), ("a", 1)]) == [
        ("a", 1),
        ("b", 2),
        ("c", 3),
    ]

def test_posortuj_liste_wzgledem_dlugosci_napisow():
    assert posortuj_liste_wzgledem_dlugosci_napisow(
        [("ccc", 3), ("z", 1), ("xx", 2)]
    ) == [("z", 1), ("xx", 2), ("ccc", 3)]

if __name__ == "__main__":
    test_posortuj_liste_wzgledem_liczb()
    test_posortuj_liste_wzgledem_dlugosci_napisow()

