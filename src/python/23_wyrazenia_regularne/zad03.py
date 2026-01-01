"""
ZAD-03 — Sprawdź, czy napis składa się wyłącznie z cyfr

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis. Sprawdź, czy składa się wyłącznie z cyfr (`0–9`).

### Wejście

Jedna linia:

* `s`

### Wyjście

Jedna linia:

* `Prawda` — jeśli napis zawiera tylko cyfry
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
1234
```

**Wyjście:**

```
Prawda
```

"""

import re


def czy_numeryczny_v1(napis):
    """
    Funkcja sprawdza, czy napis sklada sie wylacznie z cyfr.
    """
    if not napis:
        return False

    for znak in napis:
        if znak not in "0123456789":
            return False
    return True


def czy_numeryczny_v2(napis):
    """
    Funkcja sprawdza, czy napis sklada sie wylacznie z cyfr.
    """
    return re.match(r"^[0-9]+$", napis) is not None


def test_czy_numeryczny_v1():
    assert czy_numeryczny_v1("123")
    assert not czy_numeryczny_v1("123a")
    assert not czy_numeryczny_v1("")


def test_czy_numeryczny_v2():
    assert czy_numeryczny_v2("123")
    assert not czy_numeryczny_v2("123a")
    assert not czy_numeryczny_v2("")


if __name__ == "__main__":
    test_czy_numeryczny_v1()
    test_czy_numeryczny_v2()
