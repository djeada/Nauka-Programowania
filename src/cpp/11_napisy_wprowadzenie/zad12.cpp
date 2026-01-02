/*
ZAD-12 — Usuń spacje ze zdania

**Poziom:** ★☆☆
**Tagi:** `replace`, `string`

### Treść

Wczytaj zdanie i usuń z niego wszystkie spacje.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie bez spacji

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
Alamakota
```

*/
#include <algorithm>
#include <cassert>
#include <string>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(n)
void usunSpacjeV1(std::string &slowo) {
  std::string pom;

  for (const auto &znak : slowo) {
    if (znak != ' ') pom += znak;
  }

  slowo = pom;
}

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
void usunSpacjeV2(std::string &slowo) {
  slowo.erase(remove(slowo.begin(), slowo.end(), ' '), slowo.end());
}

void test1() {
  std::string zdanie = "lezy jezy na wierzy";
  std::string wynik = "lezyjezynawierzy";

  usunSpacjeV1(zdanie);
  assert(zdanie == wynik);
}

void test2() {
  std::string zdanie = "lezy jezy na wierzy";
  std::string wynik = "lezyjezynawierzy";

  usunSpacjeV2(zdanie);
  assert(zdanie == wynik);
}

int main() {
  test1();
  test2();

  return 0;
}
