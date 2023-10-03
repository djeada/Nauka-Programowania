"""
Tytul: Sortowanie listy binarnej.
Tresc: Otrzymujesz liste liczb skladajacych sie tylko z zer i jedynek. Posortuj te liste.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Posortowana lista liczb naturalnych.
Przyklad:
Dla listy: [1, 0, 1, 0, 1, 1], powinna zostac zwrocona lista: [0, 0, 1, 1, 1, 1].

"""

# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(1)
def sortuj_tablice_binarna(lista):
    """
    Funkcja sortuje liste binarna.
    """
    zera = lista.count(0)

    for i in range(zera):
        lista[i] = 0

    for i in range(zera, len(lista)):
        lista[i] = 1

    return lista


def test_sortuj_binarna_tablice_v1():
    tablica = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    oczekiwane = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

    assert sortuj_tablice_binarna(tablica) == oczekiwane


if __name__ == "__main__":
    test_sortuj_binarna_tablice_v1()
