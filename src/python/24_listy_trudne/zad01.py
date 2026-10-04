r"""
ZAD-01 — Najdłuższy ciąg jedynek

**Poziom:** ★★☆
**Tagi:** `list`, `0/1`, `analiza`, `indeksy`

### Treść

Otrzymujesz listę składającą się wyłącznie z zer i jedynek. Znajdź **indeks zera**, którego zamiana na `1` da **najdłuższy nieprzerwany ciąg jedynek**.

* Jeśli kilka zer daje ciąg o tej samej, maksymalnej długości — wybierz zero o **najmniejszym indeksie**.
* Jeśli lista składa się wyłącznie z zer **albo** wyłącznie z jedynek — wypisz `-1`.

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb `0` lub `1` oddzielonych spacjami

### Wyjście

Jedna liczba całkowita: indeks szukanego zera albo `-1`.

### Ograniczenia

* `1 ≤ n ≤ 1000`

### Przykład

**Wejście:**

```
10
0 0 1 0 1 1 1 0 1 1
```

**Wyjście:**

```
7
```

Zamiana zera o indeksie `7` daje sześć jedynek pod rząd (indeksy 4–9). Zamiana zera o indeksie `3` dałaby tylko pięć jedynek (indeksy 2–6).

### Uwagi

* Po zamianie zera łączą się jedynki stojące bezpośrednio przed nim i za nim — wystarczy więc znać pozycje sąsiednich zer. Da się to policzyć w jednym przejściu po liście, w czasie $O(n)$.

"""


def indeks_zera_do_zamiany(lista):
    """Zwraca indeks zera, którego zamiana na 1 daje najdłuższy ciąg jedynek (albo -1)."""
    zera = [i for i, x in enumerate(lista) if x == 0]

    if len(zera) == 0 or len(zera) == len(lista):
        return -1

    # Strażnicy: „zero” przed początkiem i za końcem listy.
    granice = [-1] + zera + [len(lista)]

    najlepszy_indeks = -1
    najlepsza_dlugosc = 0

    # Po zamianie k-tego zera łączą się jedynki między sąsiednimi zerami.
    for k in range(1, len(granice) - 1):
        dlugosc = granice[k + 1] - granice[k - 1] - 1
        if dlugosc > najlepsza_dlugosc:
            najlepsza_dlugosc = dlugosc
            najlepszy_indeks = granice[k]

    return najlepszy_indeks


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(indeks_zera_do_zamiany(lista))
