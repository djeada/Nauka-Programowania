"""
Tytul: Sortowanie listy liczb z zakresu 0-2.
Tresc: Otrzymujesz liste liczb skladajacych sie tylko z zer, jedynek i dwojek. Posortuj te liste.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Posortowana lista liczb naturalnych.
Przyklad:
Dla listy: [1, 0, 1, 2, 2, 0, 1], powinna zostac zwrocona lista: [0, 0, 1, 1, 1, 2, 2].

"""

# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(1)
def sortuj_liste(lista):
    """
    Funkcja sortujaca liste liczb z zakresu 0-2.
    """
    start, srodek = 0, 0
    koniec = len(lista) - 1
    piwot = 1

    while srodek <= koniec:
        # lista[srodek] == 0
        if lista[srodek] < piwot:
            lista[start], lista[srodek] = lista[srodek], lista[start]
            start += 1
            srodek += 1

        # lista[srodek] == 2
        elif lista[srodek] > piwot:
            lista[koniec], lista[srodek] = lista[srodek], lista[koniec]
            koniec -= 1

        # lista[srodek] == 1
        else:
            srodek += 1

    return lista

def test_sortuj_liste():
    lista = [0, 2, 2, 0, 1, 1, 2, 2, 1, 1]
    wynik = [0, 0, 1, 1, 1, 1, 2, 2, 2, 2]

    assert sortuj_liste(lista) == wynik

def test_sortuj_liste():
    lista = [1, 1, 1, 1, 2, 1, 1, 1]
    wynik = [1, 1, 1, 1, 1, 1, 1, 2]

    assert sortuj_liste(lista) == wynik

def test_sortuj_liste():
    lista = [2, 0, 0, 1, 1, 1, 1, 1]
    wynik = [0, 0, 1, 1, 1, 1, 1, 2]

    assert sortuj_liste(lista) == wynik

if __name__ == "__main__":
    test_sortuj_liste()

