/*
ZAD-01 — Czy słowo jest palindromem?

**Poziom:** ★☆☆
**Tagi:** `string`, `palindrom`, `I/O`

### Treść

Wczytaj jedno słowo i sprawdź, czy jest palindromem (czytane od lewej do prawej
i od prawej do lewej jest takie samo).

### Wejście

* 1. linia: słowo (same litery, bez spacji)

### Wyjście

Jedna linia:

* `Prawda` — jeśli słowo jest palindromem
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
kajak
```

**Wyjście:**

```
Prawda
```

### Uwagi o formatowaniu

* Jeśli chcesz ignorować wielkość liter, porównuj wersje `lower()`.

*/
#include <algorithm>
#include <cassert>
#include <string>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
bool palindrom(std::string &slowo) {
  int N = slowo.length() - 1;
  for (int i = 0; i <= N / 2; i++) {
    if (slowo[i] != slowo[N - i]) return false;
  }

  return true;
}

void test1() {
  std::string slowo = "kajak";
  assert(palindrom(slowo));
}

void test2() {
  std::string slowo = "Pan";
  assert(!palindrom(slowo));
}

int main() {
  test1();
  test2();

  return 0;
}
