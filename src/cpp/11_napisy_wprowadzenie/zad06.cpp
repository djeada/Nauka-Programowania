/*
ZAD-06 — Zamień litery „a” na „?”

**Poziom:** ★☆☆
**Tagi:** `string`, `replace`

### Treść

Wczytaj napis i zamień wszystkie wystąpienia litery `a` na znak `?`.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: napis po zamianie

### Przykład

**Wejście:**

```
Latarnik
```

**Wyjście:**

```
L?t?rnik
```

*/
#include <algorithm>
#include <cassert>
#include <string>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
void zamienV1(std::string &napis) {
  for (auto &znak : napis) {
    if (znak == 'a') znak = '?';
  }
}

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
void zamienV2(std::string &napis) {
  replace(napis.begin(), napis.end(), 'a', '?');
}

void test1() {
  std::string napis = "pacZka!";
  std::string wynik = "p?cZk?!";

  zamienV1(napis);
  assert(napis == wynik);
}

void test2() {
  std::string napis = "pacZka!";
  std::string wynik = "p?cZk?!";

  zamienV2(napis);
  assert(napis == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}
