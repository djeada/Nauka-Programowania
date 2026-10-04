r"""
ZAD-07 — Pojemność wody między słupkami

**Poziom:** ★★★
**Tagi:** `two pointers`, `prefix`, `trapping rain water`

### Treść

Otrzymujesz wysokości `n` słupków stojących obok siebie; każdy słupek ma szerokość `1`. Oblicz, ile jednostek wody zatrzyma się pomiędzy słupkami po deszczu (woda spływa poza pierwszy i ostatni słupek).

Nad słupkiem o indeksie `i` zatrzyma się $\min(L_i, P_i) - h_i$ jednostek wody, gdzie $L_i$ to najwyższy słupek na lewo od `i` (włącznie z nim), a $P_i$ — najwyższy słupek na prawo od `i` (włącznie z nim).

### Wejście

* 1. linia: `n` — liczba słupków
* 2. linia: `n` nieujemnych liczb całkowitych — wysokości słupków

### Wyjście

Jedna liczba całkowita — łączna ilość wody.

### Ograniczenia

* `1 ≤ n ≤ 1000`
* $0 \le h_i \le 10^4$

### Przykład

**Wejście:**

```
5
3 0 1 0 2
```

**Wyjście:**

```
5
```

Nad słupkami o indeksach 1, 2 i 3 woda sięga wysokości $\min(3, 2) = 2$, więc zatrzyma się tam odpowiednio $2 + 1 + 2 = 5$ jednostek.

### Uwagi

* Liczenie $L_i$ i $P_i$ od nowa dla każdego słupka daje czas $O(n^2)$. Oczekiwane rozwiązanie działa w czasie $O(n)$: policz maksima prefiksowe i sufiksowe w dwóch przejściach albo użyj dwóch wskaźników idących od końców listy.

"""


def ile_wody(slupki):
    """Oblicza ilość wody zatrzymanej między słupkami (metoda dwóch wskaźników)."""
    lewy, prawy = 0, len(slupki) - 1
    maks_lewy, maks_prawy = 0, 0
    woda = 0

    while lewy < prawy:
        if slupki[lewy] <= slupki[prawy]:
            maks_lewy = max(maks_lewy, slupki[lewy])
            woda += maks_lewy - slupki[lewy]
            lewy += 1
        else:
            maks_prawy = max(maks_prawy, slupki[prawy])
            woda += maks_prawy - slupki[prawy]
            prawy -= 1

    return woda


if __name__ == "__main__":
    n = int(input())
    slupki = [int(x) for x in input().split()]
    print(ile_wody(slupki))
