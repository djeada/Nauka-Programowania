"""
Tytul: Lista pracownikow z najwiekszymi zyskami.
Tresc: Otrzymujesz liste par. Pierwszym elementem pary jest napis reprezentujacy imie i nazwisko pracownika, drugim zysk z transakcji, jaka dany pracownik przeprowadzil. Znajdz pracownika, ktory przyniosl firmie najwiecej zysku.
Dane wejsciowe: Lista par napisow i liczb naturalnych.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej listy:
[["Barnaba Barabash", 120],
["Jon Snow", 100],
["Kira Summer", 300],
["Barnaba Barabash", 200],
["Bob Marley", 110]]
zostanie zwrocony napis: “Barnaba Barabash”.

"""

def stworz_slownik(lista_a, lista_b):
    """
    Funkcja tworzy slownik zawierajacy klucze bedace elementami
    pierwszej listy i wartosci bedace elementami drugiej listy.
    """

    if len(lista_a) != len(lista_b):
        return {}

    return dict(zip(lista_a, lista_b))

def test_stworz_slownik():
    assert stworz_slownik([1, 2, 3], [4, 5, 6]) == {1: 4, 2: 5, 3: 6}
    assert stworz_slownik([1, 2, 3], [4, 5]) == {}

if __name__ == "__main__":

    test_stworz_slownik()

