r"""
ZAD-06 — Połączenie posortowanych list (bez powtórzeń)

**Poziom:** ★★★
**Tagi:** `merge`, `heap`, `unique`, `sorted`

### Treść

Otrzymujesz `M` list liczb całkowitych, z których każda jest posortowana niemalejąco. Połącz je w jedną listę posortowaną **rosnąco** i zawierającą każdą wartość **tylko raz** (powtórzenia mogą występować zarówno w obrębie jednej listy, jak i między listami). Niektóre listy mogą być puste.

### Wejście

* 1. linia: `M` — liczba list
* kolejne `M` linii: opis jednej listy — najpierw jej długość `k`, a po niej `k` liczb posortowanych niemalejąco (wszystko oddzielone spacjami); pusta lista to linia zawierająca samo `0`

### Wyjście

Jedna linia: elementy połączonej listy oddzielone spacjami. Jeśli wszystkie listy są puste, wypisz pustą linię.

### Ograniczenia

* `1 ≤ M ≤ 100`
* `0 ≤ k ≤ 100`
* elementy list są z przedziału $[-10^6, 10^6]$

### Przykład

**Wejście:**

```
4
4 -6 23 29 33
4 6 22 35 71
4 5 19 21 37
4 -12 -7 -3 28
```

**Wyjście:**

```
-12 -7 -6 -3 5 6 19 21 22 23 28 29 33 35 37 71
```

Pierwsza liczba w każdej linii to długość listy, a nie jej element.

### Uwagi

* Najmniejszy element wyniku to najmniejszy z **pierwszych** elementów list. Trzymaj w kopcu (`heapq`) po jednym „bieżącym” elemencie z każdej listy: zdejmuj najmniejszy, a na jego miejsce wkładaj następny element z tej samej listy. Dla $N$ elementów łącznie daje to czas $O(N \log M)$.
* Powtórzenia łatwo pominąć: wynik powstaje w kolejności rosnącej, więc wystarczy porównać nowy element z ostatnio dopisanym.

### Kod startowy

```python
def polacz_listy(listy):
    wynik = []
    return wynik


m = int(input())
listy = []
for _ in range(m):
    dane = [int(x) for x in input().split()]
    listy.append(dane[1:])  # pierwsza liczba to długość listy
print(" ".join(str(x) for x in polacz_listy(listy)))
```

"""

import heapq


def polacz_listy(listy):
    """Scala posortowane listy w jedną posortowaną listę bez powtórzeń."""
    # Kopiec trzyma krotki (wartość, numer listy, indeks w tej liście).
    kopiec = [(lista[0], i, 0) for i, lista in enumerate(listy) if lista]
    heapq.heapify(kopiec)
    wynik = []

    while kopiec:
        wartosc, i, j = heapq.heappop(kopiec)

        if not wynik or wynik[-1] != wartosc:
            wynik.append(wartosc)

        if j + 1 < len(listy[i]):
            heapq.heappush(kopiec, (listy[i][j + 1], i, j + 1))

    return wynik


if __name__ == "__main__":
    m = int(input())
    listy = []
    for _ in range(m):
        dane = [int(x) for x in input().split()]
        listy.append(dane[1:])  # pierwsza liczba to długość listy
    print(" ".join(str(x) for x in polacz_listy(listy)))
