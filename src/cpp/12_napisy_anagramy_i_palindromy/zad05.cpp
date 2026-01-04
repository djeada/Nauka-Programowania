/*
ZAD-05 — Anagramy słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `anagram`, `string`, `zliczanie`

### Treść

Wczytaj zdanie oraz słowo-klucz. Wypisz wszystkie słowa ze zdania, które są
anagramami słowa-klucza (ignoruj wielkość liter).

### Wejście

* 1. linia: zdanie
* 2. linia: słowo-klucz `k`

### Wyjście

Każde słowo ze zdania będące anagramem `k` — w osobnej linii (w kolejności
występowania).

### Przykład

**Wejście:**

```
Sroga kara.
arak
```

**Wyjście:**

```
kara
```

### Uwagi

* Tak jak wyżej: usuń interpunkcję z brzegów słów.
* Porównuj np. posortowane litery w `lower()`.

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
void naMale(std::string &slowo) {
  transform(slowo.begin(), slowo.end(), slowo.begin(), ::tolower);
}

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
bool anagram(std::string s1, std::string s2) {
  unsigned int N = s1.length();
  unsigned int M = s2.length();

  if (N != M) return false;

  int pom[256] = {0};

  for (const auto &znak : s1) pom[znak]++;

  for (const auto &znak : s2) pom[znak]--;

  for (const auto &x : pom) {
    if (x != 0) return false;
  }

  return true;
}

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
std::vector<std::string> anagramyV1(const std::string &zdanie,
                                    const std::string &napis) {
  std::vector<std::string> wynik;
  size_t pocz = 0;
  size_t konc = 0;
  while ((konc = zdanie.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = zdanie.substr(pocz, konc - pocz);
      wyczysc(slowo);
      naMale(slowo);
      if (!slowo.empty() && anagram(slowo, napis)) wynik.push_back(slowo);
    }
    pocz = konc + 1;
  }
  if (pocz < zdanie.size()) {
    auto slowo = zdanie.substr(pocz);
    wyczysc(slowo);
    naMale(slowo);
    if (!slowo.empty() && anagram(slowo, napis)) wynik.push_back(slowo);
  }

  return wynik;
}

void test1() {
  std::string zdanie =
      "Za jego nikczemne uczynki, spotakla go wysoce sroga kara.";
  std::string slowo = "arak";
  std::vector<std::string> wynik({"kara"});
  assert(anagramyV1(zdanie, slowo) == wynik);
}

int main() {
  test1();

  return 0;
}
