r"""
ZAD-09 — Usuń fragment napisu od pierwszego wystąpienia słowa klucz

**Poziom:** ★★☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj tekst wielowierszowy i słowo klucz. Znajdź **pierwsze** wystąpienie słowa klucz w tekście jako **całego słowa** (zob. konwencje rozdziału; wielkość liter ma znaczenie). Usuń wszystko od początku tego wystąpienia do **końca tekstu** — także wszystkie dalsze wiersze — i wypisz to, co zostało.

Jeśli słowo klucz nie występuje w tekście, wypisz tekst bez zmian. Jeśli słowo klucz jest pierwszym słowem tekstu, nic nie wypisuj.

### Wejście

* 1. linia: `n` — liczba wierszy tekstu
* kolejne `n` linii: tekst
* ostatnia linia: słowo klucz (tylko litery i cyfry)

### Wyjście

Pozostała część tekstu: wiersze przed wierszem z wystąpieniem słowa klucz w całości, a z tego wiersza — tylko fragment przed słowem klucz.

### Ograniczenia

* $1 \le n \le 100$

### Przykład

**Wejście:**

```
3
Ala ma kota, a kot ma Alę.
Kot lubi mleko i spać.
Mleko jest białe.
mleko
```

**Wyjście:**

```
Ala ma kota, a kot ma Alę.
Kot lubi
```

Słowo `Mleko` w trzecim wierszu nie pasuje (wielka litera), a pierwsze `mleko` jest w drugim wierszu.

### Uwagi

* Złącz wiersze w jeden napis (`"\n".join(...)`) i znajdź wystąpienie przez `re.search()` — metoda `start()` dopasowania poda jego pozycję.
* Sprawdzarka ignoruje spacje na końcu wierszy i puste wiersze na końcu wyjścia.

"""

import re


def usun_od_slowa(tekst, klucz):
    """Zwraca tekst obcięty tuż przed pierwszym wystąpieniem słowa klucz."""
    dopasowanie = re.search(r"\b" + re.escape(klucz) + r"\b", tekst)
    if dopasowanie is None:
        return tekst
    return tekst[: dopasowanie.start()]


if __name__ == "__main__":
    n = int(input())
    tekst = "\n".join(input() for _ in range(n))
    klucz = input()

    wynik = usun_od_slowa(tekst, klucz)
    if wynik:
        print(wynik)
