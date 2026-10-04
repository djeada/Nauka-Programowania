r"""
ZAD-01 — Liczba większa od 5

**Poziom:** ★☆☆
**Tagi:** `if`, `porównania`, `I/O`

### Treść

Wczytaj jedną liczbę naturalną `n`.
Jeśli $n > 5$, wypisz `n`. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1 linia: `n` — liczba całkowita, $0 \le n \le 10^9$

### Wyjście

* Jeśli $n > 5$: jedna linia z liczbą `n`.
* Jeśli $n \le 5$: brak wyjścia.

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
    n = int(input())

    if n > 5:
        print(n)
