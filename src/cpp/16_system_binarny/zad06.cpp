/*
ZAD-06 — Konwersja między dowolnymi systemami (2..36)

**Poziom:** ★★☆
**Tagi:** `konwersja`, `base`, `string`

### Treść

Wczytaj:

1. liczbę `X` zapisaną w systemie o podstawie `p`
2. podstawę `p` (2..36)
3. podstawę docelową `q` (2..36)

i wypisz reprezentację `X` w systemie o podstawie `q`.

### Wejście

Trzy linie:

1. `X` (zapis liczby; dla podstaw >10 może zawierać litery `A-Z`)
2. `p` (2..36)
3. `q` (2..36)

### Wyjście

Jedna linia: zapis liczby w systemie o podstawie `q` (używaj `0–9` i `A–Z`).

### Przykład

**Wejście:**

```
4301
10
4
```

**Wyjście:**

```
1003031
```

### Uwagi o formacie

* `X` może być duże — traktuj jako napis, a nie typ int „na wejściu”.
* Dla wartości 10..35 stosuj `A..Z`.

*/
#include <algorithm>
#include <cassert>
#include <cmath>
#include <string>

int naDziesietny(std::string liczba, int staraPodstawa) {
  /*
   * Funkcja zamienia liczbe z reprezentacji w systemie stara_podstawa na
   * reprezentacje w systemie dziesietnym.
   */

  int reprezentacjaDziesietna = 0;

  for (int i = liczba.size() - 1; i >= 0; i--) {
    if (liczba[i] >= 'A' && liczba[i] < 'Z')
      reprezentacjaDziesietna +=
          (liczba[i] - 'A' + 10) * pow(staraPodstawa, (liczba.size() - 1 - i));

    else
      reprezentacjaDziesietna +=
          (liczba[i] - '0') * pow(staraPodstawa, (liczba.size() - 1 - i));
  }

  return reprezentacjaDziesietna;
}

void zmianaPodstawy(std::string &liczba, int staraPodstawa, int nowaPodstawa) {
  /*
   * Funkcja zamienia liczbe z reprezentacji w systemie stara_podstawa na
   * reprezentacje w systemie dziesietnym.
   */
  if (staraPodstawa > (10 + 'Z' - 'A'))
    throw std::invalid_argument("Podstawa systemu nie moze byc wieksza niz 36");

  int reprezentacjaDziesietna = naDziesietny(liczba, staraPodstawa);
  liczba = "";
  podstawa = nowaPodstawa;

  while (reprezentacjaDziesietna > 0) {
    int reszta = reprezentacjaDziesietna % podstawa;
    reprezentacjaDziesietna /= podstawa;

    char nowyZnak = '0' + reszta;

    if (nowyZnak > '9') nowyZnak = 'A' + (nowyZnak - '9') - 1;

    liczba += nowyZnak;
  }

  reverse(liczba.begin(), liczba.end());
}

void testZmianaPodstawy() {
  std::string liczba = "4301";
  std::string wynik = "1003031";
  zmianaPodstawy(liczba, 10, 4);

  assert(liczba == wynik);
}

int main() {
  testZmianaPodstawy();

  return 0;
}
