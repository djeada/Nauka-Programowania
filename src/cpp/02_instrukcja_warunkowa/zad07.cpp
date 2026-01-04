/*
ZAD-07 — Prawa logiki (p i q)

**Poziom:** ★★☆
**Tagi:** `bool`, `logika`, `tabele prawdy`, `formatowanie`

### Treść

Dla wszystkich kombinacji wartości logicznych `p` i `q` (True/False) sprawdź
poprawność praw:

1. Wyłączony środek: `p OR (NOT p)`
2. Niesprzeczność: `NOT (p AND (NOT p))`
3. Przemienność AND: `p AND q` vs `q AND p`
4. Przemienność OR: `p OR q` vs `q OR p`
5. De Morgana 1: `NOT (p AND q)` vs `(NOT p) OR (NOT q)`
6. De Morgana 2: `NOT (p OR q)` vs `(NOT p) AND (NOT q)`

### Wejście

Brak.

### Wyjście

Żeby wynik był **jednoznaczny i łatwy do sprawdzenia**, zastosuj dokładnie ten
format:

Dla każdego z 6 praw wypisz:

* nazwę prawa w jednej linii,
* następnie w osobnych liniach wynik dla każdej kombinacji `p, q` w kolejności:

  1. `p=False, q=False`
  2. `p=False, q=True`
  3. `p=True, q=False`
  4. `p=True, q=True`

Każda linia kombinacji ma mieć format:
`p=<...> q=<...> L=<...> R=<...> EQ=<...>`

Gdzie `<...>` to dosłownie `True` albo `False`.

### Przykład fragmentu (dla jednego prawa)

```
Przemienność alternatywy:
p=False q=False L=False R=False EQ=True
p=False q=True L=True R=True EQ=True
p=True q=False L=True R=True EQ=True
p=True q=True L=True R=True EQ=True
```

### Uwagi o formatowaniu

* Dokładne nazwy praw (nagłówki) użyj jak poniżej:

  1. `Prawo wyłączonego środka:`
  2. `Prawo niesprzeczności:`
  3. `Przemienność koniunkcji:`
  4. `Przemienność alternatywy:`
  5. `Pierwsze prawo de Morgana:`
  6. `Drugie prawo de Morgana:`
* Między blokami praw możesz wstawić **jedną pustą linię** (zalecane), ale nie
więcej.

*/
#include <iostream>
#include <string>

std::string bool_to_str(bool b) { return b ? "True" : "False"; }

void test_law(const std::string &name, bool p, bool q, bool left, bool right) {
  std::cout << "p=" << bool_to_str(p) << " q=" << bool_to_str(q)
            << " L=" << bool_to_str(left) << " R=" << bool_to_str(right)
            << " EQ=" << bool_to_str(left == right) << std::endl;
}

int main() {
  bool values[] = {false, true};

  // Prawo wyłączonego środka: p OR (NOT p)
  std::cout << "Prawo wyłączonego środka:" << std::endl;
  for (bool p : values) {
    for (bool q : values) {
      bool left = p || !p;
      bool right = true;
      test_law("", p, q, left, right);
    }
  }
  std::cout << std::endl;

  // Prawo niesprzeczności: NOT (p AND (NOT p))
  std::cout << "Prawo niesprzeczności:" << std::endl;
  for (bool p : values) {
    for (bool q : values) {
      bool left = !(p && !p);
      bool right = true;
      test_law("", p, q, left, right);
    }
  }
  std::cout << std::endl;

  // Przemienność koniunkcji: p AND q vs q AND p
  std::cout << "Przemienność koniunkcji:" << std::endl;
  for (bool p : values) {
    for (bool q : values) {
      bool left = p && q;
      bool right = q && p;
      test_law("", p, q, left, right);
    }
  }
  std::cout << std::endl;

  // Przemienność alternatywy: p OR q vs q OR p
  std::cout << "Przemienność alternatywy:" << std::endl;
  for (bool p : values) {
    for (bool q : values) {
      bool left = p || q;
      bool right = q || p;
      test_law("", p, q, left, right);
    }
  }
  std::cout << std::endl;

  // Pierwsze prawo de Morgana: NOT (p AND q) vs (NOT p) OR (NOT q)
  std::cout << "Pierwsze prawo de Morgana:" << std::endl;
  for (bool p : values) {
    for (bool q : values) {
      bool left = !(p && q);
      bool right = !p || !q;
      test_law("", p, q, left, right);
    }
  }
  std::cout << std::endl;

  // Drugie prawo de Morgana: NOT (p OR q) vs (NOT p) AND (NOT q)
  std::cout << "Drugie prawo de Morgana:" << std::endl;
  for (bool p : values) {
    for (bool q : values) {
      bool left = !(p || q);
      bool right = !p && !q;
      test_law("", p, q, left, right);
    }
  }

  return 0;
}
