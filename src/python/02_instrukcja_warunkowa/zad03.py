r"""
ZAD-03 — Określanie znaku liczby

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `porównania`, `string`

### Treść

Wczytaj liczbę całkowitą `x` i wypisz jeden z komunikatów:

* dla $x < 0$: `Liczba jest ujemna.`
* dla $x > 0$: `Liczba jest dodatnia.`
* dla $x = 0$: `Liczba jest zerem.`

### Wejście

* 1 linia: `x` — liczba całkowita, $-10^9 \le x \le 10^9$

### Wyjście

Jedna linia — dokładnie jeden komunikat.

### Przykład 1

**Wejście:**

```
-5
```

**Wyjście:**

```
Liczba jest ujemna.
```

### Przykład 2

**Wejście:**

```
2
```

**Wyjście:**

```
Liczba jest dodatnia.
```

"""


def znak_liczby(x):
    if x < 0:
        return "Liczba jest ujemna."
    elif x > 0:
        return "Liczba jest dodatnia."
    else:
        return "Liczba jest zerem."


if __name__ == "__main__":
    x = int(input())
    print(znak_liczby(x))
