/*
ZAD-14 — Napis z liczb od 1 do n

**Poziom:** ★☆☆
**Tagi:** `pętle`, `string`

### Treść

Wczytaj `n` i wypisz napis złożony z kolejnych liczb od 1 do `n`, bez
separatorów.

### Wejście

* 1. linia: liczba naturalna `n` (n ≥ 1)

### Wyjście

* 1. linia: ciąg `1..n` bez spacji

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
123
```

*/
#include <algorithm>
#include <cassert>
#include <string>

// Zlozonosc Czasowa: O(n * log10(n))
// Zlozonosc Pamieciowa: O(n * log10(n))
std::string liczby(int n) {
  std::string wynik = "";

  for (int i = 1; i <= n; i++) wynik += std::to_string(i);

  return wynik;
}

void test1() {
  int n = 5;
  std::string wynik = "12345";
  assert(liczby(n) == wynik);
}

void test2() {
  int n = -1;
  std::string wynik = "";
  assert(liczby(n) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}
