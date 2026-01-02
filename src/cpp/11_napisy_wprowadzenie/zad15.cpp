/*
ZAD-15 — Słowa jako lista

**Poziom:** ★☆☆
**Tagi:** `split`, `list`

### Treść

Wczytaj zdanie i wypisz listę słów w formacie `["Ala", "ma", "kota"]`.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: lista słów (jak w przykładzie)

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
["Ala", "ma", "kota"]
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
      napis.erase(it);
    else
      it++;
  }
}

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(n)
std::vector<std::string> slowaV1(std::string &napis) {
  std::vector<std::string> wynik;
  unsigned int pocz = 0;
  unsigned int konc = 0;
  while ((konc = napis.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = napis.substr(pocz, konc - pocz);
      wyczysc(slowo);
      if (!slowo.empty()) wynik.push_back(slowo);
    }
    pocz = konc + 1;
  }
  if (konc != pocz) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    if (!slowo.empty()) wynik.push_back(slowo);
  }

  return wynik;
}

void test1() {
  std::string napis = "We think in generalities, but we live in details";
  std::vector<std::string> wynik{"We", "think", "in", "generalities", "but",
                                 "we", "live",  "in", "details"};
  assert(slowaV1(napis) == wynik);
}

void test2() {
  std::string napis = "";
  std::vector<std::string> wynik;
  assert(slowaV1(napis) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}
