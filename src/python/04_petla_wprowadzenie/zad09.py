r"""
ZAD-09 — Ciąg Collatza

**Poziom:** ★☆☆
**Tagi:** `while`, `pętle`, `warunki`

### Treść

Ciąg Collatza zaczyna się od liczby `n`. Każdy kolejny wyraz powstaje z poprzedniego `x` według reguły:

* jeśli `x` jest parzyste, następny wyraz to $\frac{x}{2}$,
* jeśli `x` jest nieparzyste, następny wyraz to $3x + 1$.

Ciąg kończy się, gdy osiągnie wartość `1`.

Wczytaj `n` i wypisz, ile kroków (przejść do kolejnego wyrazu) potrzeba, aby dojść do `1`, oraz jaka jest największa wartość, która pojawiła się w ciągu (łącznie z samym `n`).

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Dwie liczby całkowite, każda w osobnej linii:

1. liczba kroków potrzebnych do osiągnięcia `1`,
2. największa wartość w ciągu.

### Ograniczenia

* `1 ≤ n ≤ 1000000`

### Przykład

**Wejście:**

```
6
```

**Wyjście:**

```
8
16
```

Ciąg ma postać $6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$: to `8` kroków, a największy wyraz to `16`.

### Uwagi

* Nie wiadomo z góry, ile kroków wykona pętla — to typowe zastosowanie pętli `while`.
* Dla `n = 1` ciąg od razu jest w `1`: wypisz `0` i `1`.
* Do dzielenia używaj `//`, żeby wyrazy ciągu pozostały liczbami całkowitymi.
* Nikt nie udowodnił, że ciąg Collatza zawsze dochodzi do `1` (to słynna hipoteza Collatza), ale sprawdzono to dla wszystkich liczb z zakresu zadania.

"""


def nastepny_wyraz(x):
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1


def collatz(n):
    """Zwraca parę (liczba kroków, największa wartość w ciągu)."""
    kroki = 0
    najwieksza = n
    while n != 1:
        n = nastepny_wyraz(n)
        kroki += 1
        if n > najwieksza:
            najwieksza = n
    return kroki, najwieksza


if __name__ == "__main__":
    n = int(input())

    kroki, najwieksza = collatz(n)
    print(kroki)
    print(najwieksza)
