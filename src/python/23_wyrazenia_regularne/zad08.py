"""
ZAD-08 — Cyfry w słowach

**Poziom:** ★★☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz zdanie. Wyodrębnij wszystkie ciągi cyfr, które są częścią słów (czyli są bezpośrednio połączone z literami). Nie uwzględniaj cyfr oddzielonych od liter spacjami.

### Wejście

Jedna linia:

* `zdanie`

### Wyjście

Każdy znaleziony ciąg cyfr w osobnej linii (w kolejności występowania).

### Przykład

**Wejście:**

```
Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego
```

**Wyjście:**

```
29
37
3
91
```

"""

import re


def cyfry_w_slowach(tekst):
    """
    Funkcja zwraca liste cyfr w slowach w tekscie.
    """
    return [
        re.sub("[^\d]", "", e) for e in tekst.split() if re.search(r"\B[0-9]+\B", e)
    ]


def test_cyfry_w_slowach():
    assert cyfry_w_slowach("jerzy29 i an37a s3uc8ali91 lekcji jezyka polki3go") == [
        "29",
        "37",
        "3891",
        "3",
    ]


if __name__ == "__main__":
    test_cyfry_w_slowach()
