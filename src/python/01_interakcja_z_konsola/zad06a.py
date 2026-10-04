r"""
ZAD-06A — Kilogramy → gramy

**Poziom:** ★☆☆
**Tagi:** `konwersje`

### Treść

Wczytaj masę w kilogramach `kg` i przelicz ją na gramy: $g = kg \cdot 1000$.

### Wejście

* 1 linia: `kg` — liczba całkowita lub zmiennoprzecinkowa

### Wyjście

Jedna linia: `g` jako **liczba całkowita** (bez części ułamkowej).

### Ograniczenia

* $0 \le kg \le 10^6$
* `kg` ma co najwyżej 3 cyfry po przecinku, więc wynik w gramach jest całkowity.

### Przykład

**Wejście:**

```
2.5
```

**Wyjście:**

```
2500
```

### Uwagi

* Uwaga na błędy zaokrągleń liczb zmiennoprzecinkowych: np. `1.001 * 1000` daje w Pythonie `1000.9999999999999`, więc `int(...)` zwróciłoby `1000`. Zamiast obcinać, zaokrąglij wynik: `round(kg * 1000)`.

"""


def kilogramy_na_gramy(kg):
    return round(kg * 1000)


if __name__ == "__main__":
    kg = float(input())
    print(kilogramy_na_gramy(kg))
