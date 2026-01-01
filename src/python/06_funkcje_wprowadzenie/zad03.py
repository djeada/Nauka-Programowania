"""
ZAD-03 — Sprawdzanie warunków logicznych

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `bool`, `warunki`

### Treść

Napisz funkcję `sprawdz_warunki(a, b)`, która dla dwóch liczb naturalnych zwraca cztery wartości logiczne (np. jako krotkę) odpowiadające warunkom:

a) Czy `a > b`?
b) Czy `a + b < 10`?
c) Czy obie liczby są nieparzyste?
d) Czy `max(a, b) < a^2`?

### Wejście

Dwa argumenty funkcji:

* `a` (liczba całkowita, `a ≥ 0`)
* `b` (liczba całkowita, `b ≥ 0`)

### Wyjście

Cztery wartości logiczne w kolejności a), b), c), d).

### Przykład

**Wywołanie funkcji:**

```python
A, B, C, D = sprawdz_warunki(3, 2)
print(A)
print(B)
print(C)
print(D)
```

**Wyjście:**

```
True
True
False
True
```

"""


def pierwsza_wieksza(pierwsza_liczba, druga_liczba):
    """
    Funkcja sprawdza czy pierwsza liczba jest wieksza od drugiej liczby.
    """
    return pierwsza_liczba > druga_liczba


def suma_mniejsza_10(pierwsza_liczba, druga_liczba):
    """
    Funkcja sprawdza czy suma liczb jest mniejsza niz 10.
    """
    return pierwsza_liczba + druga_liczba < 10


def obie_nieparzyste(pierwsza_liczba, druga_liczba):
    """
    Funkcja sprawdza czy obie liczby sa nieparzyste.
    """
    return pierwsza_liczba % 2 != 0 and druga_liczba % 2 != 0


def wieksza_mniejsza_pierwsza_kwadrat(pierwsza_liczba, druga_liczba):
    """
    Funkcja sprawdza czy wieksza liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu.
    """
    return max(pierwsza_liczba, druga_liczba) < pierwsza_liczba**2


def test_pierwsza_wieksza():
    assert not pierwsza_wieksza(1, 2)
    assert pierwsza_wieksza(2, 1)


def test_suma_mniejsza_10():
    assert suma_mniejsza_10(1, 2)
    assert not suma_mniejsza_10(2, 1)


def test_obie_nieparzyste():
    assert obie_nieparzyste(1, 2)
    assert obie_nieparzyste(2, 1)
    assert not obie_nieparzyste(2, 2)


def test_wieksza_mniejsza_pierwsza_kwadrat():
    assert wieksza_mniejsza_pierwsza_kwadrat(1, 2)
    assert not wieksza_mniejsza_pierwsza_kwadrat(2, 1)
    assert not wieksza_mniejsza_pierwsza_kwadrat(2, 2)


if __name__ == "__main__":

    test_pierwsza_wieksza()
    test_suma_mniejsza_10()
    test_obie_nieparzyste()
    test_wieksza_mniejsza_pierwsza_kwadrat()
