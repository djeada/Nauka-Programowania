"""
ZAD-02 — Sprawdź poprawność hasła

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `walidacja`

### Treść

Otrzymujesz napis reprezentujący hasło. Sprawdź, czy hasło spełnia wszystkie warunki:

1. Zawiera co najmniej jedną małą literę `[a–z]`.
2. Zawiera co najmniej jedną wielką literę `[A–Z]`.
3. Zawiera co najmniej jedną cyfrę `[0–9]`.
4. Zawiera co najmniej jeden znak specjalny spośród:
   `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`.
5. Ma długość co najmniej 8 znaków.
6. Ma długość nie większą niż 20 znaków.

### Wejście

Jedna linia:

* `haslo`

### Wyjście

Jedna linia:

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
abc1234
```

**Wyjście:**

```
Fałsz
```

"""

import re


def czy_haslo_poprawne(haslo):
    """
    Sprawdza czy haslo jest poprawne.
    """
    if len(haslo) < 8 or len(haslo) > 20:
        return False
    if re.search(r"[a-z]", haslo) is None:
        return False
    if re.search(r"[A-Z]", haslo) is None:
        return False
    if re.search(r"[0-9]", haslo) is None:
        return False
    if re.search(r"[! # $ % & \' * + - / = ? ^ _ ` { | } ~]", haslo) is None:
        return False
    return True


def test_czy_haslo_poprawne():
    assert not czy_haslo_poprawne("Ab1!")
    assert not czy_haslo_poprawne("haslo")
    assert not czy_haslo_poprawne("HASLO")
    assert not czy_haslo_poprawne("HASLO123!@#")
    assert not czy_haslo_poprawne("12345678")
    assert not czy_haslo_poprawne("proste_haslo")
    assert not czy_haslo_poprawne("Haslo123")
    assert czy_haslo_poprawne("Haslo123!")
    assert czy_haslo_poprawne("Haslo123!#")
    assert czy_haslo_poprawne("Haslo123!#$")
    assert czy_haslo_poprawne("Haslo123!#$%&*")


if __name__ == "__main__":
    test_czy_haslo_poprawne()
