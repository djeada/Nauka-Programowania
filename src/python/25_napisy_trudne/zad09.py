r"""
ZAD-09 — Najdłuższy wspólny podnapis

**Poziom:** ★★★
**Tagi:** `string`, `dp`, `substring`

### Treść

Otrzymujesz dwa napisy `A` i `B`. Znajdź ich **najdłuższy wspólny podnapis**, czyli najdłuższy ciągły fragment, który występuje zarówno w `A`, jak i w `B`.

* Jeśli kilka różnych podnapisów ma tę samą, maksymalną długość — wypisz ten, który w napisie `A` **zaczyna się najwcześniej**.
* Jeśli napisy nie mają ani jednego wspólnego znaku — wypisz pustą linię.

### Wejście

* 1. linia: napis `A`
* 2. linia: napis `B`

### Wyjście

Jedna linia: najdłuższy wspólny podnapis albo pusta linia.

### Ograniczenia

* `1 ≤ |A|, |B| ≤ 1000`

### Przykład

**Wejście:**

```
ijkabcdl
xxxxabcd
```

**Wyjście:**

```
abcd
```

### Przykład 2

**Wejście:**

```
xyab
abxy
```

**Wyjście:**

```
xy
```

Oba podnapisy `xy` i `ab` mają długość 2; w `A` wcześniej zaczyna się `xy`.

### Uwagi

* Programowanie dynamiczne: niech `d[i][j]` oznacza długość najdłuższego wspólnego fragmentu **kończącego się** na znakach `A[i - 1]` i `B[j - 1]`. Jeśli te znaki są równe, `d[i][j] = d[i - 1][j - 1] + 1`, w przeciwnym razie `0`. Największa wartość w tablicy to długość wyniku. Czas $O(|A| \cdot |B|)$.

"""


def najdluzszy_wspolny_podnapis(napis_a, napis_b):
    """Najdłuższy wspólny podnapis; przy remisie ten, który zaczyna się najwcześniej w A."""
    m, n = len(napis_a), len(napis_b)
    # dl[i][j] — długość wspólnego fragmentu kończącego się na napis_a[i-1] i napis_b[j-1]
    dl = [[0] * (n + 1) for _ in range(m + 1)]

    najlepszy_koniec, najlepsza_dlugosc = 0, 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if napis_a[i - 1] == napis_b[j - 1]:
                dl[i][j] = dl[i - 1][j - 1] + 1
                if dl[i][j] > najlepsza_dlugosc:
                    najlepsza_dlugosc = dl[i][j]
                    najlepszy_koniec = i

    return napis_a[najlepszy_koniec - najlepsza_dlugosc : najlepszy_koniec]


if __name__ == "__main__":
    napis_a = input()
    napis_b = input()
    print(najdluzszy_wspolny_podnapis(napis_a, napis_b))
