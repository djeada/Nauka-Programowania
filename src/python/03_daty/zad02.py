r"""
ZAD-02 — Pełnoletność (18 lat)

**Poziom:** ★☆☆
**Tagi:** `daty`, `porównywanie`, `if`

### Treść

Wczytaj datę urodzenia oraz datę „dzisiejszą” i sprawdź, czy osoba ma **ukończone 18 lat** w dniu daty dzisiejszej.

Pełnoletność osiąga się **w dniu 18. urodzin**. Osoba jest więc pełnoletnia wtedy, gdy data (`d1`, `m1`, `y1 + 18`) jest **nie późniejsza** niż data dzisiejsza (`d2`, `m2`, `y2`). Daty porównuj najpierw po roku, przy równych latach po miesiącu, a przy równych miesiącach po dniu.

Wypisz:

* `Osoba jest pełnoletnia.` — jeśli ma ukończone 18 lat,
* `Osoba nie jest pełnoletnia.` — w przeciwnym razie.

### Wejście

6 liczb całkowitych, każda w osobnej linii:

1. `d1` — dzień urodzenia
2. `m1` — miesiąc urodzenia
3. `y1` — rok urodzenia
4. `d2` — dzisiejszy dzień
5. `m2` — dzisiejszy miesiąc
6. `y2` — dzisiejszy rok

### Wyjście

Jedna linia — jeden z komunikatów.

### Ograniczenia

* Obie daty są poprawne (nie musisz ich sprawdzać), $1 \le y1, y2 \le 9999$.
* Data urodzenia nie jest późniejsza niż data dzisiejsza.

### Przykład

**Wejście:**

```
5
12
1999
20
11
2020
```

**Wyjście:**

```
Osoba jest pełnoletnia.
```

Osiemnaste urodziny wypadły 5.12.2017, a więc przed 20.11.2020.

### Uwagi

* Porównujesz same liczby, więc data (`d1`, `m1`, `y1 + 18`) nie musi istnieć w kalendarzu. Osoba urodzona 29 lutego obchodzi 18. urodziny w roku nieprzestępnym (np. urodzona 29.02.2004 — w 2022 roku), więc zgodnie z regułą 28 lutego jest jeszcze niepełnoletnia, a pełnoletnia staje się 1 marca.

"""


def czy_pelnoletnia(dzien_ur, miesiac_ur, rok_ur, dzien, miesiac, rok):
    rok_18_urodzin = rok_ur + 18
    if rok_18_urodzin != rok:
        return rok_18_urodzin < rok
    if miesiac_ur != miesiac:
        return miesiac_ur < miesiac
    return dzien_ur <= dzien


if __name__ == "__main__":
    dzien_ur = int(input())
    miesiac_ur = int(input())
    rok_ur = int(input())
    dzien = int(input())
    miesiac = int(input())
    rok = int(input())

    if czy_pelnoletnia(dzien_ur, miesiac_ur, rok_ur, dzien, miesiac, rok):
        print("Osoba jest pełnoletnia.")
    else:
        print("Osoba nie jest pełnoletnia.")
