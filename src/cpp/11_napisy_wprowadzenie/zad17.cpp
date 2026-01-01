/*
ZAD-17 — Konwersja listy na napis

**Poziom:** ★☆☆
**Tagi:** `list`, `string`

### Treść

Otrzymujesz listę liczb naturalnych w zapisie tekstowym (np. `[2, 4, 7]`).
Połącz liczby bez separatorów i wypisz jako napis.

### Wejście

* 1. linia: lista w formacie podobnym do Pythona, np. `[2, 4, 7]`

### Wyjście

* 1. linia: napis z połączonych liczb, np. `247`

### Przykład

**Wejście:**

```
[2, 4, 7]
```

**Wyjście:**

```
247
```

### Uwagi

* Najprościej: usuń nawiasy `[` `]`, rozdziel po przecinkach, `strip()`, potem
sklej.

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

std::string liczby(const std::vector<int> &lista) {
  std::string wynik = "";

  for (auto liczba : lista) wynik += std::to_string(liczba);

  return wynik;
}

void test1() {
  std::vector<int> lista({2, 4, 7});
  std::string wynik = "247";
  assert(liczby(lista) == wynik);
}

void test2() {
  std::vector<int> lista;
  std::string wynik = "";
  assert(liczby(lista) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}
