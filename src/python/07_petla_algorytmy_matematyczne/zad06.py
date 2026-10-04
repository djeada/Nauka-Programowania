r"""
ZAD-06 — Najmniejsza wspólna wielokrotność (NWW)

**Poziom:** ★☆☆
**Tagi:** `nww`, `nwd`, `arytmetyka`

### Treść

Napisz funkcję `nww(a, b)`, która zwraca najmniejszą wspólną wielokrotność liczb `a` i `b`.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba naturalna (`a ≥ 1`)
* 2. linia: `b` — liczba naturalna (`b ≥ 1`)

### Wyjście

Jedna liczba całkowita — $\text{NWW}(a, b)$.

### Przykład

**Wejście:**

```
7
9
```

**Wyjście:**

```
63
```

### Uwagi

* Możesz skorzystać z funkcji `nwd` z poprzedniego zadania i zależności $\text{NWW}(a, b) = \frac{a \cdot b}{\text{NWD}(a, b)}$.
* Wynik jest liczbą całkowitą — użyj dzielenia całkowitego `//`.

### Kod startowy

```python
def nwd(a, b):
    pass


def nww(a, b):
    pass


a = int(input())
b = int(input())
print(nww(a, b))
```

"""


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nww(a, b):
    return a * b // nwd(a, b)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(nww(a, b))
