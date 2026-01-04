/*
ZAD-07 — Minimalna liczba usunięć, aby uzyskać anagramy

**Poziom:** ★★★
**Tagi:** `anagram`, `zliczanie`, `greedy`

### Treść

Wczytaj dwa słowa. Jeśli mają różne długości, wypisz `-1`.
W przeciwnym razie oblicz minimalną liczbę znaków, które trzeba usunąć (łącznie
z obu słów), aby pozostałe napisy były anagramami.

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

* jedna liczba całkowita: minimalna liczba usunięć lub `-1`

### Przykład

**Wejście:**

```
grazyna
razynax
```

**Wyjście:**

```
2
```

### Uwagi

* Dla tej samej długości: policz zliczenia liter i zsumuj wartości `abs(c1[lit]
- c2[lit])`, a wynik wypisz jako tę sumę. (To jest łączna liczba usunięć.)

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <unordered_map>
#include <vector>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
int liczbaZnakow(const std::string &slowoA, const std::string &slowoB) {
  if (slowoA.length() != slowoB.length()) return -1;

  std::vector<int> pom(256, 0);

  for (auto znak : slowoA) pom[znak - 'a']++;

  for (auto znak : slowoB) pom[znak - 'a']--;

  long wynik = 0;

  for (auto liczba : pom) wynik += abs(liczba);

  return wynik;
}

void test1() {
  std::string slowoA = "grazyna";
  std::string slowoB = "razynax";
  int wynik = 2;
  assert(liczbaZnakow(slowoA, slowoB) == wynik);
}

void test2() {
  std::string slowoA = "pan cytryna";
  std::string slowoB = "pan pomarancza";
  int wynik = -1;
  assert(liczbaZnakow(slowoA, slowoB) == wynik);
}

void test3() {
  std::string slowoA = "20ejdy0978oa";
  std::string slowoB = "akv81w39j1ob";
  int wynik = 14;
  assert(liczbaZnakow(slowoA, slowoB) == wynik);
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}
