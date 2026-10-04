r"""
ZAD-01 — Wczytaj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `I/O`, `odwracanie`

### Treść

Wczytaj listę `n` liczb całkowitych, a następnie:

a) wypisz elementy listy od początku do końca — każdy w osobnej linii,
b) utwórz nową listę z tymi samymi elementami w odwrotnej kolejności i wypisz ją w **jednej** linii.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Najpierw `n` linii z elementami w kolejności wczytania (podpunkt a), a potem jedna linia z odwróconą listą, w formacie `print(lista)` (podpunkt b).

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
3
8 12 7
```

**Wyjście:**

```
8
12
7
[7, 12, 8]
```

"""


def wypisz_od_poczatku(lista):
    """Wypisuje elementy listy, każdy w osobnej linii."""
    for element in lista:
        print(element)


def odwroc(lista):
    """Zwraca nową listę z elementami w odwrotnej kolejności."""
    odwrocona = []
    for i in range(len(lista) - 1, -1, -1):
        odwrocona.append(lista[i])
    return odwrocona


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    wypisz_od_poczatku(lista)
    print(odwroc(lista))
