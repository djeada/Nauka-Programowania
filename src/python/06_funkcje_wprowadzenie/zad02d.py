r"""
ZAD-02D — Iloraz całkowity: a // b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `dzielenie`, `//`

### Treść

Napisz funkcję `iloraz(a, b)`, która zwraca iloraz całkowity `a // b`.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `a`
* 2. linia: liczba całkowita `b`

### Wyjście

Jedna liczba całkowita: `a // b`.

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
0
```

### Uwagi

* Operator `//` zaokrągla wynik dzielenia **w dół**, także dla liczb ujemnych, np. `-7 // 2` daje `-4`.

### Kod startowy

```python
def iloraz(a, b):
    pass


a = int(input())
b = int(input())
print(iloraz(a, b))
```

"""


def iloraz(a, b):
    """Zwraca iloraz całkowity a // b."""
    return a // b


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(iloraz(a, b))
