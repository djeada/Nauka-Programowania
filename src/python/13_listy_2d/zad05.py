r"""
ZAD-05 — Czy macierz jest magiczna?

**Poziom:** ★★☆
**Tagi:** `macierze`, `suma`, `warunki`

### Treść

Wczytaj macierz kwadratową `n×n` z dodatnimi liczbami całkowitymi. Sprawdź, czy jest **kwadratem magicznym**, czyli czy suma każdego wiersza, każdej kolumny oraz obu przekątnych jest taka sama.

### Wejście

* 1. linia: `n`
* następnie `n` linii po `n` liczb oddzielonych spacjami

### Wyjście

Jedno słowo: `Prawda`, jeśli macierz jest kwadratem magicznym, w przeciwnym razie `Fałsz`.

### Ograniczenia

* `1 ≤ n ≤ 10`

### Przykład

**Wejście:**

```
3
6 7 2
1 5 9
8 3 4
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Sprawdzamy wyłącznie sumy — liczby w macierzy **nie muszą** być różne (np. macierz `2×2` z samymi dwójkami jest kwadratem magicznym).
* Pamiętaj o drugiej przekątnej (od prawego górnego do lewego dolnego rogu) — macierz może mieć równe sumy wierszy, kolumn i jednej przekątnej, a mimo to nie być magiczna.
* Macierz `1×1` jest kwadratem magicznym.

"""


def czy_kwadrat_magiczny(macierz):
    """
    Sprawdza, czy sumy wszystkich wierszy, wszystkich kolumn
    oraz obu przekątnych macierzy kwadratowej są równe.
    """
    n = len(macierz)
    wzorzec = sum(macierz[0])

    for wiersz in macierz:
        if sum(wiersz) != wzorzec:
            return False

    for kolumna in range(n):
        suma_kolumny = 0
        for wiersz in range(n):
            suma_kolumny += macierz[wiersz][kolumna]
        if suma_kolumny != wzorzec:
            return False

    przekatna = 0
    antyprzekatna = 0
    for i in range(n):
        przekatna += macierz[i][i]
        antyprzekatna += macierz[i][n - 1 - i]

    return przekatna == wzorzec and antyprzekatna == wzorzec


if __name__ == "__main__":
    n = int(input())
    macierz = [[int(x) for x in input().split()] for _ in range(n)]

    if czy_kwadrat_magiczny(macierz):
        print("Prawda")
    else:
        print("Fałsz")
