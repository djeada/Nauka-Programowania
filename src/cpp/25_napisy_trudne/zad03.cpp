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
#include <string>

bool jednakowyPoczatekV1(string slowoA, string slowoB) {
  transform(slowoA.begin(), slowoA.end(), slowoA.begin(), ::tolower);
  transform(slowoB.begin(), slowoB.end(), slowoB.begin(), ::tolower);

  return !slowoA.find(slowoB);
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

int main() {
  test1();
  test2();

  return 0;
}
