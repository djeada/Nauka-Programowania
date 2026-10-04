r"""
ZAD-02C — Iloczyn dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `iloczyn(a, b)`, która zwraca iloczyn $a \cdot b$.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `a`
* 2. linia: liczba całkowita `b`

### Wyjście

Jedna liczba całkowita: $a \cdot b$.

### Przykład

**Wejście:**

```
3
5
```

**Wyjście:**

```
15
```

### Kod startowy

```python
def iloczyn(a, b):
    pass


a = int(input())
b = int(input())
print(iloczyn(a, b))
```

"""


def iloczyn(a, b):
    """Zwraca iloczyn a * b."""
    return a * b


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(iloczyn(a, b))
