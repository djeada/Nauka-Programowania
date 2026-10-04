r"""
ZAD-01 — Warunek kończący pętlę

**Poziom:** ★☆☆
**Tagi:** `while`, `break`, `I/O`

### Treść

Wczytuj kolejne liczby naturalne (każdą z osobnej linii), dopóki nie wczytasz liczby `7`.
Siódemka kończy wczytywanie — po niej program nie wczytuje już żadnych danych.

Na koniec wypisz, ile liczb wczytano **przed** pierwszą siódemką (samej siódemki nie liczymy).

### Wejście

Kolejne liczby naturalne, każda w osobnej linii.

### Wyjście

Jedna liczba całkowita — liczba wczytanych liczb poprzedzających pierwszą siódemkę.

### Ograniczenia

* Wśród danych na pewno jest co najmniej jedna liczba `7`.
* Po pierwszej siódemce mogą występować kolejne linie — program ma je pominąć.

### Przykład

**Wejście:**

```
3
10
5
7
```

**Wyjście:**

```
3
```

Przed siódemką wczytano trzy liczby: `3`, `10` i `5`.

### Uwagi

* Jeśli pierwszą wczytaną liczbą jest `7`, wypisz `0`.
* Liczby takie jak `17` czy `70` nie kończą wczytywania — liczy się tylko liczba równa `7`.

"""


def policz_przed_siodemka():
    """Wczytuje liczby aż do pierwszej siódemki i zwraca, ile ich było przed nią."""
    licznik = 0
    liczba = int(input())
    while liczba != 7:
        licznik += 1
        liczba = int(input())
    return licznik


if __name__ == "__main__":
    print(policz_przed_siodemka())
