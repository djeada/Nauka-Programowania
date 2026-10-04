r"""
ZAD-03 — Pierwsze wystąpienie klucza

**Poziom:** ★☆☆
**Tagi:** `listy`, `wyszukiwanie`, `indeksy`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `klucz`. Wypisz indeks pierwszego wystąpienia liczby `klucz` w liście.
Jeśli `klucz` nie występuje w liście — wypisz `-1`.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba całkowita `klucz`

### Wyjście

Jedna liczba całkowita: indeks pierwszego wystąpienia klucza albo `-1`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
2 9 -1 3 8
-1
```

**Wyjście:**

```
2
```

"""


def znajdz_klucz(lista, klucz):
    """Zwraca indeks pierwszego wystąpienia klucza albo -1."""
    for i in range(len(lista)):
        if lista[i] == klucz:
            return i
    return -1


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    klucz = int(input())
    print(znajdz_klucz(lista, klucz))
