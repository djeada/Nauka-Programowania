"""
ZAD-03 — Czy napis A jest początkiem napisu B?

**Poziom:** ★★☆
**Tagi:** `string`, `prefix`

### Treść

Otrzymujesz dwa napisy:

1. Napis `A` — potencjalny przedrostek,
2. Napis `B` — napis testowany.

Sprawdź, czy `B` **zaczyna się** od `A`.

### Wejście

* 1 linia: `A`
* 2 linia: `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
Dino
Dinozaur jest zly
```

**Wyjście:**

```
Prawda
```

"""


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
