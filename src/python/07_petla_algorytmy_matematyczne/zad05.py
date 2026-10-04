r"""
ZAD-05 — Największy wspólny dzielnik (NWD)

**Poziom:** ★☆☆
**Tagi:** `Euklides`, `modulo`, `pętle`

### Treść

Napisz funkcję `nwd(a, b)`, która zwraca największy wspólny dzielnik liczb `a` i `b`. Użyj pętli (np. algorytmu Euklidesa), a nie funkcji `math.gcd()`.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba naturalna (`a ≥ 1`)
* 2. linia: `b` — liczba naturalna (`b ≥ 1`)

### Wyjście

Jedna liczba całkowita — $\text{NWD}(a, b)$.

### Przykład

**Wejście:**

```
60
45
```

**Wyjście:**

```
15
```

### Uwagi

* Algorytm Euklidesa: dopóki $b \neq 0$, zastępuj parę $(a, b)$ parą $(b, a \bmod b)$. Na końcu wynikiem jest $a$.

### Kod startowy

```python
def nwd(a, b):
    pass


a = int(input())
b = int(input())
print(nwd(a, b))
```

"""


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(nwd(a, b))
