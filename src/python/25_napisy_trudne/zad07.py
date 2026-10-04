r"""
ZAD-07 — Najdłuższy powtarzający się podnapis

**Poziom:** ★★★
**Tagi:** `string`, `substrings`, `dp`

### Treść

Otrzymujesz napis. Znajdź **najdłuższy podnapis, który występuje w nim co najmniej dwa razy**. Wystąpienia mogą na siebie nachodzić — na przykład w napisie `aaaa` podnapis `aaa` występuje dwa razy (od indeksu 0 i od indeksu 1).

* Jeśli kilka różnych podnapisów ma tę samą, maksymalną długość — wypisz ten, którego **pierwsze wystąpienie zaczyna się najwcześniej**.
* Jeśli żaden znak się nie powtarza (nie ma powtarzającego się podnapisu) — wypisz pustą linię.

### Wejście

Jedna linia: napis `S`.

### Wyjście

Jedna linia: najdłuższy powtarzający się podnapis albo pusta linia.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`

### Przykład

**Wejście:**

```
pythonpython
```

**Wyjście:**

```
python
```

### Przykład 2

**Wejście:**

```
cdabxabycd
```

**Wyjście:**

```
cd
```

Podnapisy `cd` i `ab` powtarzają się i oba mają długość 2, ale `cd` występuje po raz pierwszy wcześniej (od indeksu 0), a `ab` — dopiero od indeksu 2.

### Uwagi

* Programowanie dynamiczne: niech `w[i][j]` (dla `i < j`) oznacza długość najdłuższego wspólnego początku fragmentów `S[i:]` i `S[j:]`. Jeśli `S[i] == S[j]`, to `w[i][j] = w[i + 1][j + 1] + 1`, w przeciwnym razie `0`. Wynikiem jest największa wartość w tablicy. Jeśli przeglądasz pary `(i, j)` w kolejności rosnącego `i` i zmieniasz wynik tylko na ściśle dłuższy, remisy rozstrzygną się same. Czas $O(n^2)$.
* Sprawdzanie każdego podnapisu (jest ich około $n^2/2$) z osobnym wyszukiwaniem w całym napisie daje czas $O(n^3)$ — przy długich napisach to za dużo.

"""


def najdluzsze_powtorzenie(napis):
    """Najdłuższy podnapis występujący co najmniej dwa razy (wystąpienia mogą się nakładać).

    Przy remisie wybiera podnapis, którego pierwsze wystąpienie zaczyna się najwcześniej.
    """
    n = len(napis)
    # wspolne[i][j] — długość najdłuższego wspólnego początku napis[i:] i napis[j:]
    wspolne = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if napis[i] == napis[j]:
                wspolne[i][j] = wspolne[i + 1][j + 1] + 1

    najlepszy_start, najlepsza_dlugosc = 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            if wspolne[i][j] > najlepsza_dlugosc:
                najlepsza_dlugosc = wspolne[i][j]
                najlepszy_start = i

    return napis[najlepszy_start : najlepszy_start + najlepsza_dlugosc]


if __name__ == "__main__":
    napis = input()
    print(najdluzsze_powtorzenie(napis))
