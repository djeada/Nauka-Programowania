r"""
ZAD-02 — Wypisywanie liczb mniejszych od podanej

**Poziom:** ★☆☆
**Tagi:** `for`, `while`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` i wypisz wszystkie liczby naturalne dodatnie mniejsze od `n` w kolejności malejącej — od `n - 1` do `1`.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Liczby `n - 1`, `n - 2`, …, `1`, każda w osobnej linii.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
1
```

### Uwagi

* Dla `n = 1` nie wypisuj nic.

"""


def wypisz_mniejsze(n):
    for liczba in range(n - 1, 0, -1):
        print(liczba)


if __name__ == "__main__":
    n = int(input())
    wypisz_mniejsze(n)
