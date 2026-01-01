"""
ZAD-04 — Sprawdź, czy słowo występuje w zdaniu jako osobne słowo

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz dwa napisy: zdanie oraz słowo. Sprawdź, czy słowo występuje w zdaniu jako samodzielne słowo (nie jako fragment innego słowa).

### Wejście

Dwie linie:

1. `zdanie`
2. `slowo`

### Wyjście

Jedna linia:

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
Siała baba mak.
babcia
```

**Wyjście:**

```
Fałsz
```

"""

import re


def czy_pierwszy_napis_zawiera_drugi_napis_v1(napis1, napis2):
    return napis2 in napis1


def czy_pierwszy_napis_zawiera_drugi_napis_v2(napis1, napis2):
    return re.search(napis2, napis1)


def test_czy_pierwszy_napis_zawiera_drugi_napis_v1():
    assert not czy_pierwszy_napis_zawiera_drugi_napis_v1("Ala ma kota", "kotek")
    assert not czy_pierwszy_napis_zawiera_drugi_napis_v1("Ala ma kota", "ala")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v1("Ala ma kota", "ma")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v1("Ala ma kota", "Ala")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v1("Ala ma kota", "Ala ma")


def test_czy_pierwszy_napis_zawiera_drugi_napis_v2():
    assert not czy_pierwszy_napis_zawiera_drugi_napis_v2("Ala ma kota", "kotek")
    assert not czy_pierwszy_napis_zawiera_drugi_napis_v2("Ala ma kota", "ala")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v2("Ala ma kota", "ma")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v2("Ala ma kota", "Ala")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v2("Ala ma kota", "Ala ma")


if __name__ == "__main__":
    test_czy_pierwszy_napis_zawiera_drugi_napis_v1()
    test_czy_pierwszy_napis_zawiera_drugi_napis_v2()
