"""
Otrzymujesz dwie listy binarne, A oraz B. 
Znajdz dlugosc takich podciagow obu list o rownej sumie, ktorych suma jest najwieksza.
Podciagi nie musza byc takie same.
"""

# Wersja 1
# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(n)
def znajdz_podciag_v1(lista_a, lista_b):

    if len(lista_a) != len(lista_b):
        raise ValueError("Listy musza byc rownej dlugosci.")

    histo = {}

    histo[0] = -1

    wynik, suma_a, suma_b = 0, 0, 0

    for i in range(len(lista_a)):

        suma_a += lista_a[i]
        suma_b += lista_b[i]

        roznica = suma_a - suma_b

        if roznica not in histo:
            histo[roznica] = i

        else:
            wynik = max(wynik, i - histo[roznica])

    return wynik


# Testy Poprawnosci
def test_1():
    lista_a = [0, 0, 1, 1, 1, 1]
    lista_b = [0, 1, 1, 0, 1, 0]
    wynik = 5

    assert znajdz_podciag_v1(lista_a, lista_b) == wynik


def test_2():
    lista_a = [0, 0, 1, 1]
    lista_b = [0, 1, 1, 0, 1, 0]

    try:
        znajdz_podciag_v1(lista_a, lista_b)()
        assert False
    except ValueError:
        assert True


def main():
    test_1()
    test_2()


if __name__ == "__main__":
    main()
