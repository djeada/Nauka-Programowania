r"""
ZAD-08 — Najbliższa potęga dwójki (>= n)

**Poziom:** ★☆☆
**Tagi:** `potęgi 2`, `bitwise`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz najmniejszą potęgę liczby 2, która jest **większa lub równa** `n`, czyli najmniejsze $2^k \ge n$ dla całkowitego $k \ge 0$.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: najmniejsza potęga dwójki nie mniejsza od `n`.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
111
```

**Wyjście:**

```
128
```

### Uwagi

* $2^0 = 1$, więc dla `n = 0` i `n = 1` wynik to `1`.
* Jeśli `n` jest potęgą dwójki, wynikiem jest samo `n`.
* Kolejne potęgi dwójki otrzymasz przesunięciem `potega << 1`.

"""


def najblizsza_potega_dwojki(n):
    """Zwraca najmniejszą potęgę dwójki większą lub równą n (dla n <= 1 jest to 1)."""
    potega = 1
    while potega < n:
        potega <<= 1
    return potega


if __name__ == "__main__":
    n = int(input())
    print(najblizsza_potega_dwojki(n))
