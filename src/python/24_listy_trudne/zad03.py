r"""
ZAD-03 — Minimalny iloczyn trzech liczb

**Poziom:** ★★☆
**Tagi:** `list`, `min`, `math`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź **najmniejszy możliwy iloczyn trzech elementów** tej listy (trzech elementów o różnych indeksach; wartości mogą się powtarzać).

Jeśli lista ma mniej niż 3 elementy — wypisz iloczyn wszystkich jej elementów.

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna liczba całkowita — najmniejszy iloczyn.

### Ograniczenia

* `1 ≤ n ≤ 1000`
* elementy listy są z przedziału $[-1000, 1000]$

### Przykład

**Wejście:**

```
6
3 -1 -3 2 9 4
```

**Wyjście:**

```
-108
```

Najmniejszy iloczyn daje trójka $-3 \cdot 9 \cdot 4 = -108$.

### Uwagi

* Uważaj na liczby ujemne: iloczyn dwóch ujemnych jest dodatni. Wystarczy porównać dwóch kandydatów: trzy najmniejsze liczby oraz najmniejszą liczbę razy dwie największe.
* Sprawdzanie wszystkich trójek zajmuje czas $O(n^3)$ — przy $n = 1000$ to ponad $10^8$ trójek. Oczekiwane rozwiązanie działa w czasie $O(n \log n)$ (sortowanie) albo $O(n)$.

"""


def min_iloczyn_trzech(lista):
    """Zwraca najmniejszy iloczyn trzech elementów (dla krótszej listy: iloczyn wszystkich)."""
    if len(lista) < 3:
        iloczyn = 1
        for x in lista:
            iloczyn *= x
        return iloczyn

    posortowana = sorted(lista)

    # Kandydaci: trzy najmniejsze liczby albo najmniejsza z dwiema największymi.
    trzy_najmniejsze = posortowana[0] * posortowana[1] * posortowana[2]
    najmniejsza_i_dwie_najwieksze = posortowana[0] * posortowana[-1] * posortowana[-2]

    return min(trzy_najmniejsze, najmniejsza_i_dwie_najwieksze)


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(min_iloczyn_trzech(lista))
