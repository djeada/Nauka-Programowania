/*
ZAD-03 — Sprawdź, czy napis składa się wyłącznie z cyfr

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis. Sprawdź, czy składa się wyłącznie z cyfr (`0–9`).

### Wejście

Jedna linia:

* `s`

### Wyjście

Jedna linia:

* `Prawda` — jeśli napis zawiera tylko cyfry
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
1234
```

**Wyjście:**

```
Prawda
```

*/

#include <cassert>
#include <regex>
#include <string>

bool jedynieCyfry(std::string &napis) {
  std::regex wzorzec("[0-9]+");
  return regex_match(napis, wzorzec);
}

void test1() {
  std::string napis = "123542";
  assert(jedynieCyfry(napis));
}

void test2() {
  std::string napis = "2bab3";
  assert(!jedynieCyfry(napis));
}

void test3() {
  std::string napis = "124131a";
  assert(!jedynieCyfry(napis));
}

void test4() {
  std::string napis = "abc2";
  assert(!jedynieCyfry(napis));
}

int main() {
  test1();
  test2();
  test3();
  test4();

  return 0;
}
