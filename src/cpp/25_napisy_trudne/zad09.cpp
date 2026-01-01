/*
ZAD-09 — Najdłuższy wspólny podnapis

**Poziom:** ★★★
**Tagi:** `string`, `dp`, `substring`

### Treść

Otrzymujesz dwa napisy. Znajdź **najdłuższy wspólny podnapis** (ciągły
fragment), który występuje w obu napisach.

### Wejście

* 1 linia: napis `A`
* 2 linia: napis `B`

### Wyjście

* 1 linia: najdłuższy wspólny podnapis
  (jeśli jest kilka o tej samej długości — wybierz ten, który występuje
**najwcześniej w A**; jeśli nadal remis, najwcześniej w B)

### Przykład

**Wejście:**

```
ijkabcdl
xxxxabcd
```

**Wyjście:**

```
abcd
```

*/
#include <cassert>
#include <string>
#include <vector>

std::string najdluzszyPodnapisV1(const std::string &slowoA,
                                 const std::string &slowoB) {
  auto m = slowoA.length();
  auto n = slowoB.length();

  std::vector<std::vector<int>> pom(m, vector<int>(n));

  for (auto i = 1; i <= m; i++) {
    for (auto j = 1; j <= n; j++) {
      if (slowoA[i - 1] == slowoB[j - 1])
        pom[i][j] = pom[i - 1][j - 1] + 1;
      else
        pom[i][j] = 0;
    }
  }

  std::string wynik = "";
  for (auto i = 1; i <= m; i++) {
    for (auto j = 1; j <= n; j++) {
      if (pom[i][j] > wynik.length())
        wynik = slowoA.substr((i - pom[i][j] + 1) - 1, pom[i][j]);
    }
  }
  return wynik;
}

// Testy Poprawnosci
void test1() {
  std::string slowoA = "abcdxyz";
  std::string slowoB = "xyzabcd";
  std::string wynik = "abcd";

  assert(najdluzszyPodnapisV1(slowoA, slowoB) == wynik);
}

void test2() {
  std::string slowoA = "hhaall";
  std::string slowoB = "hhaall";
  std::string wynik = "hhaall";

  assert(najdluzszyPodnapisV1(slowoA, slowoB) == wynik);
}

void test3() {
  std::string slowoA;
  std::string slowoB;
  std::string wynik;

  assert(najdluzszyPodnapisV1(slowoA, slowoB) == wynik);
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}
