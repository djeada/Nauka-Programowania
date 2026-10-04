r"""
ZAD-02 — Sprawdź poprawność hasła

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `walidacja`

### Treść

Wczytaj hasło i sprawdź, czy spełnia **wszystkie** warunki:

1. ma od 8 do 20 znaków (włącznie),
2. zawiera co najmniej jedną małą literę `a–z`,
3. zawiera co najmniej jedną wielką literę `A–Z`,
4. zawiera co najmniej jedną cyfrę `0–9`,
5. zawiera co najmniej jeden znak specjalny spośród:
   `!` `#` `$` `%` `&` `'` `*` `+` `-` `/` `=` `?` `^` `_` `` ` `` `{` `|` `}` `~`.

Hasło może zawierać także inne znaki (np. spację, `@` albo `ą`). Są one dozwolone, ale nie liczą się do warunków 2–5: `ą` nie jest literą z zakresu `a–z`, a `@` nie należy do listy znaków specjalnych.

### Wejście

* 1. linia: hasło

### Wyjście

* `Prawda` — jeśli hasło spełnia wszystkie warunki,
* `Fałsz` — w przeciwnym razie.

### Przykład

**Wejście:**

```
abc1234
```

**Wyjście:**

```
Fałsz
```

Hasło jest za krótkie, nie ma wielkiej litery ani znaku specjalnego.

### Przykład 2

**Wejście:**

```
Tajne_Haslo7
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Każdy z warunków 2–5 sprawdzisz osobnym `re.search()`, np. `re.search(r"[a-z]", haslo)`.

"""

import re

WARUNKI = [
    r"^.{8,20}$",  # długość od 8 do 20 znaków
    r"[a-z]",  # mała litera
    r"[A-Z]",  # wielka litera
    r"[0-9]",  # cyfra
    r"[!#$%&'*+/=?^_`{|}~-]",  # znak specjalny
]


def czy_haslo_poprawne(haslo):
    return all(re.search(wzorzec, haslo) for wzorzec in WARUNKI)


if __name__ == "__main__":
    haslo = input()
    print("Prawda" if czy_haslo_poprawne(haslo) else "Fałsz")
