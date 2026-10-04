r"""
ZAD-08 — Czy można zbudować trójkąt?

**Poziom:** ★☆☆
**Tagi:** `if`, `geometria`, `warunek trójkąta`

### Treść

Wczytaj trzy dodatnie długości odcinków `a`, `b`, `c`.
Sprawdź, czy można z nich zbudować trójkąt (niezdegenerowany).

Trójkąt istnieje wtedy i tylko wtedy, gdy spełnione są **wszystkie** trzy nierówności:

* $a + b > c$
* $a + c > b$
* $b + c > a$

Wypisz:

* jeśli tak: `Trójkąt można zbudować z podanych boków.`
* jeśli nie: `Trójkąta nie można zbudować z podanych boków.`

### Wejście

* 1 linia: `a` — liczba całkowita
* 2 linia: `b` — liczba całkowita
* 3 linia: `c` — liczba całkowita

### Wyjście

Jedna linia — dokładnie jeden z komunikatów.

### Ograniczenia

* $1 \le a, b, c \le 10^9$

### Przykład 1

**Wejście:**

```
3
4
5
```

**Wyjście:**

```
Trójkąt można zbudować z podanych boków.
```

### Przykład 2

**Wejście:**

```
1
2
5
```

**Wyjście:**

```
Trójkąta nie można zbudować z podanych boków.
```

### Uwagi

* Jeśli suma dwóch boków jest **równa** trzeciemu (np. 1, 2, 3), odcinki leżą na jednej prostej — taki „trójkąt” nie istnieje.

"""


def czy_trojkat(a, b, c):
    return a + b > c and a + c > b and b + c > a


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    if czy_trojkat(a, b, c):
        print("Trójkąt można zbudować z podanych boków.")
    else:
        print("Trójkąta nie można zbudować z podanych boków.")
