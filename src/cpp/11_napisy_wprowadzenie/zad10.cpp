/*
ZAD-10 — Najdłuższe i najkrótsze słowo

**Poziom:** ★☆☆
**Tagi:** `string`, `min/max`, `len`

### Treść

Wczytaj zdanie i znajdź:

a) najdłuższe słowo,
b) najkrótsze słowo.

Jeśli jest remis, wybierz słowo, które występuje wcześniej.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: najdłuższe słowo
* 2. linia: najkrótsze słowo

### Przykład

**Wejście:**

```
Kaczka lubi wiosnę.
```

**Wyjście:**

```
Kaczka
lubi
```

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
void wyczysc(std::string &napis) {
  auto it = napis.begin();

  while (it != napis.end()) {
    if (ispunct(*it))
      it = napis.erase(it);
    else
      it++;
  }
}

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(n)
std::string najdluzsze(std::string &napis) {
  std::string wynik;
  size_t dlugosc = 0;
  size_t pocz = 0;
  size_t konc = 0;
  while ((konc = napis.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = napis.substr(pocz, konc - pocz);
      wyczysc(slowo);

      if (slowo.size() > dlugosc) {
        wynik = slowo;
        dlugosc = slowo.size();
      }
    }
    pocz = konc + 1;
  }
  if (pocz < napis.size()) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    if (slowo.size() > dlugosc) {
      wynik = slowo;
      dlugosc = slowo.size();
    }
  }

  return wynik;
}

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(n)
std::string najkrotsze(std::string &napis) {
  std::string wynik;
  size_t dlugosc = napis.size();
  size_t pocz = 0;
  size_t konc = 0;
  while ((konc = napis.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = napis.substr(pocz, konc - pocz);
      wyczysc(slowo);

      if (slowo.size() < dlugosc) {
        wynik = slowo;
        dlugosc = slowo.size();
      }
    }
    pocz = konc + 1;
  }
  if (pocz < napis.size()) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    if (slowo.size() < dlugosc) {
      wynik = slowo;
      dlugosc = slowo.size();
    }
  }

  return wynik;
}

void test1() {
  std::string napis = "Kaczka lubi wiosne.";
  std::string wynik = "Kaczka";
  assert(najdluzsze(napis) == wynik);
}

void test2() {
  std::string napis = "Kaczka lubi wiosne.";
  std::string wynik = "lubi";
  assert(najkrotsze(napis) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}
