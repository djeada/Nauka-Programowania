"""
ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `wyrównanie stopni`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich sumą.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki sumy od najwyższej potęgi, oddzielone spacją.

### Przykład

**Wejście:**

```
2
3 5 2
2
2 -8 1
```

**Wyjście:**

```
5 -3 3
```

### Uwagi o formatowaniu

* Jeśli stopnie są różne, wyrównaj listy „od końca” (od wyrazu wolnego), dopisując zera na początku krótszej.

"""


def suma_wielomianow_rek(w1, w2):
    """
    Sumuje dwa wielomiany rekurencyjnie.
    Wyrównanie od końca (wyrazy wolne).

    Złożoność czasowa: O(max(n, m))
    Złożoność pamięciowa: O(max(n, m))
    """
    if not w1:
        return w2[:]
    if not w2:
        return w1[:]

    # Wyrównanie długości
    len1, len2 = len(w1), len(w2)
    if len1 > len2:
        # w1 dłuższy - bierz pierwszy element w1 i rekurencja na reszcie
        return [w1[0]] + suma_wielomianow_rek(w1[1:], w2)
    elif len2 > len1:
        # w2 dłuższy
        return [w2[0]] + suma_wielomianow_rek(w1, w2[1:])
    else:
        # Równe długości - dodaj pierwsze elementy
        return [w1[0] + w2[0]] + suma_wielomianow_rek(w1[1:], w2[1:])


if __name__ == "__main__":
    n1 = int(input().strip())
    w1 = list(map(int, input().strip().split()))
    n2 = int(input().strip())
    w2 = list(map(int, input().strip().split()))
    wynik = suma_wielomianow_rek(w1, w2)
    print(" ".join(map(str, wynik)))
