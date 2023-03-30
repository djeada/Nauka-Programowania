"""
Tytul: Konwersja listy na napis
Tresc: Otrzymujesz liste liczb naturalnych. Zamie liste na napis.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej listy: [2, 4, 7], powinien zostac zwrocony napis: “247”.

"""

def znamien_na_napis(lista):
    napis = ""
    for liczba in lista:
        napis += str(liczba)
    return napis

def test_znamien_na_napis():
    assert znamien_na_napis([1, 2, 3, 4, 5]) == "12345"

if __name__ == "__main__":

    test_znamien_na_napis()

