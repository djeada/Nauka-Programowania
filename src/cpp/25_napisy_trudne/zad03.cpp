/*
ZAD-03 — Czy napis A jest początkiem napisu B?

**Poziom:** ★★☆
**Tagi:** `string`, `prefix`

### Treść

Otrzymujesz dwa napisy:

1. Napis `A` — potencjalny przedrostek,
2. Napis `B` — napis testowany.

Sprawdź, czy `B` **zaczyna się** od `A`.

### Wejście

* 1 linia: `A`
* 2 linia: `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
Dino
Dinozaur jest zly
```

**Wyjście:**

```
Prawda
```

*/
#include <algorithm>
#include <cassert>
#include <cctype>
#include <string>

// Sprawdza (bez rozrozniania wielkosci liter), czy slowoA zaczyna sie od
// slowoB.
bool jednakowyPoczatekV1(std::string slowoA, std::string slowoB) {
  auto naMale = [](unsigned char znak) {
    return static_cast<char>(std::tolower(znak));
  };
  std::transform(slowoA.begin(), slowoA.end(), slowoA.begin(), naMale);
  std::transform(slowoB.begin(), slowoB.end(), slowoB.begin(), naMale);

  return slowoA.compare(0, slowoB.size(), slowoB) == 0;
}

// Testy Poprawnosci
void test1() {
  std::string slowoA = "Dinozaur jest zly";
  std::string slowoB = "Dino";

  assert(jednakowyPoczatekV1(slowoA, slowoB));
}

void test2() {
  std::string slowoA = "Dinozaur jest zly";
  std::string slowoB = "Pies";

  assert(!jednakowyPoczatekV1(slowoA, slowoB));
}

void test3() {
  // slowoB wystepuje w slowoA, ale nie na poczatku
  assert(!jednakowyPoczatekV1("Dinozaur jest zly", "jest"));
  // slowoB dluzsze niz slowoA
  assert(!jednakowyPoczatekV1("Dino", "Dinozaur"));
  assert(jednakowyPoczatekV1("Dinozaur", ""));
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}
