"""
Otrzymujesz tablice skladajaca sie wylacznie z zer, jedynek i dwojek (cyfry: 0, 1, 2). Posortuj tablice w liniowym czasie.
"""

# Wersja 1
# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(1)
def sortujV1(lista):
    start, srodek = 0, 0
    koniec = len(lista) - 1
    piwot = 1

    while srodek <= koniec:
        # mamy 0
        if lista[srodek] < piwot:
            lista[start], lista[srodek] = lista[srodek], lista[start]
            start += 1
            srodek += 1

        # mamy 2
        elif lista[srodek] > piwot:
            lista[koniec], lista[srodek] = lista[srodek], lista[koniec]
            koniec -= 1

        # mamy 1
        else:
            srodek += 1

    return lista


# Testy Poprawnosci
lista = [0, 2, 2, 0, 1, 1, 2, 2, 1, 1]
wynik = [0, 0, 1, 1, 1, 1, 2, 2, 2, 2]

assert sortujV1(lista) == wynik

lista = [1, 1, 1, 1, 2, 1, 1, 1]
wynik = [1, 1, 1, 1, 1, 1, 1, 2]

assert sortujV1(lista) == wynik

lista = [2, 0, 0, 1, 1, 1, 1, 1]
wynik = [0, 0, 1, 1, 1, 1, 1, 2]

assert sortujV1(lista) == wynik
