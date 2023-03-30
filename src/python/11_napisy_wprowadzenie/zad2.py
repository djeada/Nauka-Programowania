"""
Tytul: Srednia dlugosc slow w zdaniu.
Tresc: Otrzymasz napis reprezentujacy zdanie. Oblicz srednia dlugosc slow w zdaniu. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanego napisu: "Zepsuty rower.", powinna zostac zwrocona liczba: 6.

"""

def liczba_wystapien(napis, znak):
    return napis.count(znak)

def test_liczba_wystapien():
    assert liczba_wystapien("ala ma kota", "a") == 3
    assert liczba_wystapien("ala ma kota", "k") == 1

if __name__ == "__main__":

    test_liczba_wystapien()

