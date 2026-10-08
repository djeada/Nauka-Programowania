r"""
ZAD-06B — Dwucyfrowe większe od n o różnych cyfrach

**Poziom:** ★★☆
**Tagi:** `pętle`, `cyfry`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby dwucyfrowe `x` (od `10` do `99`) takie, że `x > n` i cyfra dziesiątek liczby `x` jest **różna** od jej cyfry jedności.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
90
```

**Wyjście:**

```
91
92
93
94
95
96
97
98
```

Liczba `99` jest większa od `90`, ale ma dwie jednakowe cyfry, więc jej nie wypisujemy.

### Uwagi

* Cyfrę jedności liczby `x` daje `x % 10`, a cyfrę dziesiątek liczby dwucyfrowej — `x // 10`.
* Nierówność jest ostra: samej liczby `n` nie wypisujemy.
* Dla `n ≥ 98` żadna liczba nie spełnia warunku.

"""


def rozne_cyfry(x):
    """Sprawdza, czy cyfra dziesiątek liczby dwucyfrowej x różni się od cyfry jedności."""
    return x // 10 != x % 10


if __name__ == "__main__":
    n = int(input())

    for x in range(max(n + 1, 10), 100):
        if rozne_cyfry(x):
            print(x)
