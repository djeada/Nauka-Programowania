"""
ZAD-13 — Brakujący element w ciągu arytmetycznym

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `ciąg arytmetyczny`, `listy`

### Treść

Wczytaj `N` liczb naturalnych. Lista jest fragmentem ciągu arytmetycznego z **jednym brakującym elementem**. Znajdź i wypisz brakującą wartość.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba naturalna — brakujący element.

### Przykład

**Wejście:**

```
4
5
2
1
3
```

**Wyjście:**

```
4
```

"""


def suma_ciag_aryt(lista):
    return (len(lista) + 1) * (min(lista) + max(lista)) // 2


def brakujacy_element(lista):

    suma_przedzialu = suma_ciag_aryt(lista)
    suma_listy = sum(lista)

    wynik = suma_przedzialu - suma_listy

    if wynik not in lista:
        return wynik

    return 0


def test_brakujacy_element():
    assert brakujacy_element([6, 8, 4, 10, 14, 2]) == 12
    assert brakujacy_element([1, 2, 4, 5, 6]) == 3
    assert brakujacy_element([1, 2, 3]) == 0


if __name__ == "__main__":

    test_brakujacy_element()
