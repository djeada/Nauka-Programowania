/*
ZAD-11 — Średnia długość słów

**Poziom:** ★☆☆
**Tagi:** `string`, `arytmetyka`

### Treść

Wczytaj zdanie i oblicz średnią długość słów. Wynik ma być liczbą całkowitą.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: średnia długość słów (liczba całkowita)

### Przykład

**Wejście:**

```
Zepsuty rower.
```

**Wyjście:**

```
6
```

### Uwagi

* Licz jako: `suma_dlugosci // liczba_slow` (dzielenie całkowite).

*/
#include <algorithm>
#include <cassert>
#include <string>

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
int srednia(const std::string &napis) {
  size_t calk_dlugosc = 0;
  size_t n = 0;
  size_t pocz = 0;
  size_t konc = 0;
  while ((konc = napis.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = napis.substr(pocz, konc - pocz);
      wyczysc(slowo);
      if (!slowo.empty()) {
        n++;
        calk_dlugosc += slowo.size();
      }
    }
    pocz = konc + 1;
  }
  if (pocz < napis.size()) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    if (!slowo.empty()) {
      n++;
      calk_dlugosc += slowo.size();
    }
  }

  return calk_dlugosc / n;
}

void test1() {
  std::string napis = "Kaczka lubi wiosne.";
  int wynik = 5;
  assert(srednia(napis) == wynik);
}

void test2() {
  std::string napis = "Ile to   ma :  slow w swoim zdaniu na   koniec?";
  int wynik = 3;
  assert(srednia(napis) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}
