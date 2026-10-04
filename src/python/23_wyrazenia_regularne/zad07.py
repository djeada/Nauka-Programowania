r"""
ZAD-07 — Podziel tekst względem znaków interpunkcyjnych

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj tekst (jedno lub kilka zdań) i podziel go na fragmenty w miejscach występowania znaków interpunkcyjnych `,` `.` `!` `?` `;` `:`. Inne znaki (np. myślnik czy cudzysłów) nie dzielą tekstu.

Z każdego fragmentu usuń spacje z początku i końca. Puste fragmenty (np. między `?` a `!` w `?!` albo po kropce na końcu tekstu) pomiń.

### Wejście

* 1. linia: tekst

### Wyjście

Każdy niepusty fragment w osobnej linii, w kolejności występowania.

### Ograniczenia

* Tekst zawiera co najmniej jedną literę, więc zawsze jest co najmniej jeden fragment.

### Przykład

**Wejście:**

```
Ani nie poszedł do kina, ani nie wybrał się do teatru.
```

**Wyjście:**

```
Ani nie poszedł do kina
ani nie wybrał się do teatru
```

### Uwagi

* Podział zrobi `re.split(r"[,.!?;:]", tekst)`.

"""

import re


def podziel_tekst(tekst):
    fragmenty = re.split(r"[,.!?;:]", tekst)
    return [fragment.strip() for fragment in fragmenty if fragment.strip()]


if __name__ == "__main__":
    tekst = input()
    for fragment in podziel_tekst(tekst):
        print(fragment)
