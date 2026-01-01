/*
ZAD-04 — Sprawdź, czy słowo występuje w zdaniu jako osobne słowo

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz dwa napisy: zdanie oraz słowo. Sprawdź, czy słowo występuje w zdaniu
jako samodzielne słowo (nie jako fragment innego słowa).

### Wejście

Dwie linie:

1. `zdanie`
2. `slowo`

### Wyjście

Jedna linia:

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
Siała baba mak.
babcia
```

**Wyjście:**

```
Fałsz
```

*/

#include <cassert>
#include <regex>
#include <string>

bool nalezyDoZdania(std::string &zdanie, std::string &napis) {
  return regex_search(zdanie, std::regex(napis));
}

void test1() {
  std::string zdanie = "Mozart gra na skrzypcach";
  std::string napis = "skrzyp";
  assert(nalezyDoZdania(zdanie, napis));
}

void test2() {
  std::string zdanie = "Lezy jerzy na wiezy";
  std::string napis = "nan";
  assert(!nalezyDoZdania(zdanie, napis));
}

int main() {
  test1();
  test2();

  return 0;
}
