r"""
ZAD-03B — Dzielenie całkowite przy pomocy odejmowania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `odejmowanie`, `dzielenie`

### Treść

Napisz funkcję `iloraz(a, b)`, która zwraca wynik dzielenia całkowitego `a // b` obliczony przy użyciu **tylko odejmowania** i pętli (bez operatorów `/`, `//` i `%`).

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba naturalna (`a ≥ 0`)
* 2. linia: `b` — liczba naturalna (`b ≥ 1`)

### Wyjście

Jedna liczba całkowita — wynik dzielenia całkowitego `a // b`.

### Przykład

**Wejście:**

```
17
5
```

**Wyjście:**

```
3
```

Od `17` można trzy razy odjąć `5` (zostaje reszta `2`), więc wynik to `3`.

### Uwagi

* Gdy `a < b`, wynik wynosi `0`.

### Kod startowy

```python
def iloraz(a, b):
    pass


a = int(input())
b = int(input())
print(iloraz(a, b))
```

"""


def iloraz(a, b):
    wynik = 0
    while a >= b:
        a -= b
        wynik += 1
    return wynik


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(iloraz(a, b))
