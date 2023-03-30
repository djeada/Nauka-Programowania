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

def pracownik_z_najwiekszym_zyskiem(lista_par):
    """
    Funkcja zwraca napis reprezentujacy imie i nazwisko pracownika, ktory
    przyniosl firmie najwiecej zysku.
    """

    zyski = {}
    for para in lista_par:
        if para[0] in zyski:
            zyski[para[0]] += para[1]
        else:
            zyski[para[0]] = para[1]

    return max(zyski, key=zyski.get)

def test_pracownik_z_najwiekszym_zyskiem():

    assert (
        pracownik_z_najwiekszym_zyskiem(
            [
                ("Barnaba Barabash", 120),
                ("Jon Snow", 100),
                ("Kira Summer", 300),
                ("Barnaba Barabash", 200),
                ("Bob Marley", 110),
            ]
        )
        == "Barnaba Barabash"
    )

if __name__ == "__main__":

    test_pracownik_z_najwiekszym_zyskiem()

