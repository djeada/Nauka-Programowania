r"""
ZAD-04 — Sprawdź, czy słowo występuje w zdaniu jako osobne słowo

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj zdanie i słowo. Sprawdź, czy słowo występuje w zdaniu jako **całe słowo**, a nie tylko jako fragment innego słowa. Wielkość liter ma znaczenie.

Słowa rozumiemy jak w konwencjach rozdziału, więc np. w zdaniu `flaga biało-czerwona` występuje słowo `czerwona`, ale nie występuje słowo `flag`.

### Wejście

* 1. linia: zdanie
* 2. linia: słowo (tylko litery i cyfry)

### Wyjście

* `Prawda` — jeśli słowo występuje w zdaniu jako całe słowo,
* `Fałsz` — w przeciwnym razie.

### Przykład

**Wejście:**

```
Siała baba mak.
mak
```

**Wyjście:**

```
Prawda
```

### Przykład 2

**Wejście:**

```
Siała baba mak.
bab
```

**Wyjście:**

```
Fałsz
```

`bab` jest tylko fragmentem słowa `baba`.

### Uwagi

* Otocz słowo granicami `\b`: `re.search(r"\b" + re.escape(slowo) + r"\b", zdanie)`.

"""

import re


def czy_zawiera_slowo(zdanie, slowo):
    return re.search(r"\b" + re.escape(slowo) + r"\b", zdanie) is not None


if __name__ == "__main__":
    zdanie = input()
    slowo = input()
    print("Prawda" if czy_zawiera_slowo(zdanie, slowo) else "Fałsz")
