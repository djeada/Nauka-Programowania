r"""
ZAD-04 — Podstawowe operacje arytmetyczne

**Poziom:** ★☆☆
**Tagi:** `arytmetyka`, `I/O`

### Treść

Wczytaj dwie liczby naturalne `a` i `b` i wypisz kolejno:

1. sumę $a + b$,
2. różnicę $a - b$,
3. iloczyn $a \cdot b$,
4. iloraz całkowity $\lfloor a / b \rfloor$ (w Pythonie `a // b`),
5. resztę z dzielenia `a` przez `b` (w Pythonie `a % b`),
6. potęgę $a^b$ (w Pythonie `a ** b`).

### Wejście

* 1. linia: `a` — liczba całkowita
* 2. linia: `b` — liczba całkowita

### Wyjście

6 linii — wyniki działań w kolejności 1–6, każdy jako liczba całkowita.

### Ograniczenia

* $0 \le a \le 1000$
* $1 \le b \le 10$ (dzięki temu dzielenie i reszta są zawsze poprawne)
* $a^b \le 10^{18}$

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
5
1
6
1
1
9
```

"""

if __name__ == "__main__":
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a**b)
