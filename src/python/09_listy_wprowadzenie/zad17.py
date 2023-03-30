"""
Tytul: Usun duplikaty.
Tresc: Otrzymujesz liste liczb naturalnych. Usun z niej wszystkie duplikaty, tak aby kazda liczba pozostala tylko raz.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Lista liczb naturalnych.
Przyklad:
Dla otrzymanej listy: [3, 2, 1, 3, 2, 2], powinna zostac zwrocona lista: [3, 2, 1].

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

