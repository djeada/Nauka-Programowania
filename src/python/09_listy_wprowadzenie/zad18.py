"""
Tytul: Czy punkty moga stanowic wierzcholki trojkata?
Tresc: Otrzymujesz dokladnie 6 liczb calkowitych, ktore odpowiadaja wspolrzednym punktow A, B, C w kolejnosci: xA, yA, xB, yB, xC, yC. Sprawdz, czy punkty A, B, C moga stanowic wierzcholki trojkata.
Dane wejsciowe: Lista liczb calkowitych reprezentujaca wspolrzedne punktow A, B, C.
Dane wyjsciowe: Wartosc logiczna okreslajaca, czy punkty A, B, C moga stanowic wierzcholki trojkata.
Przyklad:
Dla otrzymanej listy [-3, -2, -3, 1, -3, 0], powinna zostac zwrocona wartosc logiczna: Falsz.

"""


def znajdz_min_indeks(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return i + 1

    return 0


def test_znajdz_min_indeks():
    assert znajdz_min_indeks([7, 8, -1, 4, 5]) == 2
    assert znajdz_min_indeks([2, 3, 4, 5, 6]) == 0
    assert znajdz_min_indeks([8, 9, 10, 11, 1]) == 4


if __name__ == "__main__":

    test_znajdz_min_indeks()

