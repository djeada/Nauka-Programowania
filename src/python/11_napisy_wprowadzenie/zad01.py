"""
ZAD-01 — Odwróć napis

**Poziom:** ★☆☆
**Tagi:** `string`, `I/O`

### Treść

Wczytaj napis i wypisz go od tyłu.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: odwrócony napis

### Przykład

**Wejście:**

```
barszcz
```

**Wyjście:**

```
zczsrab
```

"""


def odwroc_v1(napis):
    return napis[::-1]


def odwroc_v2(napis):
    nowy_napis = ""
    i = len(napis) - 1
    while i >= 0:
        nowy_napis += napis[i]
        i -= 1
    return nowy_napis


def test_odwroc_v1():
    assert odwroc_v1("ala ma kota") == "kota ma ala"
    assert odwroc_v1("") == ""
    assert odwroc_v1("ala") == "ala"
    assert odwroc_v1("kot") == "tko"


def test_odwroc_v2():
    assert odwroc_v2("ala ma kota") == "kota ma ala"
    assert odwroc_v2("") == ""
    assert odwroc_v2("ala") == "ala"
    assert odwroc_v2("kot") == "tko"


if __name__ == "__main__":

    test_odwroc_v1()
    test_odwroc_v2()
