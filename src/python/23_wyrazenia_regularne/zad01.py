r"""
ZAD-01 — Sprawdź poprawność adresu e-mail

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `walidacja`

### Treść

Wczytaj napis i sprawdź, czy jest poprawnym adresem e-mail według poniższych (uproszczonych) reguł.

* Adres ma postać `identyfikator@domena`: zawiera **dokładnie jeden** znak `@`, a identyfikator i domena są niepuste.
* **Identyfikator** składa się wyłącznie z:
  * liter `a–z` i `A–Z` (bez polskich znaków),
  * cyfr `0–9`,
  * znaków specjalnych `!` `#` `$` `%` `&` `'` `*` `+` `-` `/` `=` `?` `^` `_` `` ` `` `{` `|` `}` `~`,
  * kropek `.` — ale kropka nie może być pierwszym ani ostatnim znakiem identyfikatora i nie mogą stać dwie kropki obok siebie.
* **Domena** składa się wyłącznie z liter `a–z` i `A–Z`, cyfr `0–9`, kropek `.` i myślników `-`, przy czym:
  * zawiera co najmniej jedną kropkę,
  * nie zaczyna się ani nie kończy kropką ani myślnikiem,
  * żadne dwa znaki spośród `.` i `-` nie stoją obok siebie (niedozwolone są np. `..`, `--`, `.-`, `-.`).
* Żadne inne znaki (np. spacje) nie mogą wystąpić w adresie.

### Wejście

* 1. linia: napis do sprawdzenia

### Wyjście

* `Prawda` — jeśli napis jest poprawnym adresem e-mail,
* `Fałsz` — w przeciwnym razie.

### Przykład

**Wejście:**

```
adam@gmail.com
```

**Wyjście:**

```
Prawda
```

### Przykład 2

**Wejście:**

```
jan..nowak@poczta.pl
```

**Wyjście:**

```
Fałsz
```

W identyfikatorze stoją obok siebie dwie kropki.

### Uwagi

* Do sprawdzenia, czy **cały** napis pasuje do wzorca, służy `re.fullmatch(wzorzec, napis)`.
* Fragment „ciąg znaków bez kropek, a potem dowolnie wiele razy: kropka i znowu ciąg znaków” zapiszesz jako `X+(\.X+)*`, gdzie `X` to klasa dozwolonych znaków.
* W klasie znaków `[...]` myślnik umieść na końcu albo poprzedź go `\`, inaczej oznacza zakres (np. `+-/` to zakres od `+` do `/`).

"""

import re

# Identyfikator: ciągi dozwolonych znaków rozdzielone pojedynczymi kropkami.
ZNAK_IDENTYFIKATORA = r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]"
IDENTYFIKATOR = ZNAK_IDENTYFIKATORA + r"+(?:\." + ZNAK_IDENTYFIKATORA + r"+)*"

# Domena: co najmniej dwie etykiety rozdzielone kropkami; etykieta to ciągi
# liter i cyfr rozdzielone pojedynczymi myślnikami.
ETYKIETA = r"[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*"
DOMENA = ETYKIETA + r"(?:\." + ETYKIETA + r")+"

EMAIL = IDENTYFIKATOR + "@" + DOMENA


def czy_email_poprawny(email):
    return re.fullmatch(EMAIL, email) is not None


if __name__ == "__main__":
    email = input()
    print("Prawda" if czy_email_poprawny(email) else "Fałsz")
