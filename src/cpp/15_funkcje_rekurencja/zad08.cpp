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

#include <cassert>
#include <utility>
#include <vector>

using Ruchy = std::vector<std::pair<char, char>>;

// Zlozonosc Czasowa: O(2^n)
// Zlozonosc Pamieciowa: O(n) - przez stos rekurencji (plus O(2^n) na wynik)
void hanoi(int n, char skad, char dokad, char pomocniczy, Ruchy& ruchy) {
  // Dopisuje do listy ruchy przenoszace n krazkow ze slupka skad na dokad.
  if (n == 0) return;

  hanoi(n - 1, skad, pomocniczy, dokad, ruchy);
  ruchy.emplace_back(skad, dokad);
  hanoi(n - 1, pomocniczy, dokad, skad, ruchy);
}

Ruchy hanoi(int n) {
  Ruchy ruchy;
  hanoi(n, 'A', 'B', 'C', ruchy);
  return ruchy;
}

void test1() {
  Ruchy wynik = {{'A', 'B'}, {'A', 'C'}, {'B', 'C'}, {'A', 'B'},
                 {'C', 'A'}, {'C', 'B'}, {'A', 'B'}};

  assert(hanoi(3) == wynik);
}

void test2() {
  Ruchy wynik = {{'A', 'C'}, {'A', 'B'}, {'C', 'B'}};

  assert(hanoi(2) == wynik);
  assert(hanoi(10).size() == 1023);
}

int main() {
  test1();
  test2();

  return 0;
}
