"""
ZAD-08 — Najdłuższy wspólny przedrostek

**Poziom:** ★★★
**Tagi:** `string`, `prefix`, `list`

### Treść

Otrzymujesz listę napisów (w kolejnych liniach). Znajdź najdłuższy przedrostek wspólny dla wszystkich.

### Wejście

* 1 linia: `n` — liczba napisów
* kolejne `n` linii: napisy

### Wyjście

* 1 linia: najdłuższy wspólny przedrostek (może być pusty)

### Przykład

**Wejście:**

```
3
Remolada
Remux
Remmy
```

**Wyjście:**

```
Rem
```

"""


# Wersja 1
# Zlozonosc czasowa O(n^2)
def najdluzszy_przedrostek_v1(slowa):

    wynik = ""
    n = len(slowa)
    j = float("inf")

    for slowo in slowa:
        s = len(slowo)
        if j > s:
            j = s

    for i in range(j):
        pom = slowa[0][i]
        k = 1
        while k < n:
            if pom == slowa[k][i]:
                k += 1
            else:
                return wynik
        wynik += pom

    return wynik


# Testy Poprawnosci
def test_1():
    slowa = ["abcdefgh", "abcefgh", "abcd"]
    wynik = "abc"
    assert najdluzszy_przedrostek_v1(slowa) == wynik


def test_2():
    slowa = ["flower", "flow", "flight", "flix"]
    wynik = "fl"
    assert najdluzszy_przedrostek_v1(slowa) == wynik


def test_3():
    slowa = ["student", "studio", "stress", "lol"]
    wynik = ""
    assert najdluzszy_przedrostek_v1(slowa) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
