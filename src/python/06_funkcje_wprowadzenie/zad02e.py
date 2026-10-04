r"""
ZAD-02E — Reszta z dzielenia: a % b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `modulo`, `%`

### Treść

Napisz funkcję `reszta(a, b)`, która zwraca resztę z dzielenia `a % b`.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `a`
* 2. linia: liczba całkowita `b`

### Wyjście

Jedna liczba całkowita: `a % b`.

### Ograniczenia

* $b \neq 0$

### Przykład

**Wejście:**

```
3
5
```

**Wyjście:**

```
3
```

### Uwagi

* W Pythonie wynik `a % b` ma ten sam znak co `b`, np. `-7 % 3` daje `2`.

### Kod startowy

```python
def reszta(a, b):
    pass


a = int(input())
b = int(input())
print(reszta(a, b))
```

"""


def reszta(a, b):
    """Zwraca resztę z dzielenia a % b."""
    return a % b


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(reszta(a, b))
