/*
ZAD-13 — Znaki na indeksach będących liczbami pierwszymi

**Poziom:** ★☆☆
**Tagi:** `liczby pierwsze`, `indeksy`, `string`

### Treść

Wczytaj napis. Zbierz znaki, których **indeksy (od 0)** są liczbami pierwszymi
(2, 3, 5, 7, ...). Wypisz wynik jako listę w stylu Pythona.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: lista znaków, np. `['o', 'ń']`

### Przykład

**Wejście:**

```
Słoń
```

**Wyjście:**

```
['o', 'ń']
```

### Uwagi

* Indeksy: `S(0) ł(1) o(2) ń(3)` → bierz 2 i 3.

*/
#include <cassert>
#include <cmath>
#include <string>
#include <vector>

bool czyPierwsza(int n) {
  if (!(n % 2) && n < 2) return false;

  for (int i = 3; i <= sqrt((double)n); i += 2) {
    if (!(n % i)) return false;
  }

  return true;
}

std::vector<char> znaki(const std::string &napis) {
  std::vector<char> znaki;

  for (unsigned int i = 0; i < napis.size(); i++) {
    if (czyPierwsza(i)) znaki.push_back(napis[i]);
  }

  return znaki;
}

void test1() {
  std::string napis = "Kaczka lubi wiosne.";
  std::vector<char> wynik{'c', 'z', 'a', 'l', ' ', 'i', 'e'};
  assert(znaki(napis) == wynik);
}

int main() {
  test1();
  return 0;
}
