"""
ZAD-05 — Sortowanie trzech liczb

**Poziom:** ★★☆
**Tagi:** `sort`, `warunki`, `porządkowanie`

### Treść

Wczytaj trzy liczby naturalne `a`, `b`, `c` i wypisz je w kolejności rosnącej.

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)
* 3 linia: `c` (całkowita, `c ≥ 0`)

### Wyjście

Jedna linia: trzy liczby rosnąco, oddzielone pojedynczymi spacjami.

### Przykład

**Wejście:**

```
2
1
4
```

**Wyjście:**

```
1 2 4
```

### Uwagi

* Możesz użyć wbudowanego sortowania, ale da się też rozwiązać czystymi warunkami.

"""

if __name__ == "__main__":

    print("podaj trzy liczby")

    a = int(input())
    b = int(input())
    c = int(input())

    if a >= b and a >= c:
        if b >= c:
            print(c, b, a)
        else:
            print(b, c, a)

    elif c >= b and c >= a:
        if a >= b:
            print(b, a, c)
        else:
            print(a, b, c)

    else:
        if a >= c:
            print(c, a, b)
        else:
            print(a, c, b)
