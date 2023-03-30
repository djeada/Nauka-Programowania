"""
Tytul: Znalezienie elementow wspolnych dwoch list.
Tresc: Otrzymujesz dwie listy liczb calkowitych. Znajdz elementy wystepujace zarowno w pierwszej, jak i w drugiej liscie.
Dane wejsciowe: Dwie listy liczb calkowitych.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] zostanie zwrocona lista: [2, 4].

"""

def srednia_wazona(wartosci, wagi):

    if len(wartosci) != len(wagi):
        raise ValueError("Listy roznej dlugosci")

    suma = 0
    for waga, wartosc in zip(wagi, wartosci):
        suma += waga * wartosc

    return suma / sum(wartosci)

def test_srednia_wazona():
    assert srednia_wazona([1, 2, 3], [1, 1, 1]) == 1
    assert srednia_wazona([0, -23, -5, 2, -3, 4, 9], [1, 2, 3, 4, 5, 6, 7]) == -1.1875

if __name__ == "__main__":
    test_srednia_wazona()

