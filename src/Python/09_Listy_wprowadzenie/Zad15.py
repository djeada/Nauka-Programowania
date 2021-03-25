"""
Dla otrzymanej listy liczb naturalnych, znajdz elemnt 
dominujacy. Element dominujacy to element, ktorego liczba 
wystapien w liscie jest wieksza niz polowa dlugosci listy. 
Jesli lista nie ma elementu dominujacego, zwroc -1.
"""

# Wersja 1
# bez uzycia slownika
def elementDominujacyV1(lista):

    for i in range(len(lista) // 2 + 1):
        licznik = 1
        for j in range(i + 1, len(lista)):
            if lista[j] == lista[i]:
                licznik += 1

        if licznik > len(lista) // 2:
            return lista[i]

    return -1


# Wersja 2
# z uzyciem slownika
def elementDominujacyV2(lista):

    histo = {}

    for x in lista:
        assert type(x) == int

        if x in histo:
            histo[x] += 1
        else:
            histo[x] = 1

        if histo[x] > len(lista) // 2:
            return x

    return -1


if __name__ == "__main__":
    # Testy Poprawnosci
    lista = [4, 7, 4, 4, 2]
    wynik = 4
    assert elementDominujacyV1(lista) == wynik
    assert elementDominujacyV2(lista) == wynik

    lista = [0, 0, 2, 1, 9]
    wynik = -1
    assert elementDominujacyV1(lista) == wynik
    assert elementDominujacyV2(lista) == wynik
