"""
ZAD-01 — Liczba większa od 5

**Poziom:** ★☆☆
**Tagi:** `if`, `porównania`, `I/O`

### Treść

Wczytaj jedną liczbę naturalną `n`.
Jeśli `n > 5`, wypisz `n`. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1 linia: `n` (liczba całkowita, `n ≥ 0`)

### Wyjście

* Jeśli `n > 5`: jedna linia z liczbą `n`
* Jeśli `n ≤ 5`: brak wyjścia

### Przykład 1

**Wejście:**

```
10
```

**Wyjście:**

```
10
```

### Przykład 2

**Wejście:**

```
3
```

**Wyjście:** *(brak)*

"""

if __name__ == "__main__":

    print("podaj liczbe:")

    x = int(input())

    if x > 5:
        print(x)
