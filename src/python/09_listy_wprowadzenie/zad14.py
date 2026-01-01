"""
ZAD-14 — Element bez pary

**Poziom:** ★★☆
**Tagi:** `XOR`, `listy`, `zliczanie`

### Treść

Wczytaj listę liczb całkowitych o nieparzystej długości: wszystkie liczby poza jedną występują dokładnie dwa razy. Znajdź liczbę bez pary.

### Wejście

* 1. linia: `N` (nieparzyste, `N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna liczba całkowita — element bez pary.

### Przykład

**Wejście:**

```
7
1
3
1
7
3
1
1
```

**Wyjście:**

```
7
```

"""


def element_bez_pary(lista):
    for i in lista:
        if lista.count(i) % 2 == 1:
            return i


def test_element_bez_pary():
    assert element_bez_pary([1, 3, 1, 7, 3, 1, 1]) == 7
    assert element_bez_pary([1, 1, 2, 2, 3, 4, 4, 5, 5]) == 3
    assert element_bez_pary([1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 2]) == 2


if __name__ == "__main__":

    test_element_bez_pary()
