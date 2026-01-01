"""
ZAD-02 — Połączenie dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `indeksy`, `concat`

### Treść

Wczytaj dwie listy liczb całkowitych i wykonaj niezależnie:

**a)** Połącz listy, doklejając drugą listę na koniec pierwszej.
**b)** W pierwszej liście **podmień** elementy o parzystych indeksach (0, 2, 4, …) elementami z drugiej listy o tych samych indeksach — o ile taki indeks istnieje w obu listach.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: wynik dla **a)** jako lista
* 2 linia: wynik dla **b)** jako lista

### Przykład

**Wejście:**

```
[1, 2, 3]
[4, 5, 6]
```

**Wyjście:**

```
[1, 2, 3, 4, 5, 6]
[4, 2, 6]
```

"""


def dostawienie_na_koniec(lista_a, lista_b):
    lista_a.extend(lista_b)
    return lista_a


def wstawianie_parzystych_indeksow(lista_a, lista_b):
    for i in range(len(lista_a)):
        if i % 2 == 0:
            del lista_a[i]
            lista_a.insert(i, lista_b[i])
    return lista_a


def test_dostawienie_na_koniec():
    assert dostawienie_na_koniec([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_wstawianie_parzystych_indeksow():
    assert wstawianie_parzystych_indeksow([1, 1, 1], [4, 5, 6]) == [4, 1, 6]


if __name__ == "__main__":

    test_dostawienie_na_koniec()
    test_wstawianie_parzystych_indeksow()
