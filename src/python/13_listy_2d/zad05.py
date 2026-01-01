"""
ZAD-05 — Czy macierz jest magiczna?

**Poziom:** ★★☆
**Tagi:** `macierze`, `suma`, `warunki`

### Treść

Wczytaj macierz kwadratową `n×n` z dodatnimi liczbami naturalnymi. Sprawdź, czy to **kwadrat magiczny**: suma każdego wiersza, każdej kolumny oraz obu przekątnych jest taka sama.

### Wejście

* 1. linia: `n`
* następnie `n` wierszy po `n` liczb

### Wyjście

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
3
6 7 2
1 5 9
8 3 4
```

**Wyjście:**

```
Prawda
```

"""


def czy_kwadrat_magiczny(macierz):
    # sprawdzenie, czy macierz jest kwadratem
    if len(macierz) != len(macierz[0]):
        return False

    # sprawdz czy suma elementow w kazdym wierszu jest taka sama
    suma_wiersz = sum(macierz[0])

    for wiersz in macierz:
        if suma_wiersz != sum(wiersz):
            return False

    # sprawdz czy suma elementow w kazdej kolumnie jest taka sama i rowna sumie elementow w kazdym wierszu
    for kolumna in range(len(macierz[0])):
        suma_kolumna = 0
        for wiersz in macierz:
            suma_kolumna += wiersz[kolumna]
        if suma_kolumna != suma_wiersz:
            return False

    # sprawdz czy suma elementow na obu przekatnych jest taka sama i rowna sumie elementow w kazdym wierszu
    suma_przekatna = 0
    for i in range(len(macierz)):
        suma_przekatna += macierz[i][i]
    if suma_przekatna != suma_wiersz:
        return False

    suma_przekatna = 0
    for i in range(len(macierz)):
        suma_przekatna += macierz[i][len(macierz) - 1 - i]
    if suma_przekatna != suma_wiersz:
        return False

    return True


def test_czy_kwadrat_magiczny():

    assert czy_kwadrat_magiczny([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
    assert not czy_kwadrat_magiczny([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert czy_kwadrat_magiczny([[2, 7, 6], [9, 5, 1], [4, 3, 8]])


if __name__ == "__main__":

    test_czy_kwadrat_magiczny()
