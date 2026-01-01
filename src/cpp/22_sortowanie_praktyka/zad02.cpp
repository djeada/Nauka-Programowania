/*
ZAD-02 — Sortowanie słów w zdaniu

**Poziom:** ★★☆
**Tagi:** `sort`, `string`, `split`

### Treść

Otrzymujesz zdanie. Podziel je na słowa, traktując znaki interpunkcyjne jako
separatory, a następnie posortuj słowa alfabetycznie i wypisz listę.

### Wejście

* 1 linia: napis `zdanie`

### Wyjście

* 1 linia: lista słów w formacie jak w przykładzie, np. `['Ala', 'kota', 'ma']`

### Przykład

**Wejście:**

```
Lemur wygina śmiało ciało
```

**Wyjście:**

```
['Lemur', 'ciało', 'wygina', 'śmiało']
```

### Uwagi o formatowaniu

* Ignoruj znaki interpunkcyjne (np. `.,!?;:`) — nie są częścią słów.
* Wielkość liter pozostaje bez zmian (nie zamieniaj na małe/duże), sortujesz to,
co w tekście.

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

std::vector<std::string> slowa(std::string &napis) {
  std::vector<std::string> wynik;
  int pocz = 0;
  int konc = 0;
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

void sortuj(std::vector<std::string> &lista) {
  std::sort(lista.begin(), lista.end());
}

void test1() {
  std::string napis = "Lemur wygina smialo cialo";
  std::vector<std::string> wynik{"Lemur", "cialo", "smialo", "wygina"};
  auto napisy = slowa(napis);
  sortuj(napisy);

  assert(napisy == wynik);
}

int main() {
  test1();

  return 0;
}
