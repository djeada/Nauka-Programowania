r"""
ZAD-02 — Porównanie dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `if-else`, `równość`, `string`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Jeśli są równe, wypisz:
`Liczby są identyczne.`
W przeciwnym razie wypisz:
`Liczby są różne.`

### Wejście

* 1 linia: `a` — liczba całkowita, $0 \le a \le 10^9$
* 2 linia: `b` — liczba całkowita, $0 \le b \le 10^9$

### Wyjście

Jedna linia — dokładnie jeden z komunikatów.

### Przykład 1

**Wejście:**

```
7
4
```

**Wyjście:**

```
Liczby są różne.
```

### Przykład 2

**Wejście:**

```
5
5
```

**Wyjście:**

```
Liczby są identyczne.
```

"""


def porownaj(a, b):
    if a == b:
        return "Liczby są identyczne."
    else:
        return "Liczby są różne."


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(porownaj(a, b))
