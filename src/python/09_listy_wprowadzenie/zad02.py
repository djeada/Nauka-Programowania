r"""
ZAD-02 — Wczytaj, zmodyfikuj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `indeksy`, `modyfikacja`

### Treść

Wczytaj listę `n` liczb całkowitych. Następnie utwórz i wypisz trzy nowe listy, każdą na podstawie **wczytanej** (oryginalnej) listy:

a) każdy element zwiększony o `1`,
b) każdy element pomnożony przez swój indeks,
c) wszystkie elementy zastąpione wartością pierwszego elementu.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Trzy linie — listy z podpunktów a), b), c) w tej kolejności, w formacie `print(lista)`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
3
3 9 7
```

**Wyjście:**

```
[4, 10, 8]
[0, 9, 14]
[3, 3, 3]
```

W podpunkcie b): $3 \cdot 0 = 0$, $9 \cdot 1 = 9$, $7 \cdot 2 = 14$.

"""


def dodaj_1(lista):
    return [element + 1 for element in lista]


def pomnoz_przez_indeks(lista):
    return [element * indeks for indeks, element in enumerate(lista)]


def zastap_pierwszym(lista):
    return [lista[0] for _ in lista]


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(dodaj_1(lista))
    print(pomnoz_przez_indeks(lista))
    print(zastap_pierwszym(lista))
