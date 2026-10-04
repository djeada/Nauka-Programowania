r"""
ZAD-02 — Zamiana kolejności liczb

**Poziom:** ★☆☆
**Tagi:** `I/O`, `zmienne`

### Treść

Wczytaj dwie liczby całkowite i wypisz je w odwrotnej kolejności (każdą w osobnej linii).

### Wejście

* 1. linia: `a` — liczba całkowita
* 2. linia: `b` — liczba całkowita

### Wyjście

Dwie linie:

* 1. linia: `b`
* 2. linia: `a`

### Ograniczenia

* $-10^9 \le a, b \le 10^9$

### Przykład

**Wejście:**

```
-7
4
```

**Wyjście:**

```
4
-7
```

"""

if __name__ == "__main__":
    a = int(input())
    b = int(input())

    print(b)
    print(a)
