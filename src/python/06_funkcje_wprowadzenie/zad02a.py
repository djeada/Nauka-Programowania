r"""
ZAD-02A — Suma dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `suma(a, b)`, która zwraca sumę $a + b$ dwóch liczb całkowitych.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `a`
* 2. linia: liczba całkowita `b`

### Wyjście

Jedna liczba całkowita: $a + b$.

### Przykład

**Wejście:**

```
3
5
```

**Wyjście:**

```
8
```

### Kod startowy

```python
def suma(a, b):
    pass


a = int(input())
b = int(input())
print(suma(a, b))
```

"""


def suma(a, b):
    """Zwraca sumę a + b."""
    return a + b


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(suma(a, b))
