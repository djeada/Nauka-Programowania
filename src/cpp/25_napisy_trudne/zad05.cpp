/*
ZAD-05 — Usuń powtórzenia sąsiadujących znaków

**Poziom:** ★★★
**Tagi:** `string`, `compress`, `run-length`

### Treść

Otrzymujesz napis. Usuń powtórzenia znaków występujących **bezpośrednio obok
siebie**, pozostawiając jedno wystąpienie z każdej „serii”.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: napis po redukcji sąsiadów

### Przykład

**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

**Wyjście:**

```
ABA
```

*/
#include <cassert>
#include <string>

// Dopisuje znak tylko wtedy, gdy rozpoczyna nowa serie (jest pierwszy albo
// rozni sie od poprzedniego znaku).
// Zlozonosc czasowa: O(n)
// Zlozonosc pamieciowa: O(n)
std::string usunPowtorzeniaV1(const std::string &slowo) {
  std::string wynik;

  for (std::size_t i = 0; i < slowo.size(); i++) {
    if (i == 0 || slowo[i] != slowo[i - 1]) wynik += slowo[i];
  }

  return wynik;
}

// Testy Poprawnosci
void test1() {
  std::string napis = "AAAAAAAAAABBBBBBBBA";
  std::string wynik = "ABA";

  assert(usunPowtorzeniaV1(napis) == wynik);
}

void test2() {
  std::string napis = "XXXYYASFBY";
  std::string wynik = "XYASFBY";

  assert(usunPowtorzeniaV1(napis) == wynik);
}

void test3() {
  std::string napis = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC";
  std::string wynik = "C";

  assert(usunPowtorzeniaV1(napis) == wynik);
}

void test4() {
  std::string napis = "AAABB";
  std::string wynik = "AB";

  assert(usunPowtorzeniaV1(napis) == wynik);
}

void test5() {
  std::string napis;
  std::string wynik;

  assert(usunPowtorzeniaV1(napis) == wynik);
}

int main() {
  test1();
  test2();
  test3();
  test4();
  test5();

  return 0;
}

