r"""
ZAD-05 — Sortowanie szybkie

**Poziom:** ★★☆
**Tagi:** `sorting`, `quick-sort`, `recursion`

### Treść

Napisz rekurencyjną funkcję `sortowanie_szybkie(lista)`, która zwraca nową, posortowaną rosnąco listę, korzystając z algorytmu **Quick Sort**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana, zwróć ją.
2. Jako **pivot** wybierz **pierwszy** element listy.
3. Podziel elementy listy na trzy grupy (zachowując ich kolejność z listy):
   * `mniejsze` — mniejsze od pivota,
   * `rowne` — równe pivotowi (w tym sam pivot),
   * `wieksze` — większe od pivota.
4. **Wypisz** trzy grupy w jednej linii: `print(mniejsze, rowne, wieksze)`.
5. Rekurencyjnie posortuj najpierw grupę `mniejsze`, a potem `wieksze`.
6. Zwróć sklejony wynik: posortowane `mniejsze` + `rowne` + posortowane `wieksze`.

Program wczytuje listę, sortuje ją i na końcu wypisuje posortowaną listę.

### Wejście

* 1. linia: liczba całkowita $n$ — liczba elementów
* 2. linia: $n$ liczb całkowitych oddzielonych spacjami

### Wyjście

* Dla każdego podziału (w kolejności wykonywania) jedna linia z trzema listami oddzielonymi spacją, np. `[2, 1, 4] [6] [27]`. Pusta grupa to `[]`.
* Ostatnia linia: posortowana lista w formacie listy Pythona.

### Ograniczenia

* $2 \le n \le 20$
* Elementy są liczbami całkowitymi z przedziału $[-1000, 1000]$.

### Przykład

**Wejście:**

```
5
6 2 1 4 27
```

**Wyjście:**

```
[2, 1, 4] [6] [27]
[1] [2] [4]
[1, 2, 4, 6, 27]
```

Pierwszy podział (pivot `6`) daje grupy `[2, 1, 4]`, `[6]`, `[27]`. Grupa `[2, 1, 4]` jest dzielona dalej (pivot `2`). Grupy jednoelementowe są już posortowane, więc nie są dzielone.

### Uwagi o algorytmie

* Średnio: $O(n \log n)$, w pesymistycznym przypadku (np. lista już posortowana przy pivocie z początku): $O(n^2)$.
* Wybór pivota ma wpływ na wydajność.

### Kod startowy

```python
def sortowanie_szybkie(lista):
    pass


n = int(input())
lista = [int(x) for x in input().split()]
print(sortowanie_szybkie(lista))
```

"""


def sortowanie_szybkie(lista):
    if len(lista) < 2:
        return lista
    pivot = lista[0]
    mniejsze = [x for x in lista if x < pivot]
    rowne = [x for x in lista if x == pivot]
    wieksze = [x for x in lista if x > pivot]
    print(mniejsze, rowne, wieksze)
    return sortowanie_szybkie(mniejsze) + rowne + sortowanie_szybkie(wieksze)


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(sortowanie_szybkie(lista))
