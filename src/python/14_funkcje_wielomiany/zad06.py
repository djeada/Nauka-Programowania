"""
ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

**Poziom:** ★★☆
**Tagi:** `funkcje`, `delta`, `pierwiastki`

### Treść

Napisz funkcję, która otrzymuje listę współczynników równania kwadratowego `[a, b, c]` dla `a x^2 + b x + c` i zwraca listę **rzeczywistych** miejsc zerowych.

### Wejście (argumenty funkcji)

* `coef` — lista trzech liczb `[a, b, c]`

### Wyjście (zwracana wartość)

* lista liczb zmiennoprzecinkowych:

  * jeśli `Δ < 0` → pusta lista `[]`
  * jeśli `Δ = 0` → dwa jednakowe pierwiastki `[x, x]`
  * jeśli `Δ > 0` → dwa pierwiastki `[x1, x2]` (kolejność dowolna)

### Przykład

Dla `[1, 2, 1]` funkcja zwraca:
`[-1.0, -1.0]`

### Ograniczenia / gwarancje

* Zakładamy `a ≠ 0` (to naprawdę równanie kwadratowe).

### Uwagi

* Licz `Δ = b^2 - 4ac`.
* Pierwiastki: `(-b ± sqrt(Δ)) / (2a)`.

"""


def miesca_zerowe(wspolczynniki):
    """
    Funkcja zwraca liste miejsc zerowych rownania kwadratowego.
    """
    a = wspolczynniki[0]
    b = wspolczynniki[1]
    c = wspolczynniki[2]
    delta = b**2 - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        return [-b / (2 * a)]
    else:
        return [-b / (2 * a) + delta**0.5, -b / (2 * a) - delta**0.5]


def test_miesca_zerowe():

    assert miesca_zerowe([1, 2, 1]) == [-1]
    assert miesca_zerowe([3, 9, -12]) == [13.5, -16.5]


if __name__ == "__main__":

    test_miesca_zerowe()
