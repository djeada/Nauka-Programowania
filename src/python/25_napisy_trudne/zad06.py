"""
ZAD-06 — Rotacje napisów

**Poziom:** ★★★
**Tagi:** `string`, `rotation`, `substring`

### Treść

Otrzymujesz dwa napisy `A` i `B`. Sprawdź, czy jeden z nich jest **rotacją** drugiego (mają tę samą długość i da się uzyskać jeden przez przesunięcie cykliczne drugiego).

### Wejście

* 1 linia: napis `A`
* 2 linia: napis `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
malpka
pkamal
```

**Wyjście:**

```
Prawda
```

"""


def czy_rotacja_v1(slowo_a, slowo_b):

    if len(slowo_a) != len(slowo_b):
        return False

    return (slowo_a + slowo_a).find(slowo_b) > -1


# Testy Poprawnosci
def test_1():
    slowo_a = "malpka"
    slowo_b = "kamapl"
    assert not czy_rotacja_v1(slowo_a, slowo_b)


def test_2():
    slowo_a = "malpka"
    slowo_b = "pkamal"
    assert czy_rotacja_v1(slowo_a, slowo_b)


def main():
    test_1()
    test_2()


if __name__ == "__main__":
    main()
