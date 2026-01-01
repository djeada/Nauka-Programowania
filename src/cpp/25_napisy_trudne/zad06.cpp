/*
ZAD-06 — Rotacje napisów

**Poziom:** ★★★
**Tagi:** `string`, `rotation`, `substring`

### Treść

Otrzymujesz dwa napisy `A` i `B`. Sprawdź, czy jeden z nich jest **rotacją**
drugiego (mają tę samą długość i da się uzyskać jeden przez przesunięcie
cykliczne drugiego).

### Wejście

* 1 linia: napis `A`
* 2 linia: napis `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
malpka
pkamal
```

**Wyjście:**

```
Prawda
```

*/
#include <algorithm>
#include <cassert>
#include <string>

bool czyRotacjaV1(std::string &s1, std::string &s2) {
  if (s1.length() != s2.length()) return false;

  std::string pom = s1 + s1;

  return (pom.find(s2) != std::string::npos);
}

// Testy Poprawnosci
void test1() {
  std::string slowoA = "malpka";
  std::string slowoB = "kamapl";

  assert(!czyRotacjaV1(slowoA, slowoB));
}

void test2() {
  std::string slowoA = "malpka";
  std::string slowoB = "pkamal";

  assert(czyRotacjaV1(slowoA, slowoB));
}

int main() {
  test1();
  test2();

  return 0;
}
