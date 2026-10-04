r"""
ZAD-06 — Zamień litery „a” na „?”

**Poziom:** ★☆☆
**Tagi:** `napisy`, `replace`

### Treść

Wczytaj napis i zamień w nim wszystkie małe litery `a` na znak `?`. Wielkie `A` pozostaw bez zmian.

### Wejście

* 1. linia: napis (może zawierać spacje)

### Wyjście

Jedna linia: napis po zamianie.

### Przykład

**Wejście:**

```
Latarnik
```

**Wyjście:**

```
L?t?rnik
```

"""


def zamien_a_na_pytajnik(napis):
    return napis.replace("a", "?")


if __name__ == "__main__":
    napis = input()
    print(zamien_a_na_pytajnik(napis))
