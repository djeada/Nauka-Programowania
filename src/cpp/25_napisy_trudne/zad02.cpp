/*
ZAD-02 — Usuń podnapis

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Dostajesz dwa napisy:

1. Napis główny,
2. Podnapis do usunięcia.

Usuń **wszystkie wystąpienia** podnapisu z napisu głównego.

### Wejście

* 1 linia: napis `S`
* 2 linia: napis `T` (do usunięcia)

### Wyjście

* 1 linia: wynikowy napis po usunięciu wszystkich wystąpień

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
```

**Wyjście:**

```
Le je na wie
```

*/
#include <cassert>
#include <string>

std::string usunWszystkieV1(std::string zdanie, const std::string &slowo) {
  auto k = zdanie.find(slowo);

  while (k != string::npos) {
    zdanie.erase(k, slowo.length());
    k = zdanie.find(slowo);
  }

  return zdanie;
}

// Testy Poprawnosci
void test1() {
  std::string zdanie = "Lezy jezy na wiezy";
  std::string slowo = "zy";
  std::string wynik = "Le je na wie";

  assert(usunWszystkieV1(zdanie, slowo) == wynik);
}

int main() {
  test1();

  return 0;
}
