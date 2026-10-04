r"""
ZAD-01C — Zwracanie stałej wartości: True

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `bool`

### Treść

Napisz bezargumentową funkcję `zwroc_prawda()`, która zwraca wartość logiczną `True`.

Program wywołuje funkcję i wypisuje zwrócony wynik.

### Wejście

Brak.

### Wyjście

Jedna linia: wartość zwrócona przez funkcję, czyli `True`.

### Przykład

**Wejście:** *(brak)*

**Wyjście:**

```
True
```

### Uwagi

* Funkcja ma zwrócić wartość logiczną `True`, a nie napis `"True"`. Po wypisaniu wyglądają tak samo, ale to różne typy danych.

### Kod startowy

```python
def zwroc_prawda():
    pass


print(zwroc_prawda())
```

"""


def zwroc_prawda():
    """Zwraca wartość logiczną True."""
    return True


if __name__ == "__main__":
    print(zwroc_prawda())
