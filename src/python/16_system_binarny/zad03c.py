r"""
ZAD-03C — Mnożenie bitowe

**Poziom:** ★★☆
**Tagi:** `bitwise`, `shift`, `pętle`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz $a \cdot b$, używając wyłącznie operatorów bitowych i przesunięć (metoda „przesuń i dodaj”).

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: $a \cdot b$.

### Ograniczenia

* $0 \le a, b \le 10^6$ (liczby ujemne nie występują)

### Przykład

**Wejście:**

```
4
4
```

**Wyjście:**

```
16
```

### Uwagi

* Do obliczenia wyniku nie używaj `+`, `-`, `*`, `/`, `//`, `%` — tylko `&`, `|`, `^`, `~`, `<<`, `>>` i porównań.
* Dla każdego ustawionego bitu `k` liczby `b` dodaj do wyniku `a << k`. Dodawanie wykonaj bitowo, tak jak w ZAD-03A.

"""


def dodaj(a, b):
    """Dodaje liczby naturalne wyłącznie operacjami bitowymi."""
    while b != 0:
        przeniesienie = (a & b) << 1
        a = a ^ b
        b = przeniesienie
    return a


def pomnoz(a, b):
    """
    Mnoży liczby naturalne metodą „przesuń i dodaj”: dla każdego
    ustawionego bitu liczby b dodajemy odpowiednio przesunięte a.
    """
    wynik = 0
    while b != 0:
        if b & 1:
            wynik = dodaj(wynik, a)
        a <<= 1
        b >>= 1
    return wynik


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(pomnoz(a, b))
