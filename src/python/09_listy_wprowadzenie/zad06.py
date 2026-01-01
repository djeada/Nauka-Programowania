"""
ZAD-06 — Czy średnia elementów znajduje się w liście?

**Poziom:** ★☆☆
**Tagi:** `listy`, `średnia`, `wyszukiwanie`

### Treść

Wczytaj listę liczb całkowitych. Oblicz średnią arytmetyczną elementów i sprawdź, czy ta średnia jest **dokładnie** jednym z elementów listy.

Wypisz:

* `Tak` — jeśli średnia występuje w liście,
* `Nie` — w przeciwnym razie.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedno słowo: `Tak` lub `Nie`.

### Przykład

**Wejście:**

```
5
6
2
1
4
27
```

**Wyjście:**

```
Nie
```

### Uwagi

* Średnia może być ułamkiem — wtedy na pewno nie znajduje się w liście liczb całkowitych.

"""


def czy_srednia_w_liscie(lista):

    if not lista:
        return False

    srednia = sum(lista) / len(lista)

    if srednia.is_integer():
        return srednia in lista
    else:
        return round(srednia, 0) in lista


def test_czy_srednia_w_liscie_dla_pustej_listy():
    assert not czy_srednia_w_liscie([])
    assert czy_srednia_w_liscie([1, 2, 3])
    assert czy_srednia_w_liscie([-5, 7, 2, 3, -1, 4])


if __name__ == "__main__":

    test_czy_srednia_w_liscie_dla_pustej_listy()
