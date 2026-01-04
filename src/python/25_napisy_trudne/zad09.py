"""
ZAD-09 — Najdłuższy wspólny podnapis

**Poziom:** ★★★
**Tagi:** `string`, `dp`, `substring`

### Treść

Otrzymujesz dwa napisy. Znajdź **najdłuższy wspólny podnapis** (ciągły fragment), który występuje w obu napisach.

### Wejście

* 1 linia: napis `A`
* 2 linia: napis `B`

### Wyjście

* 1 linia: najdłuższy wspólny podnapis
  (jeśli jest kilka o tej samej długości — wybierz ten, który występuje **najwcześniej w A**; jeśli nadal remis, najwcześniej w B)

### Przykład

**Wejście:**

```
ijkabcdl
xxxxabcd
```

**Wyjście:**

```
abcd
```

"""


def najdluzszy_podnapis_v1(slowo_a, slowo_b):

    m = len(slowo_a)
    n = len(slowo_b)

    pom = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if slowo_a[i - 1] == slowo_b[j - 1]:
                pom[i][j] = pom[i - 1][j - 1] + 1
            else:
                pom[i][j] = 0

    wynik = ""
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pom[i][j] > len(wynik):
                wynik = slowo_a[(i - pom[i][j] + 1) - 1 : pom[i][j]]

    return wynik


# Testy Poprawnosci
def test_1():
    slowo_a = "abcdxyz"
    slowo_b = "xyzabcd"
    wynik = "abcd"
    assert najdluzszy_podnapis_v1(slowo_a, slowo_b) == wynik


def test_2():
    slowo_a = "hhaall"
    slowo_b = "hhaall"
    wynik = "hhaall"
    assert najdluzszy_podnapis_v1(slowo_a, slowo_b) == wynik


def test_3():
    slowo_a = ""
    slowo_b = ""
    wynik = ""
    assert najdluzszy_podnapis_v1(slowo_a, slowo_b) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
