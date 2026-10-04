r"""
ZAD-12 — Usuń spacje ze zdania

**Poziom:** ★☆☆
**Tagi:** `napisy`, `replace`

### Treść

Wczytaj zdanie i usuń z niego wszystkie spacje. Pozostałe znaki (także interpunkcję) pozostaw bez zmian.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jeden znak różny od spacji)

### Wyjście

Jedna linia: zdanie bez spacji.

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
Alamakota
```

"""


def usun_spacje(zdanie):
    return zdanie.replace(" ", "")


if __name__ == "__main__":
    zdanie = input()
    print(usun_spacje(zdanie))
