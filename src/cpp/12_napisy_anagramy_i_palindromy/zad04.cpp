/*
ZAD-04 — Palindromy w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `tokenizacja`, `palindrom`

### Treść

Wczytaj zdanie i wypisz wszystkie słowa, które są palindromami.
Ignoruj wielkość liter przy sprawdzaniu.

### Wejście

* 1. linia: zdanie (może zawierać spacje i znaki interpunkcyjne)

### Wyjście

Każdy znaleziony palindrom w osobnej linii, w kolejności występowania w zdaniu.

### Przykład

**Wejście:**

```
Tata zabrał kajak na wycieczkę i uderzył się w oko
```

**Wyjście:**

```
Tata
kajak
i
w
oko
```

### Uwagi o formatowaniu

* Traktuj „słowo” jako ciąg liter/cyfr po usunięciu interpunkcji z brzegów (np.
`kara.` → `kara`).
* Porównuj w wersji `lower()`, ale wypisz w oryginalnym brzmieniu z wejścia (tak
jak w przykładzie).

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
bool palindrom(std::string &slowo) {
  int N = slowo.length() - 1;
  for (int i = 0; i <= N / 2; i++) {
    if (slowo[i] != slowo[N - i]) return false;
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
std::vector<std::string> palindromyV1(std::string &napis) {
  std::vector<std::string> wynik;
  size_t pocz = 0;
  size_t konc = 0;
  while ((konc = napis.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = napis.substr(pocz, konc - pocz);
      wyczysc(slowo);
      naMale(slowo);
      if (!slowo.empty() && palindrom(slowo)) wynik.push_back(slowo);
    }
    pocz = konc + 1;
  }
  if (pocz < napis.size()) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    naMale(slowo);
    if (!slowo.empty() && palindrom(slowo)) wynik.push_back(slowo);
  }

  return wynik;
}

void test1() {
  std::string napis = "Tata zbaral kajak na wycieczke i uderzyl sie w oko";
  std::vector<std::string> wynik({"kajak", "i", "w", "oko"});
  assert(palindromyV1(napis) == wynik);
}

int main() {
  test1();

  return 0;
}
