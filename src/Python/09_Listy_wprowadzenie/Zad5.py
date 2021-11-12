"""
Otrzymujesz liste liczb, wykonaj nastepujace polecenia:
a) Zwieksz o 1 wszystkie elementy o parzystych indeksach.
b) Wyzeruj wszystkie wielokrotnosci liczby 3.
c) Podnies do kwadratu wszystkie elementy mniejsze niz 10.
d) Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace liczbami pierwszymi.
e) Zamien kazdy element na iloczyn wszystkich elementow listy poza nim samym.
"""


def zwieksz_parzyste(lista):
    for i in range(len(lista)):
        if i % 2 == 0:
            lista[i] += 1
    return lista


def wyzeruj_wielokrotnosci_3(lista):
    for i in range(len(lista)):
        if lista[i] % 3 == 0:
            lista[i] = 0
    return lista


def kwadrat_mniejsze_10(lista):
    for i in range(len(lista)):
        if lista[i] < 10:
            lista[i] = lista[i] ** 2
    return lista


def czy_pierwsza(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def suma_wszystkich_na_pierwszych_indeksach(lista):
    suma = sum(lista)
    for i in range(len(lista)):
        if czy_pierwsza(i):
            lista[i] = suma
    return lista


def zamien_na_iloczyn_wszystkich_poza_soba(lista):
    kopia = lista[:]
    for i in range(len(lista)):
        iloczyn = 1
        for j in range(len(lista)):
            if j != i:
                iloczyn *= lista[j]
        kopia[i] = iloczyn
    return kopia


def test_zwieksz_parzyste():
    assert zwieksz_parzyste([1, 2, 3, 4, 5]) == [2, 2, 4, 4, 6]
    assert zwieksz_parzyste([1, 2, 3, 4, 5, 6]) == [2, 2, 4, 4, 6, 6]
    assert zwieksz_parzyste([1, 2, 3, 4, 5, 6, 7]) == [2, 2, 4, 4, 6, 6, 8]


def test_wyzeruj_wielokrotnosci_3():
    assert wyzeruj_wielokrotnosci_3([1, 2, 3, 4, 5]) == [1, 2, 0, 4, 5]
    assert wyzeruj_wielokrotnosci_3([1, 2, 3, 4, 5, 6]) == [1, 2, 0, 4, 5, 0]
    assert wyzeruj_wielokrotnosci_3([8, 6, 5, 3, 2, 0]) == [8, 0, 5, 0, 2, 0]


def test_kwadrat_mniejsze_10():
    assert kwadrat_mniejsze_10([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert kwadrat_mniejsze_10([1, 2, 3, 4, 5, 6]) == [1, 4, 9, 16, 25, 36]
    assert kwadrat_mniejsze_10([1, 2, 3, 4, 5, 6, 7]) == [1, 4, 9, 16, 25, 36, 49]


def test_suma_wszystkich_na_pierwszych_indeksach():
    assert suma_wszystkich_na_pierwszych_indeksach([1, 2, 3, 4, 5]) == [1, 2, 15, 15, 5]
    assert suma_wszystkich_na_pierwszych_indeksach([1, 2, 3, 4, 5, 6]) == [
        1,
        2,
        21,
        21,
        5,
        21,
    ]
    assert suma_wszystkich_na_pierwszych_indeksach([0, 0, 10, -5, -2]) == [
        0,
        0,
        3,
        3,
        -2,
    ]


def test_zamien_na_iloczyn_wszystkich_poza_soba():
    assert zamien_na_iloczyn_wszystkich_poza_soba([1, 2, 3]) == [6, 3, 2]
    assert zamien_na_iloczyn_wszystkich_poza_soba([-1, 0, 3]) == [0, -3, 0]
    assert zamien_na_iloczyn_wszystkich_poza_soba([3, 5, -7, 4, 9, -11, 2]) == [
        27720,
        16632,
        -11880,
        20790,
        9240,
        -7560,
        41580,
    ]


if __name__ == "__main__":

    test_zwieksz_parzyste()
    test_wyzeruj_wielokrotnosci_3()
    test_kwadrat_mniejsze_10()
    test_suma_wszystkich_na_pierwszych_indeksach()
    test_zamien_na_iloczyn_wszystkich_poza_soba()
