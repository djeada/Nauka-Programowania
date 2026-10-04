r"""
ZAD-01B — Zwracanie stałej wartości: napis „Tak”

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `string`

### Treść

Napisz bezargumentową funkcję `zwroc_napis()`, która zwraca napis `Tak`.

Program wywołuje funkcję i wypisuje zwrócony wynik.

### Wejście

Brak.

### Wyjście

Jedna linia: napis zwrócony przez funkcję, czyli `Tak`.

### Przykład

**Wejście:** *(brak)*

**Wyjście:**

```
Tak
```

### Kod startowy

```python
def zwroc_napis():
    pass


print(zwroc_napis())
```

"""


def zwroc_napis():
    """Zwraca napis "Tak"."""
    return "Tak"


if __name__ == "__main__":
    print(zwroc_napis())
