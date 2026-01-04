/*
ZAD-03 — Czy dwa słowa są anagramami?

**Poziom:** ★☆☆
**Tagi:** `anagram`, `sortowanie`, `zliczanie`

### Treść

Wczytaj dwa słowa i sprawdź, czy są anagramami (czy da się utworzyć jedno przez
przestawienie liter drugiego).

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

Jedna linia:

* `Prawda` — jeśli anagramy
* `Fałsz` — jeśli nie

### Przykład

**Wejście:**

```
ula
lua
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Najprościej: porównaj posortowane litery albo słowniki zliczeń znaków.

*/
#include <cassert>
#include <string>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
bool anagram(std::string s1, std::string s2) {
  int N = s1.length();
  int M = s2.length();

  if (N != M) return false;

  int pom[256] = {0};

  for (const auto &znak : s1) pom[znak]++;

  for (const auto &znak : s2) pom[znak]--;

  for (const auto &x : pom) {
    if (x != 0) return false;
  }

  return true;
}

void test1() {
  std::string s1 = "adam";
  std::string s2 = "mada";
  assert(anagram(s1, s2));
}

void test2() {
  std::string s1 = "adam";
  std::string sw = "dame";
  assert(!anagram(s1, sw));
}

int main() {
  test1();
  test2();
  return 0;
}
