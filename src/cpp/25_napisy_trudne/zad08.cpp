/*
ZAD-08 — Najdłuższy wspólny przedrostek

**Poziom:** ★★★
**Tagi:** `string`, `prefix`, `list`

### Treść

Otrzymujesz listę napisów (w kolejnych liniach). Znajdź najdłuższy przedrostek
wspólny dla wszystkich.

### Wejście

* 1 linia: `n` — liczba napisów
* kolejne `n` linii: napisy

### Wyjście

* 1 linia: najdłuższy wspólny przedrostek (może być pusty)

### Przykład

**Wejście:**

```
3
Remolada
Remux
Remmy
```

**Wyjście:**

```
Rem
```

*/
#include <cassert>
#include <climits>
#include <string>
#include <vector>

std::string najdluzszyPrzedrostekV1(const std::vector<std::string> &slowa) {
  std::string wynik = "";
  auto n = slowa.size();
  auto j = INT_MAX;

  for (const auto &slowo : slowa) {
    auto s = slowo.length();
    if (j > s) j = s;
  }

  for (auto i = 0; i < j; i++) {
    auto pom = slowa[0][i];
    auto k = 1;
    while (k < n) {
      if (pom == slowa[k][i])
        k++;
      else
        return wynik;
    }
    wynik += pom;
  }
  return wynik;
}

// Testy Poprawnosci
void test1() {
  std::vector<std::string> slowa = {"abcdefgh", "abcefgh", "abcd"};
  std::string wynik = "abc";

  assert(najdluzszyPrzedrostekV1(slowa) == wynik);
}

void test2() {
  std::vector<std::string> slowa = {"flower", "flow", "flight", "flix"};
  std::string wynik = "fl";

  assert(najdluzszyPrzedrostekV1(slowa) == wynik);
}

void test3() {
  std::vector<std::string> slowa = {"student", "studio", "stress", "lol"};
  std::string wynik;

  assert(najdluzszyPrzedrostekV1(slowa) == wynik);
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}
