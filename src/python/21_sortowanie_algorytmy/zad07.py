r"""
ZAD-07 — Sortowanie przez zliczanie

**Poziom:** ★☆☆
**Tagi:** `sorting`, `counting-sort`, `list`

### Treść

Napisz funkcję `sortowanie_przez_zliczanie(lista, k)`, która sortuje rosnąco listę liczb całkowitych z przedziału $[0, k]$ algorytmem **sortowania przez zliczanie**:

1. Utwórz listę liczności `licznosci` długości $k + 1$ wypełnioną zerami.
2. Przejdź po liście i dla każdego elementu $x$ zwiększ `licznosci[x]` o 1. Po tym kroku `licznosci[v]` to liczba wystąpień wartości $v$.
3. **Wypisz** listę liczności.
4. Zbuduj wynik: dla kolejnych wartości $v = 0, 1, \dots, k$ dopisz do niego $v$ dokładnie `licznosci[v]` razy. Zwróć wynik.

Algorytm w ogóle nie porównuje elementów ze sobą.

### Wejście

* 1. linia: liczba elementów $n$
* 2. linia: $n$ liczb całkowitych z przedziału $[0, k]$ oddzielonych spacjami
* 3. linia: liczba całkowita $k$ — największa możliwa wartość

### Wyjście

* 1. linia: lista liczności (długości $k + 1$) w formacie listy Pythona
* 2. linia: posortowana lista w formacie listy Pythona

### Ograniczenia

* $1 \le n \le 100$
* $0 \le k \le 100$

### Przykład

**Wejście:**

```
8
3 0 5 3 1 0 3 5
5
```

**Wyjście:**

```
[2, 1, 0, 3, 0, 2]
[0, 0, 1, 3, 3, 3, 5, 5]
```

Wartość `0` występuje 2 razy, `1` — raz, `2` — ani razu, `3` — 3 razy, `4` — ani razu, `5` — 2 razy.

### Uwagi o algorytmie

* Złożoność czasowa: $O(n + k)$ — dla małych wartości $k$ to szybciej niż $O(n \log n)$ najlepszych algorytmów opartych na porównaniach.
* Algorytm nadaje się tylko do sortowania liczb całkowitych z niewielkiego zakresu (lista liczności ma $k + 1$ elementów).

### Kod startowy

```python
def sortowanie_przez_zliczanie(lista, k):
    pass


n = int(input())
lista = [int(x) for x in input().split()]
k = int(input())
print(sortowanie_przez_zliczanie(lista, k))
```

"""


def sortowanie_przez_zliczanie(lista, k):
    licznosci = [0] * (k + 1)
    for x in lista:
        licznosci[x] += 1
    print(licznosci)

    wynik = []
    for wartosc in range(k + 1):
        for _ in range(licznosci[wartosc]):
            wynik.append(wartosc)
    return wynik


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    k = int(input())
    print(sortowanie_przez_zliczanie(lista, k))
