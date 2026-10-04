r"""
ZAD-04 — Najdłuższy fragment o równych sumach

**Poziom:** ★★★
**Tagi:** `list`, `prefix`, `hashmap`, `podciąg`

### Treść

Otrzymujesz dwie listy binarne `A` i `B` (zera i jedynki) o tej samej długości `n`. Znajdź **największą długość** fragmentu (ciągłego zakresu indeksów od `i` do `j`), dla którego suma elementów `A` w tym zakresie jest równa sumie elementów `B` w tym samym zakresie, czyli $A_i + A_{i+1} + \ldots + A_j = B_i + B_{i+1} + \ldots + B_j$.

Jeśli taki fragment nie istnieje — wypisz `0`.

### Wejście

* 1. linia: `n` — długość list
* 2. linia: `n` liczb `0`/`1` — lista `A`
* 3. linia: `n` liczb `0`/`1` — lista `B`

### Wyjście

Jedna liczba całkowita — największa długość fragmentu albo `0`.

### Ograniczenia

* `1 ≤ n ≤ 1000`

### Przykład

**Wejście:**

```
6
0 0 1 1 1 1
0 1 1 0 1 0
```

**Wyjście:**

```
5
```

Dla indeksów 0–4 obie sumy są równe 3, więc istnieje fragment długości 5. Dłuższego nie ma: dla całych list sumy wynoszą 4 i 3.

### Uwagi

* Suma `A` i `B` na fragmencie `i..j` jest równa wtedy, gdy różnica sum prefiksowych $\sum A - \sum B$ jest taka sama tuż przed indeksem `i` i na indeksie `j`. Zapamiętuj w słowniku, gdzie każda różnica pojawiła się po raz pierwszy — da to rozwiązanie w czasie $O(n)$.

"""


def najdluzszy_fragment(lista_a, lista_b):
    """Długość najdłuższego fragmentu o równych sumach w obu listach."""
    # Suma a[i..j] == suma b[i..j]  <=>  różnica sum prefiksowych jest taka sama
    # tuż przed i oraz w j.
    pierwsze_wystapienie = {0: -1}
    roznica = 0
    wynik = 0

    for i in range(len(lista_a)):
        roznica += lista_a[i] - lista_b[i]

        if roznica in pierwsze_wystapienie:
            wynik = max(wynik, i - pierwsze_wystapienie[roznica])
        else:
            pierwsze_wystapienie[roznica] = i

    return wynik


if __name__ == "__main__":
    n = int(input())
    lista_a = [int(x) for x in input().split()]
    lista_b = [int(x) for x in input().split()]
    print(najdluzszy_fragment(lista_a, lista_b))
