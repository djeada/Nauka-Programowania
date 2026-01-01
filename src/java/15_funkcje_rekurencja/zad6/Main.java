/*
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

*/
public class Main {

  public static int ciagV1(int n) {

    if (n == 1) {
      return 1;
    }

    return 1 + ciagV1(n - 1) * 2;
  }

  public static void test1() {
    int n = 5;
    int wynik = 31;

    assert ciagV1(n) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

