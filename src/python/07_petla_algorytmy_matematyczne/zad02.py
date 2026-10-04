r"""
ZAD-02 — Potęgowanie liczby przy pomocy pętli

**Poziom:** ★☆☆
**Tagi:** `pętle`, `potęgowanie`, `mnożenie`

### Treść

Napisz funkcję `potega(a, b)`, która zwraca $a^b$ obliczone przy użyciu pętli — **bez** operatora `**` i funkcji `pow()`.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba naturalna (`a ≥ 0`)
* 2. linia: `b` — liczba naturalna (`b ≥ 0`)

### Wyjście

Jedna liczba całkowita — wartość $a^b$.

### Przykład

**Wejście:**

```
3
5
```

**Wyjście:**

```
243
```

### Uwagi

* Dla `b = 0` wynik wynosi `1` (przyjmujemy też $0^0 = 1$).

### Kod startowy

```python
def potega(a, b):
    pass


a = int(input())
b = int(input())
print(potega(a, b))
```

"""


def potega(a, b):
    wynik = 1
    for _ in range(b):
        wynik *= a
    return wynik


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(potega(a, b))
