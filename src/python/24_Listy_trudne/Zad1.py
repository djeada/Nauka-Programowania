"""
Otrzymujesz tablice skladajaca sie wylacznie z zer i jedynek. Znajdz indeks zera, ktore po zamianie na jedynke daloby najdluzszy nieprzerwany ciag jedynek.
Zachowanie dla otrzymanej tablicy skladajacej sie z samych zer jest nieokreslone.
"""

# Wersja 1
# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(1)
def znajdz_zero_do_podmiany_v1(lista):
    licznik_jedynek = 0
    indeks_zera = -1

    licznik_zer = 0
    poprzedni_indeks_zera = -1

    for i in range(len(lista)):

        if lista[i] == 1:
            licznik_zer += 1

        else:
            licznik_zer = i - poprzedni_indeks_zera
            poprzedni_indeks_zera = i

        if licznik_zer > licznik_jedynek:
            licznik_jedynek = licznik_zer
            indeks_zera = poprzedni_indeks_zera

    return indeks_zera


# Testy Poprawnosci
def test_1():
    lista = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
    wynik = 7

    assert znajdz_zero_do_podmiany_v1(lista) == wynik


def test_2():
    lista = [1, 1, 1, 1, 1, 1, 1, 1]
    wynik = -1

    assert znajdz_zero_do_podmiany_v1(lista) == wynik


def test_3():
    lista = [1, 0, 1, 1, 1, 1, 1, 1]
    wynik = 1

    assert znajdz_zero_do_podmiany_v1(lista) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
