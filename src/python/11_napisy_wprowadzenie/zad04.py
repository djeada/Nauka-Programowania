r"""
ZAD-04 — Zamień wszystkie małe litery na duże

**Poziom:** ★☆☆
**Tagi:** `napisy`, `upper`

### Treść

Wczytaj napis i zamień w nim wszystkie małe litery (także polskie, np. `ż` → `Ż`) na wielkie. Pozostałe znaki pozostaw bez zmian.

### Wejście

* 1. linia: napis (może zawierać spacje)

### Wyjście

Jedna linia: napis po zamianie.

### Przykład

**Wejście:**

```
Rumcajs
```

**Wyjście:**

```
RUMCAJS
```

"""


def na_wielkie(napis):
    return napis.upper()


if __name__ == "__main__":
    napis = input()
    print(na_wielkie(napis))
