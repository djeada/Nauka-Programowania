r"""
ZAD-13 — Gra w życie: k pokoleń

**Poziom:** ★★☆
**Tagi:** `macierze`, `symulacja`, `sąsiedzi`

### Treść

**Gra w życie** Conwaya to plansza komórek, z których każda jest żywa (`#`) albo martwa (`.`). Sąsiadami komórki jest 8 komórek stykających się z nią bokiem lub rogiem. W każdym kroku (pokoleniu) wszystkie komórki zmieniają się **jednocześnie** według reguł:

* żywa komórka z 2 lub 3 żywymi sąsiadami przeżywa, w przeciwnym razie umiera,
* martwa komórka z dokładnie 3 żywymi sąsiadami ożywa, w przeciwnym razie pozostaje martwa.

Komórki poza planszą są zawsze martwe. Wczytaj planszę i liczbę `k`, a następnie wypisz stan planszy po `k` krokach.

### Wejście

* 1. linia: `n m k` — liczba wierszy, liczba kolumn i liczba kroków
* następnie `n` linii po `m` znaków `.` lub `#`

### Wyjście

`n` linii po `m` znaków `.` lub `#` — plansza po `k` krokach (bez spacji między znakami).

### Ograniczenia

* `1 ≤ n, m ≤ 20`
* `0 ≤ k ≤ 10`

### Przykład

**Wejście:**

```
5 5 1
.....
..#..
..#..
..#..
.....
```

**Wyjście:**

```
.....
.....
.###.
.....
.....
```

Środkowa komórka ma 2 żywych sąsiadów, więc przeżywa; skrajne komórki pionowej kreski mają po 1 sąsiedzie i umierają, a komórki obok środka mają po 3 żywych sąsiadów i ożywają.

### Uwagi

* W każdym kroku buduj **nową** macierz i wypełniaj ją na podstawie starej. Jeśli zmieniasz komórki w miejscu, kolejne komórki policzą sąsiadów z już zmienionej planszy i wynik będzie błędny.
* Przy liczeniu sąsiadów sprawdzaj, czy indeksy mieszczą się w planszy (pamiętaj, że w Pythonie indeks `-1` oznacza ostatni element, a nie „poza planszą”).
* Dla `k = 0` wypisz planszę bez zmian.

"""


def zywi_sasiedzi(plansza, wiersz, kolumna):
    """Liczy żywe komórki wśród 8 sąsiadów; komórki poza planszą są martwe."""
    n, m = len(plansza), len(plansza[0])
    licznik = 0
    for dw in (-1, 0, 1):
        for dk in (-1, 0, 1):
            if dw == 0 and dk == 0:
                continue
            w, k = wiersz + dw, kolumna + dk
            if 0 <= w < n and 0 <= k < m and plansza[w][k] == "#":
                licznik += 1
    return licznik


def nastepne_pokolenie(plansza):
    """Zwraca NOWĄ planszę — stara pozostaje bez zmian."""
    nowa = []
    for w in range(len(plansza)):
        wiersz = []
        for k in range(len(plansza[0])):
            sasiedzi = zywi_sasiedzi(plansza, w, k)
            if plansza[w][k] == "#" and sasiedzi in (2, 3):
                wiersz.append("#")
            elif plansza[w][k] == "." and sasiedzi == 3:
                wiersz.append("#")
            else:
                wiersz.append(".")
        nowa.append(wiersz)
    return nowa


if __name__ == "__main__":
    n, m, k = [int(x) for x in input().split()]
    plansza = [list(input()) for _ in range(n)]

    for _ in range(k):
        plansza = nastepne_pokolenie(plansza)

    for wiersz in plansza:
        print("".join(wiersz))
