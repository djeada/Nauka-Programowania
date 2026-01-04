"""
ZAD-08 — Maksymalny zysk ze sprzedaży sznurka

**Poziom:** ★★★
**Tagi:** `dp`, `rod cutting`, `optymalizacja`

### Treść

Masz sznurek o długości `n` i cennik: ceny kawałków długości od `1` do `n`. Możesz pociąć sznurek na kawałki o całkowitych długościach. Znajdź maksymalny zysk.

### Wejście

* 1 linia: lista `prices` (długości 1..n)
* 2 linia: `n` (liczba naturalna)

### Wyjście

* 1 linia: maksymalny zysk (liczba całkowita)

### Przykład

**Wejście:**

```
[1, 5, 8, 9, 10, 17, 17, 20]
4
```

**Wyjście:**

```
10
```

"""


def podziel_sznurek_v1(ceny, n):

    if len(ceny) < n:
        raise ValueError(
            "Dlugosc sznurka do sprzedazy nie moze byc wieksza od liczby elementow listy ceny."
        )

    if n == 0:
        return 0

    maks = 0

    for i in range(n):

        cena = ceny[i] + podziel_sznurek_v1(ceny, n - i - 1)

        if cena > maks:
            maks = cena

    return maks


# Zlozonosc czasowa: O(n^2)
# Zlozonosc pamieciowa: O(n)
def podziel_sznurek_v2(ceny, n):

    if len(ceny) < n:
        raise ValueError(
            "Dlugosc sznurka do sprzedazy nie moze byc wieksza od liczby elementow listy ceny."
        )

    pom = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1):
            pom[i + 1] = max(pom[i + 1], ceny[j] + pom[i - j])

    return pom[n]


# Testy Poprawnosci
def test_1():
    ceny = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 4
    wynik = 10

    assert podziel_sznurek_v1(ceny, n) == wynik
    assert podziel_sznurek_v2(ceny, n) == wynik


def test_2():
    ceny = [3, 9, 10, 20]
    n = 5

    for funkcja in [podziel_sznurek_v1, podziel_sznurek_v2]:
        try:
            funkcja(ceny, n)()
            assert False
        except ValueError:
            assert True


def test_3():
    ceny = [5]
    n = 1
    wynik = 5

    assert podziel_sznurek_v1(ceny, n) == wynik
    assert podziel_sznurek_v2(ceny, n) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
