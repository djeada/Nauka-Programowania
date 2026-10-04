r"""
ZAD-19 — Wycinki listy

**Poziom:** ★☆☆
**Tagi:** `listy`, `wycinki`, `slicing`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `k`. Wypisz kolejno:

1. pierwsze `k` elementów listy,
2. ostatnie `k` elementów listy,
3. co drugi element listy, zaczynając od pierwszego (indeksy $0, 2, 4, \ldots$),
4. listę odwróconą,
5. listę bez pierwszego i ostatniego elementu.

Każdą z tych list uzyskaj jednym **wycinkiem** (ang. *slicing*), bez pętli.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba `k`

### Wyjście

Pięć linii — listy z punktów 1–5 w tej kolejności, w formacie `print(lista)`.

### Ograniczenia

* $1 \le k \le n$

### Przykład

**Wejście:**

```
6
1 2 3 4 5 6
2
```

**Wyjście:**

```
[1, 2]
[5, 6]
[1, 3, 5]
[6, 5, 4, 3, 2, 1]
[2, 3, 4, 5]
```

### Uwagi

* Wycinek `lista[start:stop]` to nowa lista z elementami o indeksach od `start` do `stop - 1`, np. dla `lista = [10, 20, 30, 40, 50]` wycinek `lista[1:3]` to `[20, 30]`.
* Pominięty `start` oznacza „od początku”, a pominięty `stop` — „do końca”: `lista[2:]` to `[30, 40, 50]`.
* Indeksy ujemne liczymy od końca: `lista[-1]` to ostatni element (`50`), a `lista[-2]` — przedostatni (`40`).
* Trzecia liczba to krok: `lista[start:stop:krok]` bierze co `krok`-ty element, np. `lista[1::3]` to `[20, 50]`. Krok może być ujemny — wtedy elementy są brane od końca.
* Wycinek nigdy nie zmienia oryginalnej listy.

"""


def wycinki(lista, k):
    """Zwraca pięć wycinków listy opisanych w treści zadania."""
    return [
        lista[:k],
        lista[-k:],
        lista[::2],
        lista[::-1],
        lista[1:-1],
    ]


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    k = int(input())
    for wycinek in wycinki(lista, k):
        print(wycinek)
