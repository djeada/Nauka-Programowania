r"""
ZAD-05 — Sortowanie trzech liczb

**Poziom:** ★★☆
**Tagi:** `sort`, `warunki`, `porządkowanie`

### Treść

Wczytaj trzy liczby naturalne `a`, `b`, `c` i wypisz je w kolejności niemalejącej (od najmniejszej do największej).

### Wejście

* 1 linia: `a` — liczba całkowita, $0 \le a \le 10^9$
* 2 linia: `b` — liczba całkowita, $0 \le b \le 10^9$
* 3 linia: `c` — liczba całkowita, $0 \le c \le 10^9$

### Wyjście

Jedna linia: trzy liczby w kolejności niemalejącej, oddzielone pojedynczymi spacjami.
Liczby powtarzające się wypisz tyle razy, ile wystąpiły.

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

* Możesz użyć wbudowanego sortowania, ale spróbuj rozwiązać zadanie samymi instrukcjami warunkowymi.

"""


def posortuj_trzy(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return f"{a} {b} {c}"


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(posortuj_trzy(a, b, c))
