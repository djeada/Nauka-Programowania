r"""
ZAD-03A — Mnożenie przy pomocy dodawania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `dodawanie`, `mnożenie`

### Treść

Napisz funkcję `iloczyn(a, b)`, która zwraca $a \cdot b$ obliczone przy użyciu **tylko dodawania** i pętli (bez operatora `*`).

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba naturalna (`a ≥ 0`)
* 2. linia: `b` — liczba naturalna (`b ≥ 0`)

### Wyjście

Jedna liczba całkowita — iloczyn $a \cdot b$.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
6
```

$3 \cdot 2 = 2 + 2 + 2 = 6$.

### Kod startowy

```python
def iloczyn(a, b):
    pass


a = int(input())
b = int(input())
print(iloczyn(a, b))
```

"""


def iloczyn(a, b):
    wynik = 0
    for _ in range(a):
        wynik += b
    return wynik


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(iloczyn(a, b))
