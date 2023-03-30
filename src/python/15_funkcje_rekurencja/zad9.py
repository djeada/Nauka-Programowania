"""
Tytul: Gra.
Tresc: W grze, w kazdym ruchu gracz moze zdobyc 3, 5 lub 10 punktow. Oblicz przy uzyciu rekurencji, ile sposobow istnieje, aby gracz wygral gre, gdy ma do dyspozycji N punktow.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 20, powinna zostac zwrocona liczba: 4.

"""


def znajdz(slowo, litera, pozycja=0):
    """
    Funkcja zwraca indeks pierwszego wystapienia litera w slowie.
    """
    if len(slowo) <= pozycja:
        return -1
    if slowo[pozycja] == litera:
        return pozycja
    return znajdz(slowo, litera, pozycja + 1)


def czy_slowo_elfickie(napis, elf="elf"):
    """
    Funkcja sprawdza czy wszystkie litery slowa elf wystepuja w napisie.
    """

    if len(elf) == 0:
        return True

    if len(napis) == 0:
        return False

    pozycja = znajdz(napis, elf[0])

    if pozycja == -1:
        return False

    return czy_slowo_elfickie(napis[:pozycja] + napis[pozycja + 1 :], elf[1:])


def test_czy_slowo_elfickie():
    assert czy_slowo_elfickie("elf")
    assert czy_slowo_elfickie("reflektor")
    assert not czy_slowo_elfickie("elzbieta")


if __name__ == "__main__":

    test_czy_slowo_elfickie()

