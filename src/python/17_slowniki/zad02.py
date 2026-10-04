r"""
ZAD-02 — Słownik z dwóch list (klucze i wartości)

**Poziom:** ★☆☆
**Tagi:** `dict`, `listy`

### Treść

Wczytaj dwie listy liczb całkowitych. Jeśli mają tę samą długość, utwórz słownik, w którym `i`-ty element pierwszej listy jest kluczem, a `i`-ty element drugiej listy — jego wartością. Jeśli długości są różne, wynikiem jest pusty słownik.

### Wejście

* 1. linia: `n` — długość pierwszej listy
* 2. linia: `m` — długość drugiej listy
* 3. linia: `n` liczb całkowitych oddzielonych spacjami (klucze)
* 4. linia: `m` liczb całkowitych oddzielonych spacjami (wartości)

### Wyjście

Słownik w postaci `{klucz: wartość, …}` z kluczami w kolejności z wejścia albo `{}`, gdy `n ≠ m`.

### Ograniczenia

* `1 ≤ n, m ≤ 20`

### Przykład

**Wejście:**

```
3
3
3 5 8
1 2 -1
```

**Wyjście:**

```
{3: 1, 5: 2, 8: -1}
```

### Uwagi

* Jeśli klucz powtarza się w pierwszej liście, obowiązuje jego **ostatnia** wartość, a klucz zostaje na miejscu swojego pierwszego wystąpienia — tak działa kolejne przypisanie `slownik[klucz] = wartość`. Na przykład klucze `1 2 1` i wartości `5 6 7` dają `{1: 7, 2: 6}`.

"""


def stworz_slownik(klucze, wartosci):
    """
    Zwraca słownik, w którym klucze[i] odpowiada wartosci[i].
    Dla list różnej długości zwraca pusty słownik.
    """
    if len(klucze) != len(wartosci):
        return {}
    slownik = {}
    for i in range(len(klucze)):
        slownik[klucze[i]] = wartosci[i]
    return slownik


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    klucze = [int(x) for x in input().split()]
    wartosci = [int(x) for x in input().split()]
    print(stworz_slownik(klucze, wartosci))
