/*
ZAD-02 — Policz wystąpienia znaku

**Poziom:** ★☆☆
**Tagi:** `string`, `count`

### Treść

Wczytaj napis oraz jeden znak. Wypisz, ile razy ten znak występuje w napisie.

### Wejście

* 1. linia: napis
* 2. linia: pojedynczy znak

### Wyjście

* 1. linia: liczba wystąpień

### Przykład

**Wejście:**

```
klamra
a
```

**Wyjście:**

```
2
```

*/
#include <algorithm>
#include <cassert>
#include <string>

// Zlozonosc Czasowa O(n)
// Zlozonosc Pamieciowa O(1)
int policzZnakV1(const std::string &slowo, const char &znak) {
  int licznik = 0;

  for (auto x : slowo) {
    if (x == znak) licznik++;
  }

  return licznik;
}

void test1() {
  std::string napis = "adam";
  char znak = 'a';
  int wynik = 2;

  assert(policzZnakV1(napis, znak) == wynik);
}

int main() {
  test1();
  return 0;
}
