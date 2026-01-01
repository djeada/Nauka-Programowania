"""
ZAD-07 — Zamień znaki na kody ASCII

**Poziom:** ★☆☆
**Tagi:** `ASCII`, `ord`, `string`

### Treść

Wczytaj napis i wypisz kody ASCII wszystkich jego znaków, oddzielone przecinkiem i spacją `", "`.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: kody ASCII oddzielone `, `

### Przykład

**Wejście:**

```
Robot
```

**Wyjście:**

```
82, 111, 98, 111, 116
```

"""


def znaki_na_ascii(napis):

    nowy_napis = ""
    for znak in napis:
        nowy_napis += str(ord(znak)) + ", "

    return nowy_napis[:-2]


def test_znaki_na_ascii():
    assert znaki_na_ascii("abcdef") == "97, 98, 99, 100, 101, 102"
    assert (
        znaki_na_ascii("ala ma kota")
        == "97, 108, 97, 32, 109, 97, 32, 107, 111, 116, 97"
    )


if __name__ == "__main__":

    test_znaki_na_ascii()
