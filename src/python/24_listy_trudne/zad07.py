"""
ZAD-07 — Pojemność wody między słupkami

**Poziom:** ★★★
**Tagi:** `two pointers`, `prefix`, `trapping rain water`

### Treść

Otrzymujesz listę liczb naturalnych — wysokości słupków. Oblicz, ile jednostek wody może się zatrzymać pomiędzy słupkami po deszczu.

### Wejście

* 1 linia: lista wysokości `H`

### Wyjście

* 1 linia: jedna liczba naturalna — ilość wody

### Przykład

**Wejście:**

```
[3, 0, 1, 0, 2]
```

**Wyjście:**

```
5
```

"""


def ile_wody_v1(slupki):

    n = len(slupki)
    woda = 0

    lewy = [float("-inf")]

    for i in range(n):
        lewy.append(max(lewy[i], slupki[i]))

    prawy = float("-inf")

    for i in range(n - 1, -1, -1):
        prawy = max(prawy, slupki[i])

        if min(lewy[i], prawy) > slupki[i]:
            woda += min(lewy[i], prawy) - slupki[i]

    return woda


# Testy Poprawnosci
def test_1():
    slupki = [3, 0, 1, 0, 2]
    wynik = 5

    assert ile_wody_v1(slupki) == wynik


def test_2():
    slupki = [9, 2, 3, 9, 0, 2]
    wynik = 15

    assert ile_wody_v1(slupki) == wynik


def test_3():
    slupki = [1, 1]
    wynik = 0

    assert ile_wody_v1(slupki) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
