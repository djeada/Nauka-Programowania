"""
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

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)

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

if __name__ == "__main__":

    print("podaj dwie liczby")

    a = int(input())
    b = int(input())

    if a == b:
        print("liczby sa jednakowe")
    else:
        print("liczby sa rozne")
