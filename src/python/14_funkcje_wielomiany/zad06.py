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

    Złożoność czasowa: O(1)
    Złożoność pamięciowa: O(1)
    """
    a = wspolczynniki[0]
    b = wspolczynniki[1]
    c = wspolczynniki[2]
    delta = b**2 - 4 * a * c

    if delta < 0:
        return []
    elif delta == 0:
        x = -b / (2 * a)
        return [x, x]  # Dwa jednakowe pierwiastki
    else:
        import math

        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return [x1, x2]


def test_miesca_zerowe():

    assert miesca_zerowe([1, 2, 1]) == [-1.0, -1.0]
    assert miesca_zerowe([1, 0, 1]) == []


if __name__ == "__main__":
    # Wczytanie współczynników jako listy lub osobno
    try:
        # Próba wczytania jako lista
        wspolczynniki = __import__("ast").literal_eval(input().strip())
    except:
        # Wczytanie jako trzy oddzielne liczby
        line = input().strip().split()
        wspolczynniki = [float(x) for x in line]

    # Obliczenie miejsc zerowych
    # Złożoność czasowa: O(1)
    # Złożoność pamięciowa: O(1)
    wynik = miesca_zerowe(wspolczynniki)

    # Wypisanie wyniku jako lista
    print(str(wynik))
