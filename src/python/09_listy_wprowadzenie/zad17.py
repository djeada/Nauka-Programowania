"""
Tytul: Znalezienie wszystkich par elementow listy o sumie rownej podanej liczbie.
Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby x, znajdz wszystkie pary elementow listy, ktorych suma jest rowna x.
Dane wejsciowe: Lista liczb calkowitych oraz liczba calkowita.
Dane wyjsciowe: Lista par liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [1, 2, 4, 3, 7] oraz liczby 5, zostana zwrocone wszystkie pary elementow o sumie rownej 5: [(1, 4), (2, 3)].

"""

def znajdz_pary(lista, x):
    wynik = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == x:
                wynik.append((i, j))
    return wynik

def test_znajdz_pary():
    assert znajdz_pary([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == [
        (0, 8),
        (1, 7),
        (2, 6),
        (3, 5),
    ]
    assert znajdz_pary([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20) == []

if __name__ == "__main__":

    test_znajdz_pary()

