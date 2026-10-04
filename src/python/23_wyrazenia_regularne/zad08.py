r"""
ZAD-08 — Cyfry w słowach

**Poziom:** ★★☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj zdanie i wypisz wszystkie ciągi cyfr, które są „przyklejone” do liter. Chodzi o najdłuższe ciągi kolejnych cyfr `0–9`, bezpośrednio przed którymi **lub** bezpośrednio po których stoi litera (także polska).

Cyfry oddzielone od liter spacją, interpunkcją czy myślnikiem się nie liczą. Na przykład w `s3łuchali91` są dwa ciągi: `3` i `91`, w `3.5kg` tylko `5`, a samodzielna liczba `22` nie jest wynikiem.

### Wejście

* 1. linia: zdanie

### Wyjście

* Znalezione ciągi cyfr, każdy w osobnej linii, w kolejności występowania (z zerami na początku, jeśli są),
* `Brak ciągów cyfr.` — jeśli nie ma żadnego takiego ciągu.

### Przykład

**Wejście:**

```
Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego
```

**Wyjście:**

```
29
37
3
91
```

### Uwagi

* Przydadzą się asercje: `(?<=...)` sprawdza, co stoi tuż przed dopasowaniem, a `(?=...)` — co stoi tuż po nim. Dowolną literę (także polską) opisuje klasa `[^\W\d_]` („znak słowa, który nie jest cyfrą ani `_`”).

"""

import re

LITERA = r"[^\W\d_]"  # znak słowa, który nie jest cyfrą ani '_' — czyli litera
CYFRY_PRZY_LITERZE = rf"(?<={LITERA})[0-9]+|[0-9]+(?={LITERA})"


def cyfry_w_slowach(zdanie):
    return re.findall(CYFRY_PRZY_LITERZE, zdanie)


if __name__ == "__main__":
    zdanie = input()
    wynik = cyfry_w_slowach(zdanie)
    if wynik:
        print("\n".join(wynik))
    else:
        print("Brak ciągów cyfr.")
