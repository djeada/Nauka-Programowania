r"""
ZAD-14 — Para o danej sumie — szybko

**Poziom:** ★★☆
**Tagi:** `dict`, `2-sum`, `złożoność`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `x`. Znajdź indeksy `i`, `j` (gdzie $i < j$) takie, że `lista[i] + lista[j] == x`.

Jeśli takich par jest kilka, wybierz tę o najmniejszym `i`, a przy równym `i` — o najmniejszym `j`. Jeśli nie ma żadnej — wypisz `-1 -1`.

To samo zadanie rozwiązywaliśmy w rozdziale o listach (ZAD-16), ale tym razem lista może mieć nawet $2 \cdot 10^5$ elementów, więc sprawdzanie wszystkich par dwiema pętlami (około $2 \cdot 10^{10}$ porównań) jest zbyt wolne. Użyj słownika, który pozwala w jednym kroku sprawdzić, czy i gdzie w liście wystąpiła potrzebna wartość.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba całkowita `x`

### Wyjście

Jedna linia: dwie liczby `i j` oddzielone spacją albo `-1 -1`.

### Ograniczenia

* $2 \le n \le 2 \cdot 10^5$
* $-10^9 \le$ `lista[i]`, `x` $\le 10^9$

### Przykład

**Wejście:**

```
4
3 1 4 2
5
```

**Wyjście:**

```
0 3
```

Sumę $5$ dają pary indeksów $(0, 3)$: $3 + 2$ oraz $(1, 2)$: $1 + 4$. Para $(1, 2)$ kończy się wcześniej, ale wybieramy $(0, 3)$, bo ma mniejsze `i`.

### Uwagi

* Para składa się z dwóch **różnych** pozycji w liście — elementu nie można dodać do samego siebie, ale dwie równe liczby na różnych pozycjach już tak.
* Wskazówka: przechodź po liście indeksem `j` i trzymaj słownik `wartość → indeks jej pierwszego wystąpienia` dla elementów przed `j`. Wtedy najmniejsze `i` do pary z `j` to `slownik[x - lista[j]]` (o ile taki klucz istnieje). Spośród znalezionych par zapamiętaj tę o najmniejszym `i`.
* Uważaj: pierwsza znaleziona w ten sposób para ma najmniejsze `j`, a niekoniecznie najmniejsze `i` (patrz przykład).

"""


def para_o_sumie(liczby, x):
    """
    Zwraca indeksy (i, j), i < j, takie że liczby[i] + liczby[j] == x;
    spośród takich par tę o najmniejszym i, a przy równym i — o najmniejszym j.
    Gdy pary nie ma, zwraca (-1, -1). Działa w czasie O(n).
    """
    pierwszy_indeks = {}  # wartość -> indeks jej pierwszego wystąpienia
    najlepsza = (-1, -1)
    for j, liczba in enumerate(liczby):
        dopelnienie = x - liczba
        if dopelnienie in pierwszy_indeks:
            # najmniejsze i do pary z tym j; j rośnie, więc wystarczy porównać i
            i = pierwszy_indeks[dopelnienie]
            if najlepsza[0] == -1 or i < najlepsza[0]:
                najlepsza = (i, j)
        if liczba not in pierwszy_indeks:
            pierwszy_indeks[liczba] = j
    return najlepsza


if __name__ == "__main__":
    n = int(input())
    liczby = [int(x) for x in input().split()]
    x = int(input())

    i, j = para_o_sumie(liczby, x)
    print(i, j)
