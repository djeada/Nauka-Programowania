r"""
ZAD-02B — Różnica: b − a

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `roznica(a, b)`, która zwraca różnicę $b - a$ (od **drugiej** liczby odejmujemy pierwszą).

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `a`
* 2. linia: liczba całkowita `b`

### Wyjście

Jedna liczba całkowita: $b - a$.

### Przykład

**Wejście:**

```
3
5
```

**Wyjście:**

```
2
```

### Kod startowy

```python
def roznica(a, b):
    pass


a = int(input())
b = int(input())
print(roznica(a, b))
```

"""


def roznica(a, b):
    """Zwraca różnicę b - a."""
    return b - a


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(roznica(a, b))
