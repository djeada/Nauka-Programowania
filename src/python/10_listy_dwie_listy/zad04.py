r"""
ZAD-04 — Iloczyn skalarny dwóch wektorów 3D

**Poziom:** ★☆☆
**Tagi:** `listy`, `wektory`, `matematyka`

### Treść

Wczytaj dwa wektory w przestrzeni trójwymiarowej, $A = [A_x, A_y, A_z]$ oraz $B = [B_x, B_y, B_z]$, i oblicz ich **iloczyn skalarny**:
$A \cdot B = A_x B_x + A_y B_y + A_z B_z$.

### Wejście

* 1. linia: wektor $A$ — trzy liczby całkowite oddzielone spacjami
* 2. linia: wektor $B$ — trzy liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: iloczyn skalarny (liczba całkowita).

### Przykład

**Wejście:**

```
1 2 3
3 1 2
```

**Wyjście:**

```
11
```

$1 \cdot 3 + 2 \cdot 1 + 3 \cdot 2 = 11$.

"""


def iloczyn_skalarny(wektor_a, wektor_b):
    wynik = 0
    for a, b in zip(wektor_a, wektor_b):
        wynik += a * b
    return wynik


if __name__ == "__main__":
    wektor_a = [int(x) for x in input().split()]
    wektor_b = [int(x) for x in input().split()]

    print(iloczyn_skalarny(wektor_a, wektor_b))
