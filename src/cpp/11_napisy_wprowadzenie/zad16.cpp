/*
ZAD-16 — Odległość Hamminga

**Poziom:** ★★☆
**Tagi:** `string`, `porównanie`

### Treść

Wczytaj dwa napisy tej samej długości i policz, na ilu pozycjach różnią się
znakami.

### Wejście

* 1. linia: napis `s1`
* 2. linia: napis `s2`  (ta sama długość)

### Wyjście

* 1. linia: odległość Hamminga

### Przykład

**Wejście:**

```
adam
axam
```

**Wyjście:**

```
1
```

*/
#include <algorithm>
#include <cassert>
#include <string>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
int odlegloscHammingaV1(const std::string &napisA, const std::string &napisB) {
  if (napisA.size() != napisB.size()) return -1;

  int wynik = 0;

  for (unsigned int i = 0; i < napisA.size(); i++) {
    if (napisA[i] != napisB[i]) wynik++;
  }

  return wynik;
}

void test1() {
  std::string napisA = "xxbab";
  std::string napisB = "bbabb";
  int wynik = 4;
  assert(odlegloscHammingaV1(napisA, napisB) == wynik);
}

void test2() {
  std::string napisA = "test_string";
  std::string napisB = "test_string_2";
  int wynik = -1;
  assert(odlegloscHammingaV1(napisA, napisB) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}
