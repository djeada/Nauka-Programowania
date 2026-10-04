r"""
ZAD-05 — Zmodyfikuj elementy spełniające warunek

**Poziom:** ★☆☆
**Tagi:** `listy`, `warunki`, `liczby pierwsze`

### Treść

Wczytaj listę `n` liczb całkowitych. Wykonaj kolejno poniższe operacje — każda działa na liście **otrzymanej w poprzednim podpunkcie** (pierwsza na liście wczytanej). Po każdym podpunkcie wypisz aktualną listę.

a) Zwiększ o `1` elementy o **parzystych indeksach** ($0, 2, 4, \ldots$).
b) Ustaw na `0` elementy, które są **wielokrotnościami liczby 3**.
c) Podnieś do kwadratu elementy **mniejsze od 10**.
d) Oblicz sumę wszystkich elementów listy i wpisz ją w miejsce elementów o indeksach będących **liczbami pierwszymi** ($2, 3, 5, 7, 11, \ldots$).
e) Zamień każdy element na **iloczyn wszystkich pozostałych** elementów listy.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Pięć linii — lista po podpunktach a), b), c), d), e), w formacie `print(lista)`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
4
1 4 2 5
```

**Wyjście:**

```
[2, 4, 3, 5]
[2, 4, 0, 5]
[4, 16, 0, 25]
[4, 16, 45, 45]
[32400, 8100, 2880, 2880]
```

a) indeksy 0 i 2: `1 → 2`, `2 → 3`; b) `3 → 0`; c) wszystkie elementy są mniejsze od 10; d) suma $4 + 16 + 0 + 25 = 45$ trafia na indeksy 2 i 3; e) np. dla indeksu 0: $16 \cdot 45 \cdot 45 = 32400$.

### Uwagi

* Indeksy `0` i `1` nie są liczbami pierwszymi.
* `0` (także po podpunkcie b) jest wielokrotnością liczby 3, a liczby ujemne są mniejsze od 10.
* Dla listy jednoelementowej iloczyn „pozostałych” elementów w podpunkcie e) wynosi `1` (iloczyn pustego zbioru).
* Jeśli w liście jest `0`, wiele iloczynów w podpunkcie e) będzie równych `0` — to normalne.

"""


def zwieksz_parzyste_indeksy(lista):
    return [element + 1 if i % 2 == 0 else element for i, element in enumerate(lista)]


def wyzeruj_wielokrotnosci_3(lista):
    return [0 if element % 3 == 0 else element for element in lista]


def kwadrat_mniejszych_od_10(lista):
    return [element**2 if element < 10 else element for element in lista]


def czy_pierwsza(n):
    if n < 2:
        return False
    for dzielnik in range(2, n):
        if n % dzielnik == 0:
            return False
    return True


def suma_na_pierwszych_indeksach(lista):
    suma = sum(lista)
    return [suma if czy_pierwsza(i) else element for i, element in enumerate(lista)]


def iloczyn_pozostalych(lista):
    wynik = []
    for i in range(len(lista)):
        iloczyn = 1
        for j in range(len(lista)):
            if j != i:
                iloczyn *= lista[j]
        wynik.append(iloczyn)
    return wynik


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    for operacja in (
        zwieksz_parzyste_indeksy,
        wyzeruj_wielokrotnosci_3,
        kwadrat_mniejszych_od_10,
        suma_na_pierwszych_indeksach,
        iloczyn_pozostalych,
    ):
        lista = operacja(lista)
        print(lista)
