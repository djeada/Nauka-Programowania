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

void wyczysc(std::string &napis) {
  auto it = napis.begin();

  while (it != napis.end()) {
    if (ispunct(*it))
      napis.erase(it);
    else
      it++;
  }
}

std::string najdluzsze(std::string &napis) {
  std::string wynik;
  unsigned int dlugosc = 0;
  unsigned int pocz = 0;
  unsigned int konc = 0;
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
  if (konc != pocz) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    if (slowo.size() > dlugosc) {
      wynik = slowo;
      dlugosc = slowo.size();
    }
  }

  return wynik;
}

std::string najkrotsze(std::string &napis) {
  std::string wynik;
  unsigned int dlugosc = napis.size();
  unsigned int pocz = 0;
  unsigned int konc = 0;
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
  if (konc != pocz) {
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
