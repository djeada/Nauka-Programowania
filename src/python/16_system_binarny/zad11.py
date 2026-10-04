r"""
ZAD-11 — Palindrom w systemie binarnym

**Poziom:** ★★☆
**Tagi:** `binarne`, `palindrom`, `string`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jej zapis binarny (bez zer wiodących) jest palindromem, czyli czy czytany od końca jest taki sam.

### Wejście

* 1. linia: `n`

### Wyjście

Jedno słowo: `Prawda`, jeśli zapis binarny `n` jest palindromem, w przeciwnym razie `Fałsz`.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
26
```

**Wyjście:**

```
Fałsz
```

`26` ma zapis binarny `11010`, który czytany od końca daje `01011` — to nie jest palindrom.

### Uwagi

* Zapis binarny `0` to `0`, a `1` to `1` — oba są palindromami.

"""


def czy_palindrom_binarny(n):
    """Sprawdza, czy zapis binarny n (bez zer wiodących) czytany od końca jest taki sam."""
    odwrocona = 0
    reszta = n
    while reszta > 0:
        odwrocona = (odwrocona << 1) | (reszta & 1)
        reszta >>= 1
    return odwrocona == n


if __name__ == "__main__":
    n = int(input())
    if czy_palindrom_binarny(n):
        print("Prawda")
    else:
        print("Fałsz")
