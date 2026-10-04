/*
ZAD-08 — Wieża Hanoi

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `Hanoi`

### Treść

Na słupku `A` leży `N` krążków o różnych średnicach: na dole największy, a każdy kolejny jest mniejszy od poprzedniego. Słupki `B` i `C` są puste. Należy przenieść wszystkie krążki na słupek `B`, korzystając ze słupka `C` jako pomocniczego. Obowiązują zasady:

* w jednym ruchu przenosimy dokładnie jeden krążek — górny krążek z jednego słupka na inny,
* nie wolno położyć większego krążka na mniejszym.

Napisz rekurencyjną funkcję `hanoi(n, skad, dokad, pomocniczy)`, która wypisuje ruchy przenoszące `n` krążków ze słupka `skad` na słupek `dokad`. Program wczytuje `N` i wypisuje **najkrótszą** sekwencję ruchów (ma ona $2^N - 1$ ruchów i jest wyznaczona jednoznacznie).

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

$2^N - 1$ linii — kolejne ruchy w formacie `X -> Y`, gdzie `X` to słupek, z którego zdejmujemy krążek, a `Y` to słupek, na który go kładziemy.

### Ograniczenia

* `1 ≤ N ≤ 10`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
A -> B
A -> C
B -> C
A -> B
C -> A
C -> B
A -> B
```

### Uwagi

* Aby przenieść `n` krążków ze słupka `skad` na `dokad`: przenieś `n-1` górnych krążków na słupek `pomocniczy`, przenieś największy krążek na `dokad`, a na koniec przenieś `n-1` krążków ze słupka `pomocniczy` na `dokad`. Przypadek bazowy: jeden krążek (albo zero krążków — wtedy nic nie robimy).

### Kod startowy

```python
def hanoi(n, skad, dokad, pomocniczy):
    pass


n = int(input())
hanoi(n, "A", "B", "C")
```

*/

import java.util.*;

public class Main {

  // Zlozonosc Czasowa: O(2^n)
  // Zlozonosc Pamieciowa: O(n) - rekurencja uzywa stosu (plus O(2^n) na wynik)
  public static void hanoi(
      int n, char skad, char dokad, char pomocniczy, List<String> ruchy) {
    // Dopisuje ruchy "X -> Y" przenoszace n krazkow ze slupka skad na dokad.
    if (n == 0) {
      return;
    }

    hanoi(n - 1, skad, pomocniczy, dokad, ruchy);
    ruchy.add(skad + " -> " + dokad);
    hanoi(n - 1, pomocniczy, dokad, skad, ruchy);
  }

  public static List<String> hanoi(int n) {
    List<String> ruchy = new ArrayList<>();
    hanoi(n, 'A', 'B', 'C', ruchy);
    return ruchy;
  }

  public static void test1() {
    List<String> wynik =
        Arrays.asList("A -> B", "A -> C", "B -> C", "A -> B", "C -> A", "C -> B", "A -> B");

    assert wynik.equals(hanoi(3));
  }

  public static void test2() {
    assert Arrays.asList("A -> C", "A -> B", "C -> B").equals(hanoi(2));
    assert hanoi(10).size() == 1023;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}
