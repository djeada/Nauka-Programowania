"""
Tytul: Najczesciej wystepujaca litera w zdaniu
Tresc: Otrzymujesz napis reprezentujacy zdanie. Twoim zadaniem jest znalezienie najczesciej wystepujacej litery w zdaniu. Jesli wiecej niz jedna litera wystepuje te sama liczbe razy, nalezy zwrocic litere najwczesniej pojawiajaca sie w zdaniu.
Dane wejsciowe: Napis.
Dane wyjsciowe: Znak.
Przyklad:
Dla otrzymanego napisu: "lezy jerzy na wiezy"
Powinna zostac zwrocona litera: 'e'

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

