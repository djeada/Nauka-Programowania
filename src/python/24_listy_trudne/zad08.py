r"""
ZAD-08 — Maksymalny zysk ze sprzedaży sznurka

**Poziom:** ★★★
**Tagi:** `dp`, `rod cutting`, `optymalizacja`

### Treść

Masz sznurek o długości `n` i cennik: $c_d$ to cena kawałka o długości `d` (dla `d = 1, 2, …, n`). Ceny nie muszą rosnąć razem z długością. Możesz pociąć sznurek na dowolną liczbę kawałków o całkowitych długościach (albo nie ciąć go wcale) i sprzedać wszystkie kawałki. Oblicz **maksymalny możliwy zysk**.

### Wejście

* 1. linia: `n` — długość sznurka
* 2. linia: `n` nieujemnych liczb całkowitych $c_1, c_2, \ldots, c_n$ oddzielonych spacjami

### Wyjście

Jedna liczba całkowita — maksymalny zysk.

### Ograniczenia

* `1 ≤ n ≤ 500`
* $0 \le c_d \le 10^4$

### Przykład

**Wejście:**

```
4
1 5 8 9
```

**Wyjście:**

```
10
```

Najlepiej pociąć sznurek na dwa kawałki o długości 2: $5 + 5 = 10$.

### Przykład 2

**Wejście:**

```
8
1 5 8 9 10 17 17 20
```

**Wyjście:**

```
22
```

Kawałki o długościach 2 i 6: $5 + 17 = 22$.

### Uwagi

* Sprawdzanie wszystkich sposobów pocięcia (jest ich $2^{n-1}$) jest zdecydowanie za wolne — w testach `n` sięga kilkuset. Użyj programowania dynamicznego: najlepszy zysk dla długości `d` to maksimum z $c_k + \text{najlepszy}(d - k)$ po wszystkich długościach pierwszego kawałka `k`. Daje to czas $O(n^2)$.

"""


def maks_zysk(ceny, n):
    """Maksymalny zysk ze sprzedaży sznurka długości n (programowanie dynamiczne)."""
    # najlepszy[d] — maksymalny zysk ze sznurka długości d
    najlepszy = [0] * (n + 1)

    for dlugosc in range(1, n + 1):
        for kawalek in range(1, dlugosc + 1):
            zysk = ceny[kawalek - 1] + najlepszy[dlugosc - kawalek]
            if zysk > najlepszy[dlugosc]:
                najlepszy[dlugosc] = zysk

    return najlepszy[n]


if __name__ == "__main__":
    n = int(input())
    ceny = [int(x) for x in input().split()]
    print(maks_zysk(ceny, n))
