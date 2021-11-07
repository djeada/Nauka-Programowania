import string

"""
Otrzymujesz napis reprezentujacy zdanie oraz slowo. Znajdz wszystkie 
anagramy otrzymanego slowa w zdaniu. Roznice miedzy wielkimi i malymi 
literami powinny byc zignorowane.
"""


def anagramy(napis_a, napis_b):
    """
    Funkcja sprawdza, czy otrzymane napisy sa anagramami. 
    """
    if len(napis_a) != len(napis_b):
        return False

    for znak in napis_a:
        if napis_a.count(znak) != napis_b.count(znak):
            return False

    return True


def podziel_zdanie_na_slowa(zdanie):
    """
    Funkcja rozdziela zdanie na slowa. 
    """
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def anagramy_slowa_w_zdaniu(zdanie, slowo):
    """
    Funkcja zwraca liste anagramow slowa znalezionych w zdaniu. 
    """
    slowa = podziel_zdanie_na_slowa(zdanie)
    slowa = [s.lower() for s in slowa]
    wynik = []

    for slowo_z_zdania in slowa:
        if anagramy(slowo_z_zdania, slowo):
            wynik.append(slowo_z_zdania)

    return wynik


def test_anagramy_slowa_w_zdaniu():
    assert anagramy_slowa_w_zdaniu(
        "Za jego nikczemne uczynki, spotakla go wysoce sroga kara.", "arak"
    ) == ["kara"]


if __name__ == "__main__":

    test_anagramy_slowa_w_zdaniu()
