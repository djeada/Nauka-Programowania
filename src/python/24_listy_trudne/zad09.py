"""
ZAD-09 — Najdłuższy naprzemienny podciąg

**Poziom:** ★★★
**Tagi:** `dp`, `subsequence`, `naprzemienny`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź najdłuższy podciąg naprzemienny, w którym różnice między kolejnymi elementami zmieniają znak (raz dodatnia, raz ujemna, itd.).

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: lista liczb — najdłuższy naprzemienny podciąg

### Przykład

**Wejście:**

```
[1, -2, 6, 4, -3, 2, -4, -3]
```

**Wyjście:**

```
[1, -2, 6, -3, 2, -4]
```

### Uwagi

* Jeśli istnieje kilka podciągów o tej samej maksymalnej długości — wybierz ten, który pojawia się „najwcześniej” (najmniejszy możliwy indeks startu), o ile sprawdzarka tego wymaga.

"""


def najdluzszy_naprzemienny_podciag_v1(lista):

    dlugosc_maks = 1
    indeks_koncowy = 0
    dlugosc = 1

    for i in range(len(lista) - 1):

        if lista[i] * lista[i + 1] < 0:

            dlugosc += 1

            if dlugosc > dlugosc_maks:
                dlugosc_maks = dlugosc
                indeks_koncowy = i + 1

        else:
            dlugosc = 1

    wynik = lista[indeks_koncowy - dlugosc_maks + 1 : indeks_koncowy + 1]

    if len(wynik) > 1:
        return wynik

    return list()


# Testy Poprawnosci
def test_1():
    lista = [1, -2, 6, 4, -3, 2, -4, -3]
    wynik = [4, -3, 2, -4]

    assert najdluzszy_naprzemienny_podciag_v1(lista) == wynik


def test_2():
    lista = [1, 2, 3, 4, 5]
    wynik = []

    assert najdluzszy_naprzemienny_podciag_v1(lista) == wynik


def test_3():
    lista = []
    wynik = []

    assert najdluzszy_naprzemienny_podciag_v1(lista) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
