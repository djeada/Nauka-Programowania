r"""
ZAD-01 — Słownik: liczby i ich kwadraty

**Poziom:** ★☆☆
**Tagi:** `dict`, `pętla`

### Treść

Wczytaj liczbę `n`. Utwórz słownik, w którym kluczami są liczby od `1` do `n - 1`, a wartościami ich kwadraty, i wypisz go.

### Wejście

* 1. linia: `n`

### Wyjście

Słownik w postaci `{1: 1, 2: 4, …}` (klucze rosnąco). Dla `n = 1` słownik jest pusty: `{}`.

### Ograniczenia

* `1 ≤ n ≤ 30`

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
{1: 1, 2: 4, 3: 9, 4: 16}
```

"""


def slownik_kwadratow(n):
    """Zwraca słownik {liczba: liczba²} dla liczb od 1 do n - 1."""
    slownik = {}
    for liczba in range(1, n):
        slownik[liczba] = liczba**2
    return slownik


if __name__ == "__main__":
    n = int(input())
    print(slownik_kwadratow(n))
