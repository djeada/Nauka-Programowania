"""
ZAD-05 — Wyodrębnij cyfry z tekstu

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis zawierający różne znaki. Wyodrębnij wszystkie cyfry i wypisz je jako jeden napis (z zachowaniem kolejności).

### Wejście

Jedna linia:

* `tekst`

### Wyjście

Jedna linia:

* napis złożony tylko z cyfr z tekstu wejściowego

### Przykład

**Wejście:**

```
Terminator2001
```

**Wyjście:**

```
2001
```

"""

import re


def odfiltruj_cyfry(slowo):
    return re.sub("[^\d]", "", slowo)


def test_odfiltruj_cyfry():
    assert odfiltruj_cyfry("numer 32.19 wyzej niz 31.17") == "32193117"


if __name__ == "__main__":
    test_odfiltruj_cyfry()
