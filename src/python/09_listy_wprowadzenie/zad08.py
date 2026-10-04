r"""
ZAD-08 — Usuń klucz

**Poziom:** ★☆☆
**Tagi:** `listy`, `remove`, `wyszukiwanie`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `klucz`. Usuń z listy **pierwsze** wystąpienie liczby `klucz` (jeśli istnieje) i wypisz listę po tej zmianie.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba całkowita `klucz`

### Wyjście

Jedna linia: lista po usunięciu klucza, w formacie `print(lista)`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
6 2 1 4 27
4
```

**Wyjście:**

```
[6, 2, 1, 27]
```

### Uwagi

* Jeśli `klucz` nie występuje w liście, wypisz listę bez zmian.
* Jeśli po usunięciu lista jest pusta, program wypisze `[]`.

"""


def usun_klucz(lista, klucz):
    """Usuwa z listy pierwsze wystąpienie klucza (jeśli istnieje)."""
    for i in range(len(lista)):
        if lista[i] == klucz:
            lista.pop(i)
            break
    return lista


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    klucz = int(input())
    print(usun_klucz(lista, klucz))
