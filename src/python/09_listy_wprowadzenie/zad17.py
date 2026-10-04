r"""
ZAD-17 — Wszystkie pary o sumie x (wartości)

**Poziom:** ★★☆
**Tagi:** `listy`, `2-sum`, `pary`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `x`. Wypisz wszystkie pary **wartości** `a b` (nie indeksów) takie, że $a + b = x$, gdzie `a` i `b` to elementy listy stojące na **różnych** pozycjach.

Każdą parę wartości wypisz tylko raz, mniejszą liczbę jako pierwszą ($a \le b$). Pary uporządkuj rosnąco według `a`.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba całkowita `x`

### Wyjście

Każda para w osobnej linii, w formacie `a b`. Jeśli nie ma żadnej pary — program nic nie wypisuje.

### Ograniczenia

* $n \ge 2$

### Przykład

**Wejście:**

```
5
1 2 4 3 7
5
```

**Wyjście:**

```
1 4
2 3
```

### Uwagi

* Para `a a` (dwie takie same wartości) jest poprawna tylko wtedy, gdy wartość `a` występuje w liście co najmniej dwa razy.
* Jeśli jakaś wartość występuje w liście wielokrotnie, ta sama para wartości i tak jest wypisywana tylko raz.

"""


def znajdz_pary(lista, x):
    """Zwraca posortowaną listę różnych par wartości (a, b), a <= b, o sumie x."""
    pary = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == x:
                para = (min(lista[i], lista[j]), max(lista[i], lista[j]))
                if para not in pary:
                    pary.append(para)
    pary.sort()
    return pary


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    x = int(input())
    for a, b in znajdz_pary(lista, x):
        print(a, b)
