"""
ZAD-07 — Średnia dwóch największych liczb

**Poziom:** ★☆☆
**Tagi:** `listy`, `max`, `sortowanie`, `float`

### Treść

Wczytaj `N` liczb naturalnych (`N ≥ 2`). Znajdź największą i drugą największą wartość, a następnie wypisz ich średnią arytmetyczną jako liczbę zmiennoprzecinkową z dokładnością do **jednego** miejsca po przecinku.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba zmiennoprzecinkowa w formacie `%.1f`.

### Przykład

**Wejście:**

```
6
9
2
3
2
1
7
```

**Wyjście:**

```
8.0
```

"""


def srednia_dwoch_najwiekszych(lista):

    if len(lista) < 2:
        return 0.00

    najwieksza = max(lista)
    najwieksza_druga = max(lista[: lista.index(najwieksza)])
    srednia = (najwieksza + najwieksza_druga) / 2
    return srednia


def test_srednia_dwoch_najwiekszych():

    assert srednia_dwoch_najwiekszych([]) == 0.00
    assert srednia_dwoch_najwiekszych([1]) == 0.00
    assert srednia_dwoch_najwiekszych([1, 2]) == 1.50
    assert srednia_dwoch_najwiekszych([3, 5, -7, 4, 9, -11, 2]) == 7.00
    assert (
        srednia_dwoch_najwiekszych([3, -2, 4, 9, -3, -40, 8, 5, -7, 4, 9, -11, 2])
        == 6.5
    )


if __name__ == "__main__":

    test_srednia_dwoch_najwiekszych()
