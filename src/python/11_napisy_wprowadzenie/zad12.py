"""
ZAD-12 — Usuń spacje ze zdania

**Poziom:** ★☆☆
**Tagi:** `replace`, `string`

### Treść

Wczytaj zdanie i usuń z niego wszystkie spacje.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie bez spacji

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
Alamakota
```

"""


def usun_spacje(zdanie):
    return zdanie.replace(" ", "")


def test_usun_spacje():
    assert usun_spacje("Ala ma kota") == "Alamakota"


if __name__ == "__main__":

    test_usun_spacje()
