"""
ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

**Poziom:** ★★☆
**Tagi:** `delta`, `pierwiastki`, `I/O`

### Treść

Wczytaj współczynniki równania kwadratowego ( ax^2 + bx + c = 0 ). Wypisz wszystkie **rzeczywiste** miejsca zerowe w kolejności rosnącej.

### Wejście

* 1. linia: trzy liczby całkowite: `a b c` (oddzielone spacją)

### Wyjście

* Jeśli brak rzeczywistych pierwiastków: wypisz `[]`
* Jeśli jeden pierwiastek (delta = 0): wypisz go raz w formacie listy: `[x]`
* Jeśli dwa pierwiastki: wypisz w formacie listy: `[x1, x2]` gdzie `x1 ≤ x2`

**Format liczb:**

* wypisuj jako liczby zmiennoprzecinkowe (np. `-1.0`, `2.5`)

### Przykład

**Wejście:**

```
1 2 1
```

**Wyjście:**

```
[-1.0]
```

### Uwagi o formatowaniu

* Licz deltę: `Δ = b*b - 4*a*c`.
* Dla `Δ > 0`: policz oba pierwiastki i posortuj rosnąco.
* Zakładamy `a ≠ 0`.

"""


def wyraz_ciag(n):
    """
    Funkcja oblicza n-ty wyraz ciagu danego wzorem rekurencyjnym:
    a_1 = 1,
    a_n = 1 + 2a_(n-1)
    """
    if n < 1:
        raise ValueError("Liczba musi byc wieksza od zera")

    if n == 1:
        return 1
    else:
        return 1 + 2 * wyraz_ciag(n - 1)


def test_wyraz_ciag():

    assert wyraz_ciag(1) == 1
    assert wyraz_ciag(2) == 3
    assert wyraz_ciag(10) == 1023


if __name__ == "__main__":
    test_wyraz_ciag()
