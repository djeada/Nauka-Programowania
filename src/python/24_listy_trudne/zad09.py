r"""
ZAD-09 — Najdłuższy naprzemienny podciąg

**Poziom:** ★★★
**Tagi:** `dp`, `subsequence`, `naprzemienny`

### Treść

Ciąg $x_1, x_2, \ldots, x_k$ jest **naprzemienny** (zygzakowaty), jeśli różnice między kolejnymi elementami są na przemian dodatnie i ujemne, czyli $x_1 < x_2 > x_3 < x_4 > \ldots$ albo $x_1 > x_2 < x_3 > x_4 < \ldots$

Ciąg jednoelementowy też jest naprzemienny. Dwa równe sąsiednie elementy psują naprzemienność (różnica `0` nie jest ani dodatnia, ani ujemna).

Otrzymujesz listę liczb całkowitych. Wyznacz **długość najdłuższego naprzemiennego podciągu** tej listy. Podciąg powstaje przez usunięcie z listy dowolnych elementów (być może żadnego) bez zmiany kolejności pozostałych — jego elementy nie muszą ze sobą sąsiadować na liście.

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna liczba całkowita — długość najdłuższego naprzemiennego podciągu.

### Ograniczenia

* `1 ≤ n ≤ 1000`
* elementy listy są z przedziału $[-10^6, 10^6]$

### Przykład

**Wejście:**

```
8
1 -2 6 4 -3 2 -4 -3
```

**Wyjście:**

```
7
```

Przykładowy najdłuższy podciąg naprzemienny (pominięto `4`): $1 > -2 < 6 > -3 < 2 > -4 < -3$.

### Uwagi

* Podciągów jest $2^n$, więc sprawdzanie wszystkich jest wykluczone — w testach są listy z setkami elementów.
* Programowanie dynamiczne: idąc po liście, pamiętaj długość najdłuższego naprzemiennego podciągu kończącego się **wzrostem** i kończącego się **spadkiem**. Gdy bieżący element jest większy od poprzedniego, podciąg „kończący się spadkiem” można przedłużyć wzrostem (i odwrotnie). Daje to czas $O(n)$; rozwiązanie $O(n^2)$ też zdąży.

"""


def najdluzszy_naprzemienny(liczby):
    """Długość najdłuższego naprzemiennego (zygzakowatego) podciągu."""
    # w_gore — najdłuższy podciąg (z dotychczasowych elementów) kończący się wzrostem,
    # w_dol  — najdłuższy podciąg kończący się spadkiem.
    w_gore, w_dol = 1, 1

    for i in range(1, len(liczby)):
        if liczby[i] > liczby[i - 1]:
            w_gore = w_dol + 1
        elif liczby[i] < liczby[i - 1]:
            w_dol = w_gore + 1

    return max(w_gore, w_dol)


if __name__ == "__main__":
    n = int(input())
    liczby = [int(x) for x in input().split()]
    print(najdluzszy_naprzemienny(liczby))
