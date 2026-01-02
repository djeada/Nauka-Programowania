/*
ZAD-07 — Zamień znaki na kody ASCII

**Poziom:** ★☆☆
**Tagi:** `ASCII`, `ord`, `string`

### Treść

Wczytaj napis i wypisz kody ASCII wszystkich jego znaków, oddzielone przecinkiem
i spacją `", "`.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: kody ASCII oddzielone `, `

### Przykład

**Wejście:**

```
Robot
```

**Wyjście:**

```
82, 111, 98, 111, 116
```

*/
#include <algorithm>
#include <cassert>
#include <string>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(n)
void zamienV1(std::string &napis) {
  if (napis.empty()) return;

  std::string wynik = "";

  for (int numer : napis) wynik += std::to_string(numer) + ", ";

  napis = wynik.substr(0, wynik.size() - 2);
}

void test1() {
  std::string napis = "pacZka!";
  std::string wynik = "112, 97, 99, 90, 107, 97, 33";

  zamienV1(napis);
  assert(napis == wynik);
}

void test2() {
  std::string napis = "";
  std::string wynik = "";

  zamienV1(napis);
  assert(napis == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}
