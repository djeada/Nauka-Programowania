r"""
ZAD-03 — Rysowanie kształtów znakami

**Poziom:** ★☆☆
**Tagi:** `print`, `formatowanie`, `string`

### Treść

Wypisz na wyjście trzy kształty:

1. **Kwadrat 2×2** z liter `x`.
2. **Trójkąt liczbowy** z 3 linii: w linii numer `i` wypisz `i` razy cyfrę `i` (dla `i` = 1, 2, 3).
3. **Romb z jedynek** o maksymalnej szerokości 5 znaków.

Kształty oddziel **dokładnie jedną pustą linią**.

### Wejście

Brak.

### Wyjście

Dokładnie 12 linii:

* 2 linie kwadratu,
* pusta linia,
* 3 linie trójkąta,
* pusta linia,
* 5 linii rombu.

### Przykład

**Wejście:** *(brak)*

**Wyjście:**

```
xx
xx

1
22
333

  1
 111
11111
 111
  1
```

### Uwagi

* W rombie spacje na **początku** linii są istotne (spacje na końcu linii są ignorowane).
* Nie dodawaj pustych linii na początku wyjścia.

"""


def wypisz_kwadrat():
    print("x" * 2)
    print("x" * 2)


def wypisz_trojkat():
    print("1")
    print("2" * 2)
    print("3" * 3)


def wypisz_romb():
    print("  1")
    print(" " + "1" * 3)
    print("1" * 5)
    print(" " + "1" * 3)
    print("  1")


if __name__ == "__main__":
    wypisz_kwadrat()
    print()
    wypisz_trojkat()
    print()
    wypisz_romb()
