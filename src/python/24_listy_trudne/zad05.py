r"""
ZAD-05 — Zbiór potęgowy listy

**Poziom:** ★★★
**Tagi:** `list`, `subsets`, `combinatorics`, `rekurencja`

### Treść

Otrzymujesz listę liczb całkowitych (mogą się powtarzać). Wypisz **wszystkie różne podzbiory** tej listy, łącznie ze zbiorem pustym i całą listą.

Kolejność elementów w podzbiorze nie ma znaczenia: z listy `1 2 1` podzbiór złożony z `1` i `2` powstaje na dwa sposoby, ale wypisujemy go **tylko raz**.

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Każdy podzbiór w osobnej linii, zapisany jak lista w Pythonie (tak wypisuje ją `print(lista)`):

* elementy podzbioru w kolejności niemalejącej, w nawiasach kwadratowych, oddzielone przecinkiem i spacją, np. `[1, 1, 2]`; pusty podzbiór to `[]`,
* podzbiory uporządkowane **leksykograficznie**: porównujemy pierwsze elementy (jako liczby, więc `9` jest przed `10`), przy remisie drugie itd.; podzbiór, który jest początkiem dłuższego, stoi przed nim (np. `[1]` przed `[1, 1]`). Tak porównuje listy Python, więc `sorted()` na liście list daje dokładnie tę kolejność.

### Ograniczenia

* `1 ≤ n ≤ 10`
* elementy listy są z przedziału $[-100, 100]$

### Przykład

**Wejście:**

```
3
1 2 1
```

**Wyjście:**

```
[]
[1]
[1, 1]
[1, 1, 2]
[1, 2]
[2]
```

### Uwagi

* Wygodnie jest najpierw posortować listę, a potem generować podzbiory rekurencyjnie (dla każdego elementu: bierzemy go albo nie). Aby uniknąć powtórzeń, na danym poziomie rekurencji pomijaj element równy poprzedniemu.

### Kod startowy

```python
def podzbiory(liczby):
    wynik = []
    return wynik


n = int(input())
liczby = [int(x) for x in input().split()]
for podzbior in podzbiory(liczby):
    print(podzbior)
```

"""


def podzbiory(liczby):
    """Zwraca wszystkie różne podzbiory (posortowane listy) w kolejności leksykograficznej."""
    liczby = sorted(liczby)
    wynik = []
    obecny = []

    def generuj(start):
        wynik.append(list(obecny))

        for i in range(start, len(liczby)):
            # Ta sama wartość na tym samym poziomie dałaby powtórzony podzbiór.
            if i > start and liczby[i] == liczby[i - 1]:
                continue
            obecny.append(liczby[i])
            generuj(i + 1)
            obecny.pop()

    generuj(0)
    return wynik


if __name__ == "__main__":
    n = int(input())
    liczby = [int(x) for x in input().split()]
    for podzbior in podzbiory(liczby):
        print(podzbior)
