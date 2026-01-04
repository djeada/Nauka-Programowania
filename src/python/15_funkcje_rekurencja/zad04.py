"""
ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `wielomiany`, `konwolucja`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich iloczynem.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki iloczynu (długość `n+m+1`), oddzielone spacją.

### Przykład

**Wejście:**

```
3
5 0 10 6
2
1 2 4
```

**Wyjście:**

```
5 10 30 26 52 24
```

"""


def mnoz_wielomiany_rek(w1, w2):
    """
    Mnoży dwa wielomiany rekurencyjnie.

    Złożoność czasowa: O(n * m)
    Złożoność pamięciowa: O(n + m)
    """
    if not w1 or not w2:
        return []

    # Algorytm: wielomian1[0] * wielomian2 + wielomian1[1:] * wielomian2 przesunięte
    # Najprostsze podejście:
    wynik = [0] * (len(w1) + len(w2) - 1)

    def mnoz_rek_helper(i):
        if i >= len(w1):
            return
        for j in range(len(w2)):
            wynik[i + j] += w1[i] * w2[j]
        mnoz_rek_helper(i + 1)

    mnoz_rek_helper(0)
    return wynik


if __name__ == "__main__":
    n1 = int(input().strip())
    w1 = list(map(int, input().strip().split()))
    n2 = int(input().strip())
    w2 = list(map(int, input().strip().split()))
    wynik = mnoz_wielomiany_rek(w1, w2)
    print(" ".join(map(str, wynik)))
