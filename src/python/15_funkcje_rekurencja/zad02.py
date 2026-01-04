"""
ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `listy`, `I/O`

### Treść

Wczytaj współczynniki wielomianu oraz liczbę `k`. Wypisz współczynniki wielomianu powstałego przez pomnożenie każdego współczynnika przez `k`.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych: `a_n ... a_0`
* 3. linia: `k` — liczba całkowita (skalar)

### Wyjście

Jedna linia: `n+1` liczb całkowitych (współczynniki po mnożeniu), oddzielonych spacją.

### Przykład

**Wejście:**

```
2
4 -3 2
-2
```

**Wyjście:**

```
-8 6 -4
```

"""


def mnoz_przez_skalar_rek(wspolczynniki, k):
    """
    Mnoży współczynniki wielomianu przez skalar (rekurencyjnie).

    Złożoność czasowa: O(n), gdzie n to liczba współczynników
    Złożoność pamięciowa: O(n) ze względu na rekurencję
    """
    if not wspolczynniki:
        return []

    return [wspolczynniki[0] * k] + mnoz_przez_skalar_rek(wspolczynniki[1:], k)


if __name__ == "__main__":
    # Wczytanie stopnia wielomianu
    n = int(input().strip())

    # Wczytanie współczynników
    wspolczynniki = list(map(int, input().strip().split()))

    # Wczytanie skalara
    k = int(input().strip())

    # Mnożenie przez skalar
    # Złożoność czasowa: O(n)
    # Złożoność pamięciowa: O(n)
    wynik = mnoz_przez_skalar_rek(wspolczynniki, k)

    # Wypisanie wyniku
    print(" ".join(map(str, wynik)))
