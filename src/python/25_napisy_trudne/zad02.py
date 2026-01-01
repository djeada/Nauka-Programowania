"""
ZAD-02 — Usuń podnapis

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Dostajesz dwa napisy:

1. Napis główny,
2. Podnapis do usunięcia.

Usuń **wszystkie wystąpienia** podnapisu z napisu głównego.

### Wejście

* 1 linia: napis `S`
* 2 linia: napis `T` (do usunięcia)

### Wyjście

* 1 linia: wynikowy napis po usunięciu wszystkich wystąpień

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
```

**Wyjście:**

```
Le je na wie
```

"""


# Wersja 1
def usun_wszystkie_v1(zdanie, slowo):
    return zdanie.replace(slowo, "")


# Testy Poprawnosci
def test_1():
    zdanie = "Lezy jezy na wiezy"
    slowo = "zy"
    wynik = "Le je na wie"

    assert usun_wszystkie_v1(zdanie, slowo) == wynik


def main():
    test_1()


if __name__ == "__main__":
    main()
